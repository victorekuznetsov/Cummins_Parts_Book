---
aliases:
  - "Останов: низкое давление газа на входе"
type: "Процедура"
doc: "330-t02-1004"
title_en: "Sd LowGasPressIn"
title_ru: "Останов: низкое давление газа на входе"
modified: "2017-03-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
---

# Sd LowGasPressIn
**Останов: низкое давление газа на входе**

> [!abstract] Процедура · `330-t02-1004`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2017-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1004.pdf)

Printable Version

### Symptoms

All gas flow will stop and the dual fuel control module will be prevented from entering dual fuel mode.

### How To Use This Tree

**Circuit Description:**

The gas train is equipped with a low inlet pressure switch. If the switch indicates a low-pressure supply condition, the input activation stops or prevents the normal operation of the dual fuel system.

**Conditions for Running the Diagnostics:**

Any time the switch indicates a lower than accepted supply pressure and the dual fuel control module is powered ON, the system will indicate this message and assert protection.

**Conditions for Activating the Fault Message:**

Dual fuel control module is powered on and the binary input labeled BI-2 is open to battery negative.

**Actions Taken When the Fault is Active:**

Dual fuel operation will be prevented.

All gas flow will stop if system is operating in dual fuel mode.

**Conditions for Clearing the Fault Codes Automatically:**

No conditions for clearing fault automatically.

**Conditions for Clearing the Fault Codes Manually:**

The gas pressure is restored above the set point limit of the switch and the fault reset is depressed locally or via the software.

### Shoptalk

The protection element is intended to restrict gas delivery for low fuel supply pressure conditions.

When the control dual fuel module has an open circuit for BI-2, it asserts the protection.

Possible causes include:

- Gas pressure below switch set point

- Malfunctioned gas pressure switch

- Damaged contacts on gas pressure switch

- Damaged or loose wiring connections at dual fuel control module for battery negative or BI-2

- Damaged or loose wiring connections at gas pressure switch contacts

- Malfunctioned dual fuel control module

- Gas supply volume is not great enough to maintain sufficient pressures at high load.

| Table 1: Dual Fuel Control Module - Open Circuit Condition Exists |  |  |
|---|---|---|
| Codes or Messages | Reason | Effect |
| **SD LowGasPressIn** | BI-2 is open in reference to battery negative. Circuit requires a grounded input for normal operation. | Dual fuel control module will **not** allow gas operations. Dual fuel control module will stop gas flow. |

| Table 2 |  |
|---|---|
| Fault occurs when: | Possible cause(s): |
| Input changes during starting/low battery voltage to control module | Check voltage drop, loose wiring connections to dual fuel control module at battery positive and negative connections |
| Input changes intermittently or randomly at low idle or high load condition - vibration | Loose wiring, damaged connectors, or damaged pins |
| Input changes when disturbing wires or connectors | Loose wiring, damaged connectors, or damaged pins |
| Multiple binary input faults | System grounding, loose battery negative connections, malfunctioned batteries, or improper wiring connections. |
| Fault occurs **only** under moderate to heavy load conditions | Suspect actual gas pressure is dropping below switch protection level. Test with actual gas pressure recording using transducer or gauge(s) as needed to isolate. |

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Validate the fault message. |  |
|  | **STEP 1A.** Check for 'Active' fault message. | Fault active? |
|  | **STEP 1B.** Rest the fault. | Fault message cleared? |
|  | **STEP 1C.** Check for 'Not Active' fault message. | Control module has occurrences for SD LowGasPressIn? |
| STEP 2. | Verify correct fuel pressure. |  |
|  | **STEP 2A.** Check the pressure gauge reading. | Fuel pressure within specifications? |
| STEP 3. | Check the low fuel pressure switch and circuit. |  |
|  | **STEP 3A.** Inspect the low fuel pressure switch and connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the switch for correct operation. | Binary Input 2 displays a 1 using InteliMonitor? |
|  | **STEP 3C.** Check the wiring harness. | Binary Input 2 displays a 1 using InteliMonitor? |
| STEP 4. | Check the binary inputs. |  |
|  | **STEP 4A.** Test the binary input response. | Binary Input 2 displays a 1 using InteliMonitor? |
| STEP 5. | Test the system using WinScope PC tool. |  |
|  | **STEP 5A.** Test inputs using WinScope. | Any occurrences of BI-2 becoming zero using data collected and InteliMonitor? |
| STEP 6. | Restart the control panel. |  |
|  | **STEP 6A.** Restart the controller. | Dual fuel control module in shutdown condition for SD LowGasPressIn? |

### STEP 1. Validate the fault message.

#### STEP 1A. Check for 'Active' fault message.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel for an active fault message. Navigate to fault display screen. | Fault active? **YES** | 2A |
| Fault active? **NO** | 1B |  |

#### STEP 1B. Reset the fault.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect to the dual fuel panel. Use InteliMonitor. Save a copy of the configuration file (archive file) on the local PC. Reset the fault from the control module or from the software InteliMonitor. | Fault message cleared? **YES** | 1C |
| Fault message cleared? **NO** | Contact a Cummins® Authorized Repair Location for repair assistance. |  |

