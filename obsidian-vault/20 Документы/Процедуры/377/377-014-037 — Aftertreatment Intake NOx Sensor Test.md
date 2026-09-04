---
type: "Процедура"
doc: "377-014-037"
title_en: "Aftertreatment Intake NOx Sensor Test"
modified: "2025-08-25"
manuals:
  - "5411181"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-037.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-037.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Aftertreatment Intake NOx Sensor Test

> [!abstract] Процедура · `377-014-037`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2025-08-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-037.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-037.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool, or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

This procedure contains information about how to perform the Aftertreatment Intake NOx Sensor Functional Test on the aftertreatment intake NOx sensor

The purpose of this test is to check the functionality of the aftertreatment intake NOx sensor while the engine is **not** running. If the test completes successfully, this indicates that the NOx sensor is functional.

The test can be used to:

- Diagnose a heater malfunction in which the NOx sensor fails to maintain its temperature.
- Diagnose an accuracy malfunction for NOx drift high or low.
- Diagnose an accuracy malfunction for O 2 drift high or low.
- Diagnose an intermittent communication malfunction.
- Diagnose a stability malfunction for NOx/O 2.
- Validate a successful repair.

### System Requirements

- ECM Calibration code release date November 2021 or later.
- Recommended Cummins® electronic service tool, or equivalent.
- Check the engine control module (ECM) calibration revision history for calibration updates for this test. If the ECM does **not** contain that revision or higher, update the calibration. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

![[19803969.png]]

### Preparatory Steps

1. Verify engine is **not** running.
2. Use the recommended Cummins® electronic service tool, or equivalent, to check for fault codes. If any fault codes are present, follow the corresponding troubleshooting tree before performing any part of this procedure. The fault code troubleshooting tree, in some cases, will reference this procedure to complete the diagnostics.
3. Perform an exhaust system purge.

### Exhaust System Purge

1. Verify engine is **not** running.
2. Use the recommended Cummins® electronic service tool, or equivalent, to check for fault codes. If any fault codes are present, follow the corresponding troubleshooting tree before performing any part of this procedure. The fault code troubleshooting tree, in some cases, will reference this procedure to complete the diagnostics.
3. This Aftertreatment Intake NOx Sensor Test requires the NOx sensor to be in an atmosphere free of exhaust gases. To confirm this, the exhaust system **must** be purged by performing a series of engine cranking events.

Failure to perform the exhaust system purge steps will result in a false failure of the test.

- Disconnect all the injector pass-through connectors (1).

> [!note] Note · Примечание
> Depending on the engine model, there may be up to three injector pass-through connectors.

- Disconnecting the injector pass-through connectors can cause injector fault codes, these fault codes can be disregarded and cleared.
- Key engine on and crank the engine for four 15 second cycles for a total of 60 seconds.

> [!note] Note · Примечание
> For L9 Transit Bus applications **only**, perform a total of eight 15 second cranking cycles for a total of 120 seconds.

- Reconnect all the injector pass-through connectors (1).

![[19o00038.png]]

### Test

With the key switch ON and the engine **not** running, select the Aftertreatment Intake NOx Sensor Test under the ECM Diagnostics Test menu in the electronic service tool. Follow the on-screen instructions to perform the test.

To stop the test at any time during the test:

1. Select the stop button on the electronic service tool monitor screen.
2. Turn the key switch OFF.

When the test is started, the NOx sensor probe heater will be activated automatically and several measurements will be taken.

1. The NOx sensor is heated to an initial idle state to evaporate any possible condensation.
2. The NOx sensor is heated to the test state.
3. NOx and O 2 measurements are compared against known ambient conditions.

At the conclusion of the test, the NOx sensor heater will be deactivated and the probe will begin to cool. The Aftertreatment Intake NOx Sensor Test will display either a Pass, Fail or Abort message until the next key cycle.

If the Aftertreatment Intake NOx Sensor Test does **not** pass, reset the search to “Aftertreatment Intake NOx Sensor Test Did **Not** Pass”. **Only** select the solution title that matches the error message in the recommended Cummins® electronic service tool or equivalent.

If the Aftertreatment Intake NOx Sensor Test will **not** start, verify key switch is ON and engine is **not** running.

If the Aftertreatment Intake NOx Sensor Test will **not** complete, reset the search to "Aftertreatment Intake NOx Sensor Test Will **Not** Complete".

### Finishing Steps

Perform a key cycle and check for any active fault codes. If active fault codes are present, follow published troubleshooting.
