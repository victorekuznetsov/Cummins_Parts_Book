---
type: "Процедура"
doc: "493-011-144"
title_en: "Aftertreatment Diesel Exhaust Fluid Dosing System Pressure Test"
modified: "2023-10-06"
manuals:
  - "5411181"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-144.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-144.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Exhaust Fluid Dosing System Pressure Test

> [!abstract] Процедура · `493-011-144`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2023-10-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-144.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-144.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- Cummins® electronic service tool or equivalent
- Diesel Exhaust Fluid (DEF) Pressure Test Kit, Part Number 5394562
- Multimeter Kit, Part Number 3400162, or equivalent
- Multimeter pressure sensor, Part Number 3164491, or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

The purpose of this test is to measure DEF system pressures at various locations within the DEF system. The measurement is performed using the Aftertreatment DEF System Leak Test in the recommended Cummins® electronic service tool or equivalent to command the system to prime.

This procedure contains normal pressure values for the various test points. However, the test sequence and repair instructions are contained in the appropriate fault code troubleshooting manual.

The pressure test kit includes three different diagnostic lines that can be used to measure pressure at four different locations within the DEF system.

#### DEF Pressure Tool Connection Points

1. DEF dosing unit outlet
2. DEF dosing valve inlet
3. DEF dosing valve outlet
4. DEF tank return fitting.

| Part Number | Fitting Size - Inch | Measurement Location |
|---|---|---|
| 5299132 | 3/8 | DEF tank return fitting |
| 5394564 | 5/16 | DEF dosing unit outlet DEF doing valve outlet |
| 5394565 | 1/4 | DEF dosing valve inlet |

> [!note] Note · Примечание
> Some DEF tanks will have 5/16 in returns fitting instead of 3/8 in.

![[11l00243.png]]

### Setup

Clean the aftertreatment DEF diagnostic lines.

- Connect an open female Compuchek™ fitting onto the male Compuchek™ fitting of the diagnostic line.
- Thoroughly flush the diagnostic line. Use warm, clean water.
- Verify the Compuchek™ fitting is free of DEF crystal buildup.
- Verify the DEF tank is at least half full.
- Verify the DEF is **not** frozen. If the DEF is frozen, it will be necessary to run the engine to allow the system to thaw.
- Connect a multimeter pressure sensor to the Compuchek™ fitting on the diagnostic line. Set the multimeter to mV DC and zero the multimeter pressure sensor.
- Install the DEF diagnostic line at the desired location. There is **always** a chance of residual pressure being present. Open fittings slowly to allow any pressure to bleed off before removing any connections.
- Connect the electronic service tool.

![[10w00114.png]]

### Measure

1. Install the aftertreatment DEF pressure gauge between the outlet of the aftertreatment DEF dosing unit and the pressure line. This is the supply line between the aftertreatment DEF dosing unit and the aftertreatment DEF dosing valve.
2. Install the aftertreatment DEF pressure gauge between the inlet of the DEF dosing valve and the pressure line. This is the supply line between the aftertreatment DEF dosing unit and the aftertreatment DEF dosing valve.
3. Install the DEF pressure gauge at the aftertreatment DEF dosing valve outlet. This is the return line between the aftertreatment DEF dosing valve and the aftertreatment DEF tank.
4. Install the aftertreatment DEF pressure gauge at the aftertreatment DEF tank return fitting.

Follow the table specifications below (numbers in the table correlate to step numbers above):

| **Aftertreatment DEF Dosing Unit Outlet Pressure (1)** | **Aftertreatment DEF Dosing Valve Inlet (2)** | **Aftertreatment DEF Dosing Valve Outlet (3)** | **Aftertreatment DEF Tank Return Fitting (4)** | **Action** |
|---|---|---|---|---|
| Greater than 950 kPa \[ 137 psi \] | Greater than 950 kPa \[ 137 psi \] | Less than 70 kPa \[ 10 psi \] | - | Replace aftertreatment DEF dosing valve inlet screen and retest. Replace aftertreatment DEF dosing valve if persists. |
| Less than 750 kPa \[ 108 psi \] | Less than 750 kPa \[ 108 psi \] | - | - | Visually inspect the following for signs of blockage or buildup: Aftertreatment DEF dosing unit outlet fitting. Aftertreatment DEF dosing unit filter. Replace aftertreatment DEF filter regardless of condition. Aftertreatment DEF dosing valve inlet fitting screen. If there are signs of blockage or buildup, clean or replace the appropriate component. If there are no signs of blockage or buildup, replace the aftertreatment DEF dosing unit. |
| Greater than 950 kPa \[ 137 psi \] | Less than 750 kPa \[ 108 psi \] | - | - | Restricted pressure line. Clean or replace the pressure line. |
| Greater than 950 kPa \[ 137 psi \] | Greater than 950 kPa \[ 137 psi \] | Greater than 70 kPa \[ 10 psi \] | Less than 70 kPa \[ 10 psi \] | Blocked or restricted return line has been detected. Clean or replace the return line. |
| Greater than 950 kPa \[ 137 psi \] | Greater than 950 kPa \[ 137 psi \] | Greater than 70 kPa \[ 10 psi \] | Greater than 70 kPa \[ 10 psi \] | Blocked or restricted aftertreatment DEF tank header has been detected. Clean or replace the aftertreatment DEF tank header. |

### Finishing Steps

- Remove the DEF diagnostic line(s).
- Install the original DEF lines.
- Operate the engine. Check for leaks.

- Clean the aftertreatment DEF diagnostic lines.
