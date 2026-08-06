#!/usr/bin/env python3
# =====================================================================
# Выгрузка каталога запчастей Cummins (parts.cummins.com) по ESN.
#
#   python crawler.py 37292556 [--part-images] [--no-headless]
#
# Как это работает:
#   1. Playwright открывает SPA и ищет ESN — так заводится анонимная сессия
#      (куки AUTH_TOKEN / IACSESSION / XSRF-TOKEN, пользователь PUBLIC).
#   2. Дальше все вызовы API идут fetch'ем из контекста страницы с заголовком
#      x-xsrf-token (без него шлюз отдаёт 403).
#   3. Картинки качаются через context.request (те же куки).
#
# Результат: data/<ESN>/
#   engine.json          — паспорт двигателя + полный список вариантов исполнения
#   systems.json         — дерево «система -> варианты исполнения»
#   options/<OPT>.json   — состав узла: позиция (callOut), номер, название, кол-во
#   drawings/*.png       — чертежи узлов
#   parts/*.png          — фото деталей (только с --part-images)
#   report.json          — сводка и проверка полноты
# =====================================================================
import sys, io, json, re, time, argparse
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

API  = "https://parts.cummins.com/gateway/api/IACDataServices"
BASE = Path(__file__).parent


def safe(name: str) -> str:
    """Имя файла, пригодное для Windows."""
    return re.sub(r'[<>:"/\\|?*]+', "_", str(name)).strip(". ") or "unnamed"


