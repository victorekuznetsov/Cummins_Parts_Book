---
type: "TSB"
doc: "tsb110191"
title_en: "INSITE™ 7.5 Features and Parameters Issues with QSM11 and QSX15"
released: "2011-07-11"
modified: "2011-07-11"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110191.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110191.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "год/2011"
---

# INSITE™ 7.5 Features and Parameters Issues with QSM11 and QSX15

> [!abstract] TSB · `tsb110191`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Даты:** выпущен 2011-07-11 · изменён 2011-07-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110191.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110191.pdf)

## INSITE™ 7.5 Features and Parameters Issues with QSM11 and QSX15

### Core Issue

On QSM11 and QSX15 engines, INSITE™ electronic service tool 7.5.0.234 displays several parameters under Governor Setup as locked and without an ECM Value. These parameters include:

- Breakpoint 1 Speed
- Droop at Breakpoint 1
- Droop at Maximum Throttle
- Droop at Minimum Throttle
- Isochronous Breakpoint Speed

The ECM Values for these parameters are displayed as blank and can **not** be adjusted.

### Confirmation

These parameters are locked and do **not** display any ECM Values under Governor Setup.

### Resolution

As a work-around, these parameters can be adjusted under the feature Switched Droop\\Breakpoint 1.

This issue is under investigation

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
