#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Markdown (как его пишет qs2md) -> HTML для веб-каталога.

Диалект ограничен тем, что порождает конвейер базы знаний:
заголовки ##/###/####, абзацы, таблицы, списки, callout'ы Obsidian,
встроенные картинки ![[файл]] и ссылки [[заметка|подпись]].
"""
import html
import re

CALLOUT = re.compile(r"^>\s*\[!(\w+)\]-?\s*(.*)$")
IMG = re.compile(r"^!\[\[([^\]\|]+)(?:\|[^\]]*)?\]\]$")
BOLD = re.compile(r"\*\*(.+?)\*\*")
ITAL = re.compile(r"(?<![\*\w])\*([^\*\n]+?)\*(?!\*)")
CODE = re.compile(r"`([^`]+)`")
WIKI = re.compile(r"\[\[([^\]\|]+)(?:\\?\|([^\]]*))?\]\]")
MDLINK = re.compile(r"\[([^\]]+)\]\((https?://[^\)]+)\)")
UNESC = re.compile(r"\\([\\`*_\[\]|<>#^~])")

CALLOUT_RU = {
    "danger": ("callout danger", "⚠"),
    "warning": ("callout warning", "⚠"),
    "note": ("callout note", "i"),
    "tip": ("callout tip", "🔧"),
    "abstract": ("callout abstract", "≡"),
    "info": ("callout info", "i"),
    "missing": ("callout missing", "—"),
    "example": ("callout example", "≡"),
    "bug": ("callout bug", "!"),
}


class Renderer:
    """resolve(target) -> (href, css_class, label) либо None для обычного текста."""

    def __init__(self, resolve, image_url):
        self.resolve = resolve
        self.image_url = image_url

    # ---------------------------------------------------------- инлайн
    def inline(self, text):
        out = []
        pos = 0
        for m in WIKI.finditer(text):
            out.append(self._plain(text[pos:m.start()]))
            target = m.group(1).strip().replace("\\", "")
            label = (m.group(2) or "").strip() or target
            res = self.resolve(target)
            if res:
                href, cls = res
                out.append(f'<a class="{cls}" href="{href}">{html.escape(label)}</a>')
            else:
                out.append(html.escape(label))
            pos = m.end()
        out.append(self._plain(text[pos:]))
        return "".join(out)

    def _plain(self, s):
        s = UNESC.sub(r"\1", s)
        s = html.escape(s)
        s = MDLINK.sub(
            lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">'
                      f'{m.group(1)}</a>', s)
        s = CODE.sub(r"<code>\1</code>", s)
        s = BOLD.sub(r"<b>\1</b>", s)
        s = ITAL.sub(r"<i>\1</i>", s)
        return s

    # ----------------------------------------------------------- блоки
    def render(self, md):
        lines = (md or "").split("\n")
        out = []
        i = 0
        n = len(lines)
        while i < n:
            line = lines[i]
            s = line.strip()

            if not s:
                i += 1
                continue

            m = IMG.match(s)
            if m:
                name = m.group(1).strip()
                url, fallback = self.image_url(name)
                if url:
                    out.append(f'<figure class="fig"><img loading="lazy" src="{url}"'
                               f' alt="{html.escape(name)}"></figure>')
                elif fallback:
                    out.append('<div class="fig-missing">Иллюстрация <code>'
                               + html.escape(name) + '</code> не выгружена — '
                               f'<a href="{fallback}" target="_blank" rel="noopener">'
                               "открыть на QuickServe ↗</a></div>")
                i += 1
                continue

            if s.startswith("#"):
                lvl = len(s) - len(s.lstrip("#"))
                txt = self.inline(s[lvl:].strip())
                lvl = min(max(lvl, 2), 4)
                out.append(f"<h{lvl}>{txt}</h{lvl}>")
                i += 1
                continue

            m = CALLOUT.match(s)
            if m:
                kind = m.group(1).lower()
                cls, icon = CALLOUT_RU.get(kind, ("callout note", "i"))
                head = self.inline(m.group(2).strip())
                body = []
                i += 1
                while i < n and lines[i].lstrip().startswith(">"):
                    body.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                inner = self.render("\n".join(body)) if body else ""
                out.append(f'<div class="{cls}"><div class="callout-head">'
                           f'<span class="callout-ico">{icon}</span>{head}</div>'
                           f'<div class="callout-body">{inner}</div></div>')
                continue

            if s.startswith("|"):
                rows = []
                while i < n and lines[i].strip().startswith("|"):
                    rows.append(lines[i].strip())
                    i += 1
                out.append(self._table(rows))
                continue

            if re.match(r"^([-*]|\d+\.)\s+", s):
                ordered = bool(re.match(r"^\d+\.\s+", s))
                items = []
                while i < n:
                    cur = lines[i]
                    st = cur.strip()
                    if re.match(r"^([-*]|\d+\.)\s+", st):
                        items.append(re.sub(r"^([-*]|\d+\.)\s+", "", st))
                    elif st and cur.startswith(("  ", "\t")) and items:
                        items[-1] += " " + st
                    else:
                        break
                    i += 1
                tag = "ol" if ordered else "ul"
                lis = "".join(f"<li>{self.inline(x)}</li>" for x in items)
                out.append(f"<{tag}>{lis}</{tag}>")
                continue

            if s == "---":
                out.append("<hr>")
                i += 1
                continue

            para = [s]
            i += 1
            while i < n and lines[i].strip() and not re.match(
                    r"^\s*([#>|!\[]|[-*]\s|\d+\.\s|---$)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{self.inline(' '.join(para))}</p>")

        return "".join(out)

    def _table(self, rows):
        cells = []
        for r in rows:
            r = r.strip().strip("|")
            parts = re.split(r"(?<!\\)\|", r)
            cells.append([p.strip().replace("\\|", "|") for p in parts])
        if len(cells) >= 2 and all(re.fullmatch(r":?-{2,}:?", c or "-")
                                   for c in cells[1]):
            head, body = cells[0], cells[2:]
        else:
            head, body = None, cells
        out = ['<div class="tw"><table class="doc-table">']
        if head and any(h for h in head):
            out.append("<thead><tr>" + "".join(
                f"<th>{self.inline(h)}</th>" for h in head) + "</tr></thead>")
        out.append("<tbody>")
        for row in body:
            out.append("<tr>" + "".join(
                f"<td>{self.inline(c)}</td>" for c in row) + "</tr>")
        out.append("</tbody></table></div>")
        return "".join(out)
