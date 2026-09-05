---
type: "Процедура"
doc: "493-011-080"
title_en: "Aftertreatment Diesel Exhaust Fluid System Leak Test"
modified: "2020-07-15"
manuals:
  - "5411181"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-080.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-080.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Exhaust Fluid System Leak Test

> [!abstract] Процедура · `493-011-080`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2020-07-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-080.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-080.pdf)

### General Information

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required

### General Information

If the aftertreatment diesel exhaust fluid (DEF) dosing system has been serviced or repaired, it will be necessary to prime the DEF dosing system, to check for proper operation.

### Setup

> [!note] Note · Примечание
> It may be necessary to allow the aftertreatment system time to cool, to allow for accessibility to check for leaking components.

- Make sure the DEF tank is full of DEF. See equipment manufacturer service information.
- Make sure the DEF is **not** frozen. If the DEF is frozen, it will be necessary to run the engine to allow the system to thaw.
- Make sure all DEF dosing system lines are properly connected to the DEF tank, DEF dosing unit, and DEF dosing valve. See equipment manufacturer service information.
- Connect the recommended Cummins® electronic service tool or equivalent.

![[05c00344.png]]

### Prime

With the keyswitch ON and the engine **not** running, select the Aftertreatment Diesel Exhaust Fluid System Leak Test found under the engine control module (ECM) diagnostics test menu in the electronic service tool.

This test will cause the DEF dosing unit to draw DEF from the tank and pressurize it in the DEF dosing valve supply line. During this test, the dosing unit will continuously run and all unused DEF will return to the tank. An audible pumping noise will be noticeable during the test.

During the initialization of this test, a note will pop up on the screen, indicating that the system has reached a prime state.

### Inspect

> [!note] Note · Примечание
> If the system is unable to prime due to leaks, the test can be stopped using the electronic service tool.

While the test is running, inspect all DEF lines, fittings, and connections for external leaks. See one or more of the following documents.

- [[493-011-058 — Aftertreatment Diesel Exhaust Fluid Dosing Unit|Refer to Procedure 011-058 in Section 11.]]
- [[493-011-059 — Aftertreatment Diesel Exhaust Fluid Dosing Valve|Refer to Procedure 011-059 in Section 11.]]
- See equipment manufacturer service information.

Repair and replace any leaking component(s). See one or more of the following documents.

- [[493-011-058 — Aftertreatment Diesel Exhaust Fluid Dosing Unit|Refer to Procedure 011-058 in Section 11.]]
- [[493-011-059 — Aftertreatment Diesel Exhaust Fluid Dosing Valve|Refer to Procedure 011-059 in Section 11.]]
- See equipment manufacturer service information.

![[06d00193.png]]

> [!note] Note · Примечание
> If the system fails to prime a key cycle will be required before attempting to run the Aftertreatment Diesel Exhaust Fluid System Leak Test again.

> [!note] Note · Примечание
> The Aftertreatment Diesel Exhaust Fluid System Leak Test can **only** be attempted twice consecutively. A key cycle will be required before attempting to run the test again after two attempts.

If the system is able to successfully prime, a pop-up message will appear in the electronic service tool to notify the technician.

Upon completion of inspecting the lines, fittings, and connections for leaks, press the STOP button in the electronic service tool.

If the test is **not** STOPPED using the electronic service tool, it will continue to pump for 20 minutes.

If the system can **not** build pressure, it will attempt to prime multiple times before flagging a fault code.

If any fault codes occur while running this test, reference the appropriate fault code troubleshooting tree.

### Finishing Steps

- Check for fault codes.