class Crawler:
    def __init__(self, esn, page, ctx, out, part_images=False):
        self.esn, self.page, self.ctx, self.out = esn, page, ctx, out
        self.part_images = part_images
        self.xsrf = next((c["value"] for c in ctx.cookies()
                          if c["name"] == "XSRF-TOKEN"), None)
        if not self.xsrf:
            raise RuntimeError("не найдена кука XSRF-TOKEN — сессия не завелась")
        self.stats = {"api_calls": 0, "api_errors": [], "downloaded": 0, "missing": []}

    # ---------- транспорт ----------
    def api(self, path, method="GET", body=None, tries=4):
        """Вызов JSON-API из контекста страницы (нужен x-xsrf-token)."""
        url = f"{API}{path}"
        for attempt in range(1, tries + 1):
            try:
                res = self.page.evaluate("""async ([url, xsrf, method, body]) => {
                    const opt = {method, credentials: 'include', headers: {
                        'accept': 'application/json, text/plain, */*',
                        'x-xsrf-token': xsrf}};
                    if (body !== null) {
                        opt.headers['content-type'] = 'application/json';
                        opt.body = JSON.stringify(body);
                    }
                    const r = await fetch(url, opt);
                    return {status: r.status, text: await r.text()};
                }""", [url, self.xsrf, method, body])
                self.stats["api_calls"] += 1
                if res["status"] == 200:
                    return json.loads(res["text"])
                print(f"    ! HTTP {res['status']} ({attempt}/{tries}) {path[:90]}")
            except Exception as e:
                print(f"    ! ошибка ({attempt}/{tries}): {str(e)[:120]}")
            time.sleep(2 * attempt)
        self.stats["api_errors"].append(path)
        return None

    def download(self, url, dest: Path, tries=3):
        """Скачивание бинарника (чертёж/фото) через сессию браузера."""
        if dest.exists() and dest.stat().st_size > 0:
            return True
        for attempt in range(1, tries + 1):
            try:
                r = self.ctx.request.get(url, timeout=60000)
                if r.status == 200:
                    data = r.body()
                    if data:
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        dest.write_bytes(data)
                        self.stats["downloaded"] += 1
                        return True
                elif r.status == 404:
                    return False
            except Exception as e:
                print(f"    ! качаю ({attempt}/{tries}): {str(e)[:100]}")
            time.sleep(1.5 * attempt)
        self.stats["missing"].append(url)
        return False

    # ---------- шаги выгрузки ----------
    def engine_info(self):
        print(">>> Паспорт двигателя и список вариантов исполнения")
        d = self.api(f"/v2/esnInfo/{self.esn}?esnType=mbom")
        if not d:
            raise RuntimeError("не удалось получить esnInfo")
        (self.out / "engine.json").write_text(
            json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"    модель: {d.get('serviceModel')} | CPL {d.get('cpl')} | "
              f"сборка {str(d.get('buildDate'))[:10]} | конфигурация {d.get('marketingConfig')}")
        print(f"    вариантов исполнения: {len(d.get('optionList') or [])}")
        return d

    def kits_and_gaskets(self, options):
        print(">>> Комплекты прокладок и ремкомплекты")
        g = self.api(f"/v2/esnInfo/{self.esn}/gasketSets?esnType=mbom")
        if g is not None:
            (self.out / "gasketSets.json").write_text(
                json.dumps(g, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"    комплектов прокладок: {len(g)}")
        hashes = [o["componentHash"] for o in options if o.get("componentHash")]
        k = self.api(f"/v2/esnInfo/{self.esn}/kitSets?esnType=mbom", "POST", hashes)
        if k is not None:
            (self.out / "kitSets.json").write_text(
                json.dumps(k, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"    ремкомплектов: {len(k)}")

    def systems_index(self, options):
        """Дерево «система -> варианты исполнения» (SPA строит его на клиенте)."""
        tree = {}
        for o in options:
            systems = {s for p in (o.get("parts") or []) for s in (p.get("systems") or [])}
            for s in (systems or {"UNCLASSIFIED"}):
                tree.setdefault(s, []).append({
                    "optionNo": o.get("optionNo"),
                    "optionName": o.get("optionName"),
                    "componentHash": o.get("componentHash"),
                    "graphic": o.get("graphic"),
                })
        (self.out / "systems.json").write_text(
            json.dumps(tree, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f">>> Систем: {len(tree)} — " + ", ".join(sorted(tree)[:12]))
        return tree

    def option_details(self, options):
        print(f">>> Состав узлов ({len(options)} шт.)")
        odir = self.out / "options"; odir.mkdir(exist_ok=True)
        details, graphics = [], set()
        for i, o in enumerate(options, 1):
            optno = o.get("optionNo") or o.get("optionNumber") or f"opt{i}"
            f = odir / f"{safe(optno)}.json"
            if f.exists() and f.stat().st_size > 0:
                d = json.loads(f.read_text(encoding="utf-8"))
            else:
                d = self.api(f"/v2/componentDetails/option?esnType=mbom"
                             f"&componentHash={o['componentHash']}&esn={self.esn}")
                if not d:
                    print(f"    [{i}/{len(options)}] {optno}: НЕ ПОЛУЧЕНО")
                    continue
                f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
                time.sleep(0.25)
            n = sum(len(g.get("parts") or []) for g in (d.get("groups") or []))
            for g in (d.get("graphics") or []):
                if g.get("fileName"):
                    graphics.add(g["fileName"])
            if o.get("graphic"):
                graphics.add(o["graphic"])
            details.append(d)
            if i % 25 == 0 or i == len(options):
                print(f"    [{i}/{len(options)}] {optno}: позиций {n}")
        return details, sorted(graphics)

    def drawings(self, graphics):
        print(f">>> Чертежи ({len(graphics)} шт.)")
        ddir = self.out / "drawings"; ddir.mkdir(exist_ok=True)
        ok = 0
        for i, g in enumerate(graphics, 1):
            url = f"{API}/graphics/rtgraphics/english/parts{g}.png"
            if self.download(url, ddir / f"{safe(g.strip('/').replace('/', '_'))}.png"):
                ok += 1
            if i % 25 == 0 or i == len(graphics):
                print(f"    [{i}/{len(graphics)}] скачано {ok}")
        return ok

    def part_photos(self, part_nos):
        print(f">>> Фото деталей ({len(part_nos)} шт.)")
        pdir = self.out / "parts"; pdir.mkdir(exist_ok=True)
        ok = 0
        for i, pn in enumerate(sorted(part_nos), 1):
            url = f"{API}/graphics/parts/{pn[:3]}/{pn}/{pn}_iso.png"
            if self.download(url, pdir / f"{safe(pn)}.png"):
                ok += 1
            if i % 100 == 0 or i == len(part_nos):
                print(f"    [{i}/{len(part_nos)}] найдено фото {ok}")
        return ok

    def part_details(self, part_nos, views=True, models3d=False):
        """Карточка детали: атрибуты, замены номеров (supersession), где применяется,
        все ракурсы фото и (по флагу) 3D-модель."""
        print(f">>> Карточки деталей ({len(part_nos)} шт.)")
        ddir = self.out / "partdetails"; ddir.mkdir(exist_ok=True)
        pdir = self.out / "parts"; pdir.mkdir(exist_ok=True)
        mdir = self.out / "models3d"
        got = supers = imgs = 0
        nos = sorted(part_nos)
        for i, pn in enumerate(nos, 1):
            f = ddir / f"{safe(pn)}.json"
            if f.exists() and f.stat().st_size > 0:
                d = json.loads(f.read_text(encoding="utf-8"))
            else:
                d = self.api(f"/protected/partDetails?partNo={pn}&smn=")
                if not d:
                    continue
                f.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
                time.sleep(0.15)
            got += 1
            if d.get("supersession"):
                supers += 1
            if views:
                for g in (d.get("graphics") or []):
                    fn = g.get("fileName")
                    if not fn:
                        continue
                    name = fn.rsplit("/", 1)[-1]
                    if self.download(f"{API}/graphics/parts{fn}", pdir / safe(name)):
                        imgs += 1
            if models3d:
                for g in (d.get("objectFile") or []):
                    fn = g.get("fileName")
                    if fn:
                        mdir.mkdir(exist_ok=True)
                        self.download(f"{API}/graphics/parts{fn}",
                                      mdir / safe(fn.rsplit("/", 1)[-1]))
            if i % 50 == 0 or i == len(nos):
                print(f"    [{i}/{len(nos)}] карточек {got}, с заменами {supers}, фото {imgs}")
        return got, supers

    def system_images(self, engine, systems):
        """Иллюстрации систем и общий вид двигателя."""
        idir = self.out / "images"; idir.mkdir(exist_ok=True)
        names = [s.title().replace(" ", "_") for s in systems]
        if engine.get("engineGraphic"):
            names.append(engine["engineGraphic"].replace(".png", ""))
        ok = 0
        for n in names:
            if self.download(f"{API}/graphics/engines/{n}.png", idir / f"{n}.png"):
                ok += 1
        print(f">>> Иллюстрации систем: {ok}/{len(names)}")
        return ok

    def report(self, engine, details, systems, graphics, drawn, photos):
        """Проверка полноты: каждая деталь из состава двигателя должна найтись
        в детализации узлов."""
        from_engine = {p["partNo"] for o in (engine.get("optionList") or [])
                       for p in (o.get("parts") or []) if p.get("partNo")}
        from_details, positions = set(), 0
        for d in details:
            for g in (d.get("groups") or []):
                for pt in (g.get("parts") or []):
                    stack = [pt]
                    while stack:
                        node = stack.pop()
                        pn = (node.get("data") or {}).get("partNo")
                        if pn:
                            from_details.add(pn); positions += 1
                        stack.extend(node.get("children") or [])
        lost = sorted(from_engine - from_details)
        rep = {
            "esn": self.esn,
            "serviceModel": engine.get("serviceModel"),
            "cpl": engine.get("cpl"),
            "buildDate": engine.get("buildDate"),
            "marketingConfig": engine.get("marketingConfig"),
            "options_total": len(engine.get("optionList") or []),
            "options_fetched": len(details),
            "systems": len(systems),
            "positions_total": positions,
            "unique_parts_in_engine": len(from_engine),
            "unique_parts_in_details": len(from_details),
            "parts_lost": lost,
            "graphics_expected": len(graphics),
            "graphics_downloaded": drawn,
            "part_photos": photos,
            "api_calls": self.stats["api_calls"],
            "api_errors": self.stats["api_errors"],
            "downloads_missing": self.stats["missing"][:50],
        }
        (self.out / "report.json").write_text(
            json.dumps(rep, ensure_ascii=False, indent=1), encoding="utf-8")
        print("\n" + "=" * 62)
        print(f"  ESN {self.esn} | {rep['serviceModel']} | CPL {rep['cpl']}")
        print(f"  Узлов: {rep['options_fetched']}/{rep['options_total']}   "
              f"Систем: {rep['systems']}")
        print(f"  Позиций: {rep['positions_total']}   "
              f"Уникальных деталей: {rep['unique_parts_in_details']}")
        print(f"  Чертежей: {drawn}/{len(graphics)}")
        print(f"  ПОТЕРЯНО НОМЕРОВ ДЕТАЛЕЙ: {len(lost)}"
              + (f" -> {lost[:10]}" if lost else "  (ноль — полнота ок)"))
        if rep["api_errors"]:
            print(f"  Ошибок API: {len(rep['api_errors'])}")
        print("=" * 62)
        return rep


def open_session(pw, esn, headless=True):
    b = pw.chromium.launch(headless=headless)
    ctx = b.new_context(viewport={"width": 1700, "height": 1200},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")
    page = ctx.new_page()
    print(">>> Открываю parts.cummins.com")
    for attempt in range(3):
        try:
            page.goto("https://parts.cummins.com/home",
                      wait_until="networkidle", timeout=120000)
            break
        except PWTimeout:
            print(f"    таймаут загрузки, повтор {attempt + 2}/3")
    page.wait_for_timeout(2500)
    try:
        el = page.locator("#onetrust-accept-btn-handler").first
        if el.count() and el.is_visible():
            el.click(timeout=6000)
    except Exception:
        pass
    page.wait_for_timeout(1200)
    # Сессии с главной страницы достаточно: API отвечает по кукам плюс заголовок
    # x-xsrf-token. Заходить в карточку ESN не нужно — у части номеров поиск
    # уводит на страницу результатов, а не в карточку двигателя.
    cookies = {c["name"]: c["value"] for c in ctx.cookies()}
    if "XSRF-TOKEN" not in cookies:
        raise RuntimeError("сессия не завелась: нет куки XSRF-TOKEN")
    print(f">>> Сессия готова, выгружаю ESN {esn}")
    return b, ctx, page


def main():
    ap = argparse.ArgumentParser(description="Выгрузка каталога Cummins по ESN")
    ap.add_argument("esn")
    ap.add_argument("--part-images", action="store_true", help="качать фото деталей")
    ap.add_argument("--part-details", action="store_true",
                    help="карточки деталей: атрибуты, замены номеров, где применяется, все ракурсы")
    ap.add_argument("--models3d", action="store_true", help="качать 3D-модели деталей (.obj/.mtl)")
    ap.add_argument("--no-headless", action="store_true", help="показывать браузер")
    a = ap.parse_args()

    out = BASE / "data" / a.esn
    out.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    with sync_playwright() as pw:
        b, ctx, page = open_session(pw, a.esn, headless=not a.no_headless)
        try:
            c = Crawler(a.esn, page, ctx, out, a.part_images)
            engine = c.engine_info()
            options = engine.get("optionList") or []
            systems = c.systems_index(options)
            c.kits_and_gaskets(options)
            details, graphics = c.option_details(options)
            drawn = c.drawings(graphics)
            c.system_images(engine, systems.keys())
            part_nos = {p["partNo"] for o in options
                        for p in (o.get("parts") or []) if p.get("partNo")}
            photos = c.part_photos(part_nos) if a.part_images else 0
            if a.part_details:
                cards, supers = c.part_details(part_nos, models3d=a.models3d)
                print(f"    карточек деталей: {cards}, из них с заменами номеров: {supers}")
                photos = len(list((out / "parts").glob("*.png")))
            c.report(engine, details, systems, graphics, drawn, photos)
        finally:
            b.close()
    print(f"\nГотово за {time.time() - t0:.0f} c -> {out}")


if __name__ == "__main__":
    main()
