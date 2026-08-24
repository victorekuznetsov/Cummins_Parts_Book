#!/bin/bash
# =====================================================================
# Синхронизация публикационной ветки Netlify с рабочей веткой.
#
#   bash tools/sync_publish.sh
#
# Запускать ПОСЛЕ обновления каталога (build_catalog.py + commit/push
# в рабочую ветку). Скрипт вливает рабочую ветку в netlify-publish и
# пушит — Netlify пересоберёт сайт из свежей папки catalog/.
# netlify.toml живёт только в netlify-publish и при слиянии сохраняется.
# =====================================================================
set -e
WORK="claude/cummins-catalogs-cpl-eur6rd"
PUB="netlify-publish"

git fetch origin "$WORK" "$PUB"
CUR="$(git rev-parse --abbrev-ref HEAD)"

git checkout "$PUB"
git merge --no-edit "origin/$WORK"
for i in 1 2 3 4; do
  git push origin "$PUB" && break
  echo "push не прошёл, повтор через $((2**i))с"; sleep $((2**i))
done
git checkout "$CUR"
echo "OK: $PUB обновлён из $WORK, Netlify пересоберёт сайт"
