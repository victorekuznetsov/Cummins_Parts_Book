---
aliases:
  - "Останов: давление газа регулятора"
type: "Процедура"
doc: "330-t02-1007"
title_en: "Sd RegGasPress"
title_ru: "Останов: давление газа регулятора"
modified: "2017-03-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
---

# Sd RegGasPress
**Останов: давление газа регулятора**

> [!abstract] Процедура · `330-t02-1007`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2017-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1007.pdf)

Printable Version

### Symptoms

- All gas flow will stop or the dual fuel control module will be prevented from entering dual fuel mode.

### How To Use This Tree

This tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

**Circuit Description:**

The gas train is equipped with a high-pressure switch. If the switch indicates a high-pressure condition after the Cummins® regulator, the input activation stops or prevents normal operation of the dual fuel system. The switch is a maintained or latching device, meaning if the condition occurs, the device **must** be manually reset before the signal will be restored to the dual fuel control module input.

**Conditions for Running the Diagnostics:**

Any time the system is operating and is substituting gas and the pressure switch indicates greater than accepted pressure for longer than a fixed delay, the system will indicate this message and assert protection.

**Conditions for Activating the Fault Message:**

Binary input 3 (BI-3) is open to battery negative when running in dual fuel mode for longer than the delay (60 seconds).

Binary input 3 (BI-3) is open to battery negative when **not** in dual fuel mode for longer than 0.5 second.

**Conditions for Clearing the Fault Automatically:**

None.

**Conditions for Clearing the Fault Codes Manually:**

The gas pressure is restored below the set-point limit of the switch. The mechanical switch has been reset and the fault reset is depressed locally or via the software.

### Shoptalk

The protection element is to protect against excessive gas delivery pressure to the engine.

When the control module asserts the protection, the most probable cause is delivery gas pressure has spiked over the limit. The controller will not respond to the fault for 60 seconds. This can cause the operator to believe the fault occurred later than actual or the condition did not occur if monitoring pressure only as the mechanical switch is of a latching type. Inspect the switch to see if it 'tripped' before detailed troubleshooting of the circuit. A momentary spike will still cause the shutdown. If the input is open when the controller is powered ON or opens when in diesel only mode, it will cause the fault.

Possible causes include:

- Excessive gas pressure above the switch pressure limit

- Malfunctioning gas pressure switch

- Malfunctioning contacts on the gas pressure switch

- Malfunctioning or loose wiring connections at the dual fuel control module for battery negative or binary input (BI-3)

- Malfunctioning or loose wiring connections at gas pressure switch contacts

- Malfunctioning dual fuel control module

- Incorrectly installed or no orifice at switch.

| Code of Message | Reason | Effect |
|---|---|---|
| Sd RegGasPress | BI-3 open in reference to battery negative. Circuit requires a grounded input for normal operation. | Dual fuel control module will not allow gas operations. Dual fuel control module will stop gas flow. |

The following table provides reference information for this fault tree.

