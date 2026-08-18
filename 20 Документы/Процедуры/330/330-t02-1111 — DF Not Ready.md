---
aliases:
  - "Газодизельный режим не готов"
type: "Процедура"
doc: "330-t02-1111"
title_en: "DF Not Ready"
title_ru: "Газодизельный режим не готов"
modified: "2024-08-06"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
---

# DF Not Ready
**Газодизельный режим не готов**

> [!abstract] Процедура · `330-t02-1111`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2024-08-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1111.pdf)

Printable Version

### Symptoms

Unit will **not** go into dual fuel mode.

### How To Use This Tree

This tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending up the symptom.

LegCtrl-

**Circuit Description**

DF **Not** Ready is a STATUS message to indicate one of the conditions necessary for Dual Fuel operation has **not** been satisfied. In this state, the panel will **not** allow Gas operation.

**Conditions for Running the Diagnostics**

Anytime the control module is powered ON.

**Conditions for Activating the Status Message:**

See possible causes in the Shop Talk section.

**Conditions for Clearing the Status Message Automatically:**

Satisfy all conditions to start dual fuel operation.

**Conditions for Clearing the Status Message Manually:**

None.

NewCtrl-

**Circuit Description**

DF **Not** Ready message is displayed on the Newctr and InteliMonitor alarm list.

**Conditions for Running the Diagnostics**

Anytime the control module is powered ON.

**Conditions for Activating the Status Message:**

See possible causes in the Shop Talk section.

**Conditions for Clearing the Status Message Automatically:**

Satisfy all conditions to start dual fuel operation.

**Conditions for Clearing the Status Message Manually:**

### Shoptalk

Alarm is indicated when system is **not** ready for dual fuel operation due to several conditions (described in possible causes). Once all conditions are met, dual fuel operation will be enabled automatically.

In case any other alarm/s is active at the same time as DF **Not** Ready, troubleshoot that alarm/s first.

If NewCtrl: Information in InteliMonitor Tool - PLC Monitor - Sheet 5 can be used along with the troubleshooting tree.

If the input on a particular error block has a white dot on the input and the line to the input is black you need to go to the troubleshooting step associated with that input. If there is **only** a black dot on the input and the input line is blue then go to the troubleshooting step associated with that input.

LegCtrl possible causes include:

- Transmission position

- Incorrect engine speed

- Hydraulic pump power outside of the operating range

- Coolant temperature is below the minimum set point for operation

- Remote Stop is engaged

- Operator Shutdown is engaged

- Remote Operator Shutdown is engaged

- Diesel engine intake manifold temperature outside of the calibration range

- Incorrect panel shutdown.

NewCtrl possible causes include:

- Engine speed **not** within 1570-1980 rpm

- Transmission in neutral (if equipped with electronic transmission)

- PLC Setpoint UseTransGear incorrectly set

- Low inlet gas pressure

- LowGasPressIn Alarm has occurred greater than 10 times

- Coolant temperature \< 71°C

- Engine overspeed greater than 2100 rpm

- Engine load too high for Dual fuel operation (greater than 94% of Rated power)

- Engine load **not** within set limit (2250 hp: 373-1578 kW, 2500 hp: 373-1748 kW)

- Any Fls (Sensor Fail) Alarms

- IMT (Intake Manifold Temperatures) **not** within set limit (43°C to 82°C)

- Any Operator or Remote SD

- Number of Knocking events exceeded set limit (100 times per day/power cycle)

| Code of Message | Reason | Effect |
|---|---|---|
| DF **Not** Ready | Conditions exist preventing dual fuel operation. | The control panel will prevent the unit from running in dual fuel mode. |

![[05m00181.png]]

