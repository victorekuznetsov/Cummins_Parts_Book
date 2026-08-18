---
aliases:
  - "Останов: разница температур ОГ по рядам"
type: "Процедура"
doc: "330-t02-1032"
title_en: "Sd EGTBankDelta"
title_ru: "Останов: разница температур ОГ по рядам"
modified: "2017-03-03"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
---

# Sd EGTBankDelta
**Останов: разница температур ОГ по рядам**

> [!abstract] Процедура · `330-t02-1032`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2017-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/330-t02-1032.pdf)

Printable Version

### Symptoms

Dual fuel operation will be stopped.

All gas flow will stop if the system is operating in dual fuel mode.

EGT Delta is an analysis of the exhaust gas temperature balance based on the diesel oxidation catalyst (DOC) inlet temperatures. If the measured temperature has an absolute difference (delta) exceeding the defined set-point, the dual fuel control module shuts down dual fuel operation.

### How To Use This Tree

This tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending up the symptom.

**Circuit Description:**

Anytime the control module is powered ON.

**Conditions for Activating the Fault Message:**

The dual fuel control module is powered ON and the measured DOC inlet temperatures vary greater than the set-point. The system will indicate this message and protection.

**Conditions for Clearing the Fault Codes Automatically:**

None.

**Conditions for Clearing the Fault Codes Manually:**

The fault reset is operated locally or via software.

### Shoptalk

The message indicates unacceptable differences in bank-to-bank exhaust gas temperatures.

Previous use of engine control module (ECM) cylinder specific temperatures was removed due to frequent per cylinder thermocouple malfunctions.

Previous use of ECM calculated averages for bank exhaust gas temperature was removed due to frequent per cylinder thermocouple malfunctions.

Possible causes include:

- Malfunctioning thermocouple or thermocouple wiring

- Plugged or restricted DOC or silencers causing elevated temperatures.

Imbalanced bank-to-bank gas delivery due to the following:

- Differences in intake air restriction from one bank to the other

- Differences in turbocharger performance from one bank to the other

- Differences in plumbing restriction from one bank to the other

- Leaks in the intake air system at gaskets, hoses, clamps, and air crossover connections.

| Code of Message | Reason | Effect |
|---|---|---|
| Sd EGT Delta | Exhaust gas temperatures are imbalanced between the left and right (A/B) banks. | The dual fuel control module will not allow gas operations. The dual fuel control module will stop gas flow. |

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Validate the fault message. |  |
|  | **STEP 1A.** Check for engine fault codes. | Any engine related fault codes? |
|  | **STEP 1B.** Check for additional gas system alarms. | Other shutdown messages for binary inputs occurred at the same time as Sd EGTBankDelta? |
|  | **STEP 1C.** Check for 'Active' fault message. | Control module in fault condition? |
| STEP 2. | Monitor the temperature sensors. |  |
|  | **STEP 2A.** Monitor the aftertreatment exhaust gas temperature sensors. | Left bank and right bank DOC temperature sensors vary by more than 24°C or 43°F with each other using InteliMonitor? |
|  | **STEP 2B.** Monitor the aftertreatment exhaust gas temperature sensors. | Left and right bank DOC inlet temperature sensors within 38°C \[100°F\] of each other? |
|  | **STEP 2C.** Check the intake restriction. | Air cleaner elements dirty or restricted? |
|  | **STEP 2D.** Check for intake and exhaust system leaks. | Leaks found in the air intake or exhaust systems? |
|  | **STEP 2E.** Check the gas lines. | Any damage found to the gas lines? |
|  | **STEP 2F.** Check the air piping. | Any damage found to the air lines? |
|  | **STEP 2G.** Check the turbocharger operation. | Any measurements in the Inspect for Reuse section outside of the stated limits? |
|  | **STEP 2H.** Check the DOC operation. | Any debris or damage found on the DOC? |
| STEP 3. | Reset the fault. |  |
|  | **STEP 3A.** Reset the fault. | Fault returns? |

### STEP 1. Validate the fault message.

#### STEP 1A. Check for engine fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read the fault codes. | Any engine related fault codes? **YES** | Go to the appropriate fault code troubleshooting tree. |
| Any engine related fault codes? **NO** | 1B |  |

#### STEP 1B. Check for additional gas system alarms.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect to the dual fuel control panel. Use InteliMonitor. Save a copy of the control module configuration file (archive file) on the local PC. Access the history shortcut. Check for occurrences of the message Sd EGTBankDelta. Check for other shutdown messages occurring at or near the time of the Sd EGTBankDelta. | Other shutdown messages for binary inputs occurred at the same time as Sd EGTBankDelta? **YESRepair:** If other shutdown messages for binary inputs occur at the same time, see the following procedure for ground and ground loop tests. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | 2A |
| Other shutdown messages for binary inputs occurred at the same time as Sd EGTBankDelta? **NO** | 1C |  |

