---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "01-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2008-03-26"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 154
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `01-101-007`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section F - Familiarization
> **Даты:** изменён 2008-03-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-101-007.pdf)

### General Information

Power Generation

The generator-drive control system is an electronic control system designed to optimize engine control and reduce exhaust emissions.

The QSK23, QSK45, QSK60, and QSK78 fuel system design controls engine speed and fuel pressure utilizing electronic sensors within the Quantum™ system.

The QST30 system is based on the Bosch™ fuel system design. This system consists of two in-line fuel injection pumps (one for each bank). The Bosch™ fuel system controls engine fueling by placing the fuel pump racks in the correct position for the desired fueling.

The QSX15 fuel system design controls engine speed and fuel utilizing electronic sensors within the system.

Generator-Drive Control System

- Optimized engine control
- Reduced exhaust emissions.

The power generation electronic control system has its own electronic tool, INPOWER™. INSITE™ will **not** work with these ECMs. INPOWER™ can be purchased through Cummins Inc.

Refer to the INPOWER™ manual for specifics about the tools:

- INPOWER™
- INPOWER™ PRO.

![[19800902.png]]

### Programmable Features

The generator-drive control system has been designed to be flexible to meet the wide variety of engine control specifications for power generation.

![[17600025.png]]

A customer-supplied Run/Stop switch supplies a ground to the ECM. Ground supplied to the ECM allows the ECM to energize the fuel shutoff valve when cranking.

This switch can be monitored via the electronic service tool.

![[19600070.png]]

A customer-supplied Idle/Rated switch allows the selection of idle or rated speed mode. Ground supplied to the ECM allows the ECM to go from rated speed to idle speed.

This switch can be monitored via the electronic service tool.

![[19600071.png]]

A customer-supplied switch resets all shutdown/warning functions. Warning relay drivers and relay contacts can be reset while the engine is running or shut down. Shutdown relay drivers and contacts, and inactive fault codes, can be reset **only** when the engine is shut down. Before restarting the engine after a fault-induced shutdown, check the ECM for fault codes via the electronic service tool.

Idle speed is adjustable via the electronic service tool.

Refer to the manual for the electronic service tool for details on the feature.

![[19600088.png]]

A customer-supplied Alternate Frequency switch allows the selection of 50- or 60-Hz rated speed operation without requiring an electronic service tool recalibration.

This switch can be monitored via the electronic service tool.

To change frequencies, the engine **must** be shut down. For engines rated for a single operating frequency, the alternate frequency input is non-operational.

![[00a00030.png]]

Selection of a 'normal' frequency setting and an alternate frequency setting is adjustable via the electronic service tool.

Refer to the manual for the electronic service tool for details on the feature.

![[00a00030.png]]

For isochronous speed operation, the governor droop setting should be set at 0 percent.

If required, the governor droop setting can be adjusted using the electronic service tool or the droop potentiometer input.

Refer to the electronic service tool manual for details on the feature.

For droop speed operation, the governor droop setting is adjustable between 0 and 10 percent.

If required, the governor droop setting can be adjusted using the electronic service tool or the droop potentiometer input.

Refer to the electronic service tool manual for details on the feature.

![[19600073.png]]

Engine-generator sets that are to operate at 60-Hz full-load **must** have the engine no-load governed speed adjusted to 61.8 Hz \[1854 rpm\] for 3-percent speed droop or 63.0 Hz \[1890 rpm\] for 5-percent speed droop.

![[19a00085.png]]

Engine-generator sets that are to operate at 50-Hz full-load **must** have the engine no-load governed speed adjusted to 51.5 Hz \[1545 rpm\] for 3-percent speed droop or 52.5 Hz \[1575 rpm\] for 5-percent speed droop.

Percent speed droop on the engine-generator set can be verified by noting no-load and full-load speeds and using the speed droop formula.

| %S Droop = | (S NL - S FL) x 100 |
|---|---|
| S FL |  |

Where:

%S Droop = Percent Speed Droop

S FL = Full-Load Speed

S NL = No-Load Speed

| Example: | 1854 rpm - 1800 rpm | x 100 = 3% |
|---|---|---|
| 1800 rpm |  |  |

Droop governed speed under the available load can be calculated when full-load kW is **not** available using this formula.

| S al = S nl - (( | Available kW Load | ) x (S nl - S fl)) |
|---|---|---|
| Rated kW |  |  |

Where:

S al = Speed at Available kW Load

S fl = Speed at Full kW Load

S nl = Speed at No Load

Example:

Available kW Load = 400

Rated kW = 500 (Generator rating)

Speed at Full kW Load = 1800

Speed at No Load = 1854

| 1854 rpm - (( | 400 kW | ) x (1854 - 1800)) |
|---|---|---|
| 500 kW |  |  |
| 1854 rpm - (0.8 x 54) = 43.2 rpm |  |  |
| 1854 rpm - 43.2 rpm = 1810.8 or 1811 rpm |  |  |

![[19600074.png]]

The droop adjust potentiometer, located in the control, allows the adjustment of the engine speed governor droop without the aid of the electronic service tool.

Refer to isochronous and droop speed governing for more information on droop.

![[19600075.png]]

The frequency adjust potentiometer, located in the control panel, allows the adjustment of the engine speed without the aid of the electronic service tool.

> [!note] Note · Примечание
> This is **only** a fine adjustment with minimal range.

![[19600075.png]]

> [!warning] CAUTION · Осторожно
> It takes a few seconds to initiate each gain adjustment (via the governing/voltage regulator submenu or an electronic service tool). It is recommended that any increases in the governor gain setting be made in increments not exceeding 3 percent. This will prevent prolonged periods of unwanted instability.

Gain adjust can be adjusted in the electronic service tool or the generator-drive control panel. If the adjustment is set too high, output voltage will be unstable. If the gain is set too low, the output voltage will respond sluggishly to changes in load and overshoot can result.

Governor gain can be adjusted for optimum engine performance. The governor gain is adjustable between 1 and 100 percent using the electronic service tool.

Typical engine-generator combinations will **not** require adjustments to the governor gain settings as both 1500- and 1800-rpm generator sets ordinarily exhibit satisfactory steady-state stability and acceptable transient performance with the gain value as set from the factory.

![[19600075.png]]

The ECM provides for three speed acceleration ramp functions that are adjustable using the electronic service tool.

- Starting to rated - ramp time
- Idle to rated - ramp time
- Rated to idle - ramp time.

Starting-to-rated ramp time provides for speed ramping between cranking and rated speeds.

Idle-to-rated ramp time provides for speed ramping between idle and rated speeds.

Rated-to-idle ramp time provides for speed ramping between rated and idle speeds.

Refer to the electronic service tool manual for details on the features.

Ramp times (in seconds) are dependent on idle and rated speed settings. Desired ramp times are selected by choosing ramp numbers, **not** ramp times directly.

The Barber-Colman and Woodward™ Bias input feature provides the ability to integrate the ECM with either a Barber-Colman or Woodward™ Load Sharing, Auto Synchronizing, Load Commander, and so forth.

