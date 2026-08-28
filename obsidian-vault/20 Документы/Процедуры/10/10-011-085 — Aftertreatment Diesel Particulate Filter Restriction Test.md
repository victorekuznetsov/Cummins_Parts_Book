---
type: "Процедура"
doc: "10-011-085"
title_en: "Aftertreatment Diesel Particulate Filter Restriction Test"
modified: "2016-09-21"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 22
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-011-085.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-011-085.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Aftertreatment Diesel Particulate Filter Restriction Test

> [!abstract] Процедура · `10-011-085`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 11 - Exhaust System · Section 11 - Exhaust System - Group 11
> **Даты:** изменён 2016-09-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-011-085.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-011-085.pdf)

### General Information

Applications

![[00c00069.png]]

This procedure applies to ISX15 CM871 engines with Phase 2, 3, and 4 diesel particulate filters (DPF):

| DPF Part Number |  |  |  |
|---|---|---|---|
| Phase 1 | Phase 2 | Phase 3 | Phase 4 |
| 4969702 | 5283669 | 5297522 | 4388409 |
| 4969701 | 5283778 | 5297990 | 4388410 |
| 4969701 | 5283799 | 5297989 | 4388411 |

Introduction

The Aftertreatment Diesel Particulate Filter Restriction Test can be used to evaluate the aftertreatment diesel particulate filter (DPF) restriction, without requiring the use of specialized equipment. The test may be used during troubleshooting for aftertreatment system related fault codes, to determine if an aftertreatment maintenance (cleaning or exchange) interval has been reached or if the aftertreatment DPF differential pressure sensor is malfunctioning.

The Aftertreatment Diesel Particulate Filter Restriction Test will aid in the evaluation of aftertreatment DPFs to determine the following:

- Needs to be cleaned or exchanged to remove soot, ash, or foreign matter
- Meets reuse criteria for restriction after a cleaning event.

Soot accumulation in the aftertreatment DPF is a normal function of engine operation. However, the accumulation of excessive soot can cause frequent aftertreatment regenerations and is normally caused by fuel system or air handling system issues.

Ash accumulation is the result of non-combustible products collecting in the aftertreatment DPF. Excessive ash accumulation in the aftertreatment DPF can be caused by lubricating oil consumption, coolant consumption, contaminated fuel, and other issues.

Foreign material in the aftertreatment DPF is **not** normal and can be caused by issues such as degraded exhaust system components, exhaust leaks, or damage to engine or other components.

> [!note] Note · Примечание
> Check for active fault codes prior to performing the Aftertreatment Diesel Particulate Filter Restriction Test. If active fault codes are present, reference the appropriate fault code troubleshooting tree before completing this test, unless you are directed to perform this test in a troubleshooting tree.

> [!note] Note · Примечание
> The Aftertreatment Diesel Particulate Filter Restriction Test **must** be performed immediately after the successful completion of an aftertreatment diesel particulate filter regeneration, except where noted in this procedure. The aftertreatment diesel particulate filter regeneration is performed using INSITE™ electronic service tool.

Performing the aftertreatment diesel particulate filter regeneration makes sure that any exhaust residue or soot is removed from the aftertreatment DPF, resulting in a restriction measurement that is attributable to ash content, except where foreign material has entered the aftertreatment DPF. Performing the aftertreatment diesel particulate filter stationary regeneration also makes sure that the aftertreatment DPF temperature is raised to a level that provides maximum exhaust gas flow rate during the restriction test and that any moisture present has also been removed.

![[11c00245.png]]

### Preparatory Steps

Exhaust Outlet Inspection

Inspect the exhaust system outlet.

Inspection of the exhaust system outlet can aid in determining the condition of the aftertreatment DPF. The exhaust system outlet should appear clean with little to no exhaust residue or soot buildup.

> [!note] Note · Примечание
> Some accumulation of exhaust residue or soot is normal, and does **not** indicate an issue with the aftertreatment DPF.

A heavy buildup of exhaust residue or soot accumulation on the exhaust system outlet is the result of an issue with the aftertreatment DPF. Perform the Snap Acceleration Test - Aftertreatment Connected.

![[14d00033.png]]

Snap Acceleration - Aftertreatment Connected

Open INSITE™ electronic service tool, but do **not** connect to the engine control module (ECM).

Go to Tools \> Options \> Units of Measure.

In the drop down menu in the Units of Measure menu, select Metric. Select the Apply button and then select the OK button.

Close INSITE™ electronic service tool Options menu.

![[ck800wa.png]]

Connect INSITE™ electronic service tool to the service data link. [[105-019-428 — Engine Datalinks|Refer to Procedure 019-428 in Section 19.]]

Capture a work order (job image) with INSITE™ electronic service tool.

![[19803969.png]]

