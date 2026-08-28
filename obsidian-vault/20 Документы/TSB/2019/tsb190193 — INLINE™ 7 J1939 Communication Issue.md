---
aliases:
  - "Проблема связи J1939 адаптера INLINE™ 7"
type: "TSB"
doc: "tsb190193"
title_en: "INLINE™ 7 J1939 Communication Issue"
title_ru: "Проблема связи J1939 адаптера INLINE™ 7"
released: "2019-11-11"
modified: "2019-11-11"
group: "22 - Service Tools"
engines:
  - "33224404"
  - "33239746"
  - "33239899"
  - "41340468"
  - "41349633"
  - "41353297"
  - "82099327"
  - "93948840"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSB6.7"
  - "QSK19"
  - "QSK50"
  - "QSZ13"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190193.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190193.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSB6.7"
  - "двигатель/QSK19"
  - "двигатель/QSK50"
  - "двигатель/QSZ13"
  - "год/2019"
  - "тема/service-tools"
---

# INLINE™ 7 J1939 Communication Issue
**Проблема связи J1939 адаптера INLINE™ 7**

> [!abstract] TSB · `tsb190193`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK50, QSZ13
> **Даты:** выпущен 2019-11-11 · изменён 2019-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190193.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190193.pdf)

## INLINE™ 7 J1939 Communication Issue

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Products Affected**

- ISX CM870
- ISX CM871
- ISB CM2150
- ISC CM2150
- ISL CM2150

**Issue**

INSITE™ electronic service tool 5200 Error when using INLINE™ 7. See Figure 1 for 5200 Error displayed.

![[22r00348.png]]

Figure 1, INSITE™ Electronic Service Tool 5200 Error.

**Resolution**

- Use J1708 protocol: User can create an INLINE™ 7 J1708 connection using the ECM Connection Wizard in the INSITE™ electronic service tool. See Figure 2.

![[22r00349.png]]

Figure 2, INLINE™ 7 J1708 Connection.

- Use an INLINE™ 6.
- New INLINE™ 7 firmware and drivers are being developed and tested.

### Document History
