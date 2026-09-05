---
type: "Процедура"
doc: "493-011-143"
title_en: "Aftertreatment Diesel Exhaust Fluid Dosing Unit Manual Purge"
modified: "2020-11-25"
manuals:
  - "5411181"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-143.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Diesel Exhaust Fluid Dosing Unit Manual Purge

> [!abstract] Процедура · `493-011-143`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2020-11-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-011-143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-011-143.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- Cummins® electronic service tool or equivalent
- Fluid Doser Cleaner Kit, Part Number 5298533
- Multimeter pressure sensor, Part Number 3164491, or equivalent
- Aftertreatment diesel exhaust fluid (DEF) diagnostic line, Part Number 5299833.

#### Additional Service Items

- No additional service items required.

### General Information

The purpose of this procedure is to manually purge the DEF dosing unit if there are priming issue.

### Purge

Air Assisted

Disconnect the aftertreatment DEF dosing unit suction line (1) from the DEF dosing unit inlet connector.

Disconnect the aftertreatment DEF dosing unit pressure line (2) from the DEF dosing unit outlet connector.

![[11l00167.png]]

Turn the keyswitch to the ON position and connect recommended Cummins® electronic service tool or equivalent.

Select the Aftertreatment Diesel Exhaust Fluid System Leak Test found under the ECM Diagnostic Tests menu.

![[19r00163.png]]

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

While the leak test is running, use shop air to blow into the DEF dosing unit inlet connection for 15 seconds.

> [!note] Note · Примечание
> **If this test is run for an extended period of time, Fault Code 1682 will become active. Limit the test time to 5 minutes or less.**

![[11l00168.png]]

Stop the system leak test using the electronic service tool.

Run the Aftertreatment Diesel Exhaust Fluid Dosing Unit Suction Test again. [[493-011-121 — Aftertreatment Diesel Exhaust Fluid Dosing Unit Suction Test|Refer to Procedure 011-121 in section 11.]]

If the dosing unit passes the suction test, proceed to the Finishing Steps below.

If the system fails the suction test, proceed to the Liquid Assisted section of this step.

![[19r00163.png]]

Liquid Assisted

Disconnect the aftertreatment DEF dosing unit suction line (1) from the DEF dosing unit inlet connector.

Disconnect the aftertreatment DEF dosing unit pressure line (2) from the DEF dosing unit outlet connector.

![[11l00167.png]]

Remove the aftertreatment DEF dosing unit filter. Discard the dosing unit filter assembly. [[493-011-060 — Aftertreatment Diesel Exhaust Fluid Dosing Unit Filter|Refer to Procedure 011-060 in Section 11.]]

Do **not** install the new filter or DEF filter cap at this time.

Remove the DEF dosing unit inlet screen filter. Discard the inlet screen filter. [[493-011-058 — Aftertreatment Diesel Exhaust Fluid Dosing Unit|Refer to Procedure 011-058 in Section 11.]]

Clean the DEF tank thoroughly and fill with certified DEF if **not** performed earlier. See equipment manufacturer service information.

![[11l00169.png]]

Position a collection container under the aftertreatment DEF dosing unit.

> [!note] Note · Примечание
> Use distilled water, if available, and confirm the fluid doser cleaner bottle is free of debris.

Fill the fluid doser cleaner bottle from the Fluid Doser Cleaner Kit, Part Number 5298533, with clean water and connect it to the aftertreatment DEF dosing unit inlet line connector.

![[11700097.png]]

Select the Aftertreatment Diesel Exhaust Fluid System Leak Test.

> [!note] Note · Примечание
> **Only** the fluid doser cleaner bottle and the electrical connector are to be connected to the aftertreatment DEF dosing unit during this time.

Start the Aftertreatment Diesel Exhaust Fluid System Leak Test.

Squeeze the fluid doser cleaner bottle to push water into the aftertreatment DEF dosing unit. The water will flow out from the DEF filter cap cavity.

Repeat the procedure until the DEF dosing unit begins drawing fluid from the fluid doser cleaner bottle on its own.

The fluid doser cleaner bottle will start to collapse as the dosing unit starts drawing the fluid on its own. Once the aftertreatment DEF dosing unit is drawing fluid from the fluid doser cleaner bottle on its own, press the stop button on the electronic service tool to stop the test.

> [!note] Note · Примечание
> If the DEF dosing unit does **not** begin drawing fluid after one bottle full bottle, replace the DEF dosing unit.

![[11700098.png]]

> [!note] Note · Примечание
> If the DEF dosing unit has been replaced, proceed to the Finishing Steps section below.

Install an aftertreatment DEF dosing unit filter. [[493-011-060 — Aftertreatment Diesel Exhaust Fluid Dosing Unit Filter|Refer to Procedure 011-060 in Section 11.]]

Perform the Aftertreatment DEF Dosing Unit Suction Test to verify operation. [[493-011-121 — Aftertreatment Diesel Exhaust Fluid Dosing Unit Suction Test|Refer to Procedure 011-121 in Section 11.]]

![[11700056.png]]

### Finishing Steps

- Connect the DEF lines to the aftertreatment DEF dosing unit. The DEF lines will snap when locked into place. Lightly tug on the connectors to make sure they are secured.
- Operate the engine. Check for leaks.
