#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Конвертер страниц QuickServe (HTML) в чистый Markdown для Obsidian.

Разбирает выгруженные страницы Cummins QuickServe (процедуры, TSB, сервисные
бюллетени, STI, инструкции по установке, истории руководств) и отдаёт:

    meta  — словарь метаданных (заголовок, номер, даты, ревизия, ...)
    md    — тело документа в Markdown
    figs  — список путей иллюстраций (/rtgraphics/...) в порядке появления

Опасные и важные блоки Cummins превращаются в callout'ы Obsidian:
    WARNING            -> [!danger]
    CAUTION            -> [!warning]
    Note               -> [!note]
    Torque Value       -> [!tip]
"""
import re
from bs4 import BeautifulSoup, NavigableString, Tag, Comment

# мусор сайта, который никогда не входит в документ
DROP_SEL = [
    "script", "style", "noscript", "iframe", "form", "button", "input", "select",
    "#onetrust-consent-sdk", "#ot-sdk-btn-floating", ".ot-sdk-container",
    ".slider-bottom", "#qsol-common-footer", ".foot", ".header", ".navbar",
    "nav", ".feedbackViewer", ".breadcrumb", "#topcontrol", ".sr-only",
    ".graphic_size_link", ".hidden-print", ".back-to-top", ".ot-scrn-rdr",
    "#cst-section", ".cst-section", ".titlebar", ".panel-heading", ".dropdown-menu",
]
DROP_CLASS = {"ot-hide", "onetrust-pc-dark-filter"}

# иконки/логотипы сайта — не иллюстрации документа
SKIP_IMG = re.compile(r"/graphics/common/|cookielaw|logo|arrow\d*\.png|spacer", re.I)

CAT_RE = re.compile(
    r"/qs3/pubsys2/xml/\w+/(tsb|bulletin|manual|install_inst|sti|outlines|procedures)/([^?#]+)")

WS = re.compile(r"[\s\u00a0]+")


def _clean_text(s):
    s = s.replace(" ", " ").replace("’", "'").replace("™", "™")
    s = WS.sub(" ", s)
    return s.strip()


def _esc(s):
    """Экранирование символов, ломающих Markdown/Obsidian."""
    s = s.replace("\\", "\\\\")
    for ch in ("*", "_", "`", "[", "]", "|", "<", ">", "#", "^", "~"):
        s = s.replace(ch, "\\" + ch)
    return s


def doc_link_target(href):
    """/qs3/pubsys2/xml/en/procedures/20/20-008-001.html -> ('procedures', '20-008-001')"""
    m = CAT_RE.search(href or "")
    if not m:
        return None
    cat, path = m.group(1), m.group(2)
    doc_id = path.rsplit("/", 1)[-1]
    doc_id = re.sub(r"\.html?$", "", doc_id)
    return cat, doc_id


class Converter:
    def __init__(self, link_resolver=None, part_linker=None):
        # link_resolver(cat, doc_id) -> имя заметки или None
        self.link_resolver = link_resolver or (lambda c, d: None)
        # part_linker(text) -> текст с проставленными ссылками на артикулы
        self.part_linker = part_linker or (lambda t: t)

    # ------------------------------------------------------------------ разбор
    def convert(self, html):
        soup = BeautifulSoup(html, "lxml")
        meta = {}

        t = soup.find("title")
        meta["title"] = _clean_text(t.get_text()) if t else ""

        body = soup.body or soup
        upd = body.select_one(".last-update-box")
        if upd:
            m = re.search(r"([0-9]{1,2}-[A-Za-zА-Яа-я]{3}-[0-9]{4})", upd.get_text())
            if m:
                meta["modified"] = m.group(1)

        root = (body.select_one("div.divForSearch > div.container-fluid")
                or body.select_one("div.divForSearch")
                or body.select_one("div.container")
                or body)

        # шапка документа: таблицы «Номер / Дата выпуска / Ревизия»
        self._header_meta(root, meta)

        for sel in DROP_SEL:
            for el in root.select(sel):
                el.decompose()
        for el in list(root.find_all(True)):
            cls = set(el.get("class") or [])
            if cls & DROP_CLASS or any(c.startswith("ot-") for c in cls):
                el.decompose()

        self.figs = []
        self.out = []
        self._walk(root)
        md = self._finish()
        return meta, md, self.figs

    HEAD_TABLES = ("table.panel-table", "table.documenthistory-table",
                   "table.servtool-table", "table.titlebar-table",
                   "table.installinst-table", "table.bulletin-table")
    KEYMAP = {
        "technical service bulletin": "number",
        "service bulletin number": "number",
        "service tool instruction number": "number",
        "installation instruction number": "number",
        "bulletin number": "number",
        "released date": "released",
        "revision level": "revision",
        "revision date": "revised",
        "supersedes": "supersedes",
    }

    def _header_meta(self, root, meta):
        """Шапочные таблицы «Ключ: значение» -> метаданные; сами таблицы убираем."""
        for sel in self.HEAD_TABLES:
            for tab in root.select(sel):
                for cell in tab.find_all(["td", "th"]):
                    txt = _clean_text(cell.get_text(" ", strip=True))
                    m = re.match(r"([A-Za-z][A-Za-z /®™\.]{3,40}?)\s*:\s*(.+)$", txt)
                    if m:
                        key = self.KEYMAP.get(m.group(1).strip().lower())
                        if key and key not in meta:
                            meta[key] = m.group(2).strip()
                tab.decompose()

    # ------------------------------------------------------------- обход DOM
    def _walk(self, el):
        for child in el.children:
            if isinstance(child, Comment):
                continue
            if isinstance(child, NavigableString):
                s = _clean_text(str(child))
                if s:
                    self._para(_esc(s))
                continue
            if not isinstance(child, Tag):
                continue
            self._node(child)

    def _node(self, el):
        name = el.name
        cls = set(el.get("class") or [])

        if name == "img":
            self._img(el)
            return
        if name in ("br", "hr"):
            return
        if name == "table":
            self._table(el)
            return
        if name in ("ul", "ol"):
            self._list(el, ordered=(name == "ol"))
            return
        if name in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._heading(el, cls)
            return
        if "torqueelementsgroup" in cls:
            txt = _clean_text(el.get_text(" ", strip=True))
            txt = re.sub(r"^Torque Value\s*:?\s*", "", txt, flags=re.I)
            txt = WS.sub(" ", txt).replace("[ ", "[").replace(" ]", "]").strip()
            self._callout("tip", "Момент затяжки · Torque Value", [txt])
            return
        if name == "p":
            if el.select_one(".glyphicon-warning-sign") or "cautionmsg" in cls or "warningmsg" in cls:
                self._hazard(el, cls)
                return
            self._para(self._inline(el))
            return
        if name in ("div", "span", "section", "td", "tr", "tbody", "thead", "a", "b", "i",
                    "strong", "em", "font", "center", "sup", "sub", "small", "label", "li"):
            # контейнеры проходим насквозь
            if name in ("span", "a", "b", "i", "strong", "em", "font", "sup", "sub", "small"):
                txt = self._inline(el)
                if txt:
                    self._para(txt)
                return
            self._walk(el)
            return
        self._walk(el)

    # ---------------------------------------------------------------- узлы
    def _heading(self, el, cls):
        txt = self._inline(el)
        if not txt:
            return
        if "note" in cls or re.match(r"^\**Note\b", txt, re.I):
            txt = re.sub(r"^\**\s*Note\s*\**\s*:?\s*", "", txt, flags=re.I).strip()
            txt = re.sub(r"^\*\*\s*", "", txt)
            self._callout("note", "Note · Примечание", [txt])
            return
        level = {"h1": 2, "h2": 2, "h3": 3, "h4": 4, "h5": 4, "h6": 4}[el.name]
        self._emit("")
        self._emit("#" * level + " " + txt.replace("\n", " "))
        self._emit("")

    def _hazard(self, el, cls):
        txt = _clean_text(el.get_text(" ", strip=True))
        kind = "warning"
        label = "CAUTION · Осторожно"
        if re.search(r"\bWARNING\b", txt, re.I) or "warningmsg" in cls:
            kind, label = "danger", "WARNING · Опасно"
        if "cautionmsg" in cls or "warningmsg" in cls:
            # это уже текст предупреждения, а не заголовок
            self._callout(kind, label, [_esc(txt)])
            return
        # заголовок-маркер: текст лежит в следующем абзаце
        body = []
        for sib in el.next_siblings:
            if isinstance(sib, Tag):
                c = set(sib.get("class") or [])
                if c & {"cautionmsg", "warningmsg"} or (sib.name == "p" and not body):
                    body.append(_esc(_clean_text(sib.get_text(" ", strip=True))))
                    sib.extract()
                    break
                break
        self._callout(kind, label, [b for b in body if b])

    def _callout(self, kind, title, lines):
        self._emit("")
        self._emit(f"> [!{kind}] {title}")
        for ln in lines or [""]:
            for part in ln.split("\n"):
                self._emit("> " + part.strip())
        self._emit("")

    def _img(self, el):
        src = el.get("src") or ""
        if not src.startswith("/rtgraphics/") or SKIP_IMG.search(src):
            return
        self.figs.append(src)
        name = src.rsplit("/", 1)[-1]
        alt = _clean_text(el.get("alt") or "")
        if alt.upper() in ("GRAPHIC NOT FOUND", ""):
            alt = ""
        self._emit("")
        self._emit(f"![[{name}]]" + (f"\n*{_esc(alt)}*" if alt else ""))
        self._emit("")

    def _list(self, el, ordered):
        self._emit("")
        i = 0
        for li in el.find_all("li", recursive=False):
            i += 1
            inner_lists = li.find_all(["ul", "ol"], recursive=False)
            for x in inner_lists:
                x.extract()
            txt = self._inline(li)
            bullet = f"{i}." if ordered else "-"
            if txt:
                first, *rest = txt.split("\n")
                self._emit(f"{bullet} {first}")
                for r in rest:
                    self._emit("  " + r)
            for x in inner_lists:
                sub = Converter(self.link_resolver, self.part_linker)
                sub.figs, sub.out = self.figs, []
                sub._list(x, x.name == "ol")
                for ln in sub.out:
                    self._emit(("  " + ln) if ln else "")
        self._emit("")

    def _table(self, el):
        rows = []
        for tr in el.find_all("tr"):
            cells = tr.find_all(["td", "th"], recursive=False) or tr.find_all(["td", "th"])
            row = []
            for c in cells:
                # картинки внутри таблицы выносим отдельно
                for im in c.find_all("img"):
                    self._img(im)
                    im.extract()
                row.append(self._inline(c).replace("\n", " ").replace("|", "\\|"))
            if any(x.strip() for x in row):
                rows.append(row)
        if not rows:
            return
        width = max(len(r) for r in rows)
        if width == 1:
            # псевдотаблица вёрстки — просто абзацы
            for r in rows:
                if r[0].strip():
                    self._para(r[0])
            return
        rows = [r + [""] * (width - len(r)) for r in rows]
        head, body = rows[0], rows[1:]
        if not any(h.strip() for h in head):
            head, body = [""] * width, rows
        self._emit("")
        self._emit("| " + " | ".join(head) + " |")
        self._emit("|" + "---|" * width)
        for r in body:
            self._emit("| " + " | ".join(r) + " |")
        self._emit("")

    # -------------------------------------------------------- инлайн-разбор
    def _inline(self, el):
        parts = []
        for ch in el.children:
            if isinstance(ch, Comment):
                continue
            if isinstance(ch, NavigableString):
                s = _clean_text(str(ch))
                if s:
                    parts.append(_esc(s))
            elif isinstance(ch, Tag):
                if ch.name in ("b", "strong"):
                    t = self._inline(ch)
                    parts.append(f"**{t}**" if t else "")
                elif ch.name in ("i", "em"):
                    t = self._inline(ch)
                    parts.append(f"*{t}*" if t else "")
                elif ch.name == "a":
                    parts.append(self._anchor(ch))
                elif ch.name == "img":
                    self._img(ch)
                elif ch.name == "br":
                    parts.append("\n")
                elif ch.name in ("ul", "ol", "table"):
                    parts.append(_esc(_clean_text(ch.get_text(" ", strip=True))))
                else:
                    parts.append(self._inline(ch))
        txt = " ".join(p for p in parts if p)
        txt = re.sub(r"\s+([,.;:)])", r"\1", txt)
        txt = re.sub(r"\(\s+", "(", txt)
        txt = WS.sub(" ", txt).strip()
        return txt

    def _anchor(self, a):
        text = _esc(_clean_text(a.get_text(" ", strip=True)))
        href = a.get("href") or ""
        tgt = doc_link_target(href)
        if tgt:
            note = self.link_resolver(*tgt)
            if note:
                return f"[[{note}|{text or tgt[1]}]]"
            return text or tgt[1]
        if href.startswith("http"):
            return f"[{text}]({href})" if text else href
        return text

    # -------------------------------------------------------------- вывод
    def _para(self, txt):
        if not txt:
            return
        self._emit("")
        self._emit(txt)
        self._emit("")

    def _emit(self, line):
        self.out.append(line)

    def _finish(self):
        md, blank = [], True
        for ln in self.out:
            if ln.strip() == "":
                if blank:
                    continue
                blank = True
                md.append("")
            else:
                blank = False
                md.append(ln.rstrip())
        text = "\n".join(md).strip()
        text = re.sub(r"\n{3,}", "\n\n", text)
        text = re.sub(r"\*\*\s*\*\*", "", text)
        text = re.sub(r"(?m)^>\s*\*\*\s+", "> ", text)
        text = re.sub(r"(?m)^>\s*$\n(?=>)", "> ", text)
        return self.part_linker(text)
