#!/usr/bin/env python3
# =====================================================================
# Быстрая выгрузка карточек деталей Cummins (атрибуты, замены номеров,
# где применяется, все ракурсы фото, 3D-модели) — в несколько потоков.
#
#   python crawl_details.py 37292556 [--workers 8] [--models3d]
#
# Сессию (куки + x-xsrf-token) один раз заводим браузером, дальше всё
# качаем обычным requests: и JSON, и картинки — так в разы быстрее.
# Повторный запуск дозагружает недостающее.
# =====================================================================
import sys, io, json, re, time, argparse, threading
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from playwright.sync_api import sync_playwright

API  = "https://parts.cummins.com/gateway/api/IACDataServices"
BASE = Path(__file__).parent
UA   = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36")


def safe(name: str) -> str:
    return re.sub(r'[<>:"/\\|?*]+', "_", str(name)).strip(". ") or "unnamed"


def new_session():
    """Заводим анонимную сессию браузером и переносим куки в requests."""
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        ctx = b.new_context(user_agent=UA)
        page = ctx.new_page()
        for attempt in range(3):
            try:
                page.goto("https://parts.cummins.com/home",
                          wait_until="networkidle", timeout=120000)
                break
            except Exception:
                print(f"    повтор загрузки сайта {attempt + 2}/3")
        page.wait_for_timeout(2500)
        cookies = {c["name"]: c["value"] for c in ctx.cookies()}
        b.close()
    s = requests.Session()
    s.headers.update({"User-Agent": UA,
                      "Referer": "https://parts.cummins.com/esn-entry/main"})
    for k, v in cookies.items():
        s.cookies.set(k, v, domain="parts.cummins.com")
    xsrf = cookies.get("XSRF-TOKEN", "")
    if not xsrf:
        sys.exit("не удалось получить XSRF-TOKEN — сессия не завелась")
    return s, xsrf


class Fetcher:
    def __init__(self, workers=8):
        self.lock = threading.Lock()
        self.session, self.xsrf = new_session()
        self.workers = workers
        self.stat = {"json": 0, "img": 0, "miss": 0, "err": 0}

    def refresh(self):
        with self.lock:
            print("    ! обновляю сессию")
            self.session, self.xsrf = new_session()

    def get_json(self, path, tries=3):
        for a in range(1, tries + 1):
            try:
                r = self.session.get(API + path, timeout=60, headers={
                    "Accept": "application/json", "x-xsrf-token": self.xsrf})
                if r.status_code == 200:
                    with self.lock:
                        self.stat["json"] += 1
                    return r.json()
                if r.status_code in (401, 403) and a < tries:
                    self.refresh(); continue
                if r.status_code == 404:
                    return None
            except Exception:
                pass
            time.sleep(1.5 * a)
        with self.lock:
            self.stat["err"] += 1
        return None

    def get_file(self, url, dest: Path, tries=3):
        if dest.exists() and dest.stat().st_size > 0:
            return True
        for a in range(1, tries + 1):
            try:
                r = self.session.get(url, timeout=90)
                if r.status_code == 200 and r.content:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    tmp = dest.with_suffix(dest.suffix + ".part")
                    tmp.write_bytes(r.content)
                    tmp.replace(dest)
                    with self.lock:
                        self.stat["img"] += 1
                    return True
                if r.status_code == 404:
                    with self.lock:
                        self.stat["miss"] += 1
                    return False
                if r.status_code in (401, 403) and a < tries:
                    self.refresh(); continue
            except Exception:
                pass
            time.sleep(1.2 * a)
        with self.lock:
            self.stat["err"] += 1
        return False


def main():
    ap = argparse.ArgumentParser(description="Карточки деталей Cummins (параллельно)")
    ap.add_argument("esn")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--models3d", action="store_true", help="качать 3D-модели .obj/.mtl")
    a = ap.parse_args()

    out = BASE / "data" / a.esn
    engine = json.loads((out / "engine.json").read_text(encoding="utf-8"))
    part_nos = sorted({p["partNo"] for o in (engine.get("optionList") or [])
                       for p in (o.get("parts") or []) if p.get("partNo")})
    cdir = out / "partdetails"; cdir.mkdir(parents=True, exist_ok=True)
    pdir = out / "parts";       pdir.mkdir(parents=True, exist_ok=True)
    mdir = out / "models3d"

    print(f">>> Деталей к обработке: {len(part_nos)}, потоков: {a.workers}")
    f = Fetcher(a.workers)
    t0 = time.time()
    done = {"n": 0, "sup": 0}

    def handle(pn):
        card = cdir / f"{safe(pn)}.json"
        if card.exists() and card.stat().st_size > 0:
            d = json.loads(card.read_text(encoding="utf-8"))
        else:
            d = f.get_json(f"/protected/partDetails?partNo={pn}&smn=")
            if not d:
                return None
            card.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
        for g in (d.get("graphics") or []):
            fn = g.get("fileName")
            if fn:
                f.get_file(f"{API}/graphics/parts{fn}", pdir / safe(fn.rsplit("/", 1)[-1]))
        if a.models3d:
            for g in (d.get("objectFile") or []):
                fn = g.get("fileName")
                if fn:
                    f.get_file(f"{API}/graphics/parts{fn}", mdir / safe(fn.rsplit("/", 1)[-1]))
        return bool(d.get("supersession"))

    with ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(handle, pn): pn for pn in part_nos}
        for fut in as_completed(futs):
            r = fut.result()
            done["n"] += 1
            if r:
                done["sup"] += 1
            if done["n"] % 50 == 0 or done["n"] == len(part_nos):
                el = time.time() - t0
                print(f"    [{done['n']}/{len(part_nos)}] карточек {f.stat['json']}, "
                      f"фото {f.stat['img']}, нет фото {f.stat['miss']}, "
                      f"замен {done['sup']} — {el:.0f} c "
                      f"({done['n'] / max(el, 1) * 60:.0f} дет./мин)")

    cards = len(list(cdir.glob("*.json")))
    photos = len(list(pdir.glob("*.png")))
    print("\n" + "=" * 62)
    print(f"  Карточек деталей: {cards}/{len(part_nos)}")
    print(f"  Фото деталей: {photos}   Деталей с заменами номеров: {done['sup']}")
    print(f"  Ошибок: {f.stat['err']}   Время: {time.time() - t0:.0f} c")
    print("=" * 62)


if __name__ == "__main__":
    main()
