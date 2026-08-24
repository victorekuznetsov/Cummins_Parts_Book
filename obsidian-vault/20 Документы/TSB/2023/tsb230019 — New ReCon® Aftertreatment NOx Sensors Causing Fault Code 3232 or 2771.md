---
aliases:
  - "Новые датчики NOx ReCon® вызывают коды 3232 или 2771"
type: "TSB"
doc: "tsb230019"
title_en: "New ReCon® Aftertreatment NOx Sensors Causing Fault Code 3232 or 2771"
title_ru: "Новые датчики NOx ReCon® вызывают коды 3232 или 2771"
released: "2023-04-04"
modified: "2023-04-04"
group: "19 - Electronic Engine Controls"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 1
lang: "ru+en"
translation: "машинный черновик"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb230019.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "год/2023"
  - "перевод/машинный"
  - "тема/electronic-engine-controls"
---

# New ReCon® Aftertreatment NOx Sensors Causing Fault Code 3232 or 2771
**Новые датчики NOx ReCon® вызывают коды 3232 или 2771**

> [!abstract] TSB · `tsb230019`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2023-04-04 · изменён 2023-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb230019.pdf)

> [!info]- Перевод на русский — машинный черновик
> Русский текст получен автоматическим переводом с английского
> с подстановкой отраслевой терминологии Cummins; он не
> проходил редакторскую вычитку.
> **Юридически значим только английский оригинал** — он
> приведён в свёрнутом блоке в конце заметки и в PDF.


## Новые датчики NOx ReCon® вызывают коды 3232 или 2771

### Положение о гарантии

Сведения в этом документе не изменяют действующие гарантийные обязательства и практику ремонта и не дают оснований для работ по программам TRP или Campaign.

### Содержание

**Затронутая продукция**

- Все продукты, использующие датчик NOx после обработки

** Резюме проблемы**

Симптом:

- После установки «нового» датчика после обработки впускного NOx ReCon® (RX) активен код по умолчанию 3232.
- После установки нового датчика NOx после обработки ReCon® (RX) активен код ошибки 2771.

Первопричина:

- Проблема качества датчиков NOx была выявлена в ограниченном количестве датчиков, изготовленных до 19 января 2023 года.

**Проверка**

Код 3232 или 2771 по умолчанию активен сразу после установки «нового» датчика NOx после обработки ReCon® (RX). Эта проблема *** затрагивает только датчики NOx ReCon® (RX) после обработки (Частные номера перечислены в таблице 1), которые прошли процесс восстановления. Эти датчики NOx после обработки могут быть идентифицированы встроенным разъёмом, который присутствует в проводах датчика NOx после обработки, как показано на рисунке 1.

| Таблица 1, Поврежденный ReCon® После обработки NOx Датчик Части Номера |  |
|---|---|
| Номер детали | Описание сенсора |
| 4326862RX | ReCon® После обработки Ввод NOx-сенсора |
| 4326865RX | ReCon® После обработки Ввод NOx-сенсора |
| 4326867RX | ReCon® После обработки Ввод NOx-сенсора |
| 4326870RX | ReCon® После обработки Ввод NOx-сенсора |
| 4326873RX | ReCon® После обработки Ввод NOx-сенсора |
| 4327153RX | ReCon® После обработки Ввод NOx-сенсора |
| 3687930RX | ReCon® После обработки Ввод NOx-сенсора |
| 3688978RX | ReCon® После обработки Ввод NOx-сенсора |
| 5289662RX | ReCon® После обработки Ввод NOx-сенсора |
| 5295473RX | ReCon® После обработки Ввод NOx-сенсора |
| 4326861RX | ReCon® После обработки выходной NOx-сенсор |
| 4326863RX | ReCon® После обработки выходной NOx-сенсор |
| 4326864RX | ReCon® После обработки выходной NOx-сенсор |
| 4326866RX | ReCon® После обработки выходной NOx-сенсор |
| 4326868RX | ReCon® После обработки выходной NOx-сенсор |
| 4326869RX | ReCon® После обработки выходной NOx-сенсор |
| 4326871RX | ReCon® После обработки выходной NOx-сенсор |
| 4326872RX | ReCon® После обработки выходной NOx-сенсор |
| 4326874RX | ReCon® После обработки выходной NOx-сенсор |
| 5419105RX | ReCon® После обработки выходной NOx-сенсор |

![[19r99901.png]]

Рисунок 1 После обработки NOx датчик зондирования Inline Connector.

**Решение**

Заменить датчик NOx после обработки. См. соответствующее Руководство по обслуживанию. Справочная процедура 019-451 или 019-463 в разделе 19.

### История изменений документа


> [!quote]- Original (English) · английский оригинал
> ## New ReCon® Aftertreatment NOx Sensors Causing Fault Code 3232 or 2771
>
> ### Warranty Statement
>
> The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
>
> ### Contents
>
> **Product Affected**
>
> - All products utilizing an aftertreatment NOx sensor
>
> **Issue Summary**
>
> Symptom:
>
> - After installation of a “new” ReCon® (RX) aftertreatment intake NOx sensor, Fault Code 3232 is active.
> - After installation of a “new” ReCon® (RX) aftertreatment outlet NOx sensor, Fault Code 2771 is active.
>
> Root Cause:
>
> - An aftertreatment NOx sensor quality issue was identified in a limited number of sensors manufactured before 19 January 2023.
>
> **Verification**
>
> Fault Code 3232 or 2771 is active at key-on immediately after installing a “new” ReCon® (RX) aftertreatment NOx sensor. This issue **only** affects ReCon® (RX) aftertreatment NOx sensors (Part numbers are listed in Table 1) that have gone through the remanufacturing process. These aftertreatment NOx sensors can be identified by the inline connector that is present in the aftertreatment NOx sensor probe wiring as shown in Figure 1.
>
> | Table 1, Affected ReCon® Aftertreatment NOx Sensor Part Numbers |  |
> |---|---|
> | Part Number | Sensor Description |
> | 4326862RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 4326865RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 4326867RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 4326870RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 4326873RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 4327153RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 3687930RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 3688978RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 5289662RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 5295473RX | ReCon® Aftertreatment Intake NOx Sensor |
> | 4326861RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326863RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326864RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326866RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326868RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326869RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326871RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326872RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 4326874RX | ReCon® Aftertreatment Outlet NOx Sensor |
> | 5419105RX | ReCon® Aftertreatment Outlet NOx Sensor |
>
> Figure 1, Aftertreatment NOx Sensor Probe Inline Connector.
>
> **Resolution**
>
> Replace the aftertreatment NOx sensor. See corresponding Service Manual. Reference Procedure 019-451 or 019-463 in Section 19.
>
> ### Document History
