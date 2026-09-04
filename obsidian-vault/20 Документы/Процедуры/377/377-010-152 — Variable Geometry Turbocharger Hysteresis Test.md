---
type: "Процедура"
doc: "377-010-152"
title_en: "Variable Geometry Turbocharger Hysteresis Test"
modified: "2023-04-11"
manuals:
  - "5411181"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-010-152.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-010-152.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Variable Geometry Turbocharger Hysteresis Test

> [!abstract] Процедура · `377-010-152`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2023-04-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-010-152.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-010-152.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- No Cummins® Service Tools required.

#### Additional Service Items

- No additional service items required.

### General Information

Conditions necessary to perform the Variable Geometry Turbocharger Hysteresis Test:

- Engine OFF
- Keyswitch ON
- Turbocharger and actuator installed on engine
- Coolant temperature greater than 10°C \[50°F\]
- Battery voltage greater than 11.5 VDC
- No active turbocharger fault codes
- INSITE™ electronic service tool connected
- Compare the engine control module (ECM) code and revision number in the ECM to the calibration revision listed in the ECM calibration revision history for applicable changes related to the “Variable Geometry Turbocharger Hysteresis Test”. If the ECM does **not** contain this revision or higher, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code|Refer to Procedure 019-032 in Section 19.]]

The INSITE™ electronic service tool “Variable Geometry Turbocharger Hysteresis Test” **must only** be performed with the actuator mounted to the turbocharger.

In INSITE™ electronic service tool screen labeled “Variable Geometry Turbocharger Hysteresis Test”, locate the button labeled “Start”.

Follow the instructions on the screen to test the turbocharger. INSITE™ electronic service tool will indicate when the test has completed.

If INSITE™ electronic service tool status message indicates the procedure was stopped or had an error, turn the keyswitch OFF for 30 seconds, then turn the keyswitch ON. Verify all conditions above are met, and perform the test again.

> [!note] Note · Примечание
> Fault Code 2198 can become active during the Variable Geometry Turbocharger Hysteresis Test. Clear the fault code after the test if **not** accompanied by a Fault Code 1894.

If the “Variable Geometry Turbocharger Hysteresis Test” results in an output of “Fail”, the turbocharger is **not** reusable. [[377-010-033 — Turbocharger|Refer to Procedure 010-033 in Section 10.]]

Rerun the “Variable Geometry Turbocharger Hysteresis Test” after replacing the turbocharger to confirm the root cause of the issue.

If the “Variable Geometry Turbocharger Hysteresis Test” results in an output of “Fail”, the actuator is **not** reusable. [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric|Refer to Procedure 010-134]] in Section 10.

If the “Variable Geometry Turbocharger Hysteresis Test” results in an output of “Pass”, this indicates that the sector gear movement is acceptable and the actuator should **not** be removed.
