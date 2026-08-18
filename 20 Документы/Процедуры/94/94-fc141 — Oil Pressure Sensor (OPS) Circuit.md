---
aliases:
  - "Цепь датчика давления масла (OPS)"
type: "Процедура"
doc: "94-fc141"
title_en: "Oil Pressure Sensor (OPS) Circuit"
title_ru: "Цепь датчика давления масла (OPS)"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Oil Pressure Sensor (OPS) Circuit
**Цепь датчика давления масла (OPS)**

> [!abstract] Процедура · `94-fc141`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc141.pdf)

### Fault Code: 141

### Oil Pressure Sensor (OPS) Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 141 PID(P): SPN: FMI: Lamp: SRT: 00-353 | Low voltage detected at engine oil pressure sensor signal pin 12 of the engine harness Electronic Control Module (ECM) Connector. | No effect on performance. Common Warning output is energized. |

![[19a00007.png]]

### Circuit Description

The OPS monitors oil pressure and passes information to the ECM through pin 12 of the engine harness. The ECM monitors the voltage on pin 12 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation. Voltage below 0.35 VDC on pin 12 will trip Fault Code 141 and can be caused by shorts in the supply, signal, or return wires, an open in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.

### Component Location

The OPS is located on the left bank of the engine block above the fuel pump.

### Shoptalk

If Fault Code 143 or 415 are **not** present, the problem is **not** base engine related.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3822758 - male Deutsch/Cannon/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the oil pressure sensor. |  |
|  | **STEP 1A.** Inspect the oil pressure sensor and engine harness connector pins. | No damaged pins |
|  | **STEP 1B.** Check the ECM oil pressure supply voltage. | 4.75 to 5.25 VDC |
|  | **STEP 1C.** Check the ECM oil pressure signal voltage. | 0.42 to 0.58 VDC |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness adaptor cable and the ECM connector for damaged pins. | No damaged pins |
|  | **STEP 2A-1.** Inspect the engine harness connector and the engine harness extension cable(s) for damaged pins. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 2B-1.** Check for an open in the engine harness adaptor cable and any engine harness extension cables used. | Less than 10 ohms |
|  | **STEP 2C.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 2C-1.** Check engine harness for short circuit to ground. | More than 100k ohms |
|  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 2D-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used. | More than 100k ohms |
| STEP 3. | Clear the fault code. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 141 inactive |
|  | **STEP 3B.** Clear any inactive fault codes. | All faults cleared |

### STEP 1. Check the oil pressure sensor.

#### STEP 1A. Inspect the oil pressure sensor and engine harness connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the oil pressure sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or the connector missing connector seal. | No damaged pins | 1B |
| **Repair damaged pins** Repair or replace the engine harness or the OPS, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 019-203 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the OPS. Refer to Procedure 019-061 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Dry the connector by using electrical contact cleaner, Part No. 3824510. Replace the connector seal. | 3A |  |

#### STEP 1B. Check the ECM oil pressure supply voltage.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Install the oil pressure sensor break out cable, Part No. 3824775, between the sensor and the sensor harness connector. Measure the supply voltage by installing the break out cable's supply (pin A) and return connectors (pin B) into the multimeter. | 4.75 to 5.25 VDC | 1C |
|  | 2A |  |

#### STEP 1C. Check the ECM oil pressure signal voltage.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the signal voltage by installing the break out cable's signal (pin C) and return connectors (pin B) into the multimeter. | 0.42 to 0.58 VDC | 2A |
| **Replace the oil pressure sensor** Refer to Procedure 019-066 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect the engine harness adaptor cable and the ECM connector for damaged pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
| **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the ECM. Refer to OEM Procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |

#### STEP 2A-1. Inspect the engine harness connector and the engine harness expansion cable(s) for damaged pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness expansion cable(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
| **Repair the damaged pins** Repair or replace the engine harness or the engine harness expansion cable, whichever has the damaged pins. Repair the engine harness or the engine harness expansion cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness or the engine harness expansion cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 3A |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from engine harness adaptor cable connector pin 12 to oil pressure signal, pin C, of the OPS connector harness side. Measure the resistance from engine harness adaptor cable connector pin 11 and +5 VDC supply, pin A, of the OPS connector harness side. | Less than 10 ohms | 2C |
|  | 2B-1 |  |

#### STEP 2B-1. Check for an open in the engine harness adaptor cable and any engine harness extension cables used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness expansion cable(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the continuity of pin 12 for the engine harness adaptor cable and any engine harness expansion cable being used. Measure the continuity of pin 11 for the engine harness adaptor cable and any engine harness expansion cable being used. | Less than 10 ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-203 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |
| **Repair or replace the engine harness adaptor cable or the engine harness expansion cable, whichever is faulty** Repair the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 2C. Check for a short circuit to ground.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from engine harness adaptor cable connector pin 12 to engine block ground measure the resistance from engine harness adaptor cable connector pin 13 to engine block ground measure the resistance from engine harness adaptor cable connector pin 11 to engine block ground. | More than 100k ohms | 2D |
|  | 2C-1 |  |

#### STEP 2C-1. Check for a short circuit to ground.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the OPS. Disconnect the engine harness from the engine harness extension cables. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from engine harness connector pin 12 to engine block ground measure the resistance from engine harness connector pin 13 to engine block ground measure the resistance from engine harness connector pin 11 to engine block ground. | More than 100k ohms | 2D-1 |
| **Repair or replace the engine harness** Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 2D. Check for a short circuit from pin to pin.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the OPS. Disconnect the engine harness from the coolant temperature sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from engine harness adaptor cable connector pin 12 to all other pins in the connector measure the resistance from engine harness adaptor cable connector pin 13 to all other pins in the connector measure the resistance from engine harness adaptor cable connector pin 11 to all other pins in the connector. | More than 100k ohms Replace the ECM. Refer to OEM Procedures. | 3A |
|  | 2D-1 |  |

#### STEP 2D-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and any engine harness extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the engine harness expansion cable(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from pin 12 of the engine harness adaptor cable and any engine harness expansion cable used, to all other pins in the engine harness connector measure the resistance from pin 13 of the engine harness adaptor cable and any engine harness expansion cable used, to all other pins in the engine harness connector measure the resistance from pin 11 of the engine harness adaptor cable and any engine harness expansion cable used, to all other pins in the engine harness connector. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |
| **Repair or replace the engine harness adaptor cable or the engine harness expansion cable, whichever is faulty** Repair the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or the engine harness expansion cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

### STEP 3. Clear the fault code.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| connect all components start the engine and idle for one minute verify that Fault Code 141 is inactive. | Fault Code 141 inactive | 3B |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 3B. Clear the inactive fault codes.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
| **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
