---
type: "Процедура"
doc: "377-014-034"
title_en: "J1939 Data Link Diagnostic Tool"
modified: "2024-11-22"
manuals:
  - "5411181"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-034.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-034.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# J1939 Data Link Diagnostic Tool

> [!abstract] Процедура · `377-014-034`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2024-11-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-034.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-034.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent version 8.8.0 or later.
- Cummins® INLINE 7 adapter kit, Part Number 5299899 or Nexiq USB-Link 2 with 2 pin Delphi/3-pin Deutsch Adapter (with battery clips).

#### Additional Service Items

- Personal computer with Windows™ 7, or later, software.

![[19803969.png]]

### General Information

The J1939 Data Link Diagnostic Tool is used to help identify J1939 data link performance issues.

The J1939 Data Link Diagnostic Tool is only compatible with a Cummins INLINE ™ 7 adapter kit, Part Number 5299899 or a Nexiq USB-Link 2 with 2pin Delphi/3-pin Deutsch Adapter (with battery clips). Otherwise, troubleshooting the J1939 datalink will need to be performed with a digital multimeter, part number 3377161.

[[377-019-417 — Data Link Circuit, Proprietary|Refer to Procedure 019-417]] in Section 19 to continue with published troubleshooting if a Cummins INLINE ™ 7 adapter kit, Part Number 5299899 or a Nexiq USB-Link 2 with 2pin Delphi/3-pin Deutsch Adapter (with battery clips) is not available.

Using the J1939 Data Link Diagnostic Tool will disconnect all connections to the ECM.

If the recommended Cummins® electronic service tool or equivalent is needed, the J1939 Data Link Diagnostic Tool **must** be disconnected from the ECM.

The J1939 Data Link Diagnostic Tool can be used while engine is ON and can be stopped at any time.

Do **not** drive the vehicle while performing the J1939 Data Link Diagnostic Tool unless directed by published troubleshooting.

The tool is located in the recommended Cummins® electronic service tool or equivalent under the Tools tab in the upper toolbar. See Figure 1. The J1939 Data Link Diagnostic Tool was previously known as the CAN Bus Diagnostics Tool.

![[14k00033.png]]

Figure 1, INSITE Tools Tab in Upper Toolbar

When opening the J1939 Data Link Diagnostic Tool, there is a settings tab that will contain connection settings options and a file location directory to save logs after recording. See Figure 2.

![[00u00098.png]]

Figure 2, J1939 Data Link Diagnostic Tool Settings Tab

1. Tab selections
2. Connection settings options
3. Recording log file location

The J1939 Data Link Diagnostic Tool can also record logs and can be played back while being disconnected from the ECM. See Figure 3.

![[00u00099.png]]

Figure 3, Recordings Tab

1. Recordings tab
2. Available recordings

The J1939 Data Link Diagnostic Tool will **not** start or will be aborted if:

- A diagnostic test is running.
- An Inline 7 or USB Link II datalink adapter is **not** used.
- Inline 7 or USB Link II is **not** connected to the 3 pin service connector.
- Low battery voltage.

### Preparatory Steps

Do **not** use the J1939 Data Link Diagnostic Tool with active fault codes, unless guided to do so by a service procedure and/or published troubleshooting.

Prior to using the J1939 Data Link Diagnostic Tool, complete the following steps:

1. Connect the Inline 7 or USB Link II to the 3-pin service connector.
2. Connect the alligator clips of the Inline 7 or USB Link II to a reliable voltage source.

### Tool Usage

To begin using the J1939 Data Link Diagnostic Tool, complete the following steps:

- Turn the keyswitch to the OFF position.
- Connect the Inline 7 or USB Link II to the 3-pin service connector the alligator clips of the Inline 7 or USB Link II to a reliable voltage source.
- Open the J1939 Data Link Diagnostic Tool found in the Tools tab.
- Select the appropriate connection settings in the Settings Tab.
- Select the Connect button.
- Select the Record button.
- Turn the keyswitch to the ON position.
- Verify the vehicle and surrounding area are monitored during the use of the J1939 Data Link Diagnostic Tool. If any unsafe condition occurs, key OFF or turn off the engine immediately.

Reference the Analyzing The Data section of this procedure for repair actions for the results.

> [!note] Note · Примечание
> If the connection between the J1939 Data Link Diagnostic Tool and the engine control module (ECM) is lost for any reason, a pop-up message will appear. When this occurs, the J1939 Data Link Diagnostic Tool will automatically disconnect. The J1939 Data Link Diagnostic Tool can be restarted after clicking on the Connect button, and then turning the keyswitch to the ON position.