Figure 1, Legacy controller (LegCtrl, shown left) and new controller (NewCtrl, shown right)

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Determine ComAp configuration. |  |
|  | **STEP 1A.** Determine configuration | Pump equipped with LegCtrl? |
| STEP 2. | Validate the fault message. |  |
|  | **STEP 2A.** Fault message is active. | Control module in fault condition with DF **Not** Ready? |
|  | **STEP 2B.** Restart the control panel. | DF **Not** Ready displayed on the control panel display after restart? |
| STEP 3. | Verify hydraulic pump power. |  |
|  | **STEP 3A.** Verify hydraulic pump power. | Hydraulic pump power greater than 373 kW but less than 1578 kW for 2250 HP engines or 1748 kW for 2500 HP engines? |
| STEP 4. | Verify intake manifold temperature. |  |
|  | **STEP 4A.** Verify intake manifold temperature. | Intake manifold temperature between 43°C \[ 110°F \] and 82°C \[ 180°F \]? |
| STEP 5. | Verify engine speed. |  |
|  | **STEP 5A.** Verify engine speed. | Engine speed between 1400 and 2000 rpm for longer than 60 seconds? |
| STEP 6. | Verify coolant temperature. |  |
|  | **STEP 6A.** Verify coolant temperature. | Coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds? |
| STEP 7. | Check emergency stops and remote stops. |  |
|  | **STEP 7A.** Operate shutdown engaged. | Operator shutdown engaged? |
|  | **STEP 7B.** Remote Operator Shutdown is engaged. | Remote operator shutdown engaged? |
|  | **STEP 7C.** Remote Stop is engaged. | Remote stop engaged? |
| STEP 8. | Check transmission gear selection. |  |
|  | **STEP 8A.** Check transmission gear selection. | Transmission in gear for longer than 60 seconds? |
| STEP 9. | Check for errors. |  |
|  | **STEP 9A.** Check for Cummins® ECM Fault Codes. | Engine ECM indicates fault codes? |
|  | **STEP 9B.** Check for fault messages. | DF **Not** Ready alarm code present? |
|  | **STEP 9C.** Check for fault messages. | Alarm codes other than DF **Not** Ready present? |
| STEP 10. | Verify engine speed. |  |
|  | **STEP 10A.** Verify engine speed. | Engine speed between 1570-1980 rpm for longer than 60 seconds? |
| STEP 11. | Check transmission gear selection. |  |
|  | **STEP 11A.** Check transmission gear selection. | TransReqGear greater than 0 for longer than 60 seconds? |
| STEP 12. | Incorrect adjustable parameter setting. |  |
|  | **STEP 12A.** Check transmission type selection. | UseTransGear matches transmission type? |
| STEP 13. | Verify intake manifold temperature. |  |
|  | **STEP 13A.** Verify intake manifold temperature. | Intake manifold temperature between 43°C \[ 110°F \] and 82°C \[ 180°F \]? |
| STEP 14. | Verify engine coolant temperature. |  |
|  | **STEP 14A.** Verify engine coolant temperature. | Coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds? |
| STEP 15. | Engine load **not** within set limit. |  |
|  | **STEP 15A.** Verify engine load limit type. | Pump using Real Power message via J1939? |
|  | **STEP 15B.** Verify Real Power transmitted value (J1939). | Do J1939 transmitted power limits correspond with pump power rating? |
|  | **STEP 15C.** Verify engine load limits (Converted). | Do Power Limits correspond with engine power rating? |

### STEP 1. Determine ComAp configuration.

#### STEP 1A. Determine ComAp configuration.

| **Conditions:** Verify ComAp control panel configuration. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine which ComAp control panel is installed on the pump. Refer to panel identification images in alarm code overview. | Pump equipped with LegCtrl? **YES** | 2A |
| Pump equipped with LegCtrl? **NO** | 9A |  |

### STEP 2. Validate the fault message.

#### STEP 2A. Fault message is active.

| **Conditions:** Turn dual fuel control module ON. Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the local display panel for a fault message. Navigate to the fault from the display screen. | Control module in fault condition with DF **Not** Ready? **YES** | 2B |
| Control module in fault condition with DF **Not** Ready? **NORepair:** No troubleshooting needed. | Repair complete |  |

#### STEP 2B. Restart the control panel.

| **Conditions:** Turn control panel off at the power switch on the front panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Wait 30 seconds Turn the control panel ON. | DF **Not** Ready displayed on the control panel display after restart? **YES** | 3A |
| DF **Not** Ready displayed on the control panel display after restart? **NORepair:** None. Restarting the control panel removed any inactive faults **not** allowing gas flow. | Repair complete |  |

### STEP 3. Verify hydraulic pump power.

