#!/bin/bash
# Тонкая ветка для деплоя на Vercel: только то, что нужно сайту.
#
#   bash build/make_deploy_branch.sh [ветка-источник] [ветка-назначение]
#
# Что выкинуть — в переменной DROP (через пробел). По умолчанию — тонкая
# сборка для Vercel; для офлайн-копии каталога с базой знаний оставляют
# картинки: DROP="rawdata bulletins obsidian-vault quickserve"
#
# В деплой не попадают тяжёлые папки: выгрузка EPC (rawdata/), PDF документов
# (bulletins/), фотографии деталей (parts/, assets/), иллюстрации процедур,
# хранилище Obsidian. Каталог и база знаний работают полностью, кроме
# картинок в документах и локальных PDF — вместо них ссылки на QuickServe,
# фото деталей подтягиваются с parts.cummins.com.
set -e
SRC=${1:-$(git rev-parse --abbrev-ref HEAD)}
DST=${2:-deploy-vercel}
read -r -a DROP <<< "${DROP:-rawdata bulletins parts assets obsidian-vault fleet quickserve build fetch_raw.py}"

git diff --quiet && git diff --cached --quiet || {
  echo "рабочее дерево не чисто — сначала закоммитьте изменения"; exit 1; }
git checkout -q "$SRC"
git checkout -q -B "$DST"
for p in "${DROP[@]}"; do
  git rm -r -q --cached --ignore-unmatch "$p" > /dev/null
done
python3 - <<'PY'
import io
p = "index.html"
s = io.open(p, encoding="utf-8").read()
mark = "window.KB_LOCAL_FILES"
if mark not in s:
    anchor = '<script src="kb.js"></script>'
    assert s.count(anchor) == 1
    s = s.replace(anchor,
        "<script>\n"
        "  /* тонкий деплой: PDF документов и иллюстрации в этой сборке не\n"
        "     выкладываются — база знаний подставляет ссылки на QuickServe,\n"
        "     фотографии деталей берутся с parts.cummins.com */\n"
        "  window.KB_LOCAL_FILES = false;\n"
        "</script>\n" + anchor)
    io.open(p, "w", encoding="utf-8").write(s)
PY
git add index.html
git commit -q -m "Тонкая сборка для Vercel: каталог и база знаний без тяжёлых файлов

Собрано из $SRC ($(git rev-parse --short "$SRC")) скриптом build/make_deploy_branch.sh.
Без rawdata/, bulletins/, parts/, assets/ и obsidian-vault/: PDF документов и
иллюстрации открываются на QuickServe, фото деталей — с parts.cummins.com.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_019z4QTaHgUP1VTtVGmsGxoD"
echo "файлов в ветке: $(git ls-tree -r --name-only HEAD | wc -l)"
echo "объём: $(git ls-tree -r -l HEAD | awk '{n+=$4} END {printf "%.0f МБ\n", n/1048576}')"
# -f: на тонкой ветке лишние папки числятся неотслеживаемыми, обычный
# checkout откажется их перезаписывать своими же файлами
git checkout -f -q "$SRC"
echo "ветка $DST готова (вернулись на $SRC)"