Use INSITE™ electronic service tool to enable the Setup for Dynamometer ECM Diagnostic Test.

> [!note] Note · Примечание
> It is necessary to activate this test to allow the engine speed to reach the required level without requiring a change to Customer Feature and Parameter Settings (i.e. Maximum Vehicle Speed Without VSS, Load Based Speed Control, etc.)

> [!note] Note · Примечание
> The setup for the Dynamometer ECM Diagnostic Test can be found in the ECM Diagnostic Tests section of INSITE™ electronic service tool.

![[19803969.png]]

- The vehicle transmission **must** be in NEUTRAL.
- The vehicle parking brake **must** be applied.
- The vehicle hood **must** be closed.
- The manual fan switch, if equipped, and vehicle air conditioning system **must** be turned OFF to prevent engine cooling fan operation during this test.
- The engine **must** be at normal operating temperature (above 82°C \[180°F\] coolant temperature).

Start the engine.

Allow the engine to stabilize at low idle for 30 seconds.

Depress and hold the accelerator pedal to verify that the engine can reach high idle (normally 1800-2000 rpm).

Release the accelerator pedal and allow the engine to stabilize at low idle for 30 seconds.

Quickly depress the accelerator pedal from 0 percent to 100 percent and hold the engine at high idle (normally 1800 - 2000 rpm) for 5 seconds.

Release the accelerator pedal and allow the engine to stabilize at low idle for 30 seconds.

Repeat the Snap Acceleration Test - Aftertreatment Connected as needed to allow a visual check for smoke at the exhaust system outlet to be completed as the engine is accelerated from low idle to high idle.

> [!note] Note · Примечание
> The visual check may need to be performed with the aid of another technician, depending on the vehicle's exhaust configuration.

![[14c00079.png]]

During the Snap Acceleration Test - Aftertreatment Connected, check for black smoke exiting the exhaust system outlet, as the engine is accelerated from low idle to high idle.

> [!note] Note · Примечание
> In some applications, a Snap Acceleration Test may **not** provide the conditions necessary to reveal a malfunctioning aftertreatment DPF. If there is a heavy buildup of exhaust residue/soot on the exhaust outlet and a snap acceleration does **not** reveal a condition outlined in the following steps, it can be necessary to perform a brief acceleration run under partial to full load or to perform a stall test. Refer to Procedure 014-008 in Section 14.

If black smoke is found at the exhaust system outlet during these tests, reference the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600, and inspect the aftertreatment DPF for damage.

Do **not** use the Aftertreatment Diesel Particulate Filter Restriction Test to evaluate a damaged aftertreatment DPF. Incorrect test results **will** occur.

![[11c00246.png]]

If gray smoke or faint black smoke is present, reference the Aftertreatment Diesel Oxidation Catalyst and Aftertreatment Diesel Particulate Filter Reuse Guidelines, Bulletin 4021600, and inspect the aftertreatment DPF for damage. White smoke during the Snap Acceleration Test - Aftertreatment Connected may **not** indicate a malfunction. No additional troubleshooting or repair is necessary at this time.

![[11c00247.png]]

If black or gray smoke is **not** found at the exhaust system outlet, proceed to the Sensor Signal Voltage Test in this section.

![[11o00085.png]]

Sensor Signal Voltage Test

In INSITE™ electronic service tool, add the following parameters to the Data Monitor/Logger screen:

1. Engine speed (rpm)
2. Exhaust volumetric flow rate (m 3 /s)
3. Aftertreatment DPF differential pressure (kPa)
4. Aftertreatment DPF differential pressure sensor signal voltage (VDC).

![[19803969.png]]

Verify that the parameter aftertreatment DPF differential pressure sensor signal voltage reads 0.69 VDC (± 0.22 VDC at 25°C \[77°F\] and below or ± 0.14 VDC at 26°C \[78°F\] or greater) at keyswitch ON, engine OFF.

> [!note] Note · Примечание
> If the aftertreatment DPF differential pressure sensor signal voltage does **not** read within specification, inspect the aftertreatment DPF differential pressure sensor and associated wiring. Use the following procedure in the CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. Refer to Procedure 019-443 in Section 19.

![[19803969.png]]

Disconnect the aftertreatment DPF differential pressure sensor wiring harness connector.

Use INSITE™ electronic service tool to verify that Fault Codes 1881 and 3134 are active.

> [!note] Note · Примечание
> If Fault Code 1881 did **not** become active, inspect the aftertreatment DPF differential pressure sensor and associated wiring. Use the following procedure in the CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. Refer to Procedure 019-443 in Section 19.

![[19c01637.png]]

Use the Framatome™ male test lead, Part Number 3164596, or equivalent, to short the aftertreatment DPF differential pressure sensor 5 VDC SUPPLY (pin 4 of the wiring harness connector) to the aftertreatment DPF differential pressure sensor SIGNAL (pin 2 of the wiring harness connector).

