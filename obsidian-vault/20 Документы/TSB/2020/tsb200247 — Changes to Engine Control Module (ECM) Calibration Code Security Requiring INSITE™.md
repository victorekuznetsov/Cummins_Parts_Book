---
aliases:
  - "Изменения защиты калибровок ЭБУ: требуется INSITE™ версии 8.7.0 или новее"
type: "TSB"
doc: "tsb200247"
title_en: "Changes to Engine Control Module (ECM) Calibration Code Security Requiring INSITE™ Electronic Service Tool Version 8.7.0 or Newer"
title_ru: "Изменения защиты калибровок ЭБУ: требуется INSITE™ версии 8.7.0 или новее"
released: "2020-12-17"
modified: "2024-10-04"
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
  - "37292556"
  - "37295879"
  - "41340468"
  - "41349633"
  - "41353297"
  - "71156161"
  - "77804810"
  - "80141463"
  - "80248213"
  - "82099327"
  - "85017333"
  - "93058669"
  - "93087701"
  - "93948840"
families:
  - "15N"
  - "C8.3 · 6C8.3"
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
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200247.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb200247.pdf"
tags:
  - "документ/tsb"
  - "двигатель/15N"
  - "двигатель/C8.3"
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
  - "год/2020"
  - "тема/service-tools"
---

# Changes to Engine Control Module (ECM) Calibration Code Security Requiring INSITE™ Electronic Service Tool Version 8.7.0 or Newer
**Изменения защиты калибровок ЭБУ: требуется INSITE™ версии 8.7.0 или новее**

> [!abstract] TSB · `tsb200247`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33224404 — QSK50 CM2150 MCRS CPL 3391|33224404]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41340468 — QSK50 CM2150 MCRS CPL 3728|41340468]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[77804810 — 15N CM2380 M104B CPL 5977|77804810]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** 15N, C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSB6.7, QSK19, QSK23, QSK50, QSK60, QSM11, QST30, QSX15, QSZ13
> **Даты:** выпущен 2020-12-17 · изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200247.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb200247.pdf)

## Changes to Engine Control Module (ECM) Calibration Code Security Requiring INSITE™ Electronic Service Tool Version 8.7.0 or Newer

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Products Affected**

- All electronically controlled engine products

**Issue**

On 10 December 2020, new engine control module (ECM) calibration codes will be released using industry standard encryption for all electronically controlled engine products. These ECM calibration codes are **only** supported in INSITE™ electronic service tool version 8.7.0 and newer. If users do **not** upgrade, users will **not** be able to use any ECM calibrations downloaded through QuickServe® Online (QSOL) or Cal over web after 10 December 2020.

**Resolution**

On 10 December 2020, new ECM calibrations will be released using new industry standard encryption. This will require use of INSITE 8.7.0 or greater when using these calibrations downloaded from Quickserve Online (QSOL) or using the ECM Code Search feature within INSITE™. Cummins Inc. recommends users upgrade to INSITE 8.7.0 as soon as possible. Calibrations released after December 2019 or on an INCAL™ DVD from August 2020 or later can still be used with INSITE 8.7.0.

1. During the installation of the INSITE 8.7.0.exe, the user might see multiple dialog boxes of antivirus detecting suspicious files during the whole installation. The user does **not** need to acknowledge them.

![[19r99693.png]]

Figure 1, Example of Antivirus Dialog Box.

2. If a user wants to use the INSITE 8.7.0 Other Package, the extracted other package can **only** be used once. If user wants to use is a second time, the user needs to delete the extracted package and re-extract the OtherPackage.zip file.

### Document History
