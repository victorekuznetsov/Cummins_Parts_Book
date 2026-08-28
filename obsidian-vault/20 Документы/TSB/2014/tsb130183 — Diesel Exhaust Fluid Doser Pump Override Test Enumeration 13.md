---
aliases:
  - "Тест насоса-дозатора DEF, перечисление 13"
type: "TSB"
doc: "tsb130183"
title_en: "Diesel Exhaust Fluid Doser Pump Override Test Enumeration 13"
title_ru: "Тест насоса-дозатора DEF, перечисление 13"
released: "2014-01-09"
modified: "2014-01-09"
group: "22 - Service Tools"
engines:
  - "41349633"
  - "41353297"
  - "82099327"
  - "85017333"
  - "93948840"
families:
  - "QSB6.7"
  - "QSK19"
  - "QSK23"
  - "QSZ13"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130183.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb130183.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "двигатель/QSZ13"
  - "год/2014"
  - "тема/service-tools"
---

# Diesel Exhaust Fluid Doser Pump Override Test Enumeration 13
**Тест насоса-дозатора DEF, перечисление 13**

> [!abstract] TSB · `tsb130183`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** QSB6.7, QSK19, QSK23, QSZ13
> **Даты:** выпущен 2014-01-09 · изменён 2014-01-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2013/tsb130183.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb130183.pdf)

## Diesel Exhaust Fluid Doser Pump Override Test Enumeration 13

### Core Issue

When running this test, INSITE™ electronic service tool could display the following:

"The test status parameter has a value outside of the expected range. The value of the test status parameter is equal to 13."

This will be displayed while the system is dosing. The test will automatically continue after dosing has completed. The issue is due to the fact that the engine control module (ECM) software supported this enumeration before it was requested in INSITE™ electronic service tool.

### Confirmation

N/A

### Resolution

This message will be updated to “Please wait while the system is dosing.” with the release of INSITE™ 8.0.1

![[19r00194.png]]

INSITE™ electronic service tool display

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