### Analyzing the Data

This section contains five cases that help troubleshoot J1939 Data Link issues.

Select the Component Status and CAN Voltage tab in the J1939 Data Link Diagnostic Tool.

Collect the following information and relate it to the table below to proceed to the appropriate troubleshooting case section.

- CAN H (J1939 +) volts average
- CAN L (J1939 -) volts average
- Total Busload (%) average

| **CAN H (J1939 +) Volts Average** | **CAN L (J1939 -) Volts Average** | **Total Busload (%) Average** | **Troubleshooting Case Section** |
|---|---|---|---|
| Between 1 – 4.5 VDC | Between 1-4.5 VDC | 1-14 | Active Fault Code Troubleshooting |
| Less than 1 VDC | Less than 1 VDC | 0 | Short Circuit To Ground - Check |
| Less than 1 VDC | Less than 1 VDC | 1-17 |  |
| Greater than 11 VDC | Greater than 11 VDC | 0 | Short Circuit To Voltage - Check |
| Greater than 11 VDC | Greater than 11 VDC | 1-17 |  |
| Equal to 2.5 VDC (+- 0.1 VDC) | Equal to 2.5 VDC (+-0.1 VDC) | 0 | Short Circuit Between Positive and Negative J1939 Data Link |

Component names used in the tool differ slightly from Cummins published documents. Reference the J1939 Component Name table for clarification.

| **J1939 Component Name** |  |  |
|---|---|---|
| **Component Name inJ1939 Data Link Diagnostic Tool** | **Component Name inCummins Published Procedures** | **Service Procedure Number** |
| ECM 1 | Engine Control Module | [[377-019-031 — Engine Control Module\|Refer to Procedure 019-031]] in Section 19 |
| Turbocharger Actuator | Variable Geometry Turbocharger Actuator | [[377-010-134 — Variable Geometry Turbocharger Actuator, Electric\|Refer to Procedure 010-134]] in Section 10 |
| Intake NOx Sensor | Aftertreatment Intake NOx Sensor | [[377-019-463 — Aftertreatment Intake NOx Sensor\|Refer to Procedure 019-463]] in Section 19 |
| Outlet NOx Sensor | Aftertreatment Outlet NOx Sensor | Refer to Procedure 019-451 in Section 19 |
| Particulate Matter Sensor | Aftertreatment Particulate Sensor | [[493-019-478 — Aftertreatment Particulate Matter Sensor\|Refer to Procedure 019-478]] in Section 19 |
| Exhaust Gas Temperature Sensor | Aftertreatment Exhaust Gas Temperature Sensor | [[493-019-449 — Aftertreatment Exhaust Gas Temperature Sensor\|Refer to Procedure 019-449]] in Section 19 |
| Urea Quality Sensor | Aftertreatment Diesel Exhaust Fluid Quality Sensor | Refer to Procedure 019-475 in Section 19 |

For inactive fault code troubleshooting for abnormal update rate, proceed to the Inactive Fault Code Troubleshooting case section.

Inactive Fault Code Troubleshooting

For inactive fault code troubleshooting, complete the following steps in order:

Select the Disconnect button on the J1939 Data Link Diagnostic Tool.

Turn keyswitch OFF.

Disconnect each battery from each other and perform an individual load test on each battery.

Reference OEM specifications for acceptable thresholds for 12 volts and 24 volts systems. If the voltages are **not** within the OEM specification, charge or replace the batteries.

Visually inspect ECM battery supply fuses, aftertreatment battery supply fuses, and battery supply fuses for damage, corrosion, or loose connections.

Use the J1939 Data Link Diagnostic Tool to connect by pressing the Connect button and then press the Record button.

Start the engine and bring it to operating temperature (above 70°C \[158°F\]).

Perform a road test.

When road testing is complete, stop recording and press the Disconnect button.

Select the Recordings tab and select the log by pressing the Play button.

Select the J1939 Component Summary tab.

Ignore the component “Retarder – Engine”.

Collect the names of the components with a Claim Address Timestamp Delta (sec) value of 30 seconds or more. See Figure 4.

![[00k00247.png]]

Figure 4, J1939 Component Summary in Playback Mode

1. Tab name
2. Components with claim address TS delta under 30 seconds
3. Components with claim address TS delta over 30 seconds

If there are **no** J1939 components with a Claim Address TS Delta (sec) value of 30 seconds or more, proceed to the Log Navigator (Component Comm) tab.

Search for any spikes greater than 1000 milliseconds in the Log Navigator (Component Comm) tab. See Figure 5.

![[00u00100.png]]

Figure 5, Log Navigator (Component Comm) in Playback Mode

