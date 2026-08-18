---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "87-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2013-03-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 87
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `87-101-007`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2013-03-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-101-007.pdf)

### Diagnostic Fault Codes

The fuel system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which makes troubleshooting easier. The fault codes are retained in the ECM.

![[19400328.png]]

There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).

![[nobox.png]]

> [!note] Note · Примечание
> INSITE™ reads both left- and right-bank ECMs via one datalink connector on the J1939 backbone harness.

Active fault codes can be read using the warning and stop lamps (red or yellow) in the cab panel or INSITE™, Part Number 3162261. Inactive fault codes can **only** be viewed on INSITE™, Part Number 3162261.

Fault codes (active or inactive) viewed in INSITE™ are differentiated between relevant left-bank and right-bank ECMs. Fault codes on the left-bank, or primary ECM, display **only** the three-digit fault code number. Fault codes on the right-bank, or secondary ECM, display the three-digit fault code number with the letter “R” following it.

![[19a00731.png]]

When the vehicle keyswitch is turned on and the diagnostic switch is off, the fault code lamps (red, yellow, and engine protection) will illuminate for approximately 2 seconds, one after the other, to check their operation.

![[19400331.png]]

The lights will remain off until a fault code is recorded. If a red (stop) light comes on while the engine is in operation, the fault can be engine disabling. Stop the engine operation in a safe manner as soon as possible.

If the yellow (warning) light illuminates, the engine can still be operated, but it can lose some system features, which can sometimes result in a power loss. The failure **must** be repaired as soon as it is convenient.

![[19400332.png]]

The engine protection system will light the fluid lamp (orange) when an out-of-range condition occurs.

> [!note] Note · Примечание
> Lamp colors and labels will vary by OEM.

![[19400334.png]]

If the engine protection system fluid lamp comes on while driving, it means that a fault code has been recorded. The light will remain on as long as the fault is occurring.

The light will begin to flash if the condition continues to get worse. The engine power and/or speed will be gradually reduced. If the engine protection shutdown feature is enabled, the engine will shut down to prevent engine damage.

![[19400335.png]]

To check for active fault codes, first turn the vehicle keyswitch to the OFF position. Move the diagnostic switch to the ON position.

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

![[19400336.png]]

Turn the vehicle keyswitch to the ON position. If no active fault codes are recorded, all three lights will come on and stay on. If active fault codes are recorded, all three lights will come on momentarily. The yellow (warning) and red (stop) lights will begin to flash the code of the recorded fault.

![[19400337.png]]

The fault code will flash in the following sequence. First, the yellow (warning) lamp will flash. Then, there will be a short 1-second pause when both the yellow and red lights are off. Lastly, the numbers of the recorded fault code will flash in red. There will be a 1-second pause between each number. When the number is done flashing, a yellow light will appear again. The fault code number will repeat in the same sequence.

![[19400338.png]]

The lights will continue to flash the same fault code until the system is manually advanced to the next active fault code. To go to the second fault code, move the idle speed adjust switch to “+,” and then release it. You can also go back to the previous fault code by moving the switch to “-,” and then releasing it. To check the third or fourth fault code, move the switch to “+,” and then release it when all active fault codes have been viewed. Move the switch to “+” to go back to the first fault code.

![[19400339.png]]

The procedure outlined above will also be used for secondary (right-bank) ECM faults, with the exception that the white fluid light will be lit while any secondary ECM-specific fault code is being flashed out.

> [!note] Note · Примечание
> All of the primary (left-bank) ECM active fault codes are flashed out first before the system flashes out the secondary ECM active fault codes.

![[19400338.png]]

The explanation and correction of all of the fault codes is contained in the troubleshooting charts, Section TF, of this manual.

Electronic fault code troubleshooting trees are in (fault code) numerical order. A section contents is located at the beginning of Section TF.

![[nobox.png]]

To stop the diagnostic system, move the diagnostic switch to the OFF position or remove the shorting plug. Turn the vehicle keyswitch to the OFF position.

