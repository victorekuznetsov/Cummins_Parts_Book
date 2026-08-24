# Скрипты сборки хранилища

Порядок запуска (из каталога репозитория `Cummins_Parts_Book`, где лежат
`bulletins/`, `data/`, `drawings/`):

```
python3 kb_build/build_docs.py       # HTML QuickServe -> Markdown + иллюстрации из PDF
python3 kb_build/verify_figures.py   # проверка сопоставления иллюстраций голосованием
python3 kb_build/build_catalog.py    # data/<ESN>.js -> детали, узлы, комплекты
python3 kb_build/build_machines.py   # каталоги и ремонт машин NHL
python3 kb_build/copy_media.py       # чертежи, фото деталей, графика машин
python3 kb_build/write_docs.py       # заметки документов
python3 kb_build/write_catalog.py    # заметки каталога
python3 kb_build/write_machines.py   # заметки машин
python3 kb_build/build_index.py      # главная, индексы, темы
python3 kb_build/fix_missing_figs.py # пометки для не извлечённых иллюстраций
python3 kb_build/check_links.py      # проверка целостности ссылок
```

Зависимости: `beautifulsoup4`, `lxml`, `pymupdf`, `pillow`.

Пути задаются переменными окружения `KB_SRC`, `KB_VAULT`, `KB_NTE200`,
`KB_NTE240`, `KB_TR100` (значения по умолчанию — в `common.py`).

`ru_docs.json` и `ru_parts.json` — словари русских названий документов и
деталей; при новой выгрузке достаточно дополнить их новыми строками.