1. Tab name
2. First pair of spikes/dips
3. Second pair of spikes/dips
4. 1000 milliseconds tick mark

Spikes greater than 1000 milliseconds represent loss of communication.

Troubleshoot the J1939 components with spikes greater than 1000 milliseconds in the Log Navigator (Component Comm) tab.

Below is a table that shows which circuit to troubleshoot for those J1939 components with spikes.

| **Components with spikes greater than 1000 milliseconds and Claim Address TS Delta (sec) value of:** | **Circuit to troubleshoot** |
|---|---|
| Less than 30 seconds | J1939 Data Link circuit |
| More than 30 seconds | Power and Ground circuit |

Refer to the appropriate wiring diagram for the engine being worked on to troubleshoot.

**Repair Section:**

Troubleshoot the OEM wiring harness, engine wiring harness, and all interconnects.

If there are no issues with the harnesses, a malfunctioning J1939 component has been detected.

Repair or replace **only** the components that were found to be out of specification.

- Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Section 19.
- Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
- Repair or replace the aftertreatment interface wiring harness. Refer to Procedure 019-477 in Section 19.
- Replace the SAE J1939 components. Refer to the appropriate procedure for each component. Reference the J1939 Component Name table.

Refer to Conditions For Clearing The Fault Code in the Fault Code Overview section for each J1939 component that was troubleshot.

Active Fault Code Troubleshooting

For single and multiple active fault code troubleshooting, complete the following steps in order:

Select the Component Status and CAN Voltage tab.

Ignore the component “Retarder – Engine”.

Use the list below to compare which components are not present in the Component Status and CAN Voltage tab.

- ECM 1
- Turbocharger actuator
- Intake NOx sensor
- Outlet NOx sensor
- Particulate matter sensor
- Exhaust gas temperature sensor
- Urea quality sensor

Obtain the following information from the Component Status and CAN Voltage Tab.

1. The names of the components that are not present compared to the list above.
2. CAN H(J1939+) volts average
3. CAN L(J1939-) volts average
4. Total Busload(%) average

Match the information collected to the closest pattern in the J1939 Known Malfunctions Matrix. See Figure 6.

![[00k00249.png]]

Figure 6, Component Status and CAN Voltage Tab Malfunction Matching

1. Tab name
2. J1939 component communication status
3. Average statistic values
4. Corresponding pattern that has been matched

Troubleshoot the probable cause in association with the match found.

Follow the technical escalation process if there is no match identified from the J1939 Known Malfunctions Matrix.

Troubleshoot the J1939 components, OEM wiring harness, engine wiring harness, and all interconnects.

Once the issue has been confirmed, stop the recording.

**Repair Section:**

Repair or replace **only** the components that were found to be out of specification.

- Replace the SAE J1939 components. Refer to the appropriate procedure for each component. Reference the J1939 Component Name table.
- Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Section 19.
- Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
- Repair or replace the aftertreatment interface wiring harness. Refer to Procedure 019-477 in Section 19.

Refer to Conditions For Clearing The Fault Code in the Fault Code Overview section.

Short Circuit to Ground - Check

For shorted to ground cases, complete the following steps in order.

Select the Component Status and CAN Voltage tab.

Confirm that CAN H (J1939 +) Volts and CAN L (J1939 -) Volts is less than 1 VDC.

1. Disconnect the aftertreatment diesel exhaust fluid tank level/temperature/quality sensor.
2. Disconnect the aftertreatment interface harness. See Figure 7.
3. Jump the SAE J1939 Data Link (+) wire to the SAE J1939 Data Link (+) wire and SAE J1939 Data Link (-) wire to the SAE J1939 Data Link (-) wire on the female side of the OEM wiring harness that connects to the aftertreatment interface harness connector. Reference the corresponding wiring diagram for pinout identification.
4. Remove the jumper wires and connect the aftertreatment interface harness back. Disconnect the following components one at a time.
5. Disconnect the Intake NOx sensor.
6. Disconnect the OEM crossover connector.
7. Disconnect the turbocharger actuator.
8. Supply a reliable ground source to the Intake NOx sensor connector ground wire. Reference the corresponding wiring diagram for pinout identification.

![[14400069.png]]

Figure 7, Aftertreatment Interface Harness

**Repair Section:**

Repair or replace **only** the components that were found to be out of specification.

- Replace the SAE J1939 components. Refer to the appropriate procedure for each component. Reference the J1939 Component Name table.
- Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Section 19.
- Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
- Repair or replace the aftertreatment interface wiring harness. Refer to Procedure 019-477 in Section 19.

Short Circuit to Voltage - Check

