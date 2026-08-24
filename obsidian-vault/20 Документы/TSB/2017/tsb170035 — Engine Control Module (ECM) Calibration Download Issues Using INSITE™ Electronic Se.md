---
aliases:
  - "Проблемы загрузки калибровок ЭБУ через INSITE™ 8.2.0"
type: "TSB"
doc: "tsb170035"
title_en: "Engine Control Module (ECM) Calibration Download Issues Using INSITE™ Electronic Service Tool 8.2.0"
title_ru: "Проблемы загрузки калибровок ЭБУ через INSITE™ 8.2.0"
released: "2017-04-25"
modified: "2017-04-25"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170035.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb170035.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "год/2017"
  - "перевод/машинный"
  - "тема/service-tools"
---

# Engine Control Module (ECM) Calibration Download Issues Using INSITE™ Electronic Service Tool 8.2.0
**Проблемы загрузки калибровок ЭБУ через INSITE™ 8.2.0**

> [!abstract] TSB · `tsb170035`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2017-04-25 · изменён 2017-04-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170035.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb170035.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Проблемы загрузки калибровок ЭБУ через INSITE™ 8.2.0

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- Инструменты для электронных услуг INSITETM 8.2.0

**Проблема**

Симптом:

- Ошибочные значения в журналах и функциях и параметрах.
- Неправильные значения, которые использует модуль управления двигателем (ECM). Они **не** видны или настраиваются в инструментах для электронных услуг INSITETM, поэтому наличие проблемы ** не всегда очевидно.

Первопричина:

- При выполнении загрузки калибровки ECM с помощью инструментария 8.2.0 электронного сервиса INSITETM ECM может ** не** правильно получать все значения и записывать неверные данные.

**Проверка**

- Поскольку проблема калибровки ECM может проявляться или не проявляться в электронном сервисном оборудовании INSITETM, проверка проблемы ** невозможна.

**Решение**

- **Не использовать инструмент 8.2.0 для выполнения загрузок калибровки ECM.
- Используйте Cummins Inc. Менеджер обновлений для немедленного обновления инструментария электронных услуг INSITETM до версии 8.2.1.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## Engine Control Module (ECM) Calibration Download Issues Using INSITE™ Electronic Service Tool 8.2.0
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - INSITE™ electronic service tool 8.2.0
>
> **Issue**
>
> Symptom:
>
> - Erroneous values in logs and Features and Parameters.
> - Incorrect values that engine control module (ECM) uses. These are **not** visible or adjustable in INSITE™ electronic service tool, so presence of problem is **not** always apparent.
>
> Root Cause:
>
> - When performing an ECM calibration download with INSITE™ electronic service tool 8.2.0, ECM may **not** receive all values correctly and incorrect data can be written.
>
> **Verification**
>
> - Because ECM calibration issue may or may **not** manifest itself in a visible way in INSITE™ electronic service tool, verification of issue is **not** possible.
>
> **Resolution**
>
> - Do **not** use INSITE™ electronic service tool 8.2.0 to perform ECM calibration downloads.
> - Use Cummins Inc. Update Manager to upgrade INSITE™ electronic service tool to version 8.2.1 immediately.
>
> ### Document History
