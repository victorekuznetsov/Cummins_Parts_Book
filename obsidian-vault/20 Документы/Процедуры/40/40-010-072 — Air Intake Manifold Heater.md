---
type: "Процедура"
doc: "40-010-072"
title_en: "Air Intake Manifold Heater"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 23
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-072.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-072.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Air Intake Manifold Heater

> [!abstract] Процедура · `40-010-072`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-010-072.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-010-072.pdf)

### General Information

This procedure covers intake manifold heater element components for 1991 and 1994 Automotive and Industrial engine ratings. This procedure also covers upfit of intake manifold heater element components on engines **not** originally built with an intake heater option (front gear train engines only).

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury and property damage, never use starting fluid with the air intake manifold heater. Starting fluid, which contains ether, can cause an explosion.

> [!danger] WARNING · Опасно
> Starting fluid is highly flammable and explosive. Keep flames, sparks, and arcing switches away from starting fluid. This combination can cause an explosion and bodily injury.

Warning labels, Part Number 3927335, **must** be installed in locations obvious to the operator, near the most likely point of entry of ether, and on a visible side of the heater. The sun visor and the air cleaner intake is two examples.

The 12-VDC B Series charge air cooled, turbocharged, and naturally aspirated engines (6BTAA, 6BT, and 6B) use the air intake manifold heater as a cold weather starting aid. There is no air intake manifold heater for the water jacket aftercooled engine (6BTA) or 24-VDC electrical system at this time, and the air intake manifold heater is **not** compatible with marine applications.

Benefits from an air intake manifold heater include:

- Quicker start times
- Smoother engine running after starting
- Replaces ether as a starting aid
- Extends starter and battery life through less cranking.

The air intake manifold heater is very similar to the popular light-duty truck application grid heater in use since 1988. This heater electronically controls the two heating elements to optimize cold weather starts and improved cold engine running.

Engine mounted hardware includes:

- Air intake manifold heater
- Temperature sensor
- Controller
- Wiring harness.

> [!note] Note · Примечание
> The kit does **not** include 6 AWG wire or ring terminals needed for the battery and other connections.

White smoke indicates unburned fuel during cold engine operation.

The intake manifold heater system is **not** directly connected to the fuel system, but it monitors the temperature of the air to the engine. The thermistor sends varying resistance values to the electronic control module (ECM), or equivalent. The ECM in turn controls the WAIT-TO-START lamp and the heater solenoids.

The intake manifold heater elements operate in both the preheat and postheat modes.

- In preheat, the ignition switch is on, but the engine has **not** been started.
- In postheat, the engine is running.

The proper operation of the intake manifold heater system and starting procedures will preclude excessive engine starter motor use and minimize white exhaust smoke when the engine is first started.

| Normal Operation of the Intake Manifold Heater System |  |  |  |  |
|---|---|---|---|---|
| Temperature | Condition | Elements | Duration | Duty Cycle Percent ON/OFF |
| Below -19°C \[-2°F\] | Preheat | Both | 30 seconds | Continuous |
|  | Postheat | Both | 15 seconds | Continuous |
|  |  | One | 15 seconds | Continuous |
|  |  | One | 40 seconds | 50/50 |
|  |  | One | 106 seconds | 25/75 |
| -19 to -8°C \[-2 to 18°F\] | Preheat | Both | 20 seconds | Continuous |
|  | Postheat | Both | 20 seconds | Continuous |
|  |  | One | 20 seconds | Continuous |
|  |  | One | 20 seconds | Continuous |
|  |  | One | 40 seconds | 50/50 |
|  |  | One | 106 seconds | 25/75 |
| -8 to 8°C \[18 to 46°F\] | Preheat | Both | 10 seconds | Continuous |
|  | Postheat | Both | 10 seconds | Continuous |
|  |  | One | 10 seconds | Continuous |
|  |  | One | 10 seconds | Continuous |
|  |  | One | 40 seconds | 50/50 |
|  |  | One | 106 seconds | 25/75 |
| Below 8°C \[46°F\] | Preheat | None |  |  |
|  | Postheat | None |  |  |
| Amperage Draw - 95 amps per element |  |  |  |  |
| To prevent excessive drain on the batteries, the electric heater controller has incorporated a battery monitoring feature. If the battery VDC were dropped too low, the heater controller will delay the postheat cycle, preventing further drain on the batteries. This battery protection feature is **only** activated on vehicles with weak or drained batteries. |  |  |  |  |

