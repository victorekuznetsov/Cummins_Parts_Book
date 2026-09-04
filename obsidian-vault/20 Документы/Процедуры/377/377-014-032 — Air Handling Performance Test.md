---
type: "Процедура"
doc: "377-014-032"
title_en: "Air Handling Performance Test"
modified: "2025-05-08"
manuals:
  - "5411181"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-032.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Air Handling Performance Test

> [!abstract] Процедура · `377-014-032`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2025-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-032.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool, or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

The Air Handling Performance Test is a diagnostic test used to evaluate the health of the air handling components. Throughout the test, engine speed and the position of air handling actuators are controlled to create conditions for the various diagnostics to run.

Components checked in the test:

- Intake Air Throttle
- EGR Valve
- Variable Geometry Turbocharger
- EGR Cooler
- Exhaust Gas Pressure Sensor
- Intake Manifold Pressure Sensor
- EGR Differential Pressure Sensor
- Plugged or leaking EGR differential pressure ports

To start the test, engine **must** be at operating temperature and stopped with the keyswitch in the ON position. After initial actuator span checks, the test will prompt the user to start the engine. Once engine speed is detected, the test will automatically proceed with no further input from the user.

If an issue is detected, the issue **must** be addressed.

Run the test until it passes.

### System Requirements

- ECM calibration code release date September 2021 or later.
- INSITE™ electronic service tool Version 8.7.0 or later.
- Cummins® Guidanz ™ Mobile electronic service tool Version 6.2 or later.
- Cummins® Guidanz ™ Windows® electronic service tool Version 2.6 or later.
- Check the engine control module (ECM) calibration revision history for calibration updates for this test. If the ECM does **not** contain that revision or higher, update the calibration. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

![[19803969.png]]

### Preparatory Steps

1. Select an appropriate location to park the unit.
2. Park the unit securely.
3. Verify the ambient conditions are met.
4. Verify engine compartment is closed.
5. Warmup the engine. Use the recommended Cummins® electronic service tool or equivalent to verify the following:
6. Verify aftertreatment temperatures are met.

> [!note] Note · Примечание
> If Fault Codes 1921 or 1922 are present, the soot load **must** be brought down to normal levels for this test to run due to an engine protection derate. After a regeneration, run the engine at high idle (greater than 1800 rpm) for 5 minutes.

### Test

1. Begin the Air Handling Performance Test.
2. Monitor the area.

At the conclusion of the test, engine will return to idle. The Air Handling Performance Test will display either a Pass, Fail or Abort message until the next key cycle.

If test passes, then no further action is required.

If the Air Handling Performance Test does **not** pass, reset the search to “Air Handling Performance Test Did **Not** Pass”. **Only** select the solution title that matches the error message in the recommend Cummins® electronic service tool or equivalent.

If a repair is necessary, perform the repair and then run the Air Handling Performance Test until the test passes.

The Air Handling Performance Test will **not** start or will be aborted if:

- Preparatory conditions **not** within specification
- Accelerator pedal is depressed
- Clutch pedal is depressed
- Brake pedal is depressed
- Parking brake **not** set
- Parking brake configured incorrectly
- Transmission put into gear
- PTO engaged
- Vehicle speed detected
- Engine protection state active
- DPF Inlet Temperature greater than 350°C \[ 662°F \]
- DPF Outlet Temperature greater than 300°C \[ 572°F \].

If the Air Handling Performance Test will **not** start, reset the search to Air Handling Performance Test Will **Not** Start.

If the Air Handling Performance Test will **not** complete, reset the search to Air Handling Performance Test Will **Not** Complete.

If the test needs to be restarted, cycle the keyswitch OFF for 90 seconds and then back ON.

### Finishing Steps

- Check for any active fault codes. If active fault codes are present, follow the appropriate troubleshooting.