The hardware can be either analog or digital.

The feature is selectable via the electronic service tool. Refer to the electronic service tool manual for details on this feature.

This internal engine hour meter is monitorable via the electronic service tool. It allows the operator to view how many hours the engine-generator has been in service.

Fault codes snapshots will be stamped with a corresponding time stamp.

![[19a00076.png]]

The meter calibration feature allows the GOEM-installed meters for engine speed, coolant temperature, and oil pressure to be calibrated to the ECM meter drivers (0 to 1 mA).

These calibrations can be performed using the electronic service tool.

Shutdown thresholds are engine parameter values at which the ECM will record and report a shutdown fault condition. These values can be adjusted down (or up in the case of the oil and coolant level) from the factory default value.

This adjustment can be made using the electronic service tool.

Warning thresholds are engine parameter values at which the ECM will record and report a warning fault condition. These values can be adjusted down (or up in the case of the oil and coolant level) from the factory default value.

This adjustment can be made using the electronic service tool.

![[19a00078.png]]

The overspeed shutdown threshold is the engine speed value at which the ECM will shut off fueling to the engine. This value can be adjusted down from the factory default value.

This adjustment can be made using the electronic service tool.

![[19802584.png]]

### Engine Protection System

Generator-drive control system engines are equipped with an engine protection system. The system monitors critical engine speeds, temperature, and pressure, and will log diagnostic faults when an over- and under-normal operating range condition occurs. If an out-of-range condition exists, the common warning circuit is energized. The common alarm circuit will be energized when an out-of-range condition continues to get worse and engine shutdown occurs.

The engine protection shutdown-overide feature allows the customer to override engine protection shutdowns. All calibrations default to this feature disable, it **must** be enabled using the electronic service tool. If an engine protection shutdown fault code occurs while this feature is enabled, Fault Code 1416 will be logged along with the original engine protection fault.

![[19600090.png]]

### Diagnostic Fault Codes

The generator-drive control system can display and record certain detectable fault conditions. These failures are displayed as fault codes, which make troubleshooting easier. The fault codes are retained in the ECM.

There are two types of diagnostic codes:

Information codes are to inform the operator and electronic system (paralleling controllers, smart switch gear) that an event has occurred.

Fault codes are to report to the operator and the electronic system that there is a problem or potential problem with the engine or fuel system.

Fault codes can be accessed in three different ways:

1. Flashout
2. Electronic service tool
3. Operator interface panel.

![[19802544.png]]

The generator-drive control system ECM has five LEDs for diagnostics:

- OS - overspeed
- LOP - low oil pressure
- HET - high engine temperature
- Shutdown - engine protection shutdown has occurred
- Warning - engine protection warning condition exists.

The generator-drive control system has eight relay drivers for customer-supplied relays:

- Overspeed
- Low oil pressure
- High engine temperature
- Engine protection shutdown has occurred
- Engine protection warning condition exists
- Prelow oil pressure
- Prehigh engine temperature
- Fail to start.

![[19600091.png]]

To flash out a fault code, the ECM **must** be put into the diagnostic mode. Enter the diagnostic mode using the diagnostic mode switch or by connecting together the two single-pin diagnostic mode enable connectors. During normal ECM operation, the two connectors are disconnected (open circuit). The ECM is placed in diagnostic mode when these two connectors are joined (short circuit).

The warning lamp will flash (signifying the start of a new fault code), and then the fault code will flash out on the shutdown lamp.

The electronic service tool can be used to read the fault codes. Connect a personal computer, with the electronic service tool installed, to the engine using service harness, Part Number 3163156.

Refer to the electronic service tool manual for specifics about how to use the tool to read the fault codes.

![[19600090.png]]

If the customer-supplied operator interface panel has been integrated with the generator-drive control system using the RS485 datalink, the ability to read the fault codes is available. Refer to the manuals supplied with the unit for more details.

When a diagnostic fault code is recorded in the ECM, the ECM input and output data are recorded from all sensors and switches. Snapshot data allow the relationships between ECM inputs and outputs to be viewed and used during troubleshooting.

**Only** inactive fault codes can be cleared. The **only** way to clear an inactive fault code is to use the electronic service tool.

> [!note] Note · Примечание
> The engine **must** be shut down to clear inactive shutdown faults.

All fault codes recorded will either be active (fault code is presently active on the engine) or inactive (was active at some time, but is **not** presently active).

![[19802725.png]]

### Flow Diagram

QSX15

The fuel pump (3) draws fuel from the fuel tank (1). The fuel circulates through the fuel filter (2) before it enters the gear pump (3). The fuel pump governs the fuel output pressure, based on engine speed. This governed fuel pump pressure flows through the control valve body, through the fuel shutoff valve (4), to the timing actuators (6), and to the fueling actuators (5).

The control valve body is bolted to the head, and the timing and fueling actuators connect to drillings in the cylinder head. The cylinder head has drillings from the fueling actuators to the injectors (8), and from the timing actuators to the injectors (7).

![[19802581.png]]

The regulated fuel flow from the timing and fueling actuators travels through the supply drillings in the head to the injectors.

![[19400347.png]]

QST30

The fuel supply pumps (5) draw fuel from the fuel tank (7). The fuel supply relay (8) turns the fuel supply pumps (5) on. The fuel is circulated through a fuel filter and water separator (4). Measurements are taken at the temperature sensor (6) and pressure sensor (3). The fuel then flows to the right bank fuel housing and then is distributed to the left bank and right bank fuel shut off valves (2). If necessary, the pressure relief bypass valve (9) opens to route fuel to the fuel return line (11). Fuel then flows to the Bosch™ fuel injection pumps (10) and injectors (1).

![[19a00773.png]]

QST30

Upgrade

The fuel lift pump (4) draws fuel from the customer's fuel or day tank (1). The fuel is circulated through a Cummins® or customer prefilter (2) and the fuel connection block (3). The fuel then enters the fuel lift pump (4) where it is placed under pressure and circulated through the on-engine fuel filters (5). The fuel flows through the fuel shutoff valve (6) and then enters the injection pump (7), which builds injection pressure and sends fuel to each of the injectors (9) at the appropriate time.

![[19400492.png]]

The overflow valve (8) regulates the fuel supply pressure to the injection pump and sends excess fuel back to the fuel tank (1). This fuel will travel through the overflow valve (8) and through a “T” where it will join the unused fuel from the injector (9). The fuel will then flow through the fuel connection block (3) and back to the tank (1).

![[19400492.png]]

QSK23, QSK45, QSK60, and QSK78

The fuel pump (1) draws fuel from the equipment fuel tank. The fuel circulates through the fuel filters before it enters the gear pump. The fuel pump governs the fuel output pressure, based on engine speed. This governed fuel pump pressure flows to the control valve body (2).

The control valve body protects the ECM (3) from engine heat and regulates fuel flow to the timing and fueling rail lines (4). The timing and fueling lines connect to fuel blocks on the cylinder head (5). The cylinder has drillings from the fuel manifold to the injectors.