For shorted to voltage cases, complete the following steps in order.

Select the Component Status and CAN Voltage tab.

Confirm that CAN H (J1939 +) Volts and CAN L (J1939 -) Volts is greater than 11 VDC.

1. Disconnect the aftertreatment diesel exhaust fluid tank level/temperature/quality sensor.
2. Disconnect the aftertreatment interface harness. See Figure 8.
3. Jump the SAE J1939 Data Link (+) wire to the SAE J1939 Data Link (+) wire and SAE J1939 Data Link (-) wire to the SAE J1939 Data Link (-) wire on the female side of the OEM wiring harness that connects to the aftertreatment interface harness connector. Reference the corresponding wiring diagram for pinout identification.
4. Remove the jumper wires and connect the aftertreatment interface harness back. Disconnect the following components one at a time.
5. Disconnect the Intake NOx sensor.
6. Disconnect the OEM crossover connector.
7. Disconnect the turbocharger actuator.
8. Supply a reliable voltage source to the Intake NOx sensor connector voltage wire. Reference the corresponding wiring diagram for pinout identification.

![[14400069.png]]

Figure 8, Aftertreatment Interface Harness

**Repair Section:**

Repair or replace **only** the components that were found to be out of specification.

- Replace the SAE J1939 components. Refer to the appropriate procedure for each component. Reference the J1939 Component Name table.
- Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Section 19.
- Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
- Repair or replace the aftertreatment interface wiring harness. Refer to Procedure 019-477 in Section 19.

Short Circuit Between Positive and Negative J1939 Data Link

For short circuit between positive and negative J1939 data link cases, complete the following steps in order.

Select the Component Status and CAN Voltage tab.

Confirm the following:

- CAN H (J1939+) Volts equals 2.5 +- 0.1 VDC
- CAN L (J1939 -) Volts equals 2.5 +- 0.1 VDC
- Total Busload (%) equals 0.

1. Unplug the aftertreatment diesel exhaust fluid tank level/temperature/quality sensor.
2. Unplug the aftertreatment interface harness. See Figure 9.
3. Jump the SAE J1939 Data Link (+) wire to the SAE J1939 Data Link (+) wire and SAE J1939 Data Link (-) wire to the SAE J1939 Data Link (-) wire on the female side of the OEM wiring harness that connects to the aftertreatment interface harness connector. Reference the corresponding wiring diagram for pinout identification.
4. Remove the jumper wires and connect the aftertreatment interface harness back. Disconnect the following components one at a time.
5. Unplug the OEM crossover connector.
6. Unplug the turbocharger actuator.
7. Unplug the Intake NOx sensor.

![[14400069.png]]

Figure 9, Aftertreatment Interface Harness

**Repair Section:**

Repair or replace **only** the components that were found to be out of specification.

- Replace the SAE J1939 components. Refer to the appropriate procedure for each component. Reference the J1939 Component Name table.
- Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Section 19.
- Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071 in Section 19.]]
- Repair or replace the aftertreatment interface wiring harness. Refer to Procedure 019-477 in Section 19.