> [!note] Note · Примечание
> Some OEMs use a shorting plug.

![[gp8swvv.png]]

**Fault Code Snapshot Data**

When a diagnostic fault code is recorded in the ECM, ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

![[19a00292.png]]

### Engine Protection System

QST30 industrial fuel system engines are equipped with an engine protection system. The system monitors critical engine temperatures, fluid level, switch position, and pressure, and will log diagnostic faults when an above- or below-normal operating range condition occurs. If an out-of-range condition exists, engine derate action will be initiated. The operator will be alerted by the illumination of the in-cab fluid lamp. The warning lamp will start to flash when out-of-range condition continues to get worse and engine shutdown will occur. The operator **must** pull to the side of the road, when it is safe to do so, to reduce the possibility of engine damage.

> [!note] Note · Примечание
> The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

![[nobox.png]]

**Engine Protection System Monitors**

- High coolant temperature
- Low coolant level
- Low coolant pressure
- High intake manifold temperature
- Low/Very low oil pressure
- Engine overspeed.

![[nobox.png]]

If the CENSE™ option is used in conjunction with the QST30 controls system, additional engine protection system monitors are available.

**Additional Engine Protection System Monitors Available with CENSE™**

- High crankcase blowby flow rate
- High oil temperature.

![[nobox.png]]

The engine protection system has three selectable features: Engine protection enable, engine protection shutdown, and engine protection restart. If engine protection enable feature has been selected, engine power and speed will be gradually reduced, depending on the level of severity of the observed condition. If engine protection shutdown feature has been selected, the engine will be shut down. If engine protection restart feature has been selected, the engine can **not** be restarted after shutdown.

![[nobox.png]]

**Engine Protection Features**

- Engine protection enable
- Engine protection shutdown
- Engine protection restart.

![[nobox.png]]

### Flow Diagram

The fuel lift pump (4) draws fuel from the fuel tank (1). The fuel is circulated through a Cummins or customer prefilter (2) and the fuel connection block (3). The fuel then enters the fuel lift pump (4) where it is placed under pressure and circulated through the on-engine fuel filters (5). The fuel flows through the fuel shutoff valve (6) and then enters the injection pump (7), which builds injection pressure and sends fuel through the overflow valve (9), which regulates the injection pressure and sends fuel to each of the injectors (8) at the appropriate time.

![[19400609.png]]

The overflow valve (9) regulates the fuel supply pressure to the injection pump and sends excess fuel back to the fuel tank (1). This fuel will travel through the overflow valve (9) and through a “T” where it will join with the unused fuel from the injectors (8). The fuel will then flow through the fuel connection block (3) and back to the tank (1).

![[19400609.png]]

### INSITE™ Electronic Service Tool Description

INSITE™ is a service tool for the QST30 electronic control system. Use INSITE™ to:

- Program owner-specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Track fuel consumption and duty cycle information.

![[19a00734.png]]

### ESDN Description

The Electronic Software and Database Network (ESDN) is a personal computer (PC)-based system that can transfer new or updated calibration files for the QST30 industrial fuel system ECM from a central location to Cummins Distributors. A calibration file is electronic data that give the engine its performance rating.

![[nobox.png]]

The calibration file will be loaded into ESDN, which is then used to load the file into the ECM.

Reference a Cummins Inc. Service Representative and INSITE™, Part Number 3162261, for QST30 industrial fuel system.

![[19a00735.png]]

### Maintenance Monitor

> [!warning] CAUTION · Осторожно
> The maintenance monitor is designed to alert the operator of the need for a routine maintenance stop. Maintenance records must still be maintained for historical purposes.

The maintenance monitor is an optional feature that will alert the operator when it is time to change oil and perform any other simultaneous maintenance tasks. The maintenance monitor continuously monitors the time the engine has been operating, and the amount of fuel burned to determine when it is time to change oil.

![[oi803ka.png]]