| Table 1 |  |
|---|---|
| Fault Occurs When | Suspected Casue |
| Input changes during starting - low battery voltage to control module | Check voltage drop, loose wiring connections to dual fuel control module at battery positive and negative connections. |
| Input changes intermittently or randomly at low idle or very high load - vibration | Loose wiring, malfunctioning connectors, damaged pins |
| Input changes when disturbing wires or connectors | Loose wiring, malfunctioning connectors, damaged pins |
| Multiple binary input faults | System grounding, loose battery negative connections, malfunctioning batteries, improper wiring connections |
| Fault occurs as soon as BO-1 and 7 activate | Suspect actual gas pressure spike occurs due to gas regulator malfunction or excessive delivery pressure |
| Fault occurs during load shifts of approximately 25% power | Gas regulator transient (shift) response, gas delivery stability issues under load shift. Malfunctioning regulator or pressure limiting device |
| Sd fault for 'LowGasPressIn' occurs while testing for Sd RegGasPress | Gas regulator transient (shift) response, gas delivery stability issues under load shift. Malfunctioning regulator or pressure limiting device |

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Validate the fault message. |  |
|  | **STEP 1A.** Check for 'Active' fault message. | Control module in fault condition? |
|  | **STEP 1B.** Check for 'Not Active' fault message. | Control module has occurrences for Sd RegGasPres? |
|  | **STEP 1C.** Reset the fault. | Fault message cleared? |
| STEP 2. | Reset the high-pressure switch. |  |
|  | **STEP 2A.** Reset the high-pressure switch. | Above actions cleared fault? |
| STEP 3. | Check the high fuel pressure switch and circuit. |  |
|  | **STEP 3A.** Inspect the high fuel pressure switch and connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the switch. | Binary Input 3 displays a 1 using InteliMonitor? |
|  | **STEP 3C.** Check the wiring harness. | Binary Input 3 displays a 1 using InteliMonitor? |
|  | **STEP 3D.** Test the binary input response. | Binary Input 3 displays a 1 using InteliMonitor? |
| STEP 4. | Check the high-pressure fuel system. |  |
|  | **STEP 4A.** Check for a high-pressure spike. | Signs of a high-pressure spike identified? |
|  | **STEP 4B.** Check the high-pressure switch orifice. | Orifice the correct size and free of damage? |
|  | **STEP 4C.** Check the fuel pressure regulator. | Fuel pressure regulator within specifications? |
| STEP 5. | Test the system using WinScope PC tool. |  |
|  | **STEP 5A.** Test inputs using WinScope. | Any occurrences of BI-3 becoming zero using data collected and InteliMonitor? |
| STEP 6. | Reset the alarm. |  |
|  | **STEP 6A.** Reset the alarm. | Dual fuel control module in shutdown condition for Sd RegGasPress? |

### STEP 1. Validate the fault message.

#### STEP 1A. Check for 'Active' fault message.

| **Conditions:** Power ON duel fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the local display panel for a fault message. Navigate to the fault display screen. | Control module in fault condition? **YES** | 1C |
| Control module in fault condition? **NO** | 1B |  |

#### STEP 1B. Check for 'Not Active' fault message.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect to the dual fuel control panel. Use InteliMonitor. Save a copy of the control module configuration file (archive file) on the local PC. Access the history shortcut. Check for occurrences of the message Sd RegGasPress. Check for other shutdown messages occurring at or near the time of the Sd RegGasPress. Check for other shutdown messages occurring at or near the time of the Sd RegGasPress. If other shutdown messages for binary inputs occur at the same time, see the procedure for ground and ground loop tests. | Control module has occurrences for Sd RegGasPress? **YES** | 1C |
| Control module has occurrences for Sd RegGasPress? **NO** | No repair. |  |

#### STEP 1C. Reset the fault.

| **Conditions:** Power ON duel fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect to the dual fuel panel. Use InteliMonitor. Save a copy of the configuration file (archive file) on the local PC. Reset the fault from the control module or from the software InteliMonitor. | Fault message cleared? **YES** | 5A |
| Fault message cleared? **NO** | 2A |  |

### STEP 2. Reset the high-pressure switch.

#### STEP 2A. Reset the high-pressure switch.

| **Conditions:** Power ON dual fuel control module. Make sure the dual fuel control module is in AUTO mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Press the rest button on the high-pressure switch. After pressing the reset button on switch, go to the panel and reset the fault. | Above actions cleared fault? **YES** | 4A |
| Above actions cleared fault? **NO** | 3A |  |

### STEP 3. Check the high fuel pressure switch and circuit.

#### STEP 3A. Inspect the high fuel pressure switch and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the high fuel pressure switch connector from the dual fuel harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the dual fuel harness and high fuel pressure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the high fuel pressure switch or harness connector. Check all harnesses connected in series. Clean the connector and pins. Replace the damaged section of harness or damaged switch. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the switch. Refer to Procedure 019-580 in Section 19. | 5A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the switch.

| **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the high fuel pressure switch connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | Binary Input 3 displays a 1 using InteliMonitor? **YESRepair:** The high-pressure switch has malfunctioned. Replace the high pressure switch. Refer to Procedure 019-580 in Section 19. | 5A |
| Binary Input 3 displays a 1 using InteliMonitor? **NO** | 3C |  |

#### STEP 3C. Check the wiring harness.

