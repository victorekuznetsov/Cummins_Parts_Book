---
type: "TSB"
doc: "tsb100048"
title_en: "INSITE™ Electronic Service Tool 7.4 - Windows® 7 - Internet Explorer® 8 - Fault Information System Issue"
released: "2010-05-11"
modified: "2010-05-11"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
  - "QSM11"
  - "QSX15"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100048.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100048.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "год/2010"
---

# INSITE™ Electronic Service Tool 7.4 - Windows® 7 - Internet Explorer® 8 - Fault Information System Issue

> [!abstract] TSB · `tsb100048`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60, QSM11, QSX15
> **Даты:** выпущен 2010-05-11 · изменён 2010-05-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100048.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100048.pdf)

## INSITE™ Electronic Service Tool 7.4 - Windows® 7 - Internet Explorer® 8 - Fault Information System Issue

### Core Issue

This Technical Service Bulletin describes an issue with INSITE™ electronic service tool version 7.4 (7.4.0.244), on Windows® 7, with Internet Explorer® 8, when opening the fault information system (FIS). After opening a fault code, a script error window will open, instead of the troubleshooting steps.

### Confirmation

All engines supported with INSITE™ electronic service tool.

When opening the troubleshooting steps for a Fault Code with INSITE™ electronic service tool, a Script Error window will open.

None

The older FIS files format includes a pop-up warning window.

None

### Resolution

Click Yes or No on the Script Error window to open the Fault Code troubleshooting steps.

![[19000001.png]]

Screenshot of error message in INSITE™ Update Manager

The FIS files are being reformatted and will have this warning window removed. Periodically check the Cummins INSITE™ Update Manager for updated FIS files.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
