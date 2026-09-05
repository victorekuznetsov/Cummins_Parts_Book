---
type: "Процедура"
doc: "377-019-463"
title_en: "Aftertreatment Intake NOx Sensor"
modified: "2018-07-03"
manuals:
  - "5411181"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-463.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-463.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Aftertreatment Intake NOx Sensor

> [!abstract] Процедура · `377-019-463`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2018-07-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-019-463.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-019-463.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- NOx Sensor Module Diagnostic Kit, Part Number 5298821
- Battery Adapter Cable, Part Number 3823955
- Anti-seize Compound, Part Number 3824879

#### Additional Service Items

- No additional service items required

### General Information

> [!warning] CAUTION · Осторожно
> The exhaust catalyst will stay hot to the touch for long periods of time after the engine has been switched OFF.

> [!warning] CAUTION · Осторожно
> The NOx sensor will stay hot to the touch for long periods of time after the engine has been switched OFF. The NOx sensor will also be hot if the engine keyswitch is in the ON position.

> [!warning] CAUTION · Осторожно
> Do not underseal, coat, or paint any part of the NOx sensor.

> [!warning] CAUTION · Осторожно
> Wear goggles and protective clothing to reduce the possibility of personal injury.

The aftertreatment intake NOx sensor is located in the aftertreatment adapter pipe.

The NOx sensor is a one-piece unit made up of two parts, a small module with a wire connection to the metal sensor body that sits in the exhaust system. The parts **must not** be separated.

The NOx sensor is **not** serviceable. If the sensor is malfunctioning, the part **must** be replaced.

![[19t00108.png]]

### Test

Unplug the NOx sensor from the engine harness.

![[19t00108.png]]

Connect the service tool, Part Number 5298821, to the NOx sensor module.

![[19t00112.png]]

Connect the service tool data link (3-pin Deutsch™) to the engine SAE J1939 data link connection, located on the driver's side of the engine.

![[19803641.png]]

Use the vehicle 12-VDC to supply power to the service tool.

> [!note] Note · Примечание
> Battery adapter cable, Part Number 3823955, can be used to provide power from the vehicle battery supply.

For Fault Codes 3681 and 3682, the following conditions **must** be met before checking the status of the active fault.

Start the engine and allow the NOx sensor to reach operating temperature.

This diagnostic runs when the exhaust gas temperature of the aftertreatment intake outlet NOx sensor is above 200°C \[392°F\] and the engine is running. Use INSITE™ electronic service tool to monitor exhaust gas temperature.

> [!note] Note · Примечание
> For the aftertreatment outlet NOx sensor, there is also a 60 second delay after the exhaust gas temperature reaches 200°C \[392°F\].

For Fault Codes 2771 and 3232, the following conditions **must** be met before checking the status of the active fault.

This diagnostic runs continuously when the keyswitch is in the ON position.

> [!note] Note · Примечание
> If the service tool is being used on a 24-VDC sensor, battery adapter cable, Part Number 3823955, will need to be used to provide power from the vehicle battery supply.

Check for inactive fault codes after the above conditions have been met for the active fault code.

- Check to see if any of the "active" fault codes listed (2771, 3232, 3681, and 3682) now display as "inactive".
- If the active fault codes now display as "inactive", the sensor is operating normally and should **not** be replaced. The source of the fault code is located within the wiring that was isolated by the service tool.

![[19o00057.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.

### Remove

Disconnect the slide-lock connector from the NOx sensor module.

Remove the retaining capscrews.

![[19t00108.png]]

Remove the NOx sensor heat shield and capscrews.

Loosen the retaining nut and pull out the NOx sensor probe from the aftertreatment adapter pipe.

![[19l00109.png]]

### Inspect for Reuse

> [!warning] CAUTION · Осторожно
> Do not clean the NOx sensor with any kind of fluid. Do not immerse the NOx sensor in water or any kind of chemical wash. Do not jet-wash or steam clean the NOx sensor.

Inspect the NOx sensor for damage to the wiring or the body of the sensor.

![[19u00018.png]]

Inspect the tip of the NOx sensor for damage.

![[19d02417.png]]

Inspect the wire attachment bracket and the P-clip for damage.

![[19l00110.png]]

### Install

Apply a light coating of anti-seize compound, Part Number 3824879, to the threads of the NOx sensor.

Install the NOx sensor probe into the aftertreatment adapter pipe and tighten the retaining nut.

> [!tip] Момент затяжки · Torque Value
> 50 n•m [37 ft-lb]

![[19l00111.png]]

Install the aftertreatment intake NOx sensor heat shield.

> [!tip] Момент затяжки · Torque Value
> 23 n•m [204 in-lb]

![[19u00020.png]]

Route the NOx sensor wire through the p-clip (1) on the NOx sensor wire attachment bracket near the EGR mass measurement assembly.

Use cable tie (2) to secure the NOx sensor wire to the hook on the EGR cooler.

![[19l00113.png]]

Be sure that the NOx sensor is connected to the engine wiring harness.

Be sure that the orientation of the small module is with the engine wiring harness connection, located at the bottom of the sensor.

Be sure that the small module is secured to the application by the mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

> [!note] Note · Примечание
> The NOx sensor wire connection **must not** be pulled tight. Damage to the sensor can occur.

![[19t00108.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- Operate the engine.
- Use INSITE™ electronic service tool to check for active fault codes.
