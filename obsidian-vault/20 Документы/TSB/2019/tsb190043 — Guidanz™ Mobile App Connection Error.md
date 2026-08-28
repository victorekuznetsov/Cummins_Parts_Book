---
aliases:
  - "Ошибка подключения мобильного приложения Guidanz™"
type: "TSB"
doc: "tsb190043"
title_en: "Guidanz™ Mobile App Connection Error"
title_ru: "Ошибка подключения мобильного приложения Guidanz™"
released: "2019-04-09"
modified: "2024-10-04"
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
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190043.pdf"
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

# Guidanz™ Mobile App Connection Error
**Ошибка подключения мобильного приложения Guidanz™**

> [!abstract] TSB · `tsb190043`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK50, QSZ13
> **Даты:** выпущен 2019-04-09 · изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb190043.pdf)

## Guidanz™ Mobile App Connection Error

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- All electronically controlled engine products released after 2007

**IssueSymptom:**

Guidanz™ mobile app error “MODULE COMMUNICATION PROBLEM” appears while attempting Bluetooth connection to an INLINE™ 7 datalink adapter while USB cable from INLINE™ 7 datalink adapter is physically connected to a computer. See Figure 1 below.

Verification

- INLINE™ 7 datalink adapter is connected to unit and is also physically connected to computer using USB cable

AND

- Guidanz™ mobile app Bluetooth connection is attempted to INLINE™ 7

AND

- Guidanz™ mobile app error “MODULE COMMUNICATION PROBLEM” appears

![[22r00301.png]]

**Resolution**

Physically disconnect the USB cable running from the computer to the INLINE™ 7 datalink adapter when attempting Bluetooth connection with the Guidanz™ mobile app.

### Document History
