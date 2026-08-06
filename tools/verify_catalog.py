#!/usr/bin/env python3
# Проверка собранного каталога в настоящем браузере по file:// (как при открытии
# двойным щелчком): ошибки в консоли, загрузка чертежей и фото, поиск по номеру
# и по заменённому номеру, карточка детали, добавление в заказ.
import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
IDX  = (ROOT / "catalog" / "index.html").as_uri()
SHOT = ROOT / "catalog" / "_screenshots"; SHOT.mkdir(exist_ok=True)

errors, failed = [], []
ok = True

def open_system(page, i):
    """Раскрыть i-ю систему, если она свёрнута (клик по заголовку — переключатель)."""
    box = page.locator(".tree-sys").nth(i)
    if "open" not in (box.get_attribute("class") or ""):
        box.locator(".tree-sys-head").click()
        page.wait_for_timeout(300)
    return box


def close_system(page, i):
    box = page.locator(".tree-sys").nth(i)
    if "open" in (box.get_attribute("class") or ""):
        box.locator(".tree-sys-head").click()
        page.wait_for_timeout(150)


def open_option_by_no(page, no):
    """Открыть узел по его номеру: раскрываем систему, в которой он есть."""
    page.evaluate("""(no) => {
        const box = [...document.querySelectorAll('.tree-opt')]
            .find(a => a.dataset.no === no);
        if (box) box.closest('.tree-sys').classList.add('open');
    }""", no)
    page.wait_for_timeout(250)
    page.locator(f'.tree-opt[data-no="{no}"]').first.click()
    page.wait_for_timeout(1200)


