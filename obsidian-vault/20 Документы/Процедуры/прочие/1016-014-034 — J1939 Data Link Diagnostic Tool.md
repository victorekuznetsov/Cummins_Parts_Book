---
type: "Процедура"
doc: "1016-014-034"
title_en: "J1939 Data Link Diagnostic Tool"
modified: "2025-09-08"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-014-034.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-014-034.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
---

# J1939 Data Link Diagnostic Tool

> [!abstract] Процедура · `1016-014-034`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2025-09-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-014-034.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-014-034.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- INLINE™ 7 Data Link Adapter Kit, Part Number 5299899 or 5572620
- Digital multimeter, Part Number 3164488
- Cummins® electronic service tool, or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The J1939 data link diagnostic tool is used to help identify J1939 data link performance issues.

The J1939 data link diagnostic tool is **only** compatible with a Cummins® INLINE™ 7 Data Link Adapter Kit, Part Number 5299899 or 5572620. Otherwise, troubleshooting the J1939 data link will need to be performed with a digital multimeter, Part Number 3164488.

Use the following procedure to continue with published troubleshooting if a Cummins® INLINE™ 7 Data Link Adapter Kit, Part Number 5299899 or 5572620, is **not** available. Refer to Procedure 019-417 in Section 19.

Using the J1939 data link diagnostic tool will disconnect all connections to the Engine Control Module (ECM).

If the recommended Cummins® electronic service tool, or equivalent, is needed, the J1939 data link diagnostic tool **must** be disconnected from the ECM.

The J1939 data link diagnostic tool can be used while engine is on and can be stopped at any time.

Do **not** drive the vehicle while performing the J1939 data link diagnostic tool unless directed by published troubleshooting.

The tool is located in the electronic service tool under the Tools tab in the upper toolbar. See Figure 1. The J1939 data link diagnostic tool is previously known as the Controller Area Network (CAN) bus diagnostics tool.

![[14k00033.png]]

Figure 1, Tools Tab in Upper Toolbar of Electronic Service Tool

When opening the J1939 data link diagnostic tool, a Settings tab will appear that will contain connection settings options and a file location directory to save logs after recording. See Figure 2.

![[00u00098.png]]

Figure 2, J1939 Data Link Diagnostic Tool Settings Tab

1. Tab selections
2. Connection settings options
3. Recording log file location.

The J1939 data link diagnostic tool can also record logs and can be played back while being disconnected from the ECM. See Figure 3.

![[00u00099.png]]

Figure 3, Recordings Tab

1. Recordings tab
2. Available recordings.

The J1939 data link diagnostic tool will **not** start or will be aborted in the following situations:

- A diagnostic test is running.
- An INLINE™ 7 data link adapter is **not** used.
- The INLINE™ 7 data link adapter is **not** connected to the three-pin service connector.
- Low battery voltage.

### Preparatory Steps

Do **not** use the J1939 data link diagnostic tool with active fault codes, unless guided to do so by a service procedure and/or published troubleshooting.

Prior to using the J1939 data link diagnostic tool, complete the following steps:

1. Connect the INLINE™ 7 data link adapter to the three-pin service connector.
2. Connect the alligator clips of the INLINE™ 7 data link adapter to a reliable voltage source.

### Tool Usage

To begin using the J1939 data link diagnostic tool, complete the following steps:

- Turn the keyswitch to the OFF position.
- Connect the INLINE™ 7 data link adapter to the three-pin service connector and connect the alligator clips of the INLINE™ 7 data link adapter to a reliable voltage source.
- Open the J1939 data link diagnostic tool found in the Tools tab.
- Select the appropriate connection settings in the Settings tab.
- Select the Connect button.
- Select the Record button.
- Turn the keyswitch to the ON position.
- Verify the vehicle and surrounding area are monitored during the use of the J1939 data link diagnostic tool. If any unsafe condition occurs, key OFF or turn off the engine immediately.

See the Analyzing the Data section of this procedure for repair actions for the results.