#### STEP 1C. Check for 'Active' fault message.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel for fault message. Navigate to fault display screen. | Control module in fault condition? **YES** | 2A |
| Control module in fault condition? **NO** | 2B |  |

### STEP 2. Monitor the temperature sensors.

#### STEP 2A. Monitor the aftertreatment exhaust gas temperature sensors.

| **Conditions:** Power ON dual fuel control module. Key ON, engine not running. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect to the dual fuel panel. Use InteliMonitor. Save a copy of the configuration file (archive file) on the local PC. If any fault codes occur, see the appropriate fault code troubleshooting tree. If no fault codes occur, record the values of the three aftertreatment exhaust gas temperature sensors. | Left bank and right bank DOC temperature sensors vary by more than 24°C or 43°F with each other using InteliMonitor? **YESRepair:** Check for short circuit from the SIGNAL pin of the temperature sensor in question to all other pins in the harness. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] If no short is found, replace the temperature sensor reading higher or lower than the other sensors. Refer to Procedure 019-449 in Section 19. | 3A |
| Left bank and right bank DOC temperature sensors vary by more than 24°C or 43°F with each other using InteliMonitor? **NO** | Contact a Cummins® Authorized Repair Location. |  |

#### STEP 2B. Monitor the aftertreatment exhaust gas temperature sensors.

| **Conditions:** Turn dual fuel control module ON. Reset the fault on the panel. Run engine at 1500 to 2000 rpm to meet operating conditions for dual fuel operation. Turn gas control switch on the panel to OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the local display panel for the fault message. Monitor the left and right bank DOC inlet temperature sensor in Diesel Only mode. | Left and right bank DOC inlet temperature sensors within 38°C \[100°F\] of each other? **YES** | 3A |
| Left and right bank DOC inlet temperature sensors within 38°C \[100°F\] of each other? **NO** | 2C |  |

#### STEP 2C. Check the intake restriction.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the air cleaner elements. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-014 in Section 10. | Air cleaner elements dirty or restricted? **YESRepair:** Clean or replace the air filter element. See equipment manufacturer service information. | 3A |
| Air cleaner elements dirty or restricted? **NO** | 2D |  |

#### STEP 2D. Check for intake and exhaust system leaks.

| **Conditions:** Operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the air intake and exhaust system for leaks. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-024 in Section 10. | Leaks found in the air intake or exhaust systems? **YESRepair:** Repair the source of the leak. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-024 in Section 10. | 3A |
| Leaks found in the air intake or exhaust systems? **NO** | 2E |  |

#### STEP 2E. Check the gas lines.

| **Conditions:** Turn OFF engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the gas lines for damage. Refer to Procedure 005-248 in Section 5. | Any damage found to the gas lines? **YESRepair:** Replace the damaged portion of gas line. Refer to Procedure 005-248 in Section 5. | 3A |
| Any damage found to the gas lines? **NO** | 2F |  |

#### STEP 2F. Check the air piping.

| **Conditions:** Turn OFF engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the air piping for damage. Refer to Procedure 005-248 in Section 5. | Any damage found to the air lines? **YESRepair:** Replace the damaged portion of air lines. Refer to Procedure 005-248 in Section 5. | 3A |
| Any damage found to the air lines? **NO** | 2G |  |

#### STEP 2G. Check the turbocharger operation.

| **Conditions:** Turn OFF engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure turbocharger clearances. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-033 in Section 10. | Any measurements in the Inspect for Reuse section outside of the stated limits? **YESRepair:** Repair or replace the turbocharger. Use the GTA38, K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. [[28-010-033-tr — Turbocharger\|Refer to Procedure 010-033 in Section 10.]] | 3A |
| Any measurements in the Inspect for Reuse section outside of the stated limits? **NO** | 2H |  |

#### STEP 2H. Check the DOC operation.

| **Conditions:** Turn OFF engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the DOC for any damage or buildup. Refer to Procedure 011-049 in Section 11. | Any debris or damage found on the DOC? **YESRepair:** Clean or replace the DOC. Refer to Procedure 011-049 in Section 11. | 3A |
| Any debris or damage found on the DOC? **NO** | 3A |  |

### STEP 3. Reset the fault.

#### STEP 3A. Reset the fault.

| **Conditions:** Engine not operating. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Rest the fault on the control panel or through InteliMonitor. Operate the engine under conditions to allow gas substitution. | Fault returns? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |
| Fault returns? **NO** | Repair complete. |  |
