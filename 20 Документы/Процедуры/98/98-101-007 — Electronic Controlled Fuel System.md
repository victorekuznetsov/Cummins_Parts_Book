---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "98-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-03-24"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 44
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `98-101-007`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-101-007.pdf)

### Programmable Features

CENTRY™

The engine subsystem contains:

1. Electronic Control Module (ECM)
2. Main Engine Harness
3. Rail Pressure Sensor
4. Engine Speed Sensor
5. Electronic Fuel Control Valve (EFC).

![[19801566.png]]

The CENTRY™ system has been designed for both 12- and 24- VDC original equipment manufacturer (OEM) electrical systems. The following components are different between 12- and 24-VDC systems:

1. ECM
2. EFC Valve
3. Fuel Shutoff Valve
4. Electric STC Actuator (if used)
5. Auxiliary Shutdown Device (if used)

![[19801567.png]]

The following components are the same in both 12- and 24-VDC systems:

1. Main Engine Harness
2. Rail Pressure Sensor
3. Engine Speed Sensor
4. OEM throttle switch interface.

![[19801568.png]]

The CENTRY™ ECM is loaded with a calibration containing engine control and OEM application-specific information. A Cummins Authorized Repair Location can recalibrate an ECM on the equipment with INSITE™, Compulink™, or Echeck™ and the Electronic Software Database and Network (ESDN). Some adjustments can be made with the Cummins INSITE™, Compulink™, or Echek™ when a CENTRY™ cartridge is used.

![[19800109.png]]

CENTRY™ features used in an application will be displayed in INSITE™, Compulink™, or Echek™ monitor mode and view parameter screens. The OEM and calibration will determine which features are used and which parameters can be adjustable.

![[19800109.png]]

The CENTRY™ main engine harness contains the following connections and fuses:

1. ECM Connector
2. EFC Valve 90-Degree Connectors
3. Fuel Shutoff Valve Ring Terminal
4. 5-AMP Fuses
5. Engine-Side Datalink Connector
6. Rail Pressure Sensor Connector
7. OEM 9-pin Connector (C-5)
8. OEM 9-pin Connector (C-6)
9. CENTRY™ Ground Ring Terminal
10. Electric STC Ring Terminal (optional)
11. Engine Speed Sensor Connectors.

> [!note] Note · Примечание
> Harness connector breakout locations differ between engine families.

![[19801570.png]]

OEM Interface Components

**OEM Interface Components**

The CENTRY™ system is connected to the OEM equipment through the two OEM 9-pin connectors on the main engine harness.

![[19801575.png]]

The OEM equipment will supply an electronic throttle signal.

It can be supplied by an electronic foot throttle, hand throttle, switch, or equipment ECM (OEM control module).

![[19801576.png]]

Most mechanical drive transmission (vehicular) applications will use an idle validation switch in the throttle interface. The idle validation switch is an on/off switch which indicates idle or off idle. This switch will verify when the throttle is in the idle position.

Most stationary power, hydraulic pump drive, or electric drive applications will **not** use idle validation.

![[19801577.png]]

The OEM equipment can interface with one or more of the following CENTRY™ switch features:

1. Alternate Torque Control
2. Alternate Low Idle Control
3. Intermediate Speed Control
4. Alternate Droop/High Idle Control.

![[19801578.png]]

Most mechanical drive transmission (vehicular) applications will use a redundant validation switch on the alternate droop/high-idle control and intermediate-speed control switches. Switch validation provides a secondary signal to indicate whether or **not** the switch is on.

Most stationary power, hydraulic pump drive, or electric-drive applications will **not** use switch validation.

![[19801579.png]]

If none of the switched features are used, the OEM equipment can use the CENTRY™ system to read coolant temperature, oil pressure, and auxiliary oil temperature (transmission temperature). These data are available to the OEM through the public datalink and require an OEM electronic interface.

![[19801580.png]]

The OEM equipment can utilize the optional auxiliary driver lead. This can be used to power auxiliary shutdown devices or provide an engine torque output signal.

![[19801581.png]]

