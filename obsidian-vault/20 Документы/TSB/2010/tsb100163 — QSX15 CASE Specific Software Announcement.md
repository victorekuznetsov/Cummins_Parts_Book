---
type: "TSB"
doc: "tsb100163"
title_en: "QSX15 CASE Specific Software Announcement"
modified: "2002-05-31"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100163.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100163.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSX15"
---

# QSX15 CASE Specific Software Announcement

> [!abstract] TSB · `tsb100163`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Даты:** изменён 2002-05-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100163.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100163.pdf)

## QSX15 CASE Specific Software Announcement

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

This Technical Service Bulletin announces a modification to the Case STX 450 tractor and the New Holland TJ 450 tractor that necessitates a change in the electronic control module (ECM) calibration.

The information in This Technical Service Bulletin affects **only** the STX 450 horsepower, and TJ 450 horsepower tractors. It does **not** affect the CNH 375 or 425 horsepower tractor.

Beginning with the Tier II 425 and 450 HP product, CNH utilizes a hydraulically driven cooling fan. The speed at which the fan runs is determined by the following three temperatures:

1. coolant temperature
2. intake manifold temperature
3. hydraulic oil temperature.

In early February 2002, CNH introduced a new charge air cooler with improved efficiency on both the STX 450 and TJ 450 tractors. The improved efficiency of the CAC allows the engine fan to run less often and/or at slower speed, which in turn allows for more available horsepower and better fuel economy. In order to realize this benefit, the ECM calibration was modified to reduce the demand for fan cooling while still controlling the maximum intake manifold temperature to the desired level.

> [!note] Note · Примечание
> The new CAC and new calibration does **not** apply to the STX 425 and TJ 425 tractors.

The original Tier II QSX15 450 HP for CNH used Customer Interface Software option DO 1165. The new DO option for use with the improved CAC is DO 1259. When selecting the calibration for a STX 450 or TJ 450 tractor, the DO comment field will guide the user to the correct calibration. Specifically, the April 2002 ESDN INCAL CD will have the following note in the DO 1259 comment field: COMMENT: TRACTORS WITH IMPROVED COOLING SYSTEM (see Figure 1).

![[19c01391.png]]

Figure 1

For the May 2002 ESDN INCAL CD-ROM, the engine serial number first (ESNF) for the new CAC became known, so the comment fields will read as follows; Before ESN 14027676 or After ESN 14027676 (see Figure 2).

![[19c01392.png]]

Figure 2

> [!note] Note · Примечание
> If DO 1165 is installed in engines built after 14027676, the benefit of the improved CAC will be lost, but the intake manifold temperature will be maintained at an acceptable level to maintain Tier II emissions standards.

> [!note] Note · Примечание
> If DO 1269 is installed in engines built before 14027676, the intake manifold temperature could exceed the maximum allowable temperature and possibly jeopardize compliance of Tier II emission standards. Do **not** use DO 1269 in engines built prior to ESN 14027676.
