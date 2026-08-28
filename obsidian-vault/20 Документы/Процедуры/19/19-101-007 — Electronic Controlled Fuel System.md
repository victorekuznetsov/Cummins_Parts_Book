---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "19-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-03-05"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `19-101-007`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2013-03-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-101-007.pdf)

### QSK System Description

The QSK fuel system is an electronic engine control system designed to optimize engine control and reduce exhaust emissions. The QSK fuel system controls engine speed and fuel pressure based on input from the electric throttle and other equipment-specific and/or model-specific features.

![[ck800wa.png]]

### Diagnostic Fault Codes

The QSK fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which makes troubleshooting easier. The fault codes are retained in the engine control module (ECM).

There are two types of fault codes: engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at one time, but **not** at the moment).

![[19400328.png]]

Active fault codes can be read using the warning (yellow) and stop lamps (red) in the cab panel or INSITE™.

Inactive fault codes can **only** be viewed with INSITE™.

![[19400330.png]]

When the vehicle keyswitch is turned on and the diagnostic switch off, the fault code lamps (red, yellow, and engine protection) will illuminate for approximately 2 seconds, one after another, to check their operation.

> [!note] Note · Примечание
> The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are combined as red and the warning lamp as yellow.

![[19400331.png]]

The lights will remain off until a fault code is recorded. If a stop (red) light comes on while the engine is in operation, the fault can disable the engine. Stop the engine in a safe manner as soon as possible.

If the warning (yellow) light illuminates, the engine can still be operated, but it can lose some system features that can sometimes result in a power loss. The failure **must** be repaired as soon as is practicable.

The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.

![[19400332.png]]

To check for active fault codes, turn the vehicle keyswitch to the OFF position. Move the diagnostic switch to the ON position.

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

![[19400336.png]]

Turn the vehicle keyswitch to the ON position. If no active fault codes are recorded, all three lights will come on and stay on. If active fault codes are recorded, all three lights will come on momentarily. The yellow (warning) and red (stop) lights will begin to flash the code of the recorded fault.

![[19400337.png]]

The fault code will flash in the following sequence: First, the yellow (warning) lamp will flash. Then there will be a short, 1-second pause when both the yellow and red lights are off. The numbers of the recorded fault code will then flash in red. There will be a 1-second pause between each number. When the number is done flashing, a yellow light will appear again. The number will repeat in the same sequence.

![[19400338.png]]

The lights will continue to flash the same fault code until the system is advanced to the next active fault code. To go to the second fault code, move the idle speed adjust switch to "+," then release. You can also go back to the previous fault code by moving the switch to "-," then releasing. To check the third or fourth fault code, move the switch to "+," then release it when all active fault codes have been viewed. Moving the switch to "+" will go back to the first fault code. A brief explanation of all of the fault codes is in Section TF of this manual.

![[19400339.png]]

To stop the diagnostic system, move the diagnostic switch to the OFF position, or remove the shorting plug. Turn the vehicle keyswitch to the OFF position.

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

![[gp8swvv.png]]

### Fault Code Snapshot Data

When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

Fault code snapshot data can **only** be viewed with INSITE™.

![[19400349.png]]

### Engine Protection System

The QSK fuel system engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid level, switch position, and pressure and will log diagnostic faults when an over or under normal operating range condition occurs. If an out-of-range condition exists, engine derate action can be initiated. The operator will be alerted by the illumination of the in-cab maintenance lamp. The warning lamp will start to flash when out-of-range condition continues to get worse and engine shutdown will occur. The operator **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.

Engine protection system monitors:

- Coolant temperature
- Coolant level (optional)
- Intake manifold temperature
- Oil pressure
- Coolant pressure (QSK45/60/78 **only**)
- Blowby pressure (QSK45/60/78 **only**)
- Oil level (QSK45/60/78 **only**)
- Oil temperature (QSK45/60/78 with CENSE™ **only**)
- Fuel temperature (QSK23/45/60/78 **only**).

Engine protection system monitors for:

- High coolant temperature
- Low coolant level (optional)
- High intake manifold temperature
- Low/very low oil pressure
- Low coolant pressure (QSK45/60/78 **only**)
- High blowby pressure (QSK45/60/78 **only**)
- Low oil level (QSK45/60/78 **only**)
- High oil temperature (QSK45/60/78 with CENSE™ **only**)
- High fuel temperature (QSK23/45/60/78 **only**).

Depending on the calibration configuration, the engine protection system can have two selectable features: Engine protection enable and engine protection shutdown. If the engine protection feature is grayed-out on INSITE™, then the feature is **not** tool adjustable and is on by default. If engine protection enable feature is selected, engine power and speed are gradually reduced, depending on the level of severity of the observed condition. If engine protection shutdown feature is selected, the engine will shut down. The engine can be restarted by turning the keyswitch off and then back on.

Engine protection features:

- Engine protection enable
- Engine protection shutdown.

### Flow Diagram

The fuel pump (1) draws fuel from the equipment fuel tank. The fuel circulates through the fuel filters before it enters the gear pump. The fuel pump governs the fuel output pressure, based on engine speed. This governed fuel pump pressure flows to the control valve body (2).

The control valve body protects the ECM (3) from engine heat and regulates fuel flow to the timing and fueling rail lines (4). The timing and fueling lines connect to fuel blocks (5) on the cylinder head. The cylinder has drillings from the fuel manifold to the injectors.

![[19400345.png]]

QSK19 Control Valve Body

The control valve body regulates the fuel flow with timing rail actuator (2), and a fueling rail actuator (6).

Fuel flows into the control valve body at the supply fitting (1). Fuel then circulates around the timing rail actuators (2), regulated by the timing rail pressure sensor (3), and flows out the timing rail outlet (4).