\*Heater control modules or electronic control modules with serial numbers below 0080000A will **not** have a preheat cycle during this cycle.

Battery Size Requirements for B Series Engines (automotive and industrial ratings)

1991 and 1994 6BTAA and 4BTAA automotive ratings

> [!note] Note · Примечание
> Unaided starting down to 0°C \[+32°F\] or intake heater equipment\*

| 4BTAA Engine |  |  |
|---|---|---|
| Heavy accessory | Cold Cranking Amps (CCA) | Reserve Minutes |
| Light accessory | 900 | 160 |
|  | 750 | 169 |
| \* Intake heater equipment option requires a 95-amp alternator or larger. |  |  |

| 6BTAA Engine |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Reserve Minutes |
| Heavy accessories | 1000 | 160 |
| Light accessories | 850 | 160 |
| \* Intake heater equipment option requires a 95-amp alternator or larger. |  |  |

> [!note] Note · Примечание
> Unaided starting down to -12°C \[10°F\].

| 4BTAA Engine |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Reserve Minutes |
| Heavy accessories | 1350 | 320 |
| Light accessories | 1125 | 320 |

| 6BTAA Engine |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Reserve Minutes |
| Heavy accessories | 1500 | 320 |
| Light accessories | 1250 | 320 |

1994 6BTAA and 4BTAA industrial ratings

| 4BTAA Engine |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Reserve Minutes |
| Heavy accessories | 800 | 160 |
| Light accessories | 625 | 160 |

| 6BTAA Engine |  |  |
|---|---|---|
|  | Cold Cranking Amps (CCA) | Reserve Minutes |
| Heavy accessories | 950 | 160 |
| Light accessories | 800 | 160 |

> [!note] Note · Примечание
> Typical “light accessories” include alternator, small steering pump, and disengaged clutch.

> [!note] Note · Примечание
> Typical “heavy accessories” include hydraulic pump and torque convertor.

![[10900270.png]]

Air Intake Heater Controller Interconnection Diagram

![[10900271.png]]

Cold Starting System

1. Grid heater
2. Air intake temperature sensor

The following illustration shows grid heater components.

Grid Heater Component Connections

1. Ground connection
2. To WAIT-TO-START lamp(s) (dash mounted)
3. Ground connection
4. To fuse and battery
5. Ground connection

![[10900272.png]]

| Troubleshooting for Heater System |  |
|---|---|
| Wait-to-Start (WTS) Lamp **Not** Functioning | Check wiring, socket, bulb, ground signal from controller, and bulb power supply from the keyswitch. Correct any electrical problems with the WTS lamp. WTS lamp will flash one time a second if an open circuit is detected in the temperature sensor. |
| Temperature Sensor Failed | Check resistance across the temperature sensor pins J1A and J1B at room temperature and in an ice bath 0°C \[32°F\]. The resistance should be approximately 800 ohms at room temperature and 2000 ohms for the ice bath. Check the resistance to ground (-) for an open circuit. |
|  | Note: Make resistance checks with the keyswitch in the ON position to make sure there are no ground (-) problems. |
|  | Replace defective sensor. |
| Relay or Contactor Failure | Check relays or contactors for an audible click during operation. Check for pitting or burning in the relay by measuring resistance across the high-amperage terminals when relay is closed. Replace relay(s) if the resistance is high or an audible click is **not** heard when it is actuated. |
| Insufficient Ground (-) Connections | Check pin J1B for ground to the controller. Check the ground (-) strap to the grid heater for high resistance. Repair or replace wiring. |
| Controller Malfunctioning | Check pin J2A for 12-VDC signal; inspect the wiring harness for shorting, chafing, or burning. The controller operates between 6.5 VDC and 16 VDC. Check the connectors for good connections. Replace the controller, if necessary. |
|  | Note: The controller will abort postheat if it senses a voltage drop below 9.5 VDC during preheat or a 10-second delay or more between WAIT-TO-START (WTS) lamp off and cranking, or an open temperature circuit. |

6B Industrial Grid Heater

The air intake manifold heater is preferred starting aid option in production on all 185- and 200-hp ratings and optional on all other water jacket aftercooled (WJAC) engines with Bosch® in-line injection pumps. For engines **not** equipped with the air intake manifold heater option, a spacer block will be installed instead of an intake heater.

The intake heater improves cold weather starting characteristics by heating the intake air during cranking. It can also serve to reduce white smoke if it is engergized during cold ambient temperatures while the engine is at idle. The intake heaters are available for both 12-VDC and 24-VDC systems, and both draw 195 amps while energized.