#### STEP 3A. Verify hydraulic pump power.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify hydraulic pump power on the control panel display. | Hydraulic pump power greater than 373kW but less than 1578 kW for 2250 HP engines or 1748 kW for 2500 HP engines? **YES** | 4A |
| Hydraulic pump power greater than 373 kW but less than 1578 kW for 2250 HP engines or 1748 kW for 2500 HP engines? **NORepair:** Allow hydraulic pump power to reach operation range. | Repair complete |  |

### STEP 4. Verify intake manifold temperature.

#### STEP 4A. Verify intake manifold temperature.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify intake manifold temperature on the control panel display. | Intake manifold temperature between 43°C \[110 °F\] and 82°C \[180 °F\]? **YES** | 5A |
| Intake manifold temperature between 43°C \[110 °F\] and 82°C \[180 °F\]? **NORepair:** Allow the intake manifold temperature reach the temperature limits. | Repair complete |  |

### STEP 5. Verify engine speed.

#### STEP 5A. Verify engine speed.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify engine speed on the control panel display. | Engine speed between 1400 and 2000 rpm for longer than 60 seconds? **YES** | 6A |
| Engine speed between 1400 and 2000 rpm for longer than 60 seconds? **NORepair:** Allow engine to operate between 1400 and 2000 rpm for longer than 60 seconds. | Repair complete |  |

### STEP 6. Verify coolant temperature.

#### STEP 6A. Verify coolant temperature.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify engine coolant temperature on the control panel display. | Coolant temperature greater than 71°C \[160 °F\] for longer than 3 seconds? **YES** | 7A |
| Coolant temperature greater than 71°C \[160 °F\] for longer than 3 seconds? **NORepair:** Allow the coolant temperature to reach the minimum limit. | Repair complete |  |

### STEP 7. Check emergency stops and remote stops.

#### STEP 7A. Operator shutdown engaged.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the operator shutdown status on the control panel display. | Operator shutdown engaged? **YESRepair:** Reset the shutdown. | Repair complete |
| Operator shutdown engaged? **NO** | 7B |  |

#### STEP 7B. Remote Operator Shutdown is engaged.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the operator shutdown status on the control panel display. | Remote operator shutdown engaged? **YESRepair:** Reset the shutdown. | Repair complete |
| Remote operator shutdown engaged? **NO** | 7C |  |

#### STEP 7C. Remote Stop is engaged.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote stop status on the control panel display. | Remote stop engaged? **YESRepair:** Reset the remote stop. | Repair complete |
| Remote stop engaged? **NO** | 8A |  |

### STEP 8. Check transmission gear selection.

#### STEP 8A. Check transmission gear selection.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the transmission status. | Transmission in gear for longer than 60 seconds? **YES** | Contact a Cummins® Authorized Repair Location |
| Transmission in gear for longer than 60 seconds? **NORepair:** Run the transmission in gear for more than 60 seconds. | Repair complete |  |

### STEP 9. Check for errors.

#### STEP 9A. Check the engine ECM for engine fault codes.

| **Conditions:** Turn keyswitch ON. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the recommended Cummins® electronic service tool or equivalent to read the fault code. | Engine ECM indicates fault codes? **YES** | Troubleshoot engine fault codes prior to Troubleshooting Alarm Codes. |
| Engine ECM indicates fault codes? **NO** | 9B |  |

#### STEP 9B. Review the fault message(s).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel or InteliMonitor for fault messages in alarm list and history. | DF **Not** Ready alarm code is present? **YES** | 9C |
| DF **Not** Ready alarm code is present? **NO** | Return the pump to service and monitor. |  |

#### STEP 9C. Review the fault message(s).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel or InteliMonitor for fault messages in alarm list and history. | Alarm codes other than DF **Not** Ready present? **YES** | Troubleshoot all other error codes prior to troubleshooting DF **Not** Ready. |
| Alarm codes other than DF **Not** Ready present? **NO** | 10A |  |

### STEP 10. Verify engine speed.

#### STEP 10A. Verify engine speed.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the recommended Cummins® electronic service tool or equivalent to verify engine speed from engine matches value displayed in InteliMonitor. | Engine speed between 1570-1980 rpm in both modules for longer than 60 seconds? **YES** | 11A |
| Engine speed between 1570-1980 rpm in both modules for longer than 60 seconds? **NORepair:** Allow engine to operate between 1570-1980 rpm for longer than 60 seconds and verify DF operation. | Repair complete |  |