> [!warning] CAUTION · Осторожно
> Do not overextend the oil drain interval as set forth in the applicable operation and maintenance manual (Section V - Oil Drain Intervals) for your application. Cummins Engine Company, Inc. does not recommend exceeding these published intervals and is not responsible for damage sustained due to overextending drain intervals.

The maintenance monitor has two modes of operation:

- Automatic mode
- Time mode.

![[nobox.png]]

**Automatic Mode**

This feature alerts the operator when it is time to change oil based on Cummins recommended interval. It determines the maintenance interval based on engine operating time and fuel burned.

When the automatic mode is selected, the severe oil drain interval duty cycle is the default.

![[nobox.png]]

**Time Mode**

This feature allows the customer to enter a desired time interval. The maintenance monitor will then monitor the time the engine has been operating and alert the operator when the interval has been consumed.

![[nobox.png]]

**Alerting the Operator**

The maintenance monitor feature will alert the operator of the need to change oil by flashing the engine protection lamp (fluid lamp) for approximately 12 seconds after key-on. The flashing sequence will be four quick flashes followed by a pause. This flash sequence will go through four cycles in the 12-second period. This sequence will occur at every key-on until the maintenance monitor has been reset.

> [!note] Note · Примечание
> The diagnostic switch **must** be in the OFF position for the flashing sequence to occur.

![[oi803kb.png]]

**Viewing Maintenance Monitor Data**

With the use of INSITE™, the following maintenance data from the ECM can be viewed or printed:

- Percent of current interval consumed (by either distance, time, or fuel burned)
- Time since last reset
- Fuel burned since last reset
- Current maintenance monitor mode.

![[nobox.png]]

**Reset Log**

The *maximum threshold* is entered by the user either directly using the time mode, or by entering the interval factor in the automatic mode.

The *adjusted threshold* is the new threshold set automatically by the maintenance monitor when automatic mode is selected. The maintenance monitor automatically reduces the maintenance interval when the engine is operating outside the optimum oil temperature range. The longer the engine operates outside optimum oil temperature, the more the adjusted threshold is reduced.

The *interval reset* is the length of the maintenance interval at the time the maintenance monitor was reset.

![[nobox.png]]

**Interval Alert Percentage**

The maintenance setting allows the user to enter the percentage of the present interval at which the light should come on, indicating the need for an oil change. The parameter allows the user to obtain an early warning of the need for a maintenance stop.

For example, if the time mode is set to 200 hours and the interval alert percentage is set to 90 percent, the lamp will illuminate at 180 hours (90 percent of 200).

![[nobox.png]]

**Interval Factor**

This feature is used **only** in the maintenance monitor “auto” mode. It is used to adjust the maintenance interval for “severe-,” “normal-,” or “light-” duty applications. It is also used to extend the interval when using Premium Blue® 2000 oil or any other product that can extend maintenance intervals.

The original factory programmed value is NORMAL.

> [!note] Note · Примечание
> The CENSE™ system has a maintenance monitor feature that monitors the change intervals for the fuel filter, the lubricating oil and oil filters, and the coolant and coolant filters.

![[nobox.png]]

### INSITE™ Electronic Service Tool Monitor Mode

The INSITE™ monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

There is one screen in monitor mode. This screen is user-defined by running monitor setup, and limited to 16 parameters. The ECM inputs show the data that are being fed into the ECM by the system's sensors and switches. The ECM outputs are values that the ECM commands to the QST30 industrial fuel system. Monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.

![[19a00736.png]]

### QUANTUM™ System Description

The QST30 industrial fuel system is an electronic control system designed to optimize engine control and reduce emissions. This system consists of two in-line fuel injection pumps (one for each bank) and two engine control modules (ECM). These modules work in a primary/secondary setup, the left-bank module being the primary and the right-bank module being the secondary. The primary module controls fueling and timing for the left-bank fuel pump, and also commands the secondary module to control the right-bank fuel pump. These controls and commands are based on sensor input.

![[nobox.png]]

### QUANTUM™ System Components

The QST30 industrial fuel system on an engine consists of:

