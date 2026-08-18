---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "94-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 41
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `94-101-007`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-101-007.pdf)

### QSK System Description

The QST Fuel System is an electronic engine control system designed to optimize engine control and reduce exhaust emissions. This system consists of two in-line fuel injection pumps (one for each engine bank) controlled by an Electronic Control Module (ECM). The QST Fuel System controls engine fueling by placing the fuel pump racks in the correct position for the desired fueling.

![[19a00086.png]]

### Programmable Features

The QST Fuel System has been designed to be flexible to meet the wide variety of engine control needs for off-highway equipment. The electronic control module (ECM) can be programmed to meet the specified requirements of your application.

Enter the diagnostic mode by removing the diagnostic connector shorting cap from the engine harness.

![[19a00066.png]]

**Idle Speed**

The Idle Speed feature allows the engine idle speed to be adjusted between 700 rpm and 900 rpm. This adjustment can be made using INSITE™, Part No. 3825145.

![[19a00075.png]]

**Governor Gain Adjust**

This feature allows the governor gain to be adjusted for optimum engine performance. The gain is adjusted at rated speed. The idle speed gain is then automatically calculated from the rated speed gain. The Governor Gain is adjusted by using INSITE™, Part No. 3825145.

![[19a00042.png]]

**Speed Bias Input Type**

This feature allows the ECM to be configured to either Woodward or Barber-Colman speed bias inputs. The input type can be changed by using INSITE™, Part No. 3825145.

![[19a00042.png]]

**Ramp Time**

This feature allows the acceleration ramp time factor to be adjusted from 0 to 30. The acceleration ramp time is the amount of time it takes for the engine speed to accelerate from idle to rated speed or from crank to rated speed. For actual ramp time refer to the table of ramp times in the INSITE™ QST30 G-Drive User's Manual. Each value can be adjusted with INSITE™, Part No. 3825145.

![[19a00076.png]]

**Speed Adjust Knob**

The Speed Adjust Knob allows the adjustment of rated engine speed by ±6 percent using a potentiometer with a range of 500 to 5000 ohms. This ECM input can be enabled with INSITE™, Part No. 3825145.

![[00a00029.png]]

**Alternate Frequency Switch**

The Alternate Frequency switch settings can be configured using INSITE™, Part No. 3825145. The switch can be configured to one of the following options:

1. Normal = 50 Hz; Alternate = 60 Hz
2. Normal = 60 Hz; Alternate = 50 Hz
3. Always 50 Hz
4. Always 60 Hz

To change frequencies, the engine **must** first be shutdown or brought to idle then back to rated speed.

![[00a00030.png]]

**Governor Droop**

The Governor Droop feature allows the engine speed governor droop to be adjusted from 0 to 10 percent. This adjustment can be made using INSITE™, Part No. 3825145.

Speed Droop (%) = \[(no load speed - full load speed)/full load speed\] x 100

![[19a00085.png]]

**Torque Curve Adjustment**

The Torque Curve Adjustment feature allows the torque curve to be adjusted slightly in order to fine tune the engine output power with the alternator input requirements. This adjustment is made using INSITE™, Part No. 3825145.

![[00a00031.png]]

**Warning Threshold Adjustment**

Warning thresholds are engine parameter values at which the ECM will record and report a warning fault condition. The following warning thresholds are adjustable using INSITE™, Part No. 3825145:

1. High Coolant Temperature Warning
2. Low Oil Pressure Warning at idle
3. Low Oil Pressure Warning at rated rpm

![[19a00077.png]]

**Overspeed Shutdown Adjustment**

The Overspeed Shutdown Threshold is the engine speed value at which the ECM will shutoff fueling to the engine. This value can be adjusted down from the factory default value. This adjustment can be made using INSITE™, Part No. 3825145.

![[19a00079.png]]

**Meter Calibration**

The Meter Calibration feature allows the GOEM installed meters for engine speed, coolant temperature, and oil pressure to be calibrated to the ECM meter drivers (0 to 1 mA). These calibrations can be performed using INSITE™, Part No. 3825145.

![[19a00078.png]]

**ECM Time and Engine Run Time**

ECM Time is the amount of time in Hours:Minutes that the ECM has been powered up (run mode or diagnostic mode).

Engine Run Time is the amount of time in Hours:Minutes that the engine has been running (rpm \> 0).

Both of these values can be displayed using INSITE™, Part No. 3825145.

![[19a00081.png]]

**Barber-Colman Scale Factor**

The Barber-Colman Scale Factor allows the ECM to be adjusted for optimum paralleling operation with Barber-Colman paralleling equipment. This scale factor can be adjusted using INSITE™, Part No. 3825145.

> [!note] Note · Примечание
> Do **not** adjust this parameter unless absolutely necessary.

![[19a00084.png]]

**Woodward Scale Factor**

The Woodward Scale Factor allows the ECM to be adjusted for optimum paralleling operation with Woodward paralleling equipment. This scale factor can be adjusted using INSITE™, Part No. 3825145.

> [!note] Note · Примечание
> Do **not** adjust this parameter unless absolutely necessary.

![[19a00084.png]]

### Diagnostic Fault Codes

The QST Fuel System can display and record certain detectable fault conditions. These conditions are displayed as fault codes which makes troubleshooting easier. The fault codes are retained in the electronic control module (ECM).

![[19400328.png]]

There are two types of fault codes. There are engine electronic fuel system fault codes and engine protection system fault codes.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (fault code was active at some time, but is **not** presently active).

![[19400329.png]]

Fault codes can **only** be viewed using INSITE™, Part No. 3825145.

