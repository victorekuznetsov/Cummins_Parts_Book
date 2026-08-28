---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "20-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-11-05"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "3666120"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `20-101-007`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[3666120 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Operation and Maintenance Manual|3666120]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2013-11-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-101-007.pdf)

### QSK System Description

The QSK fuel system is an electronic engine control system designed to optimize engine control and reduce exhaust emissions. The QSK fuel system controls engine speed and fuel pressure based on input from the electric throttle and other equipment-specific and/or model-specific features.

![[19400349.png]]

### Diagnostic Fault Codes

The QSK fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which makes troubleshooting easier. The fault codes are retained in the engine control module (ECM).

![[19400328.png]]

There are two types of fault codes: engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at one time, but **not** at the moment).

Active fault codes can be read using the warning (amber) and stop lamps (red) in the cab panel or INSITE™ electronic service tool.

Inactive fault codes can **only** be viewed with INSITE™ electronic service tool.

![[19400330.png]]

When the vehicle keyswitch is turned on and the diagnostic switch off, the fault code lamps (red, amber, and engine protection) will illuminate for approximately two seconds, one after another, to check their operation.

![[19400331.png]]

The lights will remain off until a fault code is recorded. If a stop (red) light comes on while the engine is in operation, the fault can disable the engine. Stop the engine in a safe manner as soon as possible.

If the warning (amber) light illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The failure **must** be repaired as soon as possible.

![[19400332.png]]

The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.

The following are engine protection system out-of-range fault codes:

1. Coolant temperature
2. Coolant level (optional)
3. Oil pressure.

![[19400328.png]]

> [!note] Note · Примечание
> Lamp colors and labels vary by original equipment manufacturer (OEM).

The engine protection system will light the maintenance lamp (orange) when an out-of-range condition occurs.

![[19400334.png]]

If the engine protection system fluid lamp comes on while driving, it means a fault code has been recorded. The light will remain on as long as the fault is occurring.

The light will begin to flash if the condition continues to get worse. The engine power and/or speed will gradually reduce. If the engine protection shutdown feature is enabled, the engine will shut down to prevent engine damage.

![[19400335.png]]

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

To check for active fault codes, turn the vehicle keyswitch to the OFF position and move the diagnostic switch to the ON position.

![[19400336.png]]

Turn the vehicle keyswitch to the ON position. If no active fault codes are recorded, all three lights will come on and stay on. If active fault codes are recorded, all three lights will come on momentarily. The amber (warning) and red (stop) lights will begin to flash the code of the recorded fault.

![[19400337.png]]

The fault code will flash in the following sequence: First, the amber (warning) lamp will flash. Then there will be a short, one-second pause when both the yellow and red lights are off. The numbers of the recorded fault code will then flash in red. There will be a one-second pause between each number. When the number is done flashing, an amber light will appear again. The number will repeat in the same sequence.

![[19400338.png]]

The lights will continue to flash the same fault code until the system is advanced to the next active fault code. To go to the second fault code, move the idle speed adjust switch to "+", then release. You can also go back to the previous fault code by moving the switch to "-", then releasing. To check the third or fourth fault code, move the switch to "+", then release it when all active fault codes have been viewed. Moving the switch to "+" will go back to the first fault code. A brief explanation of all of the fault codes is in Section TF of this manual.

![[19400339.png]]

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

To stop the diagnostic system, move the diagnostic switch to the OFF position or remove the shorting plug. Turn the vehicle keyswitch to the OFF position.

![[gp8swvv.png]]

### Fault Code Snapshot Data

When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

Fault code snapshot data can **only** be viewed with INSITE™ electronic service tool.

![[19400349.png]]

### Engine Protection System

QSK fuel system engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid level, switch position, and pressure and will log diagnostic faults when an over or under normal operating range condition occurs. If an out-of-range condition exists, engine derate action can be initiated. The operator will be alerted by the illumination of the in-cab maintenance lamp. The warning lamp will start to flash when out-of-range condition continues to get worse and engine shutdown will occur. The operator **must** pull to the side of the road when it is safe to do so, to reduce the possibility of engine damage.

#### Engine protection system monitors:

- Coolant temperature
- Coolant level (optional)
- Intake manifold temperature
- Oil pressure.

#### Engine protection system monitors for:

- High coolant temperature
- Low coolant level (optional)
- High intake manifold temperature
- Low/very low oil pressure.

The engine protection system can have two selectable features: Engine protection enable and engine protection shutdown. If the engine protection enable feature is selected, engine power and speed are gradually reduced, depending on the level of severity of the observed condition. If engine protection shutdown feature is selected, the engine will shut down. The engine can be restarted by turning the keyswitch OFF and then back ON.

#### Engine protection features:

- Engine protection enable
- Engine protection shutdown.