If the connection between the J1939 data link diagnostic tool and the ECM is lost for any reason, a pop-up message will appear. In this case, the J1939 data link diagnostic tool will automatically disconnect. The J1939 data link diagnostic tool can be restarted after clicking on the Connect button, and then turning the keyswitch to the ON position.

### Analyzing the Data

Inactive Fault Code Troubleshooting

For inactive fault code troubleshooting, complete the following steps in order:

Select the Disconnect button on the J1939 data link diagnostic tool.

Turn keyswitch OFF.

Disconnect each battery from each other and perform an individual load test on each battery.

See Original Equipment Manufacturer (OEM) specifications for acceptable thresholds for 12 VDC and 24 VDC systems. If the voltages are **not** within the OEM specification, charge or replace the batteries.

Inspect ECM battery supply fuses, aftertreatment battery supply fuses, and battery supply fuses for damage, corrosion, or loose connections.

Use the J1939 data link diagnostic tool to connect by pressing the Connect button and then press the Record button.

Start the engine and bring the engine to operating temperature (above 70°C \[ 158°F \]).

Perform a road test.

When road testing is complete, stop recording and press the Disconnect button.

Select the Recordings tab and select the log by pressing the Play button.

Select the J1939 Component Summary tab.

Ignore the component “Retarder - Engine”.

Collect the names of the components with a Claim Address Timestamp Delta (sec) value of 30 seconds or more. See Figure 4.

![[00k00247.png]]

Figure 4, J1939 Component Summary in Playback Mode

1. Tab name
2. Components with Claim Address TS Delta under 30 seconds
3. Components with Claim Address TS Delta over 30 seconds.

If no J1939 components has got a Claim Address TS Delta (sec) value of 30 seconds or more, proceed to the Log Navigator (Component Comm) tab.

Search for any spikes greater than 1000 milliseconds in the Log Navigator (Component Comm) tab. See Figure 5.

![[00u00100.png]]

Figure 5, Log Navigator (Component Comm) in Playback Mode

1. Tab name
2. First pair of spikes/dips
3. Second pair of spikes/dips
4. 1000 milliseconds tick mark.

Spikes greater than 1000 milliseconds represent loss of communication.

Troubleshoot the J1939 components with spikes greater than 1000 milliseconds in the Log Navigator (Component Comm) tab.

Below is a table that shows which circuit to troubleshoot for those J1939 components with spikes.

| Components with Spikes Greater Than 1000 Milliseconds and Claim Address TS Delta (sec) Value of | Circuit to Troubleshoot |
|---|---|
| Less than 30 seconds | J1939 data link circuit |
| More than 30 seconds | Power and ground circuit |

See the appropriate wiring diagram for the engine being worked on to troubleshoot.

Active Fault Code Troubleshooting

For single and multiple active fault code troubleshooting, complete the following steps in order:

Select the Component Status and CAN Voltage tab.

Ignore the component “Retarder - Engine”.

Use the list below to compare which components are **not** present in the Component Status and CAN Voltage tab.

- ECM 1
- Intake NOx sensor
- Outlet NOx sensor
- Exhaust gas temperature sensor
- Urea quality sensor.

Obtain the following information from the Component Status and CAN Voltage Tab.

1. The names of the components that are **not** present compared to the list above
2. CAN H (J1939+) voltage average
3. CAN L (J1939-) voltage average
4. Total busload(%) average.

Match the information collected to the closest pattern in the J1939 Known Malfunctions Matrix. See Figure 6.

![[00k00249.png]]

Figure 6, Component Status and CAN Voltage Tab Malfunction Matching

1. Tab name
2. J1939 component communication status
3. Average statistic values
4. Corresponding pattern that has been matched.

Troubleshoot the probable cause in association with the match found.

Follow the technical escalation process if no match is identified from the J1939 Known Malfunctions Matrix.

Troubleshoot the J1939 components, OEM wiring harness, engine wiring harness, and all interconnects.

Once the issue has been confirmed, stop the recording.

### Finishing Steps

- Analyze the data collected from the tool.
- Turn the keyswitch to the OFF position for 90 seconds.
- Do **not** turn the keyswitch off until confirming that all components are communicating and that J1939 voltage is at nominal 2.5 VDC (±0.1 VDC).
