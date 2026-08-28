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
  - "33210083"
  - "33219033"
  - "33224343"
  - "33224404"
  - "33239746"
  - "33239899"
  - "35354607"
  - "35373113"
  - "37269910"
  - "37280605"
  - "37292556"
  - "37295879"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93948840"
families:
  - "K19"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSK50"
  - "QSK60"
  - "QSM11"
  - "QST30"
  - "QSX15"
  - "QSZ13"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170035.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb170035.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K19"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSK50"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QST30"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "год/2017"
  - "тема/service-tools"
---

# Engine Control Module (ECM) Calibration Download Issues Using INSITE™ Electronic Service Tool 8.2.0
**Проблемы загрузки калибровок ЭБУ через INSITE™ 8.2.0**

> [!abstract] TSB · `tsb170035`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K19, K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSM11, QST30, QSX15, QSZ13
> **Даты:** выпущен 2017-04-25 · изменён 2017-04-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170035.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb170035.pdf)

## Engine Control Module (ECM) Calibration Download Issues Using INSITE™ Electronic Service Tool 8.2.0

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- INSITE™ electronic service tool 8.2.0

**Issue**

Symptom:

- Erroneous values in logs and Features and Parameters.
- Incorrect values that engine control module (ECM) uses. These are **not** visible or adjustable in INSITE™ electronic service tool, so presence of problem is **not** always apparent.

Root Cause:

- When performing an ECM calibration download with INSITE™ electronic service tool 8.2.0, ECM may **not** receive all values correctly and incorrect data can be written.

**Verification**

- Because ECM calibration issue may or may **not** manifest itself in a visible way in INSITE™ electronic service tool, verification of issue is **not** possible.

**Resolution**

- Do **not** use INSITE™ electronic service tool 8.2.0 to perform ECM calibration downloads.
- Use Cummins Inc. Update Manager to upgrade INSITE™ electronic service tool to version 8.2.1 immediately.

### Document History
