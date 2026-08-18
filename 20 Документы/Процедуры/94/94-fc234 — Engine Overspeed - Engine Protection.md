---
aliases:
  - "Превышение частоты вращения — защита двигателя"
type: "Процедура"
doc: "94-fc234"
title_en: "Engine Overspeed - Engine Protection"
title_ru: "Превышение частоты вращения — защита двигателя"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Engine Overspeed - Engine Protection
**Превышение частоты вращения — защита двигателя**

> [!abstract] Процедура · `94-fc234`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc234.pdf)

### Fault Code: 234

### Engine Overspeed - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 234 PID(P): SPN: FMI: Lamp: SRT: | Engine Speed Sensor (ESS) signal on pins 21 and 22 of the engine harness electronic control module (ECM) connector indicates engine speed greater than alarm (shutdown) threshold. | Fuel shutoff valves are de-energized (valves closed). Common Alarm output is energized. Overspeed relay driver is energized. |

![[19a00001.png]]

### Circuit Description

The ESS circuit provides the engine speed signal to the ECM through the engine harness.

### Component Location

The ESS is located in the flywheel housing.

### Shoptalk

This fault code indicates that the engine speed was above the maximum allowable engine speed. An engine overspeed can be caused by either a fuel system problem or the engine being driven or reverse powered past its maximum allowable speed.

The threshold for the engine overspeed shutdown is adjustable with INSITE™, Part No. 3825145. Ensure the threshold is set to the appropriate value.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Identify the reason for the overspeed. |  |
|  | **STEP 1A.** Check for Fault Code 171. | Fault Code 171 not present |
|  | **STEP 1B.** Check for motoring of engine (reverse power). | Engine not reverse powered |
|  | **STEP 1C.** Check for alternate fuel source. | No alternate fuel source |
|  | **STEP 1D.** Check engine rpm with service tool monitor. | Correct rpm reading |
| STEP 2. | Clear fault codes. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 234 inactive |
|  | **STEP 2B.** Clear the inactive fault codes. | All faults cleared |

### STEP 1. Identify the reason for the overspeed.

#### STEP 1A. Check for Fault Code 171.

| **Conditions:** Stop/Run switch in the “STOP” position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™, Part No. 3825145. | Fault Code 171 not present | 1B |
|  | Go to Fault Code 171 |  |

#### STEP 1B. Check for motoring of engine (reverse power).

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check snapshot data for indications of reverse power. | Engine not reverse powered | 1C |
| **Check engine for damage caused by overspeed condition.** | 2A |  |

#### STEP 1C. Check for alternate fuel source.

| **Conditions:** Stop/Run switch in the “STOP” position. Controller not in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | No alternate fuel source | 1D |
| **Locate the alternate fuel source.** Locate and remove any alternate fuel source. | 2A |  |

#### STEP 1D. Check engine rpm with service tool monitor.

| **Conditions:** Stop/Run switch in the “RUN” position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Monitor the engine rpm using INSITE™, Part No. 3825145. | Correct rpm reading | 2A |
| **Inspect engine speed sensor** Refer to Procedure 019-042. | 2A |  |

### STEP 2. Clear fault codes.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect all components. Start the engine and idle for one minute. Verify Fault Code 234 is inactive. | Fault Code 234 inactive. | 2B |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 2B. Clear inactive fault codes.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
| **Troubleshoot any remaining active fault Faults.** | Appropriate troubleshooting chart |  |
