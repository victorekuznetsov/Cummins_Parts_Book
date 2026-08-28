---
aliases:
  - "Судовая защита от перегрузки — особые указания"
type: "Процедура"
doc: "122-fc5635aux"
title_en: "Marine Overload Protection - Special Instructions"
title_ru: "Судовая защита от перегрузки — особые указания"
modified: "2015-09-30"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5635aux.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5635aux.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Marine Overload Protection - Special Instructions
**Судовая защита от перегрузки — особые указания**

> [!abstract] Процедура · `122-fc5635aux`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-09-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5635aux.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5635aux.pdf)

### Fault Code: 5635

### Marine Overload Protection - Special Instructions

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 5635 PID(P): SPN: 520892 FMI: 14 Lamp: Amber SRT: | Marine Overload Protection - Special Instructions. Overload condition has been detected by the engine control module (ECM). | Reduction in engine torque. |

![[00700049.png]]

Typical Overload Region for Auxiliary Application

### Circuit Description

X - Engine Speed

Y - Torque

1 - Fuel Limited Torque Curve

2 - Overload Region

3 - 100 Percent Torque

4 - 110 Percent Torque.

The shaded region in the graph above corresponds to the calibratable overload region. Marine Overload Protection monitors the engine operating in an overload condition. This feature is needed to limit engine exposure in such working conditions by alerting the operator and, in some cases, by limiting fueling to the engine.

### Component Location

N/A

### Conditions For Running The Diagnostics

- This diagnostic runs when the engine torque exceeds the overload threshold.

### Conditions For Setting The Fault Codes

- The ECM detected speed and torque values in the overload region for more than a calibratable time.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

- The ECM detected speed and torque values in the normal operating region for more than a calibratable time.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE after the diagnostic runs and passes.

- The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.

### Shoptalk

This is an information- **only** fault code that becomes active if the engine torque exceeds the overload threshold for a calibratable time.

High counts of inactive Fault Code 5635 can indicate the engine is often operated beyond the normal expected region. Vessel operating duty cycle or equipment may need to be investigated to understand fault condition.

No repairs are necessary.

Reference the Marine Application Bulletin – 0.19.00 – Electronic Engine Controls for more information on this diagnostic.

Refer to Troubleshooting Fault Code 5635.