The OEM equipment contains a fault lamp and switch in the cab or operator location. The fault lamp will light for 1 to 2 seconds after the key is turned on. The lamp will go out if no faults are detected in the CENTRY™ system.

![[19801582.png]]

Electronic Governor Operation

**Electronic Governor Operation**

The CENTRY™ electronic governor has been designed to be flexible to meet the wide variety of engine control needs of off-highway equipment.

![[19801583.png]]

The OEM selects low- and high-idle settings along with the optimum engine response governor droop characteristics for the application. The OEMs also decide whether or **not** some of these settings will be Compulink™ or Echek™ adjustable.

![[19801584.png]]

Operational Features

**Operational Features**

The CENTRY™ system contains optional OEM-selected features to maximize engine speed, power, torque, response, and smoke performance to meet specific application needs. On all optional features, the OEM will determine the type of switch used and its location.

![[19801586.png]]

Alternate Torque Control

**Alternate Torque Control**

This feature enables an alternative electronically controlled maximum engine torque curve for optimum operating efficiency in loaded-versus-unloaded conditions.

The alternate torque feature is activated whenever the normally closed alternate torque switch is opened and 5 VDC are detected on the alternate torque signal line. Five rail-pressure-versus-engine-speed points define the alternate torque curve.

Shown is a graph illustrating an alternate torque curve that is below the normal torque curve.

![[19801587.png]]

Alternate Low-Idle Control

**Alternate Low-Idle Control**

This feature allows for two different low-idle speed settings with normal throttle control above the low-idle speed setting. This feature is often used on electric drive haul trucks when they are traveling above 5 kph \[3 mph\].

![[19801588.png]]

The alternate low-idle feature is activated whenever the normally closed alternate low-idle switch is opened and 5 VDC are detected on the alternate low-idle signal line. The following art illustrates an alternate low-idle speed that is above the normal low-idle speed.

![[19801589.png]]

Intermediate-Speed Control

**Intermediate Speed Control**

This feature will override the throttle and control the engine speed to the calibrated speed setting. This feature is often used in conjunction with power take-off (PTO) on some equipment or dynamic brake engine speed on electric-drive haul trucks.

![[19801590.png]]

The intermediate-speed feature is activated whenever the normally open intermediate-speed control switch is closed and less than 1 VDC is detected on the intermediate-speed signal line. If switch validation is used, both intermediate-speed and switch validation signals **must** be less than 1 VDC before this feature can be detected.

![[19801591.png]]

Alternate Droop/High Idle Control

**Alternate Droop/High-Idle Control**

This feature allows two different engine response and high-idle settings. This allows two different operating modes to optimize governor performance.

![[19801592.png]]

The alternate droop/high-idle feature is activated whenever the normally open alternate droop/high-idle switch is closed and less than 1 VDC is detected on the alternate droop/high-idle signal line. If switch validation is used, both alternate droop/high-idle and switch validation signals **must** be less than 1 VDC before this feature can be activated.

![[19801593.png]]

Monitor

**Monitor**

This feature can be used when none of the switched features are used. It allows for the CENTRY™ system to read oil pressure, coolant temperature, and/or an auxiliary temperature sensor and broadcasts these inputs on the datalink to an OEM electronic dash or OEM control module.

![[19801594.png]]

Shown is a wiring diagram illustrating the monitor feature circuits.

![[19801595.png]]

Auxiliary Shutdown Control

**Auxiliary Shutdown Control**

The auxiliary driver in the CENTRY™ system can be used to power auxiliary shutdown devices such as air intake flaps or additional fuel shutdown devices. It can also be used to shut off other equipment when the engine shuts down.

Auxiliary shutdown control will remove electrical power to the auxiliary driver when the keyswitch in turned off or if the engine shuts down due to an overspeed condition.

![[19801581.png]]

Torque Output Signal

**Torque Output Signal**

The torque output signal is a standard broadcast on the datalink. In addition, the auxiliary driver lead can be used to provide an engine torque output signal in applications where the CENTRY™ auxiliary shutdown control feature is **not** used.

