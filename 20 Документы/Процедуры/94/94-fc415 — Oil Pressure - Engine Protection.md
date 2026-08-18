---
aliases:
  - "Давление масла — защита двигателя"
type: "Процедура"
doc: "94-fc415"
title_en: "Oil Pressure - Engine Protection"
title_ru: "Давление масла — защита двигателя"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Oil Pressure - Engine Protection
**Давление масла — защита двигателя**

> [!abstract] Процедура · `94-fc415`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc415.pdf)

### Fault Code: 415

### Oil Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 415 PID(P): SPN: FMI: Lamp: SRT: 00-367 | Engine oil pressure has dropped below the alarm (shutdown) threshold for low oil pressure. | Engine will shutdown. Common Alarm output is energized. Low Oil Pressure (LOP) relay driver is energized. |

![[19a00007.png]]

### Circuit Description

The OPS is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.

### Component Location

The OPS is located on the left bank of the engine block above the fuel pump.

### Shoptalk

- Confirm that the OPS supply voltage is between 4.75 and 5.25 VDC at the sensor. See Fault Code 141.

- Oil pressure is a function of the engine speed, oil level and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot, at a low level, regulator has malfunctioned or a loss is occurring somewhere in the system.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the sensor accuracy. |  |
|  | **STEP 1A.** Verify the sensor accuracy with a mechanical gauge. | Sensor reading is correct |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 415 inactive |
|  | **STEP 2B.** Clear the inactive fault codes. | All the faults cleared |

### STEP 1. Check the sensor accuracy.

#### STEP 1A. Verify the sensor accuracy with a mechanical gauge.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect a mechanical oil pressure gauge of known quality and calibration to the engine at one of the plugs on top of the oil filter head. Connect INSITE™, Part No. 3825145, to the data link. Start the engine and compare the oil pressure reading on the monitor screen to the reading on the mechanical oil pressure gauge. **NOTE:** The engine speed will have to be increased to make it easier to see the differences in the readings. | Sensor reading is correct. | 2A |
| **Go To Fault Code 141** | Fault Code 141 |  |

### STEP 2. Clear the fault code.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect all the components. Start the engine and let it idle for one minute. **NOTE:** If fault was at a particular speed, run engine at that speed to verify problem is corrected. | Fault Code 415 inactive | 2B |
| Return to the troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All the faults cleared | Repair complete |
| **Troubleshoot any remaining active fault codes** | Appropriate troubleshooting chart |  |
