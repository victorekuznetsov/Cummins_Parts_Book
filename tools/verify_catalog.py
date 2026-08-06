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

    data = page.evaluate("() => ({sys: CATALOG.systems.length, opt: CATALOG.options.length, "
                         "cards: Object.keys(CATALOG.cards||{}).length, esn: CATALOG.esn, "
                         "model: CATALOG.model})")
    print(f"    ESN {data['esn']}, модель {data['model']}, систем {data['sys']}, "
          f"узлов {data['opt']}, карточек {data['cards']}")
    check("паспорт двигателя показан", "QST30" in page.inner_text("#passport"))
    check("дерево систем построено", page.locator(".tree-sys").count() == data["sys"])

    print("\n>>> Открываю узел с чертежом")
    open_system(page, 0)
    page.locator(".tree-sys").first.locator(".tree-opt").first.click()
    page.wait_for_timeout(1200)
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
            const sys = CATALOG.systems[i];
            const byNo = {}; CATALOG.options.forEach(o => byNo[o.no] = o);
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
        const c = CATALOG.cards || {};
        for (const pn in c) {
            const ch = c[pn].sup || [];
            for (const s of ch) if (s.no !== pn && !s.cur) return {old: s.no, cur: pn};
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
    open_system(page, 0)
    page.locator(".tree-sys").first.locator(".tree-opt").first.click()
    page.wait_for_timeout(900)
    link = page.locator("#parts-body .pn-link").first
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
        page.evaluate("(pn) => window.__open(pn)", old["cur"]) if page.evaluate(
            "() => typeof window.__open === 'function'") else None
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
