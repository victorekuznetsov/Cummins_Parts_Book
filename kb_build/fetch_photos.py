#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Скачивает фотографии деталей с parts.cummins.com и кладёт их рядом с
каталогом, чтобы база работала без интернета.

Адрес собирается из имени файла: 3020995_iso -> 302/3020995/3020995_iso.png
Картинка ужимается так же, как локальная выгрузка: длинная сторона 520 px,
JPEG качества 80 — примерно 12 КБ на снимок.
"""
import concurrent.futures as cf
import io
import json
import os
import sys
import threading
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PIL import Image

from common import BUILD, load_json

OUT = "/home/user/kb_web/assets/photos"
STATE = os.path.join(BUILD, "state_photos.json")
BASE = "https://parts.cummins.com/graphics/parts"
MAXSIDE = 520
QUALITY = 80
WORKERS = 16
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

lock = threading.Lock()
done = miss = fail = 0


def url_of(base):
    num = base.split("_")[0]
    return f"{BASE}/{base[:3]}/{num}/{base}.png"


def fetch(base):
    """Скачивает и сжимает один снимок. True — записан, None — нет на сервере."""
    global done, miss, fail
    dst = os.path.join(OUT, base + ".jpg")
    req = urllib.request.Request(url_of(base), headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
    except Exception as exc:                                   # noqa: BLE001
        code = getattr(exc, "code", None)
        with lock:
            if code == 404:
                miss += 1
                return None
            fail += 1
        return False
    try:
        im = Image.open(io.BytesIO(raw))
        im = im.convert("RGB")
        w, h = im.size
        if max(w, h) > MAXSIDE:
            k = MAXSIDE / max(w, h)
            im = im.resize((max(1, int(w * k)), max(1, int(h * k))), Image.LANCZOS)
        im.save(dst, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    except Exception:                                          # noqa: BLE001
        with lock:
            fail += 1
        return False
    with lock:
        done += 1
    return True


def main():
    os.makedirs(OUT, exist_ok=True)
    cat = load_json(os.path.join(BUILD, "state_catalog.json"), {})
    want = set()
    for p in cat.get("parts", {}).values():
        for f in (p.get("photos") or []):
            want.add(os.path.splitext(os.path.basename(f))[0])
    have = {os.path.splitext(f)[0] for f in os.listdir(OUT)}
    state = load_json(STATE, {})
    gone = set(state.get("нет на сервере", []))
    todo = sorted(want - have - gone)
    print(f"фото в каталоге: {len(want)} · уже есть: {len(want & have)} · "
          f"качать: {len(todo)}", flush=True)

    t0 = time.time()
    missing = []
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(fetch, b): b for b in todo}
        for n, f in enumerate(cf.as_completed(futs), 1):
            if f.result() is None:
                missing.append(futs[f])
            if n % 500 == 0:
                dt = time.time() - t0
                print(f"  {n}/{len(todo)} · записано {done}, нет на сервере {miss}, "
                      f"сбоев {fail} · {dt:.0f} c · {n/dt:.1f} шт/с", flush=True)

    state["нет на сервере"] = sorted(gone | set(missing))
    json.dump(state, open(STATE, "w", encoding="utf-8"), ensure_ascii=False)
    total = len(os.listdir(OUT))
    size = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
    print(f"готово: записано {done}, нет на сервере {miss}, сбоев {fail}, "
          f"{time.time()-t0:.0f} c")
    print(f"всего снимков: {total}, объём {size/1048576:.0f} МБ")


if __name__ == "__main__":
    main()