Use INSITE™ electronic service tool to verify that Fault Code 1879 is active.

> [!note] Note · Примечание
> If Fault Codes 1879 did **not** become active, the aftertreatment DPF differential pressure sensor signal and aftertreament diesel particulate filter outlet pressure sensor signal could be incorrectly routed. Refer to the original equipment manufacturer (OEM) service manual.

> [!note] Note · Примечание
> If Fault Codes 1881 did **not** become active, inspect the aftertreatment DPF differential pressure sensor and associated wiring. Use the following procedure in the CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. Refer to Procedure 019-443 in Section 19.

![[11y00001.png]]

Verify that issues with the aftertreatment DPF differential pressure sensor and associated wiring have been corrected by repeating the previous steps, if necessary.

Connect the aftertreatment DPF differential pressure sensor wiring harness connector.

![[ck800wa.png]]

Use INSITE™ electronic service tool to clear the inactive fault codes from the aftertreatment DPF differential pressure sensor test(s).

![[19803969.png]]

### Test

Verify that the following conditions have been met:

1. The vehicle is parked in an appropriate location, on a surface that will **not** burn or melt under high temperatures (such as clean concrete or gravel, **not** grass or asphalt) and away from anything that can burn, melt, or explode.
2. The vehicle is parked securely.
3. Set up a safe exhaust area.
4. Check the exhaust system surfaces.
5. Prepare for engine speed changes during regeneration.
6. Make sure that the vehicle and surrounding areas are monitored during regeneration. If any unsafe condition occurs, be prepared to shut the engine OFF immediately.

![[ck800wa.png]]

> [!danger] WARNING · Опасно
> During regeneration, exhaust gas temperature could reach 800°C \[1500°F\] and exhaust system surface temperature can exceed 700°C \[1300°F\], which is hot enough to ignite or melt common materials, and cause severe burn injuries. The exhaust and exhaust components can remain hot after the vehicle stopped moving. To avoid the risk of fire, property damage, burns, or other serious personal injury, make sure that no combustible materials are located where they are likely to come in contact with hot exhaust or exhaust components.

Perform the aftertreatment DPF regeneration using INSITE™ electronic service tool.

> [!note] Note · Примечание
> It is **not** necessary to allow the aftertreatment DPF regeneration to fully complete during this section of the procedure (a minimum of 30 minutes is recommended).

> [!note] Note · Примечание
> The aftertreatment DPF regeneration can be found under the ECM Diagnostic Test menu in INSITE™ electronic service tool.

> [!note] Note · Примечание
> Engine speed will increase and the turbocharger can whistle loudly during the aftertreatment DPF Regeneration Test.

To stop the aftertreatment DPF regeneration, engage the clutch, service brake, and accelerator pedal; or shut the engine OFF.

Once regeneration is complete, exhaust gas and exhaust surface temperatures will remain elevated for 3 to 5 minutes.

![[19803969.png]]

> [!danger] WARNING · Опасно
> The engine cooling fan must be fully engaged and locked in the ON position before conducting the Aftertreatment Diesel Particulate Filter Restriction Test. Failure to lock the engine cooling fan in the ON position may result in damage to the fan clutch, engine or other components.

Shut the engine OFF.

Set the engine cooling fan to the ON, ENGAGED, or LOCKED position.

> [!note] Note · Примечание
> Do **not** use INSITE™ electronic service tool to change feature and parameter settings to alter the operation of the engine cooling fan. Most engine cooling fans are designed to default to the ON, ENGAGED, or LOCKED position with a loss of air pressure or electrical current. In order to alter engine cooling fan operation, it may be necessary to disconnect the air or electrical supply. Reference the equipment manufacturer service information.

Start the engine.

Verify that the engine cooling fan will maintain the ON, ENGAGED, or LOCKED position. Reference the equipment manufacturer service information.

Shut the engine OFF.

![[ck800wa.png]]

Use INSITE™ electronic service tool to enable the Setup for Dynamometer ECM Diagnostic Test.

> [!note] Note · Примечание
> It is necessary to activate this test to allow the engine speed to reach the required level without requiring a change to customer feature and parameter settings (i.e. Maximum Vehicle Speed Without VSS, Load Based Speed Control, etc.).

> [!note] Note · Примечание
> The setup for Dynamometer ECM Diagnostic Test can be found in the ECM Diagnostic Test section of INSITE™ electronic service tool.

![[19803969.png]]

> [!note] Note · Примечание
> This procedure requires that the engine be operated at high idle for thirty (30) seconds. Do **not** attempt to perform a Snap Acceleration Test - Aftertreatment Connected during this section of the procedure. Incorrect test results will occur.

