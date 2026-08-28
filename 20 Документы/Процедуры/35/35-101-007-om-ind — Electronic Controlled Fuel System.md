---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "35-101-007-om-ind"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-03-05"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4021942"
figures: 19
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-101-007-om-ind.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-101-007-om-ind.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `35-101-007-om-ind`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4021942 — QSM11 Industrial Operation and Maintenance Manual|4021942]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2013-03-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-101-007-om-ind.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-101-007-om-ind.pdf)

### General Information

The system is an electronically controlled fuel injection system that optimizes fuel economy. It does this by controlling the torque and horsepower curve, air-fuel control (AFC) function, engine high speed, low idle, and road speed.

![[oi800v13.png]]

The engine has the capability of controlling the fan clutch actuator if an electronically controlled fan clutch is used.

The engine also allows the engine brakes to be activated by controlling the engine brake solenoids.

![[20200005.png]]

### Diagnostic Fault Codes

Industrial Applications

The system can show and record operation irregularities that present themselves as fault codes. These codes will make troubleshooting easier. The fault codes are recorded in the ECM. They can be read using the two fault lamps in the cab panel or with INSITE™.

> [!note] Note · Примечание
> **Not** all engine irregularities are shown as fault codes.

![[17c00067.png]]

There are two types of fault codes:

- Engine electronic fuel system codes
- Engine protection system codes.

![[17c00066.png]]

The engine electronic fuel system fault codes can be seen on the WARNING and STOP lights in the cab panel.

> [!note] Note · Примечание
> Inactive fault codes can **not** be blinked out on the two lights in the cab panel. An INSITE™ service tool **must** be used to read inactive faults in the ECM. Reference a Cummins® Authorized Repair Location.

![[17c00030.png]]

The STOP fault light will be red. The WARNING light will be yellow or red, depending on the OEM's preference. When the vehicle keyswitch is turned on and the diagnostic switch is off, all three lights will illuminate to check their operation. The lights will go off in sequence after about 2 seconds.

![[19200053.png]]

The lights will remain off until a fault code is recorded. If a light remains on, an active fault exists.

If the STOP light (red) is illuminated while operating, the fault can be engine disabling. The equipment **must** be shut off as soon as it can be done in a safe manner. The equipment **must** remain parked as long as this fault exists. If the WARNING light (yellow or red) is illuminated, the equipment can be safely operated, but the fault **must** be corrected as soon as possible.

![[19200435.png]]

The engine protection system logs separate fault codes for out-of-range conditions associated with any of the following sensors:

- Coolant temperature
- Coolant level
- Oil temperature
- Oil pressure
- Intake manifold temperature.

![[17c00068.png]]

This system will activate an in-cab warning device when an out-of-range condition occurs. The warning device is a light, a buzzer, or both. This system will also activate the yellow fluid lamp, if equipped.

![[oi803vz.png]]

If the engine protection system light or buzzer comes on while driving, it means a fault code has been recorded. The lamp will remain on as long as the fault exists, and engine power and speed will gradually be reduced. If the out-of-range conditions continue, the light will start to flash or blink. If the engine protection shutdown feature is enabled, the engine will be shut down to help prevent engine damage.

The fault **must** be corrected as soon as possible.

![[17c00069.png]]

Turn off the engine. To check for engine electronic fuel system and engine protection system fault codes, move the diagnostic switch to the ON position, or connect the shorting plug into the diagnostic connector.

![[gp8swvs.png]]

Turn the keyswitch to the ON position.

If no active fault codes are recorded, both lights will come on and stay on.

If active fault codes are recorded, both lights will come on momentarily, then begin to flash the code of the recorded faults.

![[gp8swgr.png]]

The fault code will flash in the following sequence:

First, a WARNING (yellow) light will flash. Then there will be a short 1- or 2-second pause after which the number of the recorded fault code will flash in STOP (red). There will be a 1- or 2-second pause between each number. When the number has finished flashing in red, a yellow light will appear again. The three-digit code will repeat in the same sequence.

![[gp800kd.png]]

The lights will continue to flash the same code until the system is told to do something else. To go to the next fault code, move the CRUISE CONTROL/PTO switch momentarily to the RESUME/ACCEL position. You can go back to the previous fault code by momentarily moving the CRUISE CONTROL/PTO switch to the SET/COAST position. If **only** one active fault is recorded, the system will continuously display the same fault code when either RESUME/ACCEL or SET/COAST switch is depressed.

![[gp8swkq.png]]

### Engine Protection System

> [!note] Note · Примечание
> Engine power and speed will be gradually reduced, depending on the level of severity of the observed condition. The engine protection system will **not** shut down the engine unless the engine protection shutdown feature has been selected. If the feature has been selected and the engine does shut down, the engine can be restarted by turning OFF the keyswitch, then turning it back ON.

The engines are equipped with an engine protection system. The system monitors critical engine temperatures and pressures, and will log diagnostic faults when an abnormal operating condition occurs. If an out-of-range condition exists and engine derate action is to be initiated, the operator will be alerted by an in-cab warning light. The warning light will blink or flash when out-of-range conditions continue to get worse. The driver **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.

![[17c00028.png]]

### Fuel System Description

Automotive Applications

The ISM fuel system on an engine consists of:

1. Fuel shutoff valve
2. Oil pressure sensor and temperature sensor
3. Intake manifold boost sensor
4. Cooling plate
5. Engine control module (ECM)
6. Engine wiring harness Deutsch connector.

![[19200112.png]]

1. OEM wiring harness
2. Engine wiring harness Deutsch connector
3. Fuel in
4. Fuel out
5. Fuel gear pump
6. Engine position sensor (EPS)
7. Coolant temperature sensor (in thermostat support)
8. Coolant level sensor (in overflow tank) - optional
9. Intake manifold temperature sensor
10. Ambient air pressure sensor.

![[19200113.png]]

The idle adjustment is in the cab panel. Use this switch to adjust the engine idle speed in increments of 25 rpm.

- Automotive - 600 to 800 rpm
- Transit Bus - 650 to 800 rpm.

![[gp2swkp01.png]]

Each time the switch is briefly moved to the minus (-) position, the idle speed is decreased by 25 rpm. When the switch is briefly moved to the plus (+) position, the idle speed is increased by 25 rpm.

![[gp8swki.png]]
