---
aliases:
  - "Введение термопарного датчика температуры ОГ (EGTS)"
type: "TSB"
doc: "tsb210002"
title_en: "New Thermocouple Exhaust Gas Temperature Sensor (EGTS) Introduction"
title_ru: "Введение термопарного датчика температуры ОГ (EGTS)"
modified: "2021-07-02"
engines:
  - "33239746"
families:
  - "QSK60 CM2150 MCRS"
parts:
  - "3093956"
  - "3657721"
  - "4951876"
  - "5376109"
  - "5538111"
  - "5538112"
  - "5538113"
  - "5538141"
  - "5538755"
  - "5572259"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210002.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210002.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60CM2150MCRS"
---

# New Thermocouple Exhaust Gas Temperature Sensor (EGTS) Introduction
**Введение термопарного датчика температуры ОГ (EGTS)**

> [!abstract] TSB · `tsb210002`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60 CM2150 MCRS
> **Даты:** изменён 2021-07-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210002.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210002.pdf)

## New Thermocouple Exhaust Gas Temperature Sensor (EGTS) Introduction

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QSK60 CM2150 MCRS

**Issue**

Symptom:

- EGTS Fault Codes (FCs): FC671, FC672, FC673, FC674, FC675, FC676, FC677, FC678, FC722, FC723, FC724, FC725, FC726, FC727, FC728, FC1521, FC1522, FC1523, FC1524, FC1525, FC1526, FC1527, FC1529, FC1532, FC1533, FC1534, FC1535, FC1536, FC1618, FC1619, FC2735, FC2736.
- No reading or incorrect EGTS signal to engine control module (ECM).

Root Cause:

- Internal EGTS damage that is **not** visually detectable. Fracture of the EGTS's platinum rhodium wire. Thermistor EGTS are unable to withstand vibrations experienced during normal engine operation.

**Verification**

- Use a multimeter to measure across the terminals of the EGTS to check for high resistance (open circuit).
- Use of recommended Cummins® electronic service tool or equivalent to confirm presence of any of the fault codes listed above.

**Resolution**

Exhaust Gas Temperature Sensors

Compatible Left Bank and Right Bank Main Engine Wiring Harnesses.

The main engine wiring harnesses now have an additional converter box connector breakout. This can be found on both the Left Bank (LB) and Right Bank (RB) main engine wiring harnesses.

![[19r99707.png]]

Figure 1, Left: New Thermocouple EGTS. Right: Existing Thermistor EGTS.

![[19r99714.png]]

Figure 2, New Converter Box.

Compatible Left Bank and Right Bank Injector/ EGTS Wiring Harnesses.

The internal wires of the injector/ EGTS wiring harnesses have been changed to wires which support the K-type thermocouples. The harness connectors have been combined to one single bigger connector which connects to the main engine harnesses.

![[19r99715.png]]

Figure 3, New Wiring Harness Connection Point.

Left Bank and Right Bank Converter Boxes and Mounting Brackets

Two converter boxes are required to house and protect the internal signal conversion modules. The internal signal conversion modules process the thermocouple EGTS's signals for the engine's ECMs. Both LB and RB converter boxes are mounted on the air intake manifold of the engine.

![[19r99716.png]]

Figure 4, Converter Box Mounted to Air Intake Manifold.

Electronic Control Module (ECM) Calibrations

A revised ECM calibration is needed to recognize, transmit, and interpret the signals of the thermocouple sensors. See Technical Service Bulletin, Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy, [[tsb210137 — Exhaust Gas Temperature (EGT) Sensor Types and Selection Strategy\|TSB210137]], for more details on the new ECM calibrations.

**Service Instructions**

For engines to use the thermocouple EGTS the following hardware is required:

- Compatible Left Bank and Right Bank Main engine wiring harnesses.
- Compatible Left Bank and Right Bank injector/ EGTS wiring harnesses.
- Left Bank and Right Bank converter boxes and mounting brackets.
- Compatible ECM calibrations.

**Service Parts Availability**

Service parts are available. See Table 1 for part numbers.

| Table 1, Service Parts |  |  |  |  |  |
|---|---|---|---|---|---|
| Part Description | Existing Part Number | Obsolete | Superseded | New Part Number | Quantity Per Engine |
| Temperature, Sensor | 4954450 | No | No | [[5376109]] | 16 |
| Clip | - | - | - | [[3657721]] or 108722 | 16 |
| Sensor Adapter | - | - | - | [[4951876]] | 16 |
| LB Main Harness- Industrial | 5374880 | No | No | [[5538755]] | 1 |
| RB Main Harness - Industrial | 3642416 | No | No | [[5538111]] | 1 |
| LB Injector/ EGTS Harness | 5375395 | No | No | [[5538113]] | 2 |
| RB Injector/ EGTS Harness | 5375396 | No | No | [[5538112]] | 2 |
| Convertor Box Mounting Bracket | - | - | - | [[5538141]] | 2 |
| Analog Convertor Box | - | - | - | [[5572259]] | 2 |
| Hexagon Flange Head Cap Screw | - | - | - | [[3093956]] | 16 |

**Part Compatibility**

Thermocouple EGTS are **not** able to be mixed with the thermistor EGTS on the same engine.

**Part Identification**

The new thermocouple EGTS are a “fish-hook” design which also mounts in each of the cylinder heads and have dark orange cables.

![[19r99717.png]]

Figure 5, New Thermocouple EGTS.

**Production Status**

Implemented for production. See Table 2.

| Table 2, Production Information |  |  |
|---|---|---|
| ESN First | Build Date 1 | Plant |
| 33222681 | 2 September 2020 | Daventry Engine Plant |
| 1 Engine build date can be found on engine dataplate. |  |  |

**Publications Affected**

| Table 3, Publications Affected |  |  |  |  |  |
|---|---|---|---|---|---|
| Manual Type | Engine | Bulletin Number | Procedure Title | Procedure | Section |
| Service Manual | QSK60 CM2150 MCRS | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] | Exhaust Gas Temperature Sensor Converter | [[122-019-450 — Exhaust Gas Temperature Sensor Converter\|Refer to Procedure 019-450]] | 19 |
| Service Manual | QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] | Exhaust Temperature Sensor | [[122-019-013 — Exhaust Temperature Sensor\|Refer to Procedure 019-013]] | 19 |

### Document History

## Детали, упомянутые в документе

| Артикул | Наименование | Русское название |
|---|---|---|
| [[3093956]] | HEXAGON FLANGE HEAD CAP SCREW | Болт с шестигранной головкой и фланцем |
| [[3657721]] | CLIP | Скоба |
| [[4951876]] | SENSOR ADAPTER | Переходник датчика |
| [[5376109]] | TEMPERATURE SENSOR | Датчик температуры |
| [[5538111]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538112]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538113]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5538141]] | MODULE BRACKET | Кронштейн модуля |
| [[5538755]] | ELECTRONIC CONTROL MODULE WIRING HARNESS | Жгут проводов блока управления |
| [[5572259]] | ELECTRONIC INTERFACE MODULE | Электронный интерфейсный модуль |