1. Fuel injection pumps (right- and left-bank)
2. Engine control modules (ECM) (right- and left-bank)
3. Fuel shutoff valves (EHAB) (right- and left-bank)
4. Intake manifold pressure sensors (right- and left-bank)
5. Intake manifold temperature sensors (right- and left-bank)
6. Needle movement sensors (right- and left-bank)
7. Oil pressure sensor
8. Coolant temperature sensor
9. Engine speed sensor
10. Engine position sensor
11. Coolant level sensor
12. Ambient air pressure sensor
13. Coolant pressure sensor
14. Fuel injectors
15. Engine wiring harness
16. OEM interface harness
17. J1939 backbone harness.

> [!note] Note · Примечание
> See Section E for component locations.

![[nobox.png]]

The QST30 industrial fuel system uses Bosch® RP39 fuel pumps. These pumps contain actuators that control the timing sleeves and fueling racks. Varying the current supply to these actuators via the ECM allows the QST30 industrial fuel system to regulate engine timing and fuel metering. The ECM supply current is based on various sensor inputs it receives.

The ECM processes the information it receives from the sensors and controls the opening and closing of the actuators. This action controls timing and fuel metering, and then produces the correct horsepower and torque for the latest engine condition.

![[19a00292.png]]

**ECM Sensor Inputs**

1. Accelerator position sensor
2. Intake manifold pressure sensor
3. Intake manifold temperature sensor
4. Oil pressure sensor
5. Coolant temperature sensor
6. Coolant level sensor
7. Coolant pressure sensor
8. Ambient air pressure sensor

![[19a00294.png]]

1. Needle movement sensor
2. Engine speed sensor
3. Engine position sensor
4. Crankcase blowby flow sensor (optional)
5. Oil temperature sensor (optional).

![[19a00733.png]]

**Secondary ECM Inputs**

1. Accelerator position sensor
2. Intake manifold pressure sensor
3. Intake manifold temperature sensor
4. Needle movement sensor
5. Engine speed sensor
6. Engine position sensor.

![[19a00296.png]]

The engine speed sensor (1) provides engine speed information to the ECM for engine governing. The engine position sensor (2) works in conjunction with the needle movement sensor to provide inputs to the ECM necessary for timing control. Both the engine speed sensor and the engine position sensor are located in the flywheel housing.

![[19a00297.png]]

The intake manifold pressure sensor and the intake manifold temperature sensor are located on the intake manifolds. The intake manifold pressure sensor monitors positive manifold pressures used in the air-fuel control function. The intake manifold temperature sensor measures the turbocharged air temperature. It is also used for the engine protection system. Both banks have their own set of sensors.

![[19400352.png]]

The coolant temperature sensor provides data for optimized timing for emissions reduction and is used for the engine protection system.

The coolant temperature sensor is located in the thermostat housing.

![[00a00036.png]]

The coolant level sensor, if equipped, is mounted in the radiator top tank. It is a fluid-level-actuated switch required for the engine protection system.

> [!note] Note · Примечание
> This is an optional sensor that will **not** be on all equipment. A shorting plug will be installed if the coolant level sensor is **not** used.

