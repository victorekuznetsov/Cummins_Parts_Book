---
type: "TSB"
doc: "tsb110073"
title_en: "ECM and Engine Distance Offset Issue with INSITE™ Electronic Service Tool"
released: "2011-03-21"
modified: "2011-03-21"
engines:
  - "33239746"
families:
  - "QSK60 CM2150 MCRS"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110073.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110073.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60CM2150MCRS"
  - "год/2011"
---

# ECM and Engine Distance Offset Issue with INSITE™ Electronic Service Tool

> [!abstract] TSB · `tsb110073`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60 CM2150 MCRS
> **Даты:** выпущен 2011-03-21 · изменён 2011-03-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110073.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110073.pdf)

## ECM and Engine Distance Offset Issue with INSITE™ Electronic Service Tool

### Core Issue

INSITE™ 7.4.2 and earlier versions do **not** calculate and display the cumulative information for ECM and Engine Distance Offsets correctly.

The ECM Distance Offset and Engine Distance Offset should be added to the Trip Information - All Trips (Cumulative) ECM Distance and Engine Distance, respectively, to display a total value in Trip Information.

### Confirmation

After an ECM Distance Offset or an Engine Distance Offset is entered, the value in Trip Information - All Trips (Cumulative) for ECM Distance or Engine Distance does **not** change.

### Resolution

This issue will be corrected with INSITE™ 7.5.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
