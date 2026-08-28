---
type: "TSB"
doc: "tsb190041"
title_en: "Unable to Create Engine Control Module (ECM) Work Order Image Using INLINE 6 and J1708 Communication Protocol"
modified: "2019-03-22"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190041.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190041.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
---

# Unable to Create Engine Control Module (ECM) Work Order Image Using INLINE 6 and J1708 Communication Protocol

> [!abstract] TSB · `tsb190041`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Даты:** изменён 2019-03-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190041.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190041.pdf)

## Unable to Create Engine Control Module (ECM) Work Order Image Using INLINE 6 and J1708 Communication Protocol

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Products Affected**

- B Gas Plus CM556
- C Gas Plus CM556
- ISB CM850
- ISBE CM800
- ISBe4 CM850
- ISC CM850
- ISL CM850
- ISLe4 CM850
- ISM CM570
- ISM CM570
- ISM CM870
- ISM CM875
- ISX CM570
- ISX CM870
- QSB3.9 30 CM550
- QSB4.5 30 CM550
- QSB5.9 30 CM550
- QSB5.9 44 CM550
- QSC8.3 CM554
- QSL9 CM554
- QSM11CM570
- QSX15 CM570

**Issue**

On engine programs that can use both J1708 and J1939 communication protocols, when trying to create a work order image with INSITE™ electronic service tool using J1708 protocol and INLINE™ 6 datalink adapter, the work order creation fails between 15 to 30% and error 10431 will be displayed.

**Resolution**

To create an engine control module (ECM) work order image, use the J1939 protocol with INLINE™ 6 datalink adapter, or use an INLINE™ 7 datalink adapter if available.

### Document History