| **J1939 Known Malfunctions Matrix** |  |  |  |  |
|---|---|---|---|---|
| **Components Not Communicating or not present** | **CAN High (J1939 +) Volts approximate** | **CAN Low (J1939 -) Volts approximate** | **Busload % approximate** | **Probable Cause** |
| Intake NOx Sensor Outlet NOx Sensor Exhaust Gas Temperature Sensor Particulate Matter Sensor Urea Quality Sensor | 2.36 – 2.45 | 2.3 – 2.37 | 9-12 | Aftertreatment relay signal/ground. Inspect relay or near OEM crossover connector. |
| Outlet NOx Sensor Exhaust Gas Temperature Sensor Particulate Matter Sensor | 2.42 – 2.48 | 2.33 – 2.42 | 10-15 | Open power wire. Inspect near aftertreatment interface harness. |
| Outlet NOx Sensor Exhaust Gas Temperature Sensor Particulate Matter Sensor | 3.33 – 3.91 | 3.19 – 3.67 | 10-15 | Open ground wire. Inspect near aftertreatment interface harness. |
| Outlet NOx Sensor Exhaust Gas Temperature Sensor Particulate Matter Sensor Urea Quality Sensor | 2.41 – 2.47 | 2.31 – 2.37 | 10-15 | Open J1939 (+) wire. Inspect OEM harness or near aftertreatment interface harness. |
| Outlet NOx Sensor Exhaust Gas Temperature Sensor Particulate Matter Sensor Urea Quality Sensor | 2.51 – 2.61 | 2.34 – 2.45 | 10-15 | Open J1939 (-) wire. Inspect OEM harness or near aftertreatment interface harness. |
| Turbocharger Actuator | 2.33 – 2.38 | 2.25 – 2.31 | 12-14 | Open power wire to actuator or actuator internal malfunction. Inspect from component connector to engine harness. |
| Turbocharger Actuator | 2.67 - 2.87 | 2.61 – 2.77 | 12-14 | Open ground wire to actuator. Inspect from component connector to engine harness. |
| Turbocharger Actuator | 1.73 – 1.93 | 1.61 – 1.75 | 12-14 | Open J1939 (+) wire to actuator. Inspect from component connector to engine harness. |
| Turbocharger Actuator | 3.07 – 3.22 | 2.97 – 3.18 | 12-14 | Open J1939 (–) wire to actuator. Inspect from component connector to engine harness. |
| Intake NOx Sensor | 2.42 – 2.48 | 2.32 – 2.41 | 13-15 | Open power wire to sensor or sensor internal malfunction. Inspect from component connector to OEM crossover connector. |
| Intake NOx Sensor | 2.78 – 2.95 | 2.52 – 2.83 | 13-15 | Open ground wire to sensor. Inspect from component connector to OEM crossover connector. |
| Intake NOx Sensor | 2.38 – 2.42 | 2.28 – 2.32 | 13-15 | Open J1939 (+) wire to sensor. Inspect sensor connector or engine harness. |
| Intake NOx Sensor | 2.51 – 2.62 | 2.42 – 2.52 | 13-15 | Open J1939 (-) wire to sensor. Inspect sensor connector or engine harness. |
| Outlet NOx Sensor | 2.43 – 2.5 | 2.32 – 2.4 | 13-15 | Open power wire to sensor or sensor internal malfunction. Inspect from sensor connector to aftertreatment interface harness. |
| Outlet NOx Sensor | 2.75 – 2.92 | 2.66 – 2.83 | 13-15 | Open ground wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Outlet NOx Sensor | 2.38 – 2.44 | 2.29 – 2.34 | 13-15 | Open J1939 (+) wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Outlet NOx Sensor | 2.58 – 2.67 | 2.46 – 2.56 | 13-15 | Open J1939 (-) wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Urea Quality Sensor | 2.46 – 2.53 | 2.37 – 2.46 | 14-16 | Open power wire to sensor or sensor internal malfunction. Inspect sensor connector or OEM harness. |
| Urea Quality Sensor | 2.86 – 3.15 | 2.7 – 2.97 | 14-16 | Open ground wire to sensor or internal malfunction. Inspect sensor connector or ground connection. |
| Urea Quality Sensor | 1.92 – 2.34 | 1.75 – 2.2 | 14-16 | Open J1939 (+) wire to sensor. Inspect from sensor connector to aftertreatment interface connector. |
| Urea Quality Sensor | 2.7 – 3.1 | 2.56 – 2.9 | 14-16 | Open J1939 (-) wire to sensor. Inspect from sensor connector to aftertreatment interface connector. |
| Exhaust Gas Temperature Sensor | 2.43 – 2.5 | 2.34 – 2.43 | 13-15 | Open power wire to sensor or sensor internal malfunction. Inspect from sensor connector to aftertreatment interface harness. |
| Exhaust Gas Temperature Sensor | 2.67 – 2.8 | 2.58 – 2.73 | 13-15 | Open ground wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Exhaust Gas Temperature Sensor | 1.84 – 2.2 | 1.71 – 2.09 | 13-15 | Open J1939 (+) wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Exhaust Gas Temperature Sensor | 2.87 – 3.19 | 2.77 – 3.05 | 13-15 | Open J1939 (-) wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Particulate Matter Sensor | 2.45 – 2.52 | 2.36 – 2.41 | 12-14 | Open power wire to sensor or sensor internal malfunction. Inspect from sensor connector to aftertreatment interface harness. |
| Particulate Matter Sensor | 2.7 – 2.86 | 2.59 – 2.74 | 12-14 | Open ground wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Particulate Matter Sensor | 2.27 – 2.34 | 2.21 – 2.28 | 12-14 | Open J1939 (+) wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |
| Particulate Matter Sensor | 2.62 – 2.7 | 2.53 – 2.61 | 12-14 | Open J1939 (-) wire to sensor. Inspect from sensor connector to aftertreatment interface harness. |

### Finishing Steps

- Analyze the data collected from the tool.
- Turn the keyswitch to the OFF position for 90 seconds.
- Do **not** turn the keyswitch OFF until confirming that all components are communicating and that J1939 voltage is at nominal 2.5 VDC (+- 0.1 DCV).
