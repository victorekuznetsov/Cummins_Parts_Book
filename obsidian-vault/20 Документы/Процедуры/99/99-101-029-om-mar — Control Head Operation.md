---
aliases:
  - "Работа поста управления"
type: "Процедура"
doc: "99-101-029-om-mar"
title_en: "Control Head Operation"
title_ru: "Работа поста управления"
modified: "2025-02-05"
engines:
  - "93047320"
  - "93058669"
  - "93087701"
families:
  - "6B5.9"
  - "C8.3 · 6C8.3"
manuals:
  - "3381968"
  - "4021538"
figures: 27
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-101-029-om-mar.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-101-029-om-mar.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/C8.3"
  - "группа/99"
---

# Control Head Operation
**Работа поста управления**

> [!abstract] Процедура · `99-101-029-om-mar`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** 6B5.9, C8.3 · 6C8.3
> **Входит в руководства:** [[3381968 — C8.3 Recreational Marine Operation and Maintenance Manual|3381968]], [[4021538 — B3.9 and B5.9 Recreational Marine Operation and Maintenance Manual|4021538]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2025-02-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-101-029-om-mar.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/99-101-029-om-mar.pdf)

### Instrument Panel

> [!note] Note · Примечание
> The information below is written for engines equipped with an OEM supplied control system. For engines equipped with the Cummins Inc. supplied controls system, reference C Command Connect and Connect Premier Marine Panel System PS102 & PS103 Owners Manual Bulletin, [[5411481 — C Command Connect and Connect Premier Marine Panel System PS102, PS103 and PS108\|5411481]], or the Marine C Command HD Elite Panel System Owners Manual Bulletin, [[4332829 — Marine C Command HD Elite Panel System Owners Manual\|4332829]], for additional information.

The control panel consists of the following:

1. Lubricating oil pressure gauge
2. Tachometer
3. Hourmeter
4. Engine coolant temperature gauge
5. Blank
6. Alarm reset button
7. Start push-button
8. Keyswitch
9. Alarm panel
10. Battery voltmeter.

![[15900027.png]]

Oil Pressure Gauge

The oil pressure gauge (1) shows the operating oil pressure of the engine.

![[15900028.png]]

Tachometer w/Hour Meter

The tachometer (2) shows the engine's crankshaft speed in revolutions per minute (rpm).

The hour meter shows the numbers of hours of operation. This function is used for maintenance of the engine(s).

![[15900029.png]]

Voltmeter

The voltmeter (10) shows the battery voltage.

![[15900030.png]]

Coolant Temperature Gauge

The coolant temperature gauge (4) shows the temperature of the engine coolant during operation.

![[15900031.png]]

### Instrument Panel

Electronic Governor Operation

Turning the illumination control knob (4) will control the panel illumination and all switch panel backlighting.

Turning the knob **clockwise** will decrease the illumination. Turning it **counterclockwise** will increase the illumination.

![[13200080.png]]

### Gauges

All of the gauges, except the voltmeter (9), used with the engine are electronically driven. The gauges receive the reading from a high-speed datalink that is connected to the different sensors. If a gauge has no information from the datalink, it will slowly toggle between its high and low extremes.

![[13200083.png]]

Oil Pressure Gauge

The oil pressure gauge (2) shows the operating oil pressure of the engine.

![[13200084.png]]

Tachometer w/Hour Meter

The tachometer (3) shows the engine's crankshaft speed in revolutions per minute (rpm).

The hour meter shows the numbers of hours of operation. This function is used for maintenance of the engine(s).

![[13200087.png]]

Voltmeter

The voltmeter (9) shows the battery voltage.

![[13200086.png]]

Coolant Temperature Gauge

The coolant temperature gauge (10) shows the temperature of the engine coolant during operation.

![[13200085.png]]

### Backup Throttle

The optional backup throttle was designed to be used in the event of a main throttle failure.

#### Backup Throttle Usage

- Rotate the backup throttle knob **counterclockwise** to the idle position, or depress the knob to bring the engine to idle.
- Put the main throttle lever in the idle position.
- Move the backup throttle switch to the ON position.
- Rotate the throttle knob **clockwise** to desired engine speed.

The backup throttle switch has a safety latch feature; press the latch down and move the switch to the ON position. The throttle also has a friction adjustment collar. Rotate the collar **clockwise** to tighten, or **counterclockwise** to loosen, until the desired throttle tension is obtained.

To turn the backup throttle off and to regain control of the engine speed using the main throttle lever:

1. Set the backup throttle to idle
2. Set the main throttle to idle
3. Put the backup throttle switch in the OFF position by depressing the bottom of the rocker switch

![[13200055.png]]

### Programmable Features

An optional station select feature allows activation of electronic features from either a primary or secondary switch control panel.

![[15200050.png]]

Engine Synchronization Switch

> [!danger] WARNING · Опасно
> The engine synchronization feature must be turned off before docking or low-speed maneuvering; this allows full and separate control of each engine. Failure to turn off the engine synchronization feature can cause personal injury, damage to the vessel, and/or the dock.

> [!note] Note · Примечание
> The engine synchronization feature is an option available **only** on twin-engine vessels.

The engine synchronization feature is used to electronically control the speed of both engines using one throttle lever.

![[15200040.png]]