Fuel also flows to the fuel shut off valve (5) and then to the fueling rail actuator (6). The regulator then passes fuel to the rail sensor and up to the fueling rail pressure outlet (8).

The fuel rail pressure sensor (7) is located under the timing rail pressure sensor (3).

The fuel rail pressure does **not** intersect with the timing rail.

![[19400346.png]]

QSK23 Engines

The control valve body regulates the fuel flow with timing rail actuator (6), and a fueling rail actuator (4).

Fuel flows into the control valve body at the supply fitting (7). Fuel then circulates around the timing rail actuators (6), regulated by the timing rail pressure sensor (1), and flows out the timing rail outlet (8).

Fuel also flows to the fuel shut off valve (10) and then to the fueling rail actuator (4). The regulator then passes fuel to the rail sensor and up to the fueling rail pressure outlet (9).

The fuel rail pressure sensor (2) is located under the timing rail pressure sensor (1).

The ambient air sensor (3) is located on the bottom of the control valve body.

The fuel rail pressure does **not** intersect with the timing rail.

![[05400182.png]]

QSK45, QSK60, and QSK78 Control Valve Body

The control valve body regulates the fuel flow with timing rail actuator (2), and a fueling rail actuator (6).

Fuel flows into the control valve body at the supply fitting (1). Fuel then circulates around the timing rail actuators (2 and 9), regulated by the timing rail pressure sensor (3), and flows out the timing rail outlet (4).

Fuel also flows to the fuel shut off valve (5) and then to the fueling rail actuator (6). The regulator then passes fuel to the rail sensor and up to the fueling rail pressure outlet (8).

The timing rail pressure sensor is shown at left (3). Fuel temperature is monitored by a fuel temperature sensor (10) mounted above the fuel rail pressure sensor (7).

![[19400975.png]]

The regulated fuel flow from the control valve body travels from the timing and fueling rail pressure lines; through the fuel block, fuel manifold, and drillings in the cylinder head; and delivered to the timing and fueling rail orifices.

![[19400347.png]]

### QSK23, QSK45, QSK60, and QSK78 System Components

The QSK fuel system on an engine consists of:

1. Fuel pump
2. Timing actuator
3. Timing pressure sensor
4. Fuel shutoff valve
5. Rail actuator
6. Rail pressure sensor
7. Intake manifold pressure sensor
8. Oil pressure sensor
9. Intake manifold air temperature sensor
10. Coolant temperature sensor
11. Engine speed sensor
12. Coolant level sensor
13. Engine harness
14. OEM interface harness
15. Engine control module (ECM)
16. Fuel cooler (**not** on QSK23)
17. Ambient air pressure sensor
18. Fuel temperature sensor (**not** on QSK19)
19. Coolant pressure sensor (**not** shown) (**not** on QSK19 and QSK23).

![[nobox.png]]

The control valve body contains actuators, fuel temperature sensor, and pressure sensors that control timing and fuel metering at the injector.

The ECM processes the information it receives from the sensors and controls the opening and closing of the actuators. This action controls timing and fuel metering, and then produces the correct horsepower and torque for the latest engine condition.

![[19400349.png]]

Engine Control Module Inputs

1. Timing pressure sensor
2. Rail pressure sensor
3. Engine speed sensor
4. Throttle position sensor
5. Idle validation switch

![[19400350.png]]

1. Intake manifold air pressure sensor
2. Oil pressure sensor
3. Intake manifold air temperature
4. Coolant temperature sensor
5. Coolant level sensor
6. Ambient air pressure sensor
7. Coolant pressure sensor
8. Fuel temperature sensor
9. Pump pressure sensor.

![[19400709.png]]

The engine speed sensor provides engine speed and position information. The sensor is located on the back side of the cylinder block gear housing flange, below the accessory drive.

The QSK23 engine speed sensor is located in the top of the flywheel housing.

![[00a00035.png]]

The intake manifold pressure sensor and the intake manifold air temperature sensor are located in the intake manifold. The intake manifold pressure sensor monitors positive manifold pressures used in the air-fuel control function. The intake manifold air temperature sensor measures the turbocharged air temperature. The intake manifold air temperature sensor is also used for the engine protection system.

![[19400352.png]]

The engine coolant temperature sensor provides data for optimized timing for emissions reduction, and is used for the engine protection system.

The coolant temperature sensor is located in the thermostat housing.

![[19400353.png]]

The coolant level sensor, if equipped, is mounted in the radiator top tank. It is a fluid level-actuated switch required for the engine protection system.

> [!note] Note · Примечание
> This is an optional sensor which will **not** be on all vehicles. A shorting plug will be installed if the coolant level sensor is **not** used.

![[19400354.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is on the engine block.

![[19400355.png]]

The coolant pressure sensor sends signals to the ECM for the engine protection system. The sensor is on the engine block.

> [!note] Note · Примечание
> This is an optional sensor which will **not** be on all vehicles.

![[19801042.png]]

Engine Control Module Outputs

The ECM processes input data and then controls these output parts:

1. Timing and rail actuators
2. Fuel shutoff valve
3. Fuel pump actuator

> [!note] Note · Примечание
> There are **two** timing actuators for QSK45, QSK60, and QSK78 engines.

![[19400356.png]]

### INSITE™ Electronic Service Tool Description

INSITE™, Part Number 3824801, is a service tool for the Quantum™ fuel system. Use INSITE™ to:

- Program owner specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Change the engine power or rated speed calibration.

Reference the INSITE™ for QSK19 Fuel System Manual.

> [!note] Note · Примечание
> INSITE will **only** communicate with the ECM over the J1587 (1708) data link protocol in all Quantum™ systems and will **not** communicate with a J1939 data link.

![[19400357.png]]