New hardware has been designed to support the grid heater installation. The engine will have the same overall installation height. The grid heater also has a provision for an air compressor intake line.

![[10900050.png]]

| Description | Part Number | Quantity |
|---|---|---|
| Grid Heater (12 VDC) | 3928465 | 1 |
| Grid Heater (24 VDC) | 3928463 | 1 |
| Spacer Block | 3928464 | 1 |
| Ground Wire | 3928702 | 1 |

![[10900053.png]]

Redesigned hardware installed on the engine to grid heater include:

1. Water jacket aftercooler
2. Water jacket aftercooler plumbing
3. High-pressure fuel lines
4. Low-pressure fuel lines
5. Crossover duct
6. Crossover duct gasket
7. Air-fuel control line.

> [!note] Note · Примечание
> This hardware will be installed on all water jacket aftercooled industrial engines with the Bosch® in-line pump. Part numbers will be listed in the 6B industrial engine parts catalog.

### Maintenance Check

Check the battery voltage.

Minimum: 6.5 VDC

![[ea900sb.png]]

Check the thermistor.

Disconnect the thermistor.

Turn the ignition switch to the ON position.

![[ee900wc.png]]

> [!note] Note · Примечание
> The WAIT-TO-START light should come on.

The solenoids should click on.

![[ee900kb.png]]

Wait 20 seconds.

The solenoids should click off.

The WAIT-TO-START light should begin flashing.

> [!note] Note · Примечание
> The WAIT-TO-START light will flash, indicating an open circuit in the thermistor wiring. Disconnecting the thermistor simulates this condition.

![[ee900kc.png]]

Turn the ignition switch to the OFF position.

Connect the thermistor wire harness.

![[ee900wd.png]]

Preheat Cycle - Check

Turn the ignition switch to the ON position.

Do **not** start the engine.

![[ee900we.png]]

The solenoids should click on.

> [!note] Note · Примечание
> If the engine has been running, the temperature is probably above 15°C \[59°F\].

![[ee900kd.png]]

After the preheat period, the WAIT-TO-START light will go off and **not** flash.

Set the multimeter scale to read DC voltage.

Connect the multimeter, Part Number 3822666, lead to the intake manifold heater terminals. Check each terminal individually.

![[ee900ke.png]]

If voltage is present, check the pull-in coil of the solenoids.

Check for voltage at the pull-in coil of solenoid.

1. If voltage at pull-in coil, replace electronic control module.
2. If no voltage present at pull-in, replace solenoid.

![[ee900kf.png]]

Start the engine.

Do **not** hold the ignition switch in the start position longer than 10 seconds.

If the engine does **not** start, turn the ignition switch to the OFF position.

![[ee900kg.png]]

Return the ignition switch to the ON position; then begin the normal starting cycle again.

![[ee900wf.png]]

### Remove

> [!danger] WARNING · Опасно
> Always lock and tag out the ignition system before working on the engine. Disable the preheater electrical system to reduce the possibility of property damage and personal injury from electrical shock.

Remove the air intake elbow from the cover.

![[ic9tbaa.png]]

Remove the air intake spacer, Part Number 3917938, from the intake cover and discard. If a manifold spacer is **not** used, replace the elbow with elbow, Part Number 3918982, or equivalent.

![[im9cvmb.png]]

### Install

Install the two gaskets, Part Number 3913352, above and below the grid heater, Part Number 3924594, with the ground (-) strap under the grid heater mounting capscrews.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [18 ft-lb]

![[10900276.png]]

Install the air intake clamps.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[ic9tbaa.png]]

Install the temperature sensor in the intake cover nearest the intake elbow.

> [!tip] Момент затяжки · Torque Value
> 35 n•m [26 ft-lb]

![[10900275.png]]

> [!note] Note · Примечание
> The wiring harness **must** be secured within 152 mm \[6 in\] of any connection to reduce the possibility of connector or ring terminal damage.

Install the wiring harness, and secure to avoid chafing or burning.

![[10900274.png]]

If the engine does **not** have an electrical shutdown solenoid or it has a timer module for the shutdown solenoid, use the 3-pin connector tee to wire the vehicle as illustrated. See the table below.

| Connector Letter | Function | Recommended Location |
|---|---|---|
| A | Module Power | Keyswitch ON power supply |
| B | Crank Sensor | "S" Terminal on starter or keyswitch "Crank" |
| C | Ground (-) | Engine, Chassis, or Battery Ground (-) |

![[10900273.png]]