![[19400354.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

![[00a00037.png]]

The coolant pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the thermostat housing.

![[19a00311.png]]

The ambient air pressure sensor sends signals to the ECM to control fueling properly for different ambient air pressures. This sensor is located on the engine block.

![[19a00312.png]]

The oil temperature sensor is provided with the CENSE™ option. It relays signals to the CENSE™ module, as well as the QST30 master module, for engine protection purposes. The oil temperature sensor is located in the oil pan on the left side of the engine.

![[19a00304.png]]

The crankcase blowby flow rate sensor is used in conjunction with the CENSE™ option. It relays signals to the CENSE™ module to monitor the crankcase blowby flow rate. The crankcase blowby flow rate sensor sends signals to the ECM for the engine protection system. The sensor is located in the gear case on the left side of the engine.

![[19a00285.png]]

**ECM Outputs**

The engine control module (ECM) processes all of the input data and then controls these output parts:

- Rack position actuator (integral to the RP39 fuel pump)
- Sleeve position actuator (integral to the RP39 fuel pump)
- Fuel shutoff valve (EHAB).

![[05a00046.png]]

### Lubrication for the Power Components

The QST30 industrial fuel system has been designed to be flexible to meet a wide variety of engine control specifications for off-highway equipment. The engine control modules (ECM) can be programmed to meet the specified need of your application.

![[cent28.png]]

Governor

The fuel system offers a choice of engine governors. The automotive governor provides a calibrated fueling for a given throttle position (engine speed varies with load). The variable-speed governor maintains a constant engine speed for a given throttle position under varying load conditions. Governor type can be selected by using INSITE™, Part Number 3162261.

![[nobox.png]]

Low-Idle Adjustment/ISC Adjustment

This feature allows the idle \[or intermediate-speed control 1 (ISC 1) speed\] to be increased or decreased in 25-rpm increments through an operator-controlled switch. This switch can be disabled by turning this feature off using INSITE™, Part Number 3162261. If this feature is turned off, the low-idle speed can still be adjusted using INSITE™, Part Number 3162261.

![[19400320.png]]

Intermediate-Speed Control

The ISC feature controls the engine at a constant rpm. Up to three different ISC set speeds (1, 2, 3) can be selected depending on original equipment manufacturer (OEM) availability (4 = engine speed, 5 = torque).

![[19800940.png]]

The ISC feature, depending on OEM availability, provides the ability to select an ISC set speed by way of an OEM-provided switch (1 = OFF, 2 = ON).

![[19800899.png]]

This feature will override the throttle and control the engine speed according to the ISC setting.

![[19800939.png]]

The ISC feature provides a single droop (6) for all intermediate speeds (1, 2, 3). This droop is independent of all other selectable droops and is enforced during ISC operation **only** (4 = engine speed, 5 = torque).

![[19800940.png]]

All ISC speed settings (1) can **not** be adjusted above the maximum ISC speed (2) or below the low-idle speed (3) (4 = engine speed, 5 = torque).

![[19800941.png]]

The intermediate-speed feature is activated whenever the normally open ISC switch (1 or 2) is closed and less than 1 VDC is detected by the ECM (7) on the ISC signal lines (4 or 5) on pins 46 and 45.

![[19802841.png]]

If ISC switch validation (6) is used, both the ISC (4 or 5) and switch validation (6) signals **must** be less than 1 VDC before this feature can be activated.

![[19400521.png]]

The ISC set speed can be adjusted by the idle/ISC increment/decrement switch (1 = increment, 2 = decrement). Set speed changes using this switch can be saved to the ECM at key-off.

![[19800901.png]]

The ISC feature can be enabled or disabled by an electronic service tool. The ISC set speeds, maximum ISC speed, and ISC droop also can be adjusted by an electronic service tool.

![[19800902.png]]

Alternate Droop

The alternate droop feature allows the droop characteristics to be changed for the high-speed governor and for the variable-speed governor. Droop is usually expressed as a percentage. The graph illustrates the isochronous (0-percent droop) and droop (more than 0-percent droop) governor characteristics. Less governor droop provides a more responsive governor for a more precise engine control. More governor droop provides smoother shifting and smoother mechanical clutch engagement.

![[19400325.png]]

The alternate droop feature, depending on OEM availability, provides the ability to select up to two additional alternate droop settings by way of an OEM-provided switch.

![[19400326.png]]

Each alternate droop setting provides the ability to select the breakpoint speed and droop percent for the high-speed governor and droop percent for variable-speed governor. The breakpoint speed determines where on the engine torque curve the high-speed governor will start to limit engine torque output. As with all other features, the selection of the alternate droop feature is accomplished by using INSITE™, Part Number 3162261.

![[19400327.png]]

Alternate Low-Idle Control

This feature allows the operator to switch between the low-idle speed setting (3) and the alternate low-idle speed setting (4) (1 = engine speed, 2 = torque).

![[19800898.png]]

The alternate low-idle speed control feature, depending on the OEM availability, provides the ability to select an alternate idle speed by way of an OEM-provided switch (1 = OFF, 2 = ON).

![[19800899.png]]

The alternate low-idle feature is activated whenever the normally open alternate low-idle switch (1) is closed and 0 VDC is detected by the ECM (2) on the alternate low-idle signal line (3) on pin 44.

![[19a00288.png]]

The alternate low idle can **not** be adjusted by the idle/ISC increment/decrement switch (1 = increment, 2 = decrement).

![[19800901.png]]

The alternate low-idle speed can **only** be adjusted with an electronic service tool.

![[19800902.png]]

This feature can **only** be enabled or disabled by calibration. An electronic service tool (1) will be required to download a calibration (2) to the engine control module (3) if this feature needs to be enabled or disabled.

![[19a00309.png]]

Alternate Torque Control

The alternate torque control feature allows the operator to switch between the 100-percent throttle torque curve 1 and up to two derated torque curves 2 and 3 (4 = engine speed, 5 = torque).

![[19800894.png]]

This feature improves operating efficiency in loaded (1) versus unloaded (2) conditions.

![[19800895.png]]

The alternate torque control feature, depending on OEM availability, provides the ability to select up to two additional derated torque curves by way of an OEM-provided switch.

> [!missing]- Иллюстрация `19800896.png` не извлечена — смотрите PDF-оригинал документа

This feature can **only** be enabled or disabled by calibration. An electronic service tool (1) will be required to download a calibration to the engine control module (3) if this feature needs to be enabled or disabled.

![[19a00309.png]]

Fuel Consumption Rate Logger

The fuel consumption rate feature allows an electronic service tool to access fuel consumption data (1 = time, 2 = gallons/hour).

> [!missing]- Иллюстрация `19800943.png` не извлечена — смотрите PDF-оригинал документа

This feature provides two 40-hour fuel consumption periods (1 and 2). Each period records fuel consumption data in forty 1-hour segments. These 40 data segments can be graphed to show fuel consumption over both 40-hour periods (A = hours, B = gallons/hour).

> [!note] Note · Примечание
> These time periods can be reset using INSITE™, Part Number 3162261.

> [!missing]- Иллюстрация `19800944.png` не извлечена — смотрите PDF-оригинал документа

An instantaneous fuel consumption rate and a lifetime or running average fuel consumption rate are available on the monitor screen of an electronic service tool.

![[19800902.png]]

Dedicated PWM Output

This feature enables the engine to produce a pulse-width-modulated output signal, which is proportional to either engine speed, engine torque, or throttle position.

![[nobox.png]]

The output signal is intended to be used to control an engine or transmission that relies on an analog signal input.

> [!missing]- Иллюстрация `19800945.png` не извлечена — смотрите PDF-оригинал документа

The output driver signal type and signal duty cycle can be monitored with an electronic service tool. The signal availability and type is **not** adjustable by an electronic service tool. This feature can **only** be enabled or disabled by a calibration, **not** an electronic service tool.

![[19800902.png]]

Duty Cycle Monitor

The duty cycle monitor tracks the time the engine spends in 50 different operating regions. These operating regions are based on engine speed and engine torque.

> [!missing]- Иллюстрация `19801115.png` не извлечена — смотрите PDF-оригинал документа

This feature provides two short-term 500-hour resettable data blocks and one long-term 100,000-hour nonresettable data block.

> [!missing]- Иллюстрация `19801116.png` не извлечена — смотрите PDF-оригинал документа

Remote Throttle

The remote throttle feature allows the operator to control the engine from a position other than the driver's seat. This feature is selected by the operator through an OEM-mounted switch.

![[19800899.png]]

This will override the primary throttle control and control the engine speed to the remote throttle setting.

![[19800939.png]]

Switched Speeds

The switched speed input feature allows for the adjustment of up to five set speeds by an electronic service tool. These set speeds are independent of all other set speeds.

The switched speed input feature can be enabled or disabled by an electronic service tool.

![[19800902.png]]