Perform the following steps:

1. Start the engine.
2. Allow the engine to stabilize at low idle for 30 seconds.
3. Depress the accelerator from 0 percent to 100 percent and hold the engine at high idle (normally 1800 to 2000 rpm)
4. Use INSITE™ electronic service tool Data Monitor/Logger to log these parameters.
5. Observe the parameter exhaust volumetric flow rate in INSITE™ electronic service tool Data Monitor/Logger.
6. Verify that the exhaust volumetric flow rate reaches 0.3 m 3 /s or higher.
7. Stop INSITE™ electronic service tool Data Monitor/Logger after 30 seconds and save the resulting log file using the file name ESN\_After\_Cleaning\_Run\_1.log.csv where ESN is the engine serial number of the vehicle being tested. Save the log file in a suitable location where it will be easy to locate. Use the ESN as the folder name.
8. Release the accelerator pedal and allow the engine to stabilize at low idle for 30 seconds.
9. Repeat the applicable step (2-8) four more times, saving the Data Monitor/Logger log file using the file names ESN\_After\_Cleaning\_Run\_2.log.csv, ESN\_After\_Cleaning\_Run\_3.log.csv, ESN\_After\_Cleaning\_Run\_4.log.csv, and ESN\_After\_Cleaning\_Run\_5.log.csv, where ESN is the engine serial number of the vehicle being tested. Save the log files in a suitable location where they will be easy to locate. Use the ESN as the folder name.

![[19803969.png]]

### Analyzing the Data

Locate the log file(s) taken with INSITE™ electronic service tool Data Monitor/Logger during the Test section of this procedure.

> [!note] Note · Примечание
> The log files will be stored in the folder C:\\Intelect\\Insite\\Logs by default where C: represents the drive letter of the hard drive on which INSITE™ electronic service tool is installed.

| DPF Part Number |  |  |  |
|---|---|---|---|
| Phase 1 | Phase 2 | Phase 3 | Phase 4 |
| 4969702 | 5283669 | 5297522 | 4388409 |
| 4969701 | 5283778 | 5297990 | 4388410 |
| 4969701 | 5283799 | 5297989 | 4388411 |

Review the log files from INSITE™ electronic service tool taken during the Test section of this procedure.

Obtain the aftertreatment DPF differential pressure (kPa) at 0.3 m3/s or greater of exhaust volumetric flow once the engine reached high idle and stabilized.

The aftertreatment DPF differential pressure should be below the Maximum - After Regeneration specification for a given exhaust volumetric flow rate, as shown in the table below:

| Aftertreatment DPF Differential Pressure (Phase 2 or 3 DPF) |  |
|---|---|
| Exhaust Volumetric Flow Rate (m 3 /s) | Maximum (kPa) |
| 0.30 | 1.75 |
| 0.35 | 2.15 |
| 0.40 | 2.55 |
| 0.45 | 3.00 |
| 0.50 | 3.40 |
| 0.55 | 3.80 |
| 0.60 | 4.20 |
| 0.65 | 4.60 |
| 0.70 | 5.00 |
| 0.75 | 5.45 |
| 0.80 | 5.85 |

If the aftertreatment DPF differential pressure is **not** below the Maximum - After Regeneration specification above, the aftertreatment DPF **must** be replaced. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11.]]

| Aftertreatment DPF Differential Pressure (Phase 4 DPF) |  |
|---|---|
| Exhaust Volumetric Flow Rate (m 3 /s) | Maximum (kPa) |
| 0.30 | 2.25 |
| 0.35 | 2.65 |
| 0.40 | 3.05 |
| 0.45 | 3.50 |
| 0.50 | 3.90 |
| 0.55 | 4.30 |
| 0.60 | 4.70 |
| 0.65 | 5.10 |
| 0.70 | 5.50 |
| 0.75 | 5.95 |
| 0.80 | 6.30 |

If the aftertreatment DPF differential pressure is **not** below the Maximum - After Regeneration specification above, the aftertreatment DPF **must** be replaced. [[101-011-041-tr — Aftertreatment Diesel Particulate Filter|Refer to Procedure 011-041 in Section 11]].

### Finishing Steps

Use INSITE™ electronic service tool to check for any active fault codes. If any active fault codes are present, reference the appropriate fault code troubleshooting tree in Section TS.

Use INSITE™ electronic service tool to clear all inactive fault codes.

Use INSITE™ electronic service tool to perform an Aftertreatment Maintenance Reset All and Aftertreatment Filter Installation procedure.

> [!note] Note · Примечание
> The Aftertreatment Maintenance Reset All and Aftertreatment Filter Installation procedure can be found in INSITE™ electronic service tool in the Advanced ECM Data section, under Aftertreatment Maintenance.

![[19803969.png]]
