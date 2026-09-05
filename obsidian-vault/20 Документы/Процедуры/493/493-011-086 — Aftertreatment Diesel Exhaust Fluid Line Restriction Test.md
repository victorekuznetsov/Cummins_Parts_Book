---
type: "Процедура"
doc: "493-011-086"
title_en: "Aftertreatment Diesel Exhaust Fluid Line Restriction Test"
modified: "2020-11-25"
manuals:
  - "5411181"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-086.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-086.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Exhaust Fluid Line Restriction Test

> [!abstract] Процедура · `493-011-086`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 11 - Exhaust System · Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2020-11-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-086.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-086.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent
- Multimeter Kit, Part Number 3400162, or equivalent
- Multimeter pressure sensor, Part Number 3164491, or equivalent
- Aftertreatment diesel exhaust fluid (DEF) diagnostic line, Part Number 5299833
- Aftertreatment DEF Extension Kit, Part Number 5299873.

#### Additional Service Items

- No additional service items required.

### General Information

The purpose of this test is to check for high intake restriction at the dosing unit.

The measurement is performed using the DEF diagnostic line and Aftertreatment Diesel Exhaust Fluid System Leak Test.

The test is performed with the DEF pressure line disconnected to create maximum flow through the DEF dosing unit.

### Setup

Allow for DEF to recirculate and depressurize after engine shut down and prior to DEF system servicing. This can take up to 15 minutes. There is **always** a chance of residual pressure being present. Open fittings slowly to allow any pressure to bleed off before removing any connections.

Clean the aftertreatment DEF diagnostic line.

- Connect an open female Compuchek™ fitting onto the male Compuchek™ fitting of the diagnostic line.
- Thoroughly flush the diagnostic line. Use warm, clean water. Make sure the Compuchek™ fitting is free of DEF crystal buildup.

![[11j00079.png]]

- Make sure the DEF tank is at least half full.
- Make sure the DEF is **not** frozen. If the DEF is frozen, it will be necessary to run the engine to allow the system to thaw.

Install the DEF diagnostic line.

- Connect the multimeter pressure sensor to the Compuchek™ fitting on the diagnostic line. Zero the sensor.
- Disconnect the intake line from the DEF dosing unit.
- Install the diagnostic line between the intake fitting on the aftertreatment DEF dosing unit and intake line.
- Open the valve on the diagnostic line.

![[11l00148.png]]

- Remove the DEF pressure line from the dosing valve. Place DEF pressure line in a bucket. Install the DEF extension line, Part Number 5299875, as necessary, from the DEF extension kit, Part Number 5299873.
- Obtain a container suitable for collection of the DEF that exits the DEF pressure line. It is recommended to use at least a 3.8 liter \[1 gal\] bucket.
- Connect recommended Cummins® electronic service tool or equivalent.

![[11w00099.png]]

### Measure

Run the Aftertreatment Diesel Exhaust Fluid System Leak Test found under the Engine Control Module (ECM) Diagnostic Test menu in the electronic service tool.

> [!note] Note · Примечание
> Once the test is initiated, it will continue to pump DEF, even when attempting to stop the test with electronic service tool. To stop the test, it is necessary to turn the keyswitch to the OFF position.

![[11w00100.png]]

Allow the dosing unit to purge the air from the diagnostic line. This will normally happen within 30 seconds.

Measure the dosing unit intake restriction.

| Dosing Unit Intake Restriction |  |  |
|---|---|---|
| mm-hg |  | in-hg |
| -254 | MAX | -10 |

If the dosing unit restriction is greater than the specification, check for the following:

- Kinked, blocked, or restricted intake line
- Restricted DEF tank filter
- Restricted DEF tank vent
- Restricted DEF tank header.

Clean or replace any damaged components.

![[11w00101.png]]

Turn the keyswitch to the OFF position to end the test.

> [!note] Note · Примечание
> If this test is run for an extended period of time, Fault Code 1682 will become active. Limit the test time to 5 minutes or less.

![[11w00102.png]]

### Finishing Steps

> [!note] Note · Примечание
> If directed to this procedure from a troubleshooting tree and the test results were within specification, leave the diagnostic line installed between the dosing unit and intake line. Return to the troubleshooting information.

- Connect the DEF pressure line to the DEF dosing unit.
- Remove the aftertreatment DEF diagnostic line.
- Connect the intake line to the DEF dosing unit.
- Discard the collected DEF in accordance with local environmental regulations.

Clean the aftertreatment DEF diagnostic line.

- Connect an open female Compuchek™ fitting onto the male Compuchek™ fitting of the diagnostic line.
- Thoroughly flush the diagnostic line. Use warm, clean water. Make sure the Compuchek™ fitting is free of DEF crystal buildup.

![[11j00079.png]]