![[19600092.png]]

> [!note] Note · Примечание
> The QSK23 will have **only** one timing rail actuator.

The control valve body regulates the fuel flow with timing rail actuator (2) and a fueling rail actuator (6).

Fuel flows into the control valve body at the supply fitting (1). Fuel then circulates around the timing rail actuators (2), regulated by the timing rail pressure sensor (3), and flows out the timing rail outlet (4).

Fuel also flows to the fuel shutoff valve (5) and then to the fueling rail actuator (6). The regulator then passes fuel to the rail sensor and up to the fueling rail pressure outlet (8).

The barometric sensor (10) is mounted beneath the timing rail pressure sensor (3). Fuel temperature is monitored by a fuel temperature sensor (9) mounted above the fuel rail pressure sensor (7).

![[19600009.png]]

The regulated fuel flow from the control valve body travels from the timing and fueling rail pressure lines; through the fuel block, fuel manifold, and drillings in the cylinder head; and is delivered to the timing and fueling rail orifices.

![[19400347.png]]

### QSX15 System Components

The QSX15 fuel system on an engine consists of:

1. Intake manifold pressure/temperature sensor
2. Fuel drain
3. Fuel inlet
4. Fuel shutoff valve
5. Oil pressure/temperature sensor.

![[19802866.png]]

1. Camshaft position sensor
2. Fueling actuators
3. Timing actuators
4. Crankshaft position sensor
5. Fuel pressure sensor
6. Barometric pressure sensor.

![[19802867.png]]

ECM Inputs

The following is a list of ECM Inputs:

1. Fueling pressure sensor
2. Crankshaft engine position sensor
3. Camshaft engine position sensor
4. Intake manifold air pressure sensor
5. Oil pressure sensor

![[19802585.png]]

1. Intake manifold air temperature
2. Coolant temperature sensor
3. Coolant level sensor
4. Barometric pressure sensor
5. Oil temperature sensor.

![[19802586.png]]

The engine speed sensor provides engine speed and position information.

The camshaft engine speed sensor is located on the intake side, above the fuel system control housing.

The crankshaft engine speed sensor is located on the intake side, front lower corner.

![[17c00050.png]]

The intake manifold pressure sensor and the intake manifold air temperature sensor are located in the intake manifold. The intake manifold pressure sensor monitors positive manifold pressures used in the air-fuel control function. The intake manifold air temperature sensor measures the turbocharged air temperature. The intake manifold air temperature sensor is also used for the engine protection system.

![[17c00051.png]]

The engine coolant temperature sensor provides data for optimized timing for emissions reduction, and is used for the engine protection system.

The coolant temperature sensor is located in the thermostat housing.

![[19c00248.png]]

The coolant level sensor, equipped by the OEM, is mounted in the radiator top tank. It is a fluid-level-actuated switch required for the engine protection system.

![[19400354.png]]

The oil pressure/temperature sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

![[19802587.png]]

ECM Outputs

The ECM processes input data and then controls these output parts:

- Timing and fuel rail actuators
- Fuel shutoff valve.

![[19600096.png]]

### QST30 System Components

The QST30 fuel system on an engine consists of:

- Fuel pump
- Fuel shutoff valve
- Fueling supply pressure sensor
- Intake manifold pressure sensor
- Oil pressure sensor
- Intake manifold air temperature sensor
- Coolant temperature sensor
- Engine speed sensor
- Rack position sensor
- Coolant level sensor
- Engine harness
- Extension harness
- Electronic control module (ECM)
- Barometric pressure sensor
- Fuel temperature sensor
- Coolant pressure sensor
- Oil level sensor
- Generator interface harness
- Fuel supply pump relay
- Oil temperature sensor.

The ECM processes the information it receives from the sensors and controls the movement of the fuel rack to control fueling. This action controls fuel metering, and then produces the correct horsepower and torque for the latest engine condition.

![[19a00788.png]]

ECM Inputs

The following is a list of ECM Inputs:

1. Fueling supply pressure sensor
2. Engine speed sensor
3. Oil level sensor.

![[19a00782.png]]

1. Intake manifold air pressure sensors
2. Oil pressure sensor
3. Intake manifold air temperature sensors
4. Coolant and oil temperature sensor
5. Coolant level sensor
6. Barometric pressure sensor
7. Coolant pressure sensor
8. Fuel temperature sensor
9. Fueling supply pressure sensor.

![[19a00795.png]]

1. Alternate frequency switch
2. Crank switch
3. Emergency stop switch
4. Remote emergency stop switch
5. Alarm reset switch
6. Idle/rated switch
7. Diagnostic mode switch
8. Droop adjust
9. Frequency adjust.

![[19802580.png]]

The intake manifold pressure sensor (1) and the intake manifold air temperature sensor (2) are located in the intake manifold. The intake manifold pressure sensor monitors positive manifold pressures used in the air-fuel control function. The intake manifold air temperature sensor measures the turbocharged air temperature. The intake manifold air temperature sensor is also used for the engine protection system.

Refer to Section E for a more detailed component location.

![[19a00783.png]]

The engine coolant temperature sensor provides data for the engine protection system.

The coolant temperature sensor is located in the thermostat housing.

Refer to Section E for a more detailed component location.

![[19a00784.png]]

The coolant level sensor, if equipped, is mounted in the radiator top tank. It is a fluid-level-actuated switch required for the engine protection system.

> [!note] Note · Примечание
> This is an optional sensor that will **not** be on all engines. A shorting plug will be installed if the coolant level sensor is **not** used.