### STEP 11. Check transmission gear selection.

#### STEP 11A. Check transmission gear selection.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Monitor TransReqGear in Intellimonitor Software or on local display panel. If Value-ECU-TransReqGear = \#, the setpoint in 12A (UseTransGear) needs to be 0. | TransReqGear greater than 0 for longer than 60 seconds? **YES** | 12A |
| TransReqGear greater than 0 for longer than 60 seconds? **NORepair:** Run the transmission in gear for more than 60 seconds and verify DF operation. | Repair complete |  |

### STEP 12. Incorrect adjustable parameter setting.

#### STEP 12A. Check transmission type selection.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify UseTransGear matches transmission type on pump. For a manual transmission equipped pump UseTransGear **must** be 0. For electronic Transmission UseTransGear **must** be 1. If Value-ECU-TransReqGear = \#, the setpoint in 12A (UseTransGear) needs to be 0. | UseTransGear matches transmission type? **YES** | 13A |
| UseTransGear matches transmission type? **NORepair:** Set UseTransGear to appropriate value and verify DF operation. This requires a level 2 password. | Repair complete |  |

### STEP 13. Verify intake manifold temperature.

#### STEP 13A. Verify intake manifold temperature(s).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the recommended Cummins® electronic service tool or equivalent to verify intake manifold temperatures from engine match values displayed in InteliMonitor. Once intake manifold temperature(s) have exceeded 82°C \[ 180°F \] they **must** drop below 79°C \[ 174°F \] in order for DF to be reenabled. | Intake manifold temperature(s) between 43°C \[ 110°F \] and 82°C \[ 180°F \] in both modules? **YES** | 14A |
| Intake manifold temperature between 43°C \[ 110°F \] and 82°C \[ 180°F \] in both modules? **NORepair:** Operate engine with intake manifold temperatures within safe range and verify DF operation. | Repair complete |  |

### STEP 14. Verify engine coolant temperature.

#### STEP 14A. Verify engine coolant temperature.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the recommended Cummins® electronic service tool or equivalent to verify coolant temperature value from engine match values displayed in InteliMonitor. | Engine coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds in both modules? **YES** | 15A |
| Engine coolant temperature greater than 71°C \[ 160°F \] for longer than 3 seconds in both modules? **NORepair:** Operate engine, allow the coolant temperature to reach the minimum limit and verify DF operation. | Repair complete |  |

### STEP 15. Engine load **not** within set limit.

#### STEP 15A. Verify source for engine power value.

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify power source in PLC Monitor. (Converted or J1939). | Pump using Real Power message via J1939? **YES** | 15B |
| Pump using Real Power message via J1939? **NO** | 15C |  |

#### STEP 15B. Verify Real Power transmitted value (J1939).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Monitor value for Real Power transmitted via J1939 on IV5 screen 7 OR IMON – ECU – Pwr-Real R. Verify engine is operating within power limits. (2250 HP engine 373-1578 kW) (2500 HP engine: 373-1748 kW) If both 4-20ma input and J1939 message are present, the J1939 message takes priority and control ignores the converted signal. All limits should still be in the same range. | Do J1939 transmitted power limits correspond with pump power rating? **YES** | Return the pump to service and monitor. |
| Do J1939 transmitted power limits correspond with pump power rating? **NORepair:** For pump with J1939 Real Power Value: Connect the recommended Cummins® electronic service tool or equivalent and verify that power rating transmitted through the ECM is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. | Refer to OEM troubleshooting. |  |

#### STEP 15C. Verify engine load limits (Converted).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Connect the recommended Cummins® electronic service tool or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the value the OEM is transmitting for Engine HP matches value read in IMON -Analog CU - FracPumpHP. OEM sends linear signal as 4-20 mA corresponding to 0-2500 HP (based on engine rating). | Do power limits correspond with pump power rating? **YES** | Verify DF Operation, return pump to service and monitor. |
| Do power limits correspond with pump power rating? **NORepair:** For pumps with converted power limits: Using a DMM, verify that power rating signal on BF1-A2 is correct. If value is incorrect from the OEM, then the OEM or customer needs to correct this value. If value from OEM is correct and error persists replace IBF Module. | Repair complete |  |