To read the fault codes, the ECM must be powered up either in the “Run” or “Diagnostic” mode.

To enter the diagnostic mode, remove the diagnostic connector shorting cap on the engine harness.

To clear fault codes the engine **must not** be running and the ECM **must** be in the diagnostic mode.

![[19a00042.png]]

The fault conditions will cause the Common Warning or Common Alarm relay outputs (2A @ 30 VDC) to be energized by the ECM. GOEM selected devices, using these circuits, will make the operator aware that a fault condition exists.

A Common Warning relay output will still allow the engine to be operated. However, if a common warning is caused by a bad sensor engine protection will be lost for that parameter. The condition **must** be repaired as soon as convenient.

A Common Alarm relay output will shutdown the engine and will **not** allow it to be operated until the Stop/Run switch is cycled.

![[00a00021.png]]

The conditions will cause the Relay Driver (200 mA @ 24 VDC) to be energized by the ECM. GOEM selected devices, using these circuits, will make the operator aware what fault condition exists.

![[19a00087.png]]

The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.

![[00a00022.png]]

The explanation and correction of all fault codes is in the troubleshooting and repair charts, Section TF of this manual. They are listed in numerical order with an index located at the beginning of the section.

![[19400340.png]]

To exit the diagnostic mode, install the shorting plug in the diagnostic connector.

![[19a00080.png]]

**Fault Code Snapshot Data**

When a diagnostic fault code is recorded in the ECM, ECM input and output data is recorded from all sensors and switches. Snapshot data allows the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

![[00a00024.png]]

### Engine Protection System

QST engines are equipped with an engine protection system. The system monitors critical engine speeds, temperature and pressure, and will log diagnostic faults when an over- or under-normal operating range condition occurs. If an out-of-range condition exists, the Common Warning circuit is energized. The operator will be alerted by an OEM selected device. The Common Alarm circuit will be energized when an out-of-range condition continues to get worse and engine shutdown occurs.

![[00a00025.png]]

### Flow Diagram

The fuel lift pump (4) draws fuel from the customer's fuel or day tank (1). The fuel is circulated through a Cummins or customer prefilter (2) and the fuel connection block (3). The fuel then enters the fuel lift pump (4) where it is placed under pressure and circulated through the on engine fuel filters (5). The fuel flows through the fuel shutoff valve (6) and then enters the injection pump (7), which builds injection pressure and sends fuel to each of the injectors (9) at the appropriate time.

![[19400492.png]]

The overflow valve (8) regulates the fuel supply pressure to the injection pump and sends excess fuel back to the fuel tank (1). This fuel will travel through the overflow valve (8) and through a “T” where it will join with the unused fuel from the injector's (9). The fuel will then flow through the fuel connection block (3) and back to the tank (1).

![[19400492.png]]

### QSK23, QSK45, QSK60, and QSK78 System Components

The QST system on a G-Drive engine consists of:

1. Fuel Pumps (2)
2. Fuel Shut Off Valves (FSOV) (2)
3. Oil Pressure Sensor (OPS)
4. Coolant Temperature Sensor (CTS)
5. Engine Speed Sensor (ESS)
6. Engine Harness
7. Engine Harness Adaptor Cable
8. OEM Harness
9. Electronic Control Module (ECM)

![[19a00074.png]]

![[00a00027.png]]

**ECM Inputs**

- Oil Pressure Sensor (OPS)
- Coolant Temperature Sensor (CTS)
- Engine Speed Sensor (ESS)

![[00a00028.png]]

The ESS provides engine speed information. The sensor is located in the flywheel housing.

![[19a00067.png]]

The engine CTS sends signals to the ECM for the engine protection system. The CTS is located in the upper casing of the thermostat housing.

![[00a00036.png]]

The OPS sends signals to the ECM for the engine protection system. The sensor is on the left bank side of the engine block behind the fuel pump.

![[00a00037.png]]

**ECM Outputs**

The ECM processes all of the input data and then controls these output parts:

- Fuel Shutoff Valves
- Common Warning circuit
- Common Alarm circuit
- Fuel Pump Rack Actuator
- Relay Drivers
- Meter Drivers

![[00a00034.png]]

### INSITE™ Description

INSITE™, Part No. 3825145, is the electronic service tool for the QST30 G-Drive system. Use INSITE™ to:

- program owner specified information into the ECM (parameters and features)
- aid in troubleshooting the engine
- configure the ECM to match the application in which it is installed.

Refer to INSITE™ G-Drive User's Manual (QST30), Bulletin No. 3666196.

![[19a00042.png]]

**INSITE™ Monitor Mode**

The INSITE™ monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

> [!missing]- Иллюстрация `19400360.png` не извлечена — смотрите PDF-оригинал документа

There is one screen in monitor mode. This screen is user defined by running monitor setup, and limited to 16 parameters. The ECM inputs show the data that is being fed into the ECM by the system's sensors and switches. The ECM outputs are values that the ECM commands to the QST system. Monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.

![[nobox.png]]

The figures in this section show all of the possible parameters that can be displayed in monitor mode as they can be seen with INSITE™.

Monitor mode can be used to look for abnormally fluctuating readings while troubleshooting. Sensors that are failed in range can also be found by looking for fixed readings (for example, coolant temperature reading does **not** change with actual coolant temperature).

![[nobox.png]]

> [!missing]- Иллюстрация `00a00032.png` не извлечена — смотрите PDF-оригинал документа

> [!missing]- Иллюстрация `00a00033.png` не извлечена — смотрите PDF-оригинал документа