The torque output signal is used in some transmission interfaces for optimization of shift schedules and to provide smoother shifting.

![[19801601.png]]

Transient Black Smoke Control

**Transient Black Smoke Control**

This feature limits fueling based on time and fuel delivery, in addition to the AFC and STC hydromechanical smoke control functions CENTRY™ vehicles have installed.

![[19801602.png]]

The CENTRY™ transient black smoke feature limits the rate of fuel rail pressure increase per unit time. On some applications, the electronic no-air, delay, and spring rate can be Compulink™/Echeck™ adjustable. These electronic parameters are similar to those on the hydromechanical AFC in the fuel pump.

![[19801603.png]]

### ADVANTAGE™

General Information

Many agricultural applications will use the CENTRY™ electronic governor to provide ADVANTAGE™ torque and power control.

![[19801596.png]]

ADVANTAGE™ control allows the engine to deliver additional horsepower and torque rise as the engine is lugged below rated speed. This provides improved operating efficiency in applications where steady ground speeds are desired with continuously changing engine load.

![[19801597.png]]

CENTRY™ ADVANTAGE™ electronically controls the maximum fuel rail pressure available according to the electronically calibrated peak power rail pressure point (advantage point) and the electronically calibrated maximum rail pressure at rated engine speed point.

![[19801598.png]]

ADVANTAGE™ provides a steeper torque rise between peak power and rated conditions than is obtainable with the hydromechanical fuel system. This results in reduced speed drop and more available power under external loading conditions.

![[19801599.png]]

### Diagnostic Fault Codes

General Information

The CENTRY™ system can display and record detectable fault conditions within its systems and circuits. A yellow diagnostic lamp near the operator's controls will be illuminated when a system fault becomes active.

![[19801604.png]]

The fault lamp should light for about 1 to 2 seconds after key-on, and then go out after no faults have been detected.

![[19802499.png]]

While a fault condition is being detected, the fault lamp will turn ON or ON FLASHING. CENTRY™ will turn the lamp ON for warning faults, and ON FLASHING for more severe faults that can affect engine operation and that need immediate attention. Active fault conditions **must** be corrected as soon as possible.

![[19801605.png]]

To determine an active CENTRY™ fault code, shut off the engine and turn keyswitch to the ON position (engine **not** running). Toggle the diagnostic switch to the ON position for 1 to 2 seconds and then release it. The fault lamp will illuminate while the diagnostic switch is held in the ON position.

![[19801606.png]]

After releasing the diagnostic switch, there is a short pause, followed by the first fault code. CENTRY™ fault codes consist of three digits with up to five flashes for each digit. There is a short pause, between each digit of the fault code. Once the three digits have flashed and the code is known, there is a longer pause followed by a repeating of the same fault code sequence.

![[19801607.png]]

Toggling the diagnostic switch will advance to the next fault code. Once all active fault codes have been displayed, the fault code flash sequence will be repeated starting from the first fault code.

![[19801608.png]]

Starting the engine or turning the keyswitch to OFF will exit the diagnostical fault flash mode.

![[19801609.png]]

Back-up Mode Operation

**Backup Mode Operation**

When certain system faults are detected, the engine will default to backup mode. The definition of backup mode is different for different faults. In general, if an idle validation switch is **not** used, the backup mode will be some constant calibrated speed. If an idle validation switch is used, the backup mode will be two speeds based on switch position: Low speed when switch on-idle, high speed when switch off-idle.

![[19801610.png]]

### INSITE™ Monitor Mode

General Information

The service tool monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

> [!note] Note · Примечание
> Each service tool monitor mode screen contains the same information, but the screens will appear differently.

![[19400360.png]]

Shown is the CENTRY™ monitor screen showing all of the possible parameters that can be displayed in monitor mode as they would be seen on an INSITE™ screen. The number of these parameters that are displayed will vary between engine applications.

Monitor mode can be used to look for abnormally fluctuating readings while troubleshooting. Sensors that are failed in range can also be found by looking for fixed readings. For example, rail pressure reading does **not** change with engine speed.

![[18800003.png]]
