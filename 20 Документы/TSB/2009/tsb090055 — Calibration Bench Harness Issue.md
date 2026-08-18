---
aliases:
  - "Проблема стендового калибровочного жгута"
type: "TSB"
doc: "tsb090055"
title_en: "Calibration Bench Harness Issue"
title_ru: "Проблема стендового калибровочного жгута"
released: "2009-08-04"
modified: "2009-08-04"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090055.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb090055.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "год/2009"
  - "тема/service-tools"
---

# Calibration Bench Harness Issue
**Проблема стендового калибровочного жгута**

> [!abstract] TSB · `tsb090055`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2009-08-04 · изменён 2009-08-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2009/tsb090055.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb090055.pdf)

## Calibration Bench Harness Issue

### Core Issue

This Early Field Notification describes an issue with the CM2150 calibration bench harness, Part Number 4918583. This cable presently uses the Cummins® Engine Network (CEN) for J1939 connections between a CM2150 electronic control module (ECM) and an electronic service tool (e.g. INSITE™) instead of the public J1939 network. Connections using CEN could possibly cause the ECM source address to be different than described in service manuals, specifically for engines with multi-module systems. Also, connection attempts made using this bench harness could possibly **only** succeed, if the attempt is made within a few seconds of key ON.

### Confirmation

- ISB CM2150
- ISC CM2150
- ISL CM2150
- B3.9/5.9/C8.3 CM2150
- ISDe CM2150C
- ISLe CM2150
- ISBe4 (4 and 6 cylinder) CM2150E
- ISB4.5, 6.7 ISD4.5, 6.7 CM2150 SN (Euro 4.5)
- ISB4.5, 6.7 ISD4.5, 6.7 CM2150 SN (Euro 5)
- ISL8.9 CM2150 SN (Euro 4.5)
- ISL8.9 CM2150 SN (Euro 5)
- ISLe CM2150C
- QSB3.3 CM2150
- QSK19 CM2150 MCRS / Power Gen
- QSK38 CM2150 MCRS / Power Gen
- QSK50 CM2150 MCRS / Power Gen
- QSK60 CM2150 MCRS / Power Gen

The use of bench calibration harness, Part Number 4918583, with a WO number (listed at the bottom of the label on the cable), less than 190363, could possibly exhibit one of the following issues:

1. An ECM that is calibrated will claim a different SAE J1939 source address as decribed in the service manuals. For example, a primary ECM from a multi-module system (switched to "PRIM" on the attached multiple module harness) normally claims SAE J1939 source address 00. On the CEN network with the same setup, the claimed SAE J1939 source address is 01 (which is the same for the secondary ECM on the public J1939 network).
2. An ECM that is calibrated and physically connected to an INLINE™ data link adapter, the CAN/J1939 light will **only** flash for a few seconds after a key ON. This light should remain flashing.

One of the symptoms mentioned in the "Symptoms and Observations" section of this Early Field Notification and cable, Part Number 4918583, with a WO number less than 190363.

Bench calibration harness, Part Number 4918583, uses the CEN network for the J1939 connections.

None.

### Resolution

Bench calibration harness, Part Number 4918583, has been rewired to use the public J1939 network. These new cables will have a WO number of 190363 or greater. Cables with WO number less than 190363 can be modified to use the public J1939 network.

To correct these cables, move terminal 51 to terminal location 01 and terminal 31 to terminal 21 on the OEM connector, using terminal removal tool, Part Number 3824815, or equivalent. The terminal removal procedure for Deutsch™ DRC connectors can be found in the following procedure in the appropriate Troubleshooting and Repair Manual. [[99-019-204 — Deutsch DRC Connector Series|Refer to Procedure 019-204 in Section 19.]]

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