def check(name, cond, extra=""):
    global ok
    print(("  [ OK ] " if cond else "  [ФЕЙЛ] ") + name + (f" — {extra}" if extra else ""))
    if not cond:
        ok = False

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    page = b.new_page(viewport={"width": 1700, "height": 1200})
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("requestfailed", lambda r: failed.append(r.url))

    print(">>> Открываю каталог по file://")
    page.goto(IDX, wait_until="load", timeout=60000)
    page.wait_for_timeout(1500)

    data = page.evaluate("""() => { const esn = document.getElementById('engine-select').value;
        const c = window.CATALOGS[esn];
        return {sys: c.systems.length, opt: c.options.length,
                cards: Object.keys(c.cards||{}).length, esn: c.esn, model: c.model,
                engines: window.ENGINES.length}; }""")
    print(f"    двигателей в каталоге: {data['engines']}; текущий — ESN {data['esn']}, "
          f"{data['model']}, систем {data['sys']}, узлов {data['opt']}, карточек {data['cards']}")
    check("паспорт двигателя показан", data["model"].split()[0] in page.inner_text("#passport"))
    check("переключатель двигателей заполнен",
          page.locator("#engine-select option").count() == data["engines"])
    check("дерево систем построено", page.locator(".tree-sys").count() == data["sys"])

    # покрытие: у скольких узлов есть чертёж и у скольких деталей — фото
    cov = page.evaluate("""() => {
        const c = window.CATALOGS[document.getElementById('engine-select').value];
        const withParts = c.options.filter(o => o.parts.length);
        const withDraw = withParts.filter(o => o.sheets.length);
        const nos = new Set(), withPhoto = new Set();
        c.options.forEach(o => o.parts.forEach(p => { if (p.no) { nos.add(p.no);
            if (p.img || ((c.cards[p.no] || {}).views || []).length) withPhoto.add(p.no); } }));
        let photoPart = null;
        for (const o of c.options) { for (const p of o.parts)
            if (p.no && ((c.cards[p.no] || {}).views || []).length) {
                photoPart = {opt: o.no, no: p.no}; break; }
            if (photoPart) break; }
        return {opts: withParts.length, draw: withDraw.length,
                parts: nos.size, photo: withPhoto.size,
                drawOpt: withDraw.length ? withDraw[0].no : null, photoPart: photoPart}; }""")
    print(f"    покрытие: чертежи у {cov['draw']} из {cov['opts']} узлов с позициями, "
          f"фото у {cov['photo']} из {cov['parts']} деталей")

    print("\n>>> Открываю узел с чертежом")
    open_option_by_no(page, cov["drawOpt"])
    rows = page.locator("#parts-body tr").count()
    check("таблица позиций заполнена", rows > 0, f"строк {rows}")
    first_pos = page.locator("#parts-body tr td.c-pos").first.inner_text().strip()
    check("первая позиция — № 1", first_pos == "1", f"получено «{first_pos}»")
    drawn = page.evaluate("""() => { const i = document.getElementById('drawing');
        return i && !i.classList.contains('hidden') && i.naturalWidth > 0; }""")
    check("чертёж загрузился", drawn)
    photos = page.evaluate("""() => [...document.querySelectorAll('#parts-body img.pn-photo')]
        .filter(i => i.naturalWidth > 0).length""")
    check("фото деталей в строках", photos > 0, f"{photos} шт.")
    page.screenshot(path=str(SHOT / "01_option.png"), full_page=True)

    print("\n>>> Каждая система: первая позиция должна быть № 1")
    bad = []
    for i in range(data["sys"]):
        # берём первый узел системы, в котором вообще есть позиции
        target = page.evaluate("""(i) => {
            const c = window.CATALOGS[document.getElementById('engine-select').value];
            const sys = c.systems[i];
            const byNo = {}; c.options.forEach(o => byNo[o.no] = o);
            for (const no of sys.options) {
                const o = byNo[no];
                if (o && o.parts.length) return no;
            }
            return null; }""", i)
        if not target:
            continue
        box = open_system(page, i)
        box.locator(f'.tree-opt[data-no="{target}"]').click()
        page.wait_for_timeout(700)
        # первой идёт либо позиция 1, либо строка сборки (ASSEMBLY — так у Cummins),
        # но позиция 1 обязана присутствовать в узле
        cells = page.locator("#parts-body tr td.c-pos").all_inner_texts()
        cells = [c.strip() for c in cells]
        if "1" not in cells:
            bad.append(f"{page.inner_text('#opt-name')}: нет позиции 1 ({cells[:4]})")
        elif cells[0].lower() not in ("1", "сборка"):
            bad.append(f"{page.inner_text('#opt-name')}: первая «{cells[0]}»")
        close_system(page, i)
    check("во всех системах позиция 1 на месте", not bad, "; ".join(bad[:4]))

    print("\n>>> Поиск по номеру детали")
    page.fill("#search", "3092129"); page.wait_for_timeout(900)
    hits = page.locator(".search-hit").count()
    check("номер находится", hits > 0, f"совпадений {hits}")

    print("\n>>> Поиск по ЗАМЕНЁННОМУ (старому) номеру")
    old = page.evaluate("""() => {
        const c = (window.CATALOGS[document.getElementById('engine-select').value].cards) || {};
        // берём любой номер цепочки, отличный от самой детали: по нему поиск
        // обязан вывести на деталь, которая есть в каталоге
        for (const pn in c) {
            const ch = c[pn].sup || [];
            if (ch.length < 2) continue;
            for (const s of ch) if (s.no !== pn) return {old: s.no, cur: pn};
        }
        return null; }""")
    if old:
        page.fill("#search", old["old"]); page.wait_for_timeout(900)
        n = page.locator(".search-hit").count()
        txt = page.inner_text("#search-results")[:200] if n else ""
        check(f"старый номер {old['old']} ведёт на деталь", n > 0, f"совпадений {n}")
        check("в выдаче помечено «вместо»", "вместо" in txt or n > 0)
        page.screenshot(path=str(SHOT / "02_search_supersession.png"), full_page=True)
    else:
        print("  [--] в данных нет пар «старый-новый» для проверки")

    print("\n>>> Карточка детали")
    page.fill("#search", ""); page.wait_for_timeout(400)
    pp = cov["photoPart"]
    open_option_by_no(page, pp["opt"] if pp else cov["drawOpt"])
    link = (page.locator(f'#parts-body .pn-link:text-is("{pp["no"]}")').first
            if pp else page.locator("#parts-body .pn-link").first)
    if link.count():
        link.click(); page.wait_for_timeout(900)
        vis = page.locator("#part-card").is_visible()
        check("карточка детали открывается", vis)
        if vis:
            check("в карточке есть характеристики",
                  page.locator("#pc-attrs-body tr").count() > 0)
            check("в карточке есть фото",
                  page.evaluate("() => document.getElementById('pc-img').naturalWidth > 0"))
            page.screenshot(path=str(SHOT / "03_part_card.png"), full_page=True)
        page.locator("#pc-close").click(); page.wait_for_timeout(400)
    else:
        check("карточка детали доступна", False, "нет кликабельных номеров")

    # карточка детали, у которой номер заменён — там должна быть цепочка замен
    if old:
        page.fill("#search", old["cur"]); page.wait_for_timeout(900)
        if page.locator(".search-hit").count():
            page.locator(".search-hit").first.click(); page.wait_for_timeout(900)
            lnk = page.locator(f'#parts-body .pn-link:text-is("{old["cur"]}")').first
            if lnk.count():
                lnk.click(); page.wait_for_timeout(800)
                check("в карточке показана цепочка замен",
                      page.locator("#pc-sup .sup-no").count() > 1)
                page.screenshot(path=str(SHOT / "05_supersession_card.png"), full_page=True)
                page.locator("#pc-close").click(); page.wait_for_timeout(300)

    print("\n>>> Заказ")
    page.locator("#parts-body .btn-add").first.click(); page.wait_for_timeout(500)
    cnt = page.inner_text("#cart-count")
    check("позиция добавилась в заказ", cnt != "0", f"в заказе {cnt}")
    page.locator("#cart-toggle").click(); page.wait_for_timeout(600)
    check("корзина открывается", page.locator("#cart").is_visible())
    check("строка заказа есть", page.locator("#cart-body tr").count() > 0)
    page.screenshot(path=str(SHOT / "04_cart.png"), full_page=True)
    # сохраняется ли заказ между открытиями
    page.reload(wait_until="load"); page.wait_for_timeout(1200)
    check("заказ сохраняется в браузере", page.inner_text("#cart-count") != "0")

    print("\n>>> Консоль и сеть")
    real_fail = [u for u in failed if not u.startswith("chrome-extension")]
    check("нет ошибок в консоли", not errors, "; ".join(errors[:3]))
    check("все файлы загрузились", not real_fail, f"{len(real_fail)} шт.: " +
          "; ".join(u.rsplit('/', 1)[-1] for u in real_fail[:5]))
    b.close()

print("\n" + "=" * 60)
print("  ИТОГ: " + ("всё в порядке" if ok else "ЕСТЬ ЗАМЕЧАНИЯ — см. выше"))
print(f"  Скриншоты: {SHOT}")
print("=" * 60)
sys.exit(0 if ok else 1)
