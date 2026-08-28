---
aliases:
  - "Цепь датчика температуры охлаждающей жидкости (CTS)"
type: "Процедура"
doc: "94-fc145"
title_en: "Coolant Temperature Sensor (CTS) Circuit"
title_ru: "Цепь датчика температуры охлаждающей жидкости (CTS)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc145.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc145.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Coolant Temperature Sensor (CTS) Circuit
**Цепь датчика температуры охлаждающей жидкости (CTS)**

> [!abstract] Процедура · `94-fc145`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc145.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc145.pdf)

### Fault Code: 145

### Coolant Temperature Sensor (CTS) Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 145 PID(P): SPN: FMI: Lamp: SRT: 00-356 | Low voltage detected at engine coolant temperature sensor signal pin 14 of the engine harness Electronic Control Module (ECM) Connector. | No effect on performance. Common Warning output is energized. |

![[19a00009.png]]

### Circuit Description

The CTS is used by the ECM to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system and fueling control. The ECM monitors the voltage on pin 14. The ECM expects to see the voltage vary between.32 and 4.69 VDC. If the voltage is below.24 VDC for more than 2 seconds, then the ECM will log Fault Code 145. Voltage below.24 VDC on pin 14 can be caused by shorts to ground on the supply or return wires or an internally grounded failed sensor.

### Component Location

The CTS is located on the side of the thermostat housing.

### Shoptalk

All Temperature Sensors

- The resistance of the sensor varies with the temperature. The reading that you observe will compare to the following table if the sensor is functioning properly.

**NOTE:** High voltages correspond to low temperatures and low voltages correspond to high temperatures.

| Temperature | Temperature | Resistance |
|---|---|---|
| (° C) | (° F) | (ohms) |
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

## Warnings and Cautions

> [!danger] WARNING · Опасно
>

**Wait until the coolant temperature is below 50° C \[120° F\] before removing the coolant system pressure cap or the CTS. Failure to do so can cause personal injury from heated coolant spray.**

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3822758 - male Deutsch/Cannon/Metri-Pack test lead Part No. 3823256 - Metri-Pack 2-way connector test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the CTS. |  |
|  | **STEP 1A.** Inspect harness and sensor connector pins. | No damaged pins |
|  | **STEP 1B.** Check the resistance of the CTS. | 600 ohms to 36k ohms See temperature/resistance table under shop talk for correct value. |
|  | **STEP 1C.** Check for a short circuit to ground in the sensor. | More than 100k ohms |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness adaptor cable and the ECM connector pins. | No damaged pins |
|  | **STEP 2A-1.** Inspect the engine harness and the engine harness extension cable(s). | No damaged pins |
|  | **STEP 2B.** Check for a short circuit from the signal and return pins to all other pins. | More than 100k ohms |
|  | **STEP 2B-1.** Check for a short circuit from the signal and return pins to all other pins. | More than 100k ohms |
|  | **STEP 2C.** Check for a short circuit to ground in the supply and signal wire. | More than 100k ohms |
|  | **STEP 2C-1.** Check for a short circuit to ground in the supply and signal wire. | More than 100k ohms |
|  | **STEP 2D.** Check for an open in the signal and return wires. | Less than 10 ohms |
|  | **STEP 2D-1.** Check for an open in the engine harness adaptor cable and any engine harness extension cable used. | Less than 10 ohms |
| STEP 3. | Clear the fault code. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 145 inactive |
|  | **STEP 3B.** Clear the inactive fault codes. | All faults cleared |

### STEP 1. Check the CTS.

#### STEP 1A. Inspect the harness and the sensor connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector missing connector seal. | No damaged pins | 1B |
| **Repair the damaged pins** Repair or replace the engine harness or the CTS, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-202 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the CTS. Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. Replace the connector seal. | 3A |  |

#### STEP 1B. Check the resistance of the CTS.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the two pins on the sensor side of the CTS connector. | 600 ohms to 36k ohms See Temperature/Resistance Table under Shop Talk for correct value. | 1C |
| **Replace the CTS** Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |

#### STEP 1C. Check for a short circuit to ground in the sensor.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the CTS. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from one of the pins on the sensor side of the CTS connector to the engine block ground. | More than 100k ohms | 2A |
| **Replace the CTS** Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect the engine harness adaptor cable and the ECM connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
| **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |

#### STEP 2A-1. Inspect the engine harness and the engine harness extension cable(s) connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
| **Repair the damaged pins** Repair or replace the engine harness or the engine harness expansion cable(s), whichever has the damaged pins. Repair the engine harness or the engine harness expansion cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or the engine harness expansion cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |

#### STEP 2B. Check for a short circuit from the signal and return pins to all other pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the CTS. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 14 of the engine harness adaptor cable connector to all other pins in the connector. Measure the resistance from pin 15 of the engine harness adaptor cable connector to all other pins in the connector. | More than 100k ohms | 2C |
|  | 2B-1 |  |

#### STEP 2B-1. Check for a short circuit from the signal and return pins to all other pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness extension cables. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance of pin 14 of the engine harness adaptor cable connector and any engine harness extension cable used, to all other pins in the connector. Measure the resistance of pin 15 of the engine harness adaptor cable connector and any engine harness extension cable used, to all other pins in the connector. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-199 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
| **Repair or replace the engine harness adaptor cable or the engine harness expansion cable(s), whichever is found faulty** Repair the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |

#### STEP 2C. Check for a short circuit to ground in the supply and signal wire.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness from CTS. Disconnect engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 14 of the engine harness adaptor cable connector to engine block ground. Measure the resistance from pin 15 of the engine harness adaptor cable connector to engine block ground. | More than 100k ohms Replace the CTS. Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
|  | 2C-1 |  |

#### STEP 2C-1. Check for a short circuit to ground in the supply and signal wire.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness from CTS. Disconnect engine harness from the engine harness expansion cable. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 14 of the engine harness connector to engine block ground. Measure the resistance from pin 15 of the engine harness connector to engine block ground. | More than 100k ohms Replace the CTS. Refer to Procedure 019-019 in the Troubleshooting and Repair Manual QST System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 2D |
| **Repair or replace the engine harness** Repair the engine harness. Refer to Procedure 019-199 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |

#### STEP 2D. Check for an open in the signal and return wires.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness adaptor cable from ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 14 of the engine harness adaptor cable to pin 15 of the connector. | Less than 10 ohms | 3A |
|  | 2D-1 |  |

#### STEP 2D-1. Check for an open in the engine harness adaptor cable and any engine harness extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness adaptor cable from ECM. Disconnect engine harness from the engine harness expansion cable. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the continuity for pin 14 of the engine harness adaptor cable and any engine harness extension cable used. Measure the continuity for pin 15 of the engine harness adaptor cable and any engine harness extension cable used. | Less than 10 ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedures 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |
| **Repair or replace the engine harness adaptor cable or the engine harness expansion cable(s), whichever is found faulty** Repair the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or the engine harness expansion cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 3A |  |

### STEP 3. Clear the fault code.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect all components. Start the engine and idle for one minute. | Fault Code 145 inactive | 3B |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 3B. Clear the inactive fault codes.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
| **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