Normally the starboard throttle is used as the master engine throttle. The distributor or dealer can change it to the port throttle, if desired, by changing the master and slave plugs in the engine wiring. Refer to the installation manual.

![[13200062.png]]

To use the engine synchronization feature:

- Both engines **must** be in the same throttle position, running at the same rpm.
- Put the ENG SYNC switch (1) in the ON position by depressing the top of the rocker switch.

Both engines will adjust to the same rpm. The master throttle will control both engines.

> [!note] Note · Примечание
> This feature will deactivate when the engine is shut down. When the engine is restarted, the switch **must** be turned OFF then turned ON again to activate the feature.

![[15200040.png]]

To turn the engine synchronization feature off:

1. Put the ENG SYNC switch (1) in the OFF position by depressing the bottom of the rocker switch.
2. Move either throttle lever to within 100 rpm of the other and the feature will deactivate. The throttle levers will now operate independently.

![[nobox.png]]

Marine Cruise Control

The marine cruise control feature provides two adjustable engine speeds. The cruise control can be used to run the engine(s) at the optimal cruise rpm or trolling rpm.

CRUISE 1 has a default setting of 2100 rpm.

CRUISE 2 has a default setting of 1200 rpm.

> [!note] Note · Примечание
> The marine cruise control feature can be used in conjunction with the engine synchronization feature.

![[15200038.png]]

To activate the marine cruise control feature:

1. Put the cruise switch (1) in the desired position, CRUISE 1 or CRUISE 2.
2. Move the throttle(s) past the desired cruise speed.

The engine(s) speed will increase to the cruise setting.

> [!note] Note · Примечание
> When using the engine synchronization feature, the master throttle is the **only** throttle that **must** be moved past the cruise point.

![[15200038.png]]

To turn the marine cruise control off, put the cruise switch (1) in the OFF position (rocker switch in the center position).

The engine(s) rpm will slowly ramp to the throttle lever setting.

![[15200038.png]]

To change the CRUISE 1 or CRUISE 2 default setting rpm:

1. With the engine running, select the cruise setting that you want by setting cruise control switch (1) to CRUISE 1 or CRUISE 2.
2. Move the throttle, both if twin-engine, to the full throttle position while underway, or at the dock with the gear in neutral. The engine will **not** exceed the existing cruise setting. For example; if CRUISE 2 is at the factory setting of 1200 rpm, the engine will **only** reach 1200 rpm at full throttle.
3. Using the RPM ± switch (2), adjust the cruise rpm to the new desired engine speed.

> [!note] Note · Примечание
> The cruise speeds can be set between idle and rated engine speed. This new setting will be saved until the cruise is readjusted.

![[15200038.png]]

Slow Idle

The SLOW-IDLE feature allows for lower idle speed for operation in “No Wake Zones”. When activated, the SLOW-IDLE feature reduces the engine speed to a programmed speed.

![[15200035.png]]

> [!note] Note · Примечание
> A single switch controls both engines on twin engine vessels.

To use the SLOW-IDLE feature:

1. The vessel **must** be in gear.
2. The throttle **must** be in the idle position.
3. Put the SLOW-IDLE switch in the ON position (1) by depressing the top of the rocker switch.

The engine(s) idle will decrease to programmed speed.

> [!note] Note · Примечание
> This feature will deactivate when the engine is shut down. When the engine is restarted, the switch **must** be turned OFF then turned ON again to activate the feature.

![[15200036.png]]

To turn the SLOW-IDLE feature off, put the SLOW-IDLE switch in the OFF position (2) by depressing the bottom of the rocker switch.

The engine(s) will adjust to the idle set speed.

> [!note] Note · Примечание
> When the SLOW-IDLE switch is on, increasing the throttle will temporarily turn off the SLOW-IDLE feature. When the throttle is moved back into the idle position, the SLOW-IDLE feature will automatically turn itself ON again.

![[15200037.png]]

Engine Speed Control

The engine speed control (rpm ±) switch (2) allows the idle speed to be adjusted in 25-rpm increments by pressing the rocker switch.

Pressing the top of the switch increases (+) engine rpm.

Pressing the bottom of the switch decreases (-) engine rpm.

> [!note] Note · Примечание
> Use slow deliberate clicks to increase or decrease the engine rpm.

When the RPM ± switch (2) is used with the engine at idle, the switch will **only** work from 600 to 1000 rpm.

> [!note] Note · Примечание
> The RPM ± switch (2) will **not** change the idle speed when the engine is in SLOW-IDLE mode.

Use of the SLOW-IDLE feature will deactivate the RPM ± feature.

![[15200038.png]]

If the engine speeds between the two engines are **not** the same, adjust both engines to the minimum rpm setting, 600 rpm, by depressing the bottom (-) of the switch until both engines are at 600 rpm.

Then using the RPM ± switch (1), adjust the idle to the desired speed, rpm.

![[15200039.png]]

Twin-Engine Vessels

If the engines are running at different speeds:

1. Adjust the cruise to the minimum or maximum setting using the RPM ± switch.
2. Adjust the cruise to the desired setting using the RPM ± switch.

> [!note] Note · Примечание
> If an engine will **not** reach rated rpm, make sure the marine cruise control feature is in the OFF position. If the marine cruise control feature is left in the CRUISE 1 or CRUISE 2 position, maximum engine speed will be limited to the set point of the position that the cruise switch is in.

![[15200035.png]]