#### STEP 1C. Check for 'Not Active' fault message.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect to the dual fuel control panel. Use InteliMonitor. Save a copy of the control module configuration file (archive file) on the local PC. Access the history shortcut. Check for occurrences of the message SD LowGasPressIn. Check for other shutdown messages occurring at or near the time of the SD LowGasPressIn. Check for other shutdown messages occurring at or near the time of the SD LowGasPressIn. If other shutdown messages for binary inputs occur at the same time, see the procedure for ground and ground loop tests. | Control module has occurrences for SD LowGasPressIn? **YES** | 5A |
| Control module has occurrences for SD LowGasPressIn? **NO** | No repair. |  |

### STEP 2. Verify correct fuel pressure.

#### STEP 2A. Check the pressure gauge reading.

| **Conditions:** Power ON dual fuel control module. Make sure the dual fuel control module is in AUTO mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the reading on the pressure gauge mounted after the fuel filter. If gas pressure is less than the low pressure switch setting of 13.78 kPa \[2 psi\], the low gas pressure switch connector is unplugged, or the switch is damaged, the fault will be active and will not reset. | Fuel pressure within specifications? **YES** | 3A |
| Fuel pressure within specifications? **NORepair:** Verify the cause of the low fuel pressure. Inspect the fuel filter on the gas train. Refer to Procedure 005-246 in Section 5. If the fuel filter is functioning properly, inspect the upstream fuel system components. See equipment manufacturer service information. | 6A |  |

### STEP 3. Check the low fuel pressure switch and circuit.

#### STEP 3A. Inspect the low fuel pressure switch and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the low fuel pressure switch connector from the dual fuel harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the dual fuel harness and low fuel pressure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the low fuel pressure switch or harness connector. Check all harnesses connected in series. Clean the connector and pins. Replace the damage section of harness of damaged sensor. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the sensor. Refer to Procedure 019-579 in Section 19. | 6A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the switch for correct operation.

| **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the low fuel pressure switch connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | Binary Input 2 displays a 1 using InteliMonitor? **YESRepair:** Check the dial setting on the switch. Verify the switch is set to 55 in-H 2 O. If the switch is set at 55 in-H 2 O, the low pressure switch has malfunctioned. Replace the low pressure switch. Refer to Procedure 019-579 in Section 19. | 6A |
| Binary Input 2 displays a 1 using InteliMonitor? **NO** | 3C |  |

#### STEP 3C. Check the wiring harness.

| **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the wiring harness from the C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | Binary Input 2 displays a 1 using InteliMonitor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 6A |
| Binary Input 2 displays a 1 using InteliMonitor? **NO** | 4A |  |

### STEP 4. Check the binary inputs.

#### STEP 4A. Test the binary input response.

| **Conditions:** Engine not operating. Power ON dual fuel control module. Place dual fuel control module in OFF mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Make a temporary connection from the panel ground stud to the binary input terminal BI-2. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | Binary Input 2 displays a 1 using InteliMonitor? **YESRepair:** Repair or replace the wiring from C3-A to the control module BI-2 (wire 4002). | 6A |
| Binary Input 2 displays a 1 using InteliMonitor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. | 6A |  |

### STEP 5. Test the system using WinScope PC tool.

#### STEP 5A. Test inputs using WinScope.

| **Conditions:** Engine not operating. Connect PC using WinScope to dual fuel controller. Switch control panel power ON. Place dual fuel control module in OFF mode. Load is available to be applied up to 85 percent nominal, in steps of 10 to 15 percent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Select the item to monitor in the channel selections, specifically in this case monitor BI-2, analog control unit battery voltage, gas regulation value 'Engine Power' and 'G/S Ratio'. Set the scope time period to capture at 150 mS and begin logging. 1. Access the harness connector for the inlet gas pressure switch (C18-1) on the gas train. Disconnect and reconnect the connector to verify the control responds to the changes, and WinScope indicates the change occurred. 2. Start the engine and observe that the input for BI-2 remains at 1 during the crank, start, and run condition. This is to locate faults caused by vibration or unreasonable drops in battery voltage supply to the control during normal operation. 3. Continue recording the binary data and attempt to create the fault by gently moving wires and the wiring harness inside the panel and at the connectors, external to the panel, to locate intermittent faults or loose connections. 4. If **no** faults occur in Steps 1-3, slowly add load to the engine in steps. Allow the engine and load to stabilize at each step for **no** less than 5 minutes. Continue logging data under load until either the fault is captured or 85 percent rated engine power has been applied. | Any occurrences of BI-2 becoming zero using data collected and InteliMonitor? **YESRepair:** Use results from the specified steps to determine the cause or reasonable steps and repair as needed. Reference Table 2 in the Shoptalk section. | 6A |
| Any occurrences of BI-2 becoming zero using data collected and InteliMonitor? **NO** | 6A |  |

### STEP 6. Restart the control panel.

#### STEP 6A. Restart the controller.

| **Conditions:** Engine not operating. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect power from the control panel. Wait 30 seconds. Restore DC power connection. Confirm the fault for SD LowGasPressIn is not present or active. | Dual fuel control module in shutdown condition for SD LowGasPressIn? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
| Dual fuel control module in shutdown condition for SD LowGasPressIn? **NO** | Repair complete. |  |