| **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the wiring harness from the C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | Binary Input 3 displays a 1 using InteliMonitor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 5A |
| Binary Input 3 displays a 1 using InteliMonitor? **NO** | 3D |  |

#### STEP 3D. Test the binary input response.

| **Conditions:** Engine not operating. Power ON dual fuel control module. Place dual fuel control module in OFF mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Make a temporary connection from the panel ground stud to the binary input terminal BI-3. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | Binary Input 3 displays a 1 using InteliMonitor? **YESRepair:** Repair or replace the wiring from C3-C to the control module BI-3 (wire 4003). | 6A |
| Binary Input 3 displays a 1 using InteliMonitor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. | 6A |  |

### STEP 4. Check the high-pressure fuel system.

#### STEP 4A. Check for a high-pressure spike.

| **Conditions:** Engine not operating. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the original equipment manufacturer (OEM) side of the fuel system is operating correctly. See equipment manufacturer service information. Review the fault history in InteliMonitor to determine if there are any faults that would cause a high-pressure spike. | Signs of a high-pressure spike identified? **YESRepair:** Correct the source of the high-pressure spike. See equipment manufacturer service information. | 6A |
| Signs of a high-pressure spike identified? **NO** | 4B |  |

#### STEP 4B. Check the high-pressure switch orifice.

| **Conditions:** Engine not operating. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove the high-pressure switch. Refer to Procedure 019-580 in Section 19. Remove the hex orifice fitting from the pressure port on the gas outlet flange. | Orifice the correct size and free of damage? **YES** | 4C |
| Orifice the correct size and free of damage? **NORepair:** Install the correct hex orifice. Refer to Procedure 019-580 in Section 19. | 6A |  |

#### STEP 4C. Check the fuel pressure regulator.

| **Conditions:** Engine operating in dual fuel mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the fuel pressure regulator is adjusted and operating correctly. Refer to Procedure 005-245 in Section 5. | Fuel pressure within specifications? **YES** | 5A |
| Fuel pressure within specifications? **NORepair:** Adjust the pressure regulator to bring the pressure within specifications. Refer to Procedure 005-245 in Section 5. If the pressure cannot be brought into specifications, a malfunctioning fuel pressure regulator has been detected. Replace the fuel pressure regulator. Refer to Procedure 005-042 in Section 5. | 6A |  |

### STEP 5. Test the system using WinScope PC tool.

#### STEP 5A. Test inputs using WinScope.

| **Conditions:** Engine not operating. Connect PC using WinScope to dual fuel controller. Switch control panel power ON. Place dual fuel control module in OFF mode. Load is available to be applied up to 85 percent nominal, in steps of 10 to 15 percent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Select the item to monitor in the channel selections, specifically in this case monitor BI-3, analog control unit battery voltage, gas regulation value 'Engine Power' and 'G/D Ratio'. Set the scope time period to capture at 150 mS and begin logging. 1. Start the engine and observe that the input for BI-3 remains at 1 during the crank, start, and run condition. This is to locate faults caused by vibration or unreasonable drops in battery voltage supply to the control during normal operation. 2. Continue recording the binary data and attempt to create the fault by gently moving wires and the wiring harness inside the panel and at the connectors, external to the panel, to locate intermittent faults or loose connections. 3. If **no** faults occur in Steps 1 or 2, slowly add load to the engine in steps. Allow the engine and load to stabilize at each step for **no** less than 5 minutes. Continue logging data under load until either the fault is captured or 85 percent rated engine power has been applied. | Any occurrences of BI-3 becoming zero using data collected and InteliMonitor? **YESRepair:** Use results from the specified steps to determine the cause or reasonable steps and repair as needed. Reference Table 2 in the Shoptalk section. | 6A |
| Any occurrences of BI-3 becoming zero using data collected and InteliMonitor? **NO** | 6A |  |

### STEP 6. Reset the alarm.

#### STEP 6A. Reset the alarm.

| **Conditions:** Engine not operating. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect power from the control panel. Wait 30 seconds. Restore DC power connection. Confirm the fault for Sd RegGasPress is not present or active. | Dual fuel control module in shutdown condition for Sd RegGasPress? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
| Dual fuel control module in shutdown condition for Sd RegGasPress? **NO** | Repair complete. |  |
