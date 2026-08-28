---
aliases:
  - "Температура охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "94-fc151"
title_en: "Coolant Temperature - Engine Protection"
title_ru: "Температура охлаждающей жидкости — защита двигателя"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc151.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc151.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Coolant Temperature - Engine Protection
**Температура охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `94-fc151`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc151.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc151.pdf)

### Fault Code: 151

### Coolant Temperature - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 151 PID(P): SPN: FMI: Lamp: SRT: 00-357 | Engine coolant temperature has exceeded the alarm (shutdown) threshold for high coolant temperature. | Engine will shutdown. Common Alarm output is energized. High Coolant Temperature (HCT) relay driver is energized. |

![[19a00009.png]]

### Circuit Description

The CTS is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The ECM monitors the voltage on the signal pin and converts this to a temperature value. The coolant temperature is used by the ECM for the engine protection system and fueling control.

### Component Location

The CTS is located on the side of the thermostat housing.

### Shoptalk

- Make sure the air flow through the radiator is **not** obstructed.

- The resistance of all the temperature sensors varies with the temperature. The reading that you observe should compare to the following table if the sensor is functioning properly.

- The threshold for the coolant temperature warning is adjustable with INSITE™, Part No. 3825145. Ensure the threshold is set to the appropriate value.

| Temperature (° C) | Temperature \[° F\] | Resistance (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

## Warnings and Cautions

> [!danger] WARNING · Опасно
>

**Wait until the coolant temperature is below 50° C \[120° F\] before removing the coolant system pressure cap or the CTS. Failure to do so can cause personal injury from heated coolant spray.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the sensor accuracy. |  |
|  | **STEP 1A.** Verify the sensor accuracy with a thermocouple or similar temperature probe. | Sensor reading is correct |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 151 inactive |
|  | **STEP 2B.** Clear the inactive fault codes. | All Faults cleared |

### STEP 1. Check the sensor accuracy.

#### STEP 1A. Verify the sensor accuracy with a thermocouple or similar temperature probe.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect the temperature probe to the engine near the CTS. Connect INSITE™, Part No. 3825145, to the data link. Compare the coolant temperature reading on the service tool monitor screen to the reading from the temperature probe. **NOTE:** If no temperature measuring device is available, then answer "OK" to this step. | Sensor reading is correct. Refer to Base Engine Troubleshooting and Repair Manual for correct specifications. | 2A |
| **Go to Fault Code 145** | Fault Code 145 |  |

### STEP 2. Clear the fault code.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect all the components. Start the engine and let it warm up to normal operating temperature to verify that the fault has been fixed. | Fault Code 151 inactive | 2B |
| Return to the troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared. | Repair complete |
| **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
