---
type: "Процедура"
doc: "493-019-478"
title_en: "Aftertreatment Particulate Matter Sensor"
modified: "2024-10-25"
manuals:
  - "5411181"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-019-478.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-019-478.pdf"
tags:
  - "документ/процедура"
  - "группа/493"
---

# Aftertreatment Particulate Matter Sensor

> [!abstract] Процедура · `493-019-478`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2024-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/493/493-019-478.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/493-019-478.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tool

- J1939 Component Isolation Kit, Part Number 5299465
- Electrical Cable, Part Number 5394621
- Battery adapter cable, Part Number 5299000
- Cummins® electronic service tool or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The aftertreatment particulate matter sensor is located after the aftertreatment selective catalytic reduction (SCR) catalyst.

The particulate matter sensor is made up of two parts:

- Sensor probe mounted in the aftertreatment SCR catalyst outlet.
- Electronic module on the aftertreatment SCR catalyst.

The two parts are permanently connected and can **not** be separated. The particulate matter sensor can **only** be replaced as an assembly.

![[19e02054.png]]

### Test

Disconnect the aftertreatment interface harness (1) from the aftertreatment particulate matter sensor (2). Refer to Procedure 019-477 procedure in Section 19.

![[11l00075.png]]

Connect service tool, Part Number 5394621 into service tool, Part Number 5299466, from kit 5299465, to aftertreatment particulate sensor.

![[19l00077.png]]

Connect the service tool data link, 3 pin Deutsch™, to the engine Society of Automotive Engineers (SAE) J1939 data link connection, located on the driver's side of the engine.

![[19803641.png]]

Use the vehicle VDC to supply power to the service tool.

> [!note] Note · Примечание
> Cummins® battery adapter cable, Part Number 5299000, can be used to provide power from the vehicle battery supply.

For Fault Code 6688, the following conditions **must** be met before checking the status of the active fault code.

This diagnostic runs continuously when the keyswitch is in the ON position.

> [!note] Note · Примечание
> If service tool is being used on 24 volt sensor, battery adapter cable, Part Number 5299000, will need to be used to provide power from the vehicle. battery supply.

Check for inactive fault codes. After the above conditions have been met for the active fault code:

- Check to see if the active fault code 6688 now displays as inactive.
- If the active fault codes now display as inactive, the sensor is operating normally and should **not** be replaced. The source of the fault code is located within the wiring that was isolated by the service tool.

![[19o00057.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.

### Remove

> [!danger] WARNING · Опасно
> The aftertreatment system will stay hot to touch for long periods of time after the engine has been shut down. To reduce the possibility of personal injury, avoid direct contact of hot components with your skin.

Disconnect the aftertreatment interface harness (1) from the aftertreatment particulate matter sensor electronic module (2). Refer to Procedure 019-477 procedure in Section 19.

![[11l00075.png]]

Remove the particulate matter sensor electronic module mounting capscrews.

If P-clips are used to hold the particulate matter sensor wiring harness to the aftertreatment SCR catalyst, mark the P-clip mounting locations prior to removal.

Remove any P-clips and associated mounting capscrews.

![[19l00078.png]]

Loosen the particulate matter sensor body retaining nut.

Remove the particulate matter sensor assembly.

![[19e02056.png]]

### Clean and Inspect for Reuse

> [!warning] CAUTION · Осторожно
> Do not clean the aftertreatment particulate matter sensor with any kind of fluid. Do not immerse the particulate matter sensor in water or any kind of chemical wash. Do not jet-wash or steam clean the particulate matter sensor.

Inspect the particulate matter sensor for damage to the wiring or to the body of the sensor.

Replace the particulate matter sensor if any damage is found.

> [!note] Note · Примечание
> If the particulate matter sensor probe was exposed to any foreign chemical or liquid (coolant, oil, fuel, etc) it can **not** be cleaned and **must** be replaced.

![[19e02057.png]]

Inspect the tip of the particulate matter sensor for damage.

Replace the particulate matter sensor if any damage is found.

![[19e02058.png]]

### Install

> [!warning] CAUTION · Осторожно
> Do not underseal or coat/paint any part of the aftertreatment particulate matter sensor.

> [!warning] CAUTION · Осторожно
> Do not to apply any additional anti-seize compound to the probe or threads as it may result in sensor malfunction.

Install the particulate matter sensor into the outlet of the aftertreatment SCR catalyst.

Tighten the retaining nut.

> [!tip] Момент затяжки · Torque Value
> 50 n•m [37 ft-lb]

![[19e02056.png]]

Install the particulate matter sensor electronic module.

Install and tighten the particulate matter sensor electronic module mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 11 n•m [97 in-lb]

![[19l00078.png]]

Connect the aftertreatment interface harness (1) to the particulate matter sensor electronic module (2).

If removed, install any P-clips and associated mounting capscrews.

![[11l00075.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- Operate the engine and check for proper operation.
- Use recommended Cummins® electronic service tool or equivalent to check for active fault codes.