![[19400354.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

Refer to Section E for a more detailed component location.

![[19a00255.png]]

The engine speed sensor provides engine speed information.

The sensor is located in the flywheel housing.

![[19a00246.png]]

ECM Outputs

The ECM processes all of the input data and then controls these output parts:

- Fuel lift pump assembly
- Fuel shutoff valve
- Fuel pump rack actuator.

There are two fuel pumps/rack actuators for the QST30.

- Meter (engine speed, oil pressure, coolant temperature).
- Fault lamps (warning, shutdown, overspeed, high coolant temperature, low oil pressure, prehigh coolant temperature, prelow oil pressure).

![[19a00787.png]]

### QST30 System Components

The QST30 Upgrade fuel system on an engine consists of:

- Fuel pumps
- Fuel shutoff valves
- Oil pressure sensor
- Coolant temperature sensor
- Engine speed sensor
- Engine harness
- Engine harness adaptor cable
- OEM harness
- Electronic control module (ECM).

A kit will be available from Cummins Inc., to upfit current QST30 generator-drive engines to the new generator-drive control system.

The upfit kit consists of:

- Generator-drive control system ECM
- Adapter harnesses.

![[19a00788.png]]

ECM Inputs

The following is a list of ECM inputs:

1. Oil pressure sensor
2. Coolant temperature sensor
3. Engine speed sensor.

![[19a00789.png]]

1. Alternate frequency switch
2. Crank switch
3. Emergency stop switch
4. Remote emergency stop switch
5. Alarm reset switch
6. Idle/rated switch
7. Diagnostic mode switch
8. Droop adjust
9. Frequency adjust
10. Gain adjust.

![[19802580.png]]

The engine speed sensor provides engine speed information. The sensor is located in the flywheel housing.

![[19a00246.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

![[19a00255.png]]

The engine coolant temperature sensor sends signals to the ECM for the engine protection system. The coolant temperature sensor is located in the upper casing of the thermostat housing.

![[00a00036.png]]

ECM Outputs

The ECM processes all of the input data and then controls these output parts:

- Fuel shutoff valves
- Common warning circuit
- Common alarm circuit
- Fuel pump rack actuator
- Relay drivers
- Meter drivers.

![[19a00787.png]]

### QSK23, QSK45, QSK60, and QSK78 System Components

The QSK23, QSK45, QSK60, and QSK78 fuel system on an engine consists of:

- Fuel pump
- Timing rail actuator
- Timing rail pressure sensor
- Fuel shutoff valve
- Fueling rail actuator
- Fueling rail pressure sensor
- Intake manifold pressure sensor
- Oil pressure sensor
- Intake manifold air temperature sensor
- Coolant temperature sensor
- Engine speed sensor
- Coolant level sensor
- Engine harness
- Extension harness
- Electronic control module (ECM)
- Fuel cooler
- Barometric pressure sensor
- Fuel temperature sensor
- Coolant pressure sensor
- Oil temperature
- Aftercooler water inlet temperature sensor
- Blowby pressure sensor
- Generator interface harness.

The control valve body contains actuators, fuel temperature sensor, and pressure sensors that control timing and fuel metering at the injector.

The ECM processes the information it receives from the sensors and controls the opening and closing of the actuators. This action controls timing and fuel metering, and then produces the correct horsepower and torque for the latest engine condition.

![[19802577.png]]

ECM Inputs

The following is a list of ECM inputs:

1. Timing rail pressure sensor
2. Fueling rail pressure sensor
3. Engine speed sensor
4. Oil temperature
5. Aftercooler water inlet temperature sensor
6. Blowby pressure sensor

![[19802578.png]]

1. Intake manifold air pressure sensor
2. Oil pressure sensor
3. Intake manifold air temperature
4. Coolant temperature sensor
5. Coolant level sensor
6. Barometric pressure sensor
7. Coolant pressure sensor
8. Fuel temperature sensor
9. Pump pressure sensor.

![[19a00795.png]]

The engine speed sensor provides engine speed and position information. The sensor is located on the backside of the cylinder block gear housing flange, below the accessory drive.

![[19a00246.png]]

The intake manifold pressure sensor and the intake manifold air temperature sensor are located in the intake manifold. The intake manifold pressure sensor monitors positive manifold pressures used in the air-fuel control function. The intake manifold air temperature sensor measures the turbocharged air temperature. The intake manifold air temperature sensor is also used for the engine protection system.

![[19400352.png]]

The engine coolant temperature sensor provides data for optimized timing for emissions reduction, and is used for the engine protection system.

The coolant temperature sensor is located in the thermostat housing.

![[19c00248.png]]

The coolant level sensor, if equipped, is mounted in the radiator top tank. It is a fluid-level-actuated switch required for the engine protection system.

![[19400354.png]]

The oil pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

![[19400355.png]]

The coolant pressure sensor sends signals to the ECM for the engine protection system. The sensor is located on the engine block.

![[19600093.png]]

ECM Outputs

The ECM processes input data and then controls these output parts:

- Timing and fuel rail actuators
- Fuel shutoff valve
- Fuel pump actuator.

> [!note] Note · Примечание
> There are two timing actuators for the QSK45, QSK60, and QSK78 engines.

- Meter (engine speed, oil pressure, coolant temperature).
- Fault relays/lamps (warning, shutdown, overspeed, high engine temperature, low oil pressure, prehigh engine temperature, prelow oil pressure).

![[19600096.png]]

### INPOWER Description

INPOWER™ is a service tool for the generator-drive control systems. Use INPOWER™ to:

- Program owner-specified information into the ECM (parameters and features)
- Aid in troubleshooting the engine
- Change the engine power or rated speed calibration.

Refer to INPOWER™ manual for specifics.

### INPOWER™ Adjust Mode

The adjustment feature allows you to make adjustments to genset parameters for trims and settings. There are several adjustment parameters and **not** all gensets will have the same adjustments available.

### INPOWER™ Monitor Mode

The INPOWER™ monitor mode is a useful troubleshooting aid that displays the key ECM inputs and outputs. This feature can be used to spot constant or abnormally fluctuating values.

The ECM inputs show the data that is being fed into the ECM by the system's sensors and switches. The ECM outputs are values that the ECM commands to the generator-drive control system. Monitor mode allows the relationship between the ECM inputs and outputs to be monitored and used during troubleshooting.

### INPOWER™ PRO Description

INPOWER™ PRO allows user to transfer new or updated calibration files for the generator-drive control system ECM from a central location to Cummins® distributors. A calibration file is electronic data that give the engine its performance rating.

The calibration file will be loaded into INPOWER™, which is then used to load the file into the ECM.

Refer to your Cummins® service representative and the INPOWER™ manual for more information.

### INPOWER™ Test Mode

The test feature is a diagnostic tool that is used to perform internal self-checks on the PowerCommand® Control to verify inputs and outputs of the control system and test engine protection functions.

### Control Panel

The control panel allows the user or service technician to interface with the generator set controls. The control panel consists of two panels, the operator interface panel and the switch panel.

![[19802694.png]]

Operator Interface Panel

The operator interface panel can be mounted on the generator set control panel as shown or remotely. The operator interface panel contains the following components:

1. Digital metering panel
2. Display menu selection buttons
3. Graphical display.

![[19802695.png]]

The digital VAC metering panel simultaneously displays three-phase line-to-line AC volts and current, kW, power factor, and frequency. The panel is composed of a series of color-coded LEDs, with green indicating normal range values, amber for warning, and red for shutdown conditions.

![[19802696.png]]

The graphical display is capable of displaying up to 9 lines of data with approximately 27 characters per line. This display is used to view the menus of the menu-driven operating system.

1. Operation line
2. Action line
3. Status line
4. Menu display area.

![[19802697.png]]

The display menu has six momentary buttons - three on each side of the graphical display window - are used to navigate through the system control menus and to adjust generator set parameters.

![[19802698.png]]

Switch Panel

The switch panel contains the following components:

- Fault Acknowledge button
- Panel Lamp/Lamp Test button
- Exercise button
- Manual Run/Stop
- Off (0)/Manual/Auto switch
- Emergency Stop button
- Remote Start indicator
- **Not** in Auto indicator
- Shutdown Status indicator
- Warning Status indicator

![[19802699.png]]

Press the Fault Acknowledge button to acknowledge warning and shutdown indications. Pressing fault acknowledge button will **not** clear the latched fault from memory. The system software **must** detect that the fault condition is corrected before the latched fault can be reset by the electronic service tool. This button is also used for fault flashout.

![[19802700.png]]

Press and hold down the Panel Lamp Test button to turn all control panel LEDs on to make sure all lamps illuminate. The bar graph LEDs will light sequentially when this button is held down. The illumination will shut off after releasing the panel lamp/lamp test button.

![[19802701.png]]

Press the Exercise button to initiate a preprogrammed exercise sequence. The Off (0)/Manual/Auto switch is used in conjunction with this button to enable this function.

![[19802702.png]]

This Manual Run/Stop button starts and stops the set locally and will bypass time delay to start and stop sequences. The Off (0)/Manual/Auto switch **must** be in the manual position to enable this button.

![[19802703.png]]

Manual position enables the use of the switch panel manual run/stop button. Auto position enables start/stop control of the engine from a remote location, and disables the use of the local run/stop button. Off (0) position prevents the starting of the set (local or remote). If moved to Off (0) during set operation, this will cause an immediate engine shutdown (bypasses cool-down timers). This type of shutdown should be avoided, if possible, to help prolong the reliability of the engine.

![[19802704.png]]

Push the Emergency Stop button in for emergency shutdown of the engine. If the engine is **not** running, pushing the button in will prevent the starting of the engine, regardless of the start signal source (local or remote). To reset:

1. Pull the button out.
2. Move the Off (0)/Manual/Auto switch to Off (0).
3. Press the front panel fault acknowledge button.
4. Select manual or auto, as required.

![[19802705.png]]

The Remote Start indicator is a green lamp that is lit whenever the control is receiving a remote run signal. When flashing, this indicates a load demand stop mode.

The **Not** in Auto indicator is a red lamp that flashes continuously when the Off (0)/Manual/Auto switch is **not** in the auto position.

![[19802706.png]]

This Shutdown Status indicator is a red lamp that is lit whenever the control detects a shutdown condition. The generator set can **not** be started when this lamp is on. Shutdown indicators can be reset by turning the Off (0)/Manual/Auto switch to the Off (0) position and pressing the fault acknowledge button.

![[19802700.png]]

The Warning Status indicator is a yellow lamp that is lit whenever the control detects a warning condition. Warning indicators can be reset by pressing the fault acknowledge button. It is **not** necessary to stop the generator set to acknowledge a warning indication.

![[19802700.png]]

### Menus

In standby mode, to activate and view the menu displays without starting the generator set, press and release any button. This will initialize the operating software and permit operation of the menu display panel. If no menu selection is made, a software timer will shut down the display power after 10 minutes. In Power-On mode, power is continuously supplied to the control panel. Display will **always** remain active.

![[19802698.png]]

The graphical display is capable of displaying up to 9 lines of data with approximately 27 characters per line. The display is used to view the menus of the menu-driven operating system. This display is also used to show the following system information:

1. Operation Line: Modes of operation such as stopped, time delay to start, and warm up at idle, as well as paralleling operations such as standby, dead BUS close, and synchronize
2. Action Line: System actions such as warning, shutdown cooldown, shutdown, and fault codes
3. Status Line: Fault code messages
4. Menu display area.

![[19802697.png]]

Six momentary buttons - three on each side of the graphical display window - are used to navigate through the system control menus and to adjust generator set parameters. The button is active when the message or symbol adjacent to the switch is highlighted (displayed in reverse text). The displayed message or symbol indicates the function of the button.

![[19802698.png]]

In the graphical display, the following symbols indicate:

- The down arrow symbol indicates that selecting the corresponding button causes the operating program to go to the next menu display - as shown in the menu diagrams.
- The up arrow symbol indicates that selecting the corresponding button causes the operating program to go back to the previous menu display.
- The double up arrow symbol indicates that selecting the corresponding button causes the operating program to go back to the previous main menu display (Menu A/B).

![[19802708.png]]

The language and units can be changed at any time by pressing the two lower menu buttons (one on each side) simultaneously. This will display the language/units submenu. To save changes made in a field, press the ENTER button.

Use the positive (+) and negative (−) buttons to increase or decrease the values in the previous fields. Use the (--\>) button to move the cursor within the desired field.

![[19802709.png]]

Language Field is used to select English, Spanish, or French for the menu language.

Local/Remote Field selection **must** be set to Local when operator interface panel is mounted on generator set, or Remote when mounted remotely away from the generator set.

When set to Remote, the control system will activate the remote Fault Reset, the \_ \\\_, and the Start and Stop buttons in the Control submenu or deactivate these buttons when set to Local.

![[19802710.png]]

Degree Field is used to select °F or °C for temperature readings.

Pressure Field is used to select PSI, KPA, BAR, or IN for pressure readings.

![[19802710.png]]

The main menus A/B list and categorize the main submenus. Each of these submenus can be viewed by pressing the desired menu button. The Adjust and Setup menus can be modified by qualified personnel **only** with the correct passwords. These menus are explained under the Calibration and Adjustment heading.

![[19802712.png]]

![[19802713.png]]

The \_ \\\_ button is used to open and close the generator set circuit breaker (CB). With the control panel Off (0)/Manual/Auto switch in the Auto position, the circuit breaker is opened or closed by the control system software. In the Manual position, the circuit breaker **must** be closed by this button.

![[19802712.png]]

The first Engine Data submenu displays general information that applies to all generator sets.

![[19802714.png]]

The data in the remaining submenus will vary according to the sensors provided with the engine.

![[19802715.png]]

![[19802716.png]]

Alternator Data Submenu has the following indications:

The Voltage L-L and L-N indicates voltage Line-to-Line and Line-to-Neutral.

The Line-to-Neutral column will **not** be displayed for a three-phase/three-wire system. The voltage Line-to-Line (L1, L2, and L3) are measured between L1 to L2, L2 to L3, and L3 to L1, respectively.

Current indicates all phases.

Frequency indicated generator set output frequency.

![[19802717.png]]

The kW, kVA, and PF displays generator set kW and kVA output (average and individual phase and direction of flow) and power factor with leading/lagging indication.

![[19802718.png]]

The % AVR: Displays voltage regulator (drive) level in percentage of maximum.

![[19802717.png]]

When the graphical display is mounted in a remote location (**not** located on the generator set control panel), the menu buttons in the Control submenu are used to perform the following remote operations. The Off (0)/Manual/Auto switch **must** be in the Auto position. To activate these menu buttons for remote use, refer to Menu Language/Units Selection.

The remote START or STOP button used to start and stop the generator set from a remote location. When the generator set is operating, STOP will be displayed for the button; and when the generator set is **not** operating, START will be displayed.

The Fault Acknowledge button is used to acknowledge Warning messages.

The Bargraph Test is used to test digital bargraphs on operator interface panel.

![[19802720.png]]

Local Control Submenu Functions has the following button:

Run at Idle/Run at Rated button is used to run the generator set at idle or rated.

The function of the Run at Idle button will **always** be active, regardless of the Remote/Local function of the Control submenu.

![[19802707.png]]

History about submenus maintains a data log of engine starts, operating hours for the engine, operating hours for the control, and megawatt hours of the generator set.

![[19802721.png]]

This is the load profile data detailing the number of hours the set has run in each percent range. This is commonly referred to as the duty cycle for the generator.

![[19802722.png]]

The About menu provides the following generator set information:

- Genset model and wattage
- Output voltage and WYE, DELTA, or SINGLE
- Frequency: 50 or 60 Hz
- Rating: Standby, Prime, or Base
- APP (Application) Rating: Generator set kW for selected rating (Standby, Prime, or Base).

![[19802723.png]]

- Version level of the controller and panel operating software
- RTOP calibration loaded into base board
- BATS base board basic software revision (boot loader).

![[19802724.png]]

Fault History: The control maintains data of all fault conditions as they occur and time-stamps them with the control and engine operating hours.

When a fault condition occurs, the fault will be recorded. If the control detects the same fault after corrective action and the control was reset, the control will consider this to be the same original fault and will **not** rerecord this fault in the fault history file.

![[19802725.png]]

Bus Data Submenu has the:

The top line of the graphical display for Paralleling Status Line, is used to indicate the following paralleling status:

- Standby
- Dead bus close
- Synchronize
- Load share
- Load govern.

![[19802726.png]]

The Bus Data submenu gives the operator the following information:

- Line-to-Line bus voltage
- Bus frequency
- Phase difference between the bus and the generator set (reference is the bus).

The bottom line of the graphical display is used to indicate the following BUS/GEN sync status.

- **Not** synchronizing
- Synchronizing
- Ready to close.

\_\\\_ Button: Used to open and close the generator set circuit breaker (CB).

![[19802726.png]]

### Calibration and Adjustment

Modifying Setup/Adjust Submenus

> [!warning] CAUTION · Осторожно
> Improper calibration or adjustment of the control can cause equipment malfunction or damage.

The Setup and Adjust submenus allow you to calibrate the graphical display meters and to adjust system parameters, customer-defined faults, generator set voltage/frequency, and paralleling applications. The setup and adjust submenus are intended for technically qualified personnel **only**.

![[19802713.png]]

There are two passwords assigned to the system software. The user password is for site personnel or authorized service personnel to use the adjust submenu. The application password is for authorized service personnel **only** to use the setup submenu.

![[19802727.png]]

The user password does **not** have to be activated; this can be used at the discretion of the operator. The application password is set to GENSET when first installed. This password **must** be used by the service technician in order to access the setup submenu. Passwords are valid for **only** 10 minutes after the last button is pressed. After this time, the password **must** be reentered.

To Enter the Password:

1. Display submenu to modify.
2. Press either the positive (+) or negative (-) button within the displayed submenu. The password menu appears.
3. Press the positive (+) and negative (-) button to select the first character of the password. Enter application password for setup submenus or user password for adjust submenu.
4. Press the --\> button to select the next character field.
5. Repeat steps 3 and 4 to enter remaining password characters.
6. Press the enter button after entering the password. The submenu selected in step 1 will reappear.

![[19802728.png]]

If changes are made in the setup or adjust submenus, the save/restore menu will appear when you press the up or down button to move to the next/previous submenu.

Pressing the save button will save changes and advance to the selected submenu. Pressing the restore button will return all changes to previous settings within that submenu and will display the previous submenu.

![[19802729.png]]

> [!warning] CAUTION · Осторожно
> Improper calibration or adjustment of the control can cause equipment malfunction or damage.

The setup procedure is intended for qualified service personnel **only**. The application password **must** be entered to modify the setup submenu fields.

![[19802730.png]]

> [!warning] CAUTION · Осторожно
> It takes a few seconds to initiate each gain adjustment. It is recommended that any increases in the governor gain setting be made in increments not exceeding 3 percent. This will prevent prolonged periods of unwanted instability.

Gov Gain: If the gain adjustment is set too high, engine speed will “hunt” or oscillate. If gain is set too low, the engine will respond too slowly to changes in load and overspeed can result. Factory setting is 100 percent gain and can be adjusted from 1 to 999 percent.

![[19802731.png]]

Gov Ramp: This adjustment sets the time for the engine to ramp to full operating speed. This adjustment applies only to startup and does **not** affect transient response. Adjustable range: 0 to 10 seconds.

VR Gain: If the gain adjustment is set too high, output voltage will be unstable. If gain is set too low, the output voltage will respond sluggishly to changes in load and overshoot can result.

Use the positive (+) and negative (-) buttons to increase or decrease the values in the previous fields. Use the --\> button to move the cursor within or to the desired field.

![[19802732.png]]

There are four customer fault inputs; the following parameters can be selected for each fault:

- Enable or disable fault
- Active closed or open
- Shutdown or warning.

![[19802733.png]]

The Enable/Disable and the Active Closed/Open fields apply to the Fault 1 and 4 submenus **only**.

![[19802733.png]]

The +/- buttons will allow you to change between closed/open, enable/disable, and shutdown/warning. You can also change the fault message “Customer Fault number” by using this button to select the appropriate characters.

![[19802734.png]]

The calibration submenus allow you to calibrate the control with the reading from a calibrated meter. Adjust the display so that it matches the reading taken on an accurate, recently calibrated meter.

Calibration is normally **only** required when replacing certain circuit cards.

![[19802735.png]]

Use the positive (+) and negative (-) buttons to increase or decrease the values in the previous fields. Use the --\> button to move the cursor within or to the desired field.

![[19802736.png]]

The isolated BUS submenus and the utility submenus adjust the control parameters for generator set protection, synchronizing, and load sharing for both isolated bus and utility (mains) paralleling applications. Utility (mains) can require the adjustment of both the isolated BUS and utility submenus.

![[19802737.png]]

The sync check (permissive) function is operational in both Auto and Manual run modes. The control will make sure that the generator set is at proper voltage, within the defined sync check window for the defined period of time and that phase rotation is correct.

![[19802738.png]]

When all criteria are met, the paralleling breaker is closed automatically by the control (Auto mode), or by operation of the breaker close switch by the operator (Manual mode).

![[19802739.png]]

The synchronizing function of the control is enabled when the control has brought the generator set to rated speed and voltage and has sensed that bus voltage is available. The control automatically adjusts the generator set speed and voltage to match the bus frequency and voltage.

![[19802740.png]]

The control can force the generator set to match a bus voltage and frequency in a range of -40 percent to +10 percent of normal Bus conditions. When the paralleling breaker has closed, the control will bring the generator set back to normal voltage and frequency.

![[19802741.png]]

When the generator set is paralleled to another generator set, the control provides automatic load-sharing functions for both real (kW) and reactive (kVAR) loads. Load sharing is proportional between generator sets based on their standby ratings.

![[19802742.png]]

If two generator sets of different sizes are paralleled, they will assume the same percentage of the system load automatically. This can be easily verified on the analog load meters on the front of the control panel.

![[19802743.png]]

When the utility paralleling mode is enabled and the generator set paralleling breaker is closed, the generator set will assume load based on external analog input signal. The input signal **must** be calibrated from 0 to 5 VDC. When the signal is at 0.5 to 1 VDC, the control will operate the generator at no load in parallel with the utility (mains) source. At 4.5 VDC and greater, the control will operate the generator set at 110 percent of the generator set base load setting.

![[19802744.png]]

When the load govern signal is between 1 VDC and 4.5 VDC, the control will operate the generator set at a load level that is determined by a linear relationship between the kW reference and the load govern signal.

![[19802745.png]]

ISO BUS Submenus:

SYNC TIME LIMIT: This parameter adjusts the time delay in seconds before the fail-to-synchronize alarm will operate.

REVERSE PWR LIMIT: Adjusts the reverse power set point. Typical set point is 10 to 15 percent.

REVERSE PWR TIME: Adjusts the reverse power function time delay. A typical time delay is 3 seconds. (Lower reverse power set points can result in nuisance reverse power shutdown faults.)

PERM WIN-PHASE: Adjusts the width of the permissive (sync-check) acceptance window. The adjustment range is from 5 to 20 electrical degrees. Recommended set point is 20 degrees for isolated bus applications and 15 degrees for utility (mains) paralleling applications.

![[19802746.png]]

PERM WIN-TIME: Adjusts the time period (in seconds) for which the generator set **must** be synchronized with the system bus, before a breaker close signal is issued by the PowerCommand® Control. Available range is 0.5 to 5 seconds. Recommended value is 0.5 seconds for isolated bus. (Adjusting the control for a smaller sync-check window or longer time delay will cause synchronizing time to be extended.)

![[19802747.png]]

SYNC GAIN: The sync gain adjustment controls how quickly the governor will respond to try to minimize the bus/generator phase difference. Increasing the gain will speed up the response. If the gain is too high, instability can result.

kW BALANCE: This function adjusts the kW load-sharing function of the generator set. Before adjusting this value, all generator set calibrations should be performed. If the total load on the system is **not** shared proportionately, the kW Balance can be used to adjust the generator set for more precise load sharing. Increasing the kW Balance value will cause the generator set to reduce the percentage of the total kW load on the set.

kVAR BALANCE: This function adjusts the kVAR load-sharing function of the generator set. Before adjusting this value, all generator set calibrations should be performed. If the total load on the system is **not** shared proportionately, the kVAR Balance can be used to adjust the generator set for more precise load sharing. Increasing the kVAR Balance value will cause the generator set to reduce the percentage of the total kVAR load on the set.

kW GAIN: Adjusts the rate of change of kW load on the generator set. With a constant load on the system, if the generator set load is constantly changing, reduce the gain adjustment on the generator set. This also allows modification of the rate of load assumption on transient load change.

kVAR GAIN: Adjusts the rate of change of kVAR load on the generator set. With a constant load on the system, if the generator set load is constantly changing, reduce the gain adjustment on the generator set. This also allows modification of the rate of load assumption on transient load change.

![[19802748.png]]

1st FAIL TIME: Time delay in seconds after a signal from the first start master is **not** sensed by the PowerCommand® Control that a FIRST START FAIL warning is displayed.

RAMP UNLOAD TIME: When a load demand stop input is sensed, the load is ramped down from the present load level on the set to the ramp unload level in the time specified in seconds.

RAMP UNLOAD LEVEL: The load demand ramp unload function will ramp the load down from the present level on the set to this level before opening the set circuit breaker. Value shown is in percent of genset standby rating.

RAMP LOAD TIME: When the load demand stop signal is removed, the load is ramped from 0 kW to the load share level in the specified time after the circuit breaker closes.

LOSS FIELD TIME: Adjusts the loss of field function time delay. A typical delay is 2 seconds.

![[19802749.png]]

The Utility Submenus use the positive (+) and (-) buttons to increase or decrease the values in the previous fields. Use the --\> button to move the cursor within or to the desired field.

![[19802750.png]]

The BASE LOAD (%) controls the maximum kW load level that the generator set will operate at when paralleled with the utility (mains). The value shown indicates the steady-state load on the generator as a percent of the generator set standby rating. Extended operation at load levels in excess of the generator set rating can cause abnormal engine wear or premature engine failure.

![[19802752.png]]

PF LEVEL: Adjusts the power factor that the generator set will run at when paralleled to the utility (mains). Recommended setting is 1.0.

RAMP LOAD TIME: This is the ramp time from present set load to level determined by the load set analog input. This is active when the control first enters the load govern mode.

RAMP UNLOAD TIME: This is the ramp time from present set load to 0 kW. This ramp is active when the load set analog input is less than 0.5 VDC.

MULTIPLE/SINGLE: This controls whether the set is to operate as part of a multiple set or single set system.

![[19802753.png]]

kW GOVERN GAIN: This controls the rate that the generator set kW load is increased after the generator set has closed to the system bus when utility (mains) paralleled.

![[19802751.png]]

Decreasing this value will result in slower loading of the generator set.

![[19802754.png]]

kW INTEGRAL GAIN: This controls the response of the generator set to large load changes when utility (mains) paralleled. Use of a higher integral value will result in slower response, and kVAR GOVERN GAIN: This controls the rate that the generator set kVAR load is increased after the generator set has closed to the system bus when utility (mains) paralleled. Decreasing this value will result in slower loading of the generator set. reduced kW overshoot on load assumption or rejection, especially on large system load changes. Decreased integral values will also result in slower load acquisition and rejection.

kVAR INTEGRAL: This controls the response of the generator set to large load changes when utility (mains) paralleled. Use of a higher integral value will result in slower response, and reduced kVAR overshoot on load assumption or rejection, especially on large system load changes. Decreased integral values will also result in slower load acquisition and rejection.

![[19802751.png]]

The Adjust Submenu has the following selections:

VOLTAGE: Used to adjust the output voltage ±5 percent.

FREQUENCY: Used to adjust the frequency ±3Hz.

START DELAY: This delay applies **only** to remote starting in the Auto mode. The Start Delay adjustment range is 0 to 300 seconds.

STOP DELAY: This delay applies **only** to remote stopping in the Auto mode. The Stop Delay adjustment range is 0 to 600 seconds.

> [!missing]- Иллюстрация `19802755.png` не извлечена — смотрите PDF-оригинал документа

Calibration Procedure

The paralleling bus **must** be de-energized while voltage calibrations are performed. If this is **not** possible, disconnect and isolate bus voltage inputs to the Bus PT Module before attempting voltage calibration.

1. Display the Voltage Calibration submenu.
2. With the genset OFF, attach a calibrated voltmeter to the AC output from L1 to L2 (L1 to Neutral for single-phase alternators).
3. Start the genset and allow it to reach normal operating speed.
4. Calibrate voltage reading for L1 so that the reading on the display agrees with the calibrated voltmeter.
5. Shut the generator set OFF.
6. Repeat steps 2 through 5 for L2 and L3. (In step 2 attach meter to the AC output from L2 to L3 to calibrate L2, L3 to L1 to calibrate L3).
7. Save or restore changes.

![[19802735.png]]

Genset Ammeter Display Calibration functions as follows:

1. Display the Current Calibration submenu.
2. With the genset OFF, attach a calibrated ammeter to L1.
3. Start the genset and allow it to reach normal operating speed.
4. Load the genset to maximum rated kVA at rated voltage.
5. Calibrate the reading for L1 current so that the reading on the display agrees with calibrated ammeter.
6. Repeat steps 2 through 5 for L2 and L3. (In step 2, attach meter to L2 to calibrate L2 current and L3 to calibrate L3 current.)
7. Save or restore changes.

![[19802736.png]]

The paralleling bus **must** be de-energized while voltage calibrations are performed. If this is **not** possible, disconnect and isolate bus voltage inputs to the Bus PT module before attempting voltage calibration.

1. Display the Bus Voltage Calibration submenu.
2. With the genset OFF, attach a calibrated voltmeter to the alternator AC output from L1 to L2.
3. Start the genset and allow it to reach normal operating speed and voltage.
4. Push the breaker close button located on Menu A and verify that the paralleling breaker has closed by observing on the control panel graphical display and physical check of the breaker.
5. Calibrate the voltage reading for Bus Volts L1 so that the reading on the display matches the reading on the calibrated meter.
6. Shut the generator set OFF.
7. Repeat steps 2 through 6 for Bus Volts L2 and L3. (In step 2 attach meter to the AC output from L2 to L3 to calibrate L2 and L3 to L1 to calibrate L3.)
8. Save or restore changes.

![[19802737.png]]

### ECM

Controls Box

The Configuration 1.0 controls box contains the electronics hardware that controls generator set operation. The controls box holds the card cage (composed of individual circuit boards), the voltage regulator, PT/CT board, Bus PT module, terminal blocks for customer connections, and other electronic devices. This configuration shown is found on some QSK60 generator sets and is located on the front of the alternator.

> [!missing]- Иллюстрация `19802811.png` не извлечена — смотрите PDF-оригинал документа

The configuration 2.0 of the controls box can be found on all QSX15 and some QSK45/60 generator sets. This controls box is located on the rear of the alternator and also houses the switch panel and the operation interface panel (if applicable).

![[19802810.png]]

Board Description

The ECM contains several circuit boards that make up the PowerCommand® Control. These boards are as follows:

- Fuel board
- Base board
- Genset board
- Parallel board (optional)
- LonWorks® board (optional).

![[19802869.png]]

The Fuel Board interfaces between the base board and the fuel control actuators. This board has a large heat sink due to the heat generated by the drivers. This board has warning and shutdown LEDs. These LEDs can be used for fault flashout.

![[19802788.png]]

The Base board has the microprocessor and memory chips. This board **only** deals with digital signals and pulse-width-modulated signals. This board has the Ready LED.

![[19802789.png]]

The Genset board interfaces between the base board and the alternator. Voltage and current signals from the alternator enter the genset board from the PT/CT module. The excitation signal goes through the genset on its way to the voltage regulator. This board has the Run LED.

![[19802790.png]]

The Parallel board interfaces between the base board and the generator and bus signals. This board performs all of the calculations needed to synchronize the generator frequency and voltage levels to the bus.

![[19802791.png]]

The LonWorks® board interfaces between PowerCommand® Control and the network. It allows the PowerCommand® Control to become a node on the LonWorks® network. This board has several network-related LEDs.

![[19802792.png]]

The potential transformer and current transformer module is the first step in measuring the generator set output voltage and current.

- The input voltage is reduced through a set of transformers to a nominal value of 18 VAC phase-to-common.
- Neutral is connected to the PT/CT module, but it is **not** carried through to the PowerCommand® Control. Neutral is assumed in the control.

The potential transformer and current transformer module voltage sensing:

- When the control is set up for a Wye or Start connection, you will see Phase-to-Neutral and Phase-to-Phase voltages.
- When the control is set up for a Delta configuration, the display shows **only** Phase-to-Phase voltages.

Potential transformer and current transformer module current sensing:

- PowerCommand® generator sets use 0.55-amp CTs instead of the industry standard 5.0-amp CTs.
- Each phase of current input is applied to a burden resistor in the PT/CT module. This is a safety measure to prevent the PT/CT module and the genset board or paralleling board from accidentally opening.
- The nominal output from the PT/CT module when the current input is at its rated maximum is 1.65 VAC.

> [!missing]- Иллюстрация `19802794.png` не извлечена — смотрите PDF-оригинал документа

The Bus PT module is mounted inside the accessory box. This module converts the bus output voltage (from the load side of the paralleling breaker) to 18 VAC and provides this to the analog board. It provides a reference signal to the PowerCommand® Control for synchronizing the generator set output to a system bus. There are four versions of this module, for primary voltages of 69, 120, 240, or 346-VAC line to neutral. For proper operation, the correct Bus PT module **must** be installed in the generator set. Correct phasing is also important as the system uses the Bus PT module output for both protection and control of the generator set.

> [!missing]- Иллюстрация `19802868.png` не извлечена — смотрите PDF-оригинал документа

The voltage regulator is a “power amplifier” for the excitation signal. This voltage regulator receives a low-level excitation signal from the genset board and amplifies it to a high enough level to control the alternator. The voltage regulator has two inputs and one output.

Inputs:

- Run signal from the base board.
- Three-phase AC voltage from the permanent magnet generator (PMG).
- Low-level pulse-width-modulated signal from genset board.

Outputs:

- Pulse-width-modulated excitation signal. The output to the F1 terminal of the exciter stator is +300 VDC (rectified from the PMG AC input). The output to the F2 terminal of the exciter is a PWM Ground Signal.
- When the ground-potential pulse to the F2 terminal of the exciter is wider (higher duty cycle), more power is sent to the exciter and the output voltage of the alternator goes up.

> [!missing]- Иллюстрация `19802793.png` не извлечена — смотрите PDF-оригинал документа

There are three LEDs on the VR:

- DS1 Green: VR has Run excitation signal from base board.
- DS2 Amber: Brightness is relative to excitation duty cycle.
- DS3 Green: PMG Voltage is 105 VAC or higher (850 rpm). This LED indicates that the secondary start disconnect contacts in the VR are open.

> [!missing]- Иллюстрация `19802793.png` не извлечена — смотрите PDF-оригинал документа

Customer monitor/control connections are attached to terminal blocks TB1, TB2, TB3, TB4, TB5, TB6, and TB8. These terminal blocks are located on the front of the ECM boards with the exception of TB3. TB3 can be mounted on the backside of the controls box or inside it, depending on configuration.

The terminal blocks provide customer connections for equipment such as a remote annunciator panel, sensing devices used to monitor genset operation, remote start/stop switches, control box heater, battery charger, circuit breakers, load sharing, load governing, network connections, and other devices.

![[19802812.png]]
