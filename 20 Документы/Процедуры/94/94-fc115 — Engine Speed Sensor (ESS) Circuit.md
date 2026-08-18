---
aliases:
  - "Цепь датчика частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "94-fc115"
title_en: "Engine Speed Sensor (ESS) Circuit"
title_ru: "Цепь датчика частоты вращения двигателя (ESS)"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Engine Speed Sensor (ESS) Circuit
**Цепь датчика частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `94-fc115`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-fc115.pdf)

### Fault Code: 115

### Engine Speed Sensor (ESS) Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 115 PID(P): SPN: FMI: Lamp: SRT: 00-681 | No engine speed detected between pins 21 and 22 of the engine harness connector. | Engine is shutdown and can **not** be run. Common Alarm output is energized. |

![[19a00001.png]]

### Circuit Description

The ESS circuit provides the engine speed signal to the electronic control module (ECM) through the engine harness.

### Component Location

The ESS is located in the Flywheel Housing.

### Shoptalk

- If the problem occurs at a certain engine temperature, be sure to check the ESS circuit while the engine is at that particular temperature.

- Clean sensor tip; debris can cause intermittent signals.

- The sensor **must** be adjusted properly to obtain a good signal. Make sure the sensor is ½ to ¾ turns out from contacting a flywheel tooth and that the locking nut is tight and properly torqued.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3823996 - female Weather-Pack test lead Part No. 3822758 - male Deutsch/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the ESS. |  |
|  | **STEP 1A.** Inspect the ESS and the engine harness connector pins. | No damaged pins |
|  | **STEP 1B.** Inspect the ESS. | No damaged ESS |
|  | **STEP 1C.** Check for an open circuit in the ESS. | Less than 1500 ohms |
|  | **STEP 1D.** Check for a short circuit to ground in the ESS. | More than 10M ohms |
|  | **STEP 1E.** Check for a short circuit between coils of the ESS. | More than 10M ohms |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness and ECM connector pins. | No damaged pins |
|  | **STEP 2A-1.** Inspect the engine harness adaptor cable and the engine harness extension cables. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit in the signal and return wires. | Less than 1500 ohms |
|  | **STEP 2B-1.** Check for an open circuit in the engine harness adaptor cable and the engine harness extension cables. | Less than 10 ohms |
|  | **STEP 2C.** Check for a short circuit to ground in the signal and return wires with the engine harness adaptor cable, and any extension cables used, installed. | More than 10M ohms |
|  | **STEP 2C-1.** Check for a short circuit to ground in the engine harness signal and return wires. | More than 10M ohms |
|  | **STEP 2D.** Check for a short circuit from the signal and return wires to all other wires in the engine harness. | More than 10M ohms |
|  | **STEP 2D-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable, and any engine harness extension cables used. | More than 10M ohms |
| STEP 3. | Clear fault codes. |  |
|  | **STEP 3A.** Clear fault codes. | All fault codes cleared |

### STEP 1. Check the ESS.

#### STEP 1A. Inspect the ESS and engine harness connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| for the following: bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 1B |
| **Repair the damaged pins** Repair or replace the engine harness or ESS, whichever has the damaged pins. Repair the engine harness. Refer to Procedure 19-202 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the ESS. Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 1B. Inspect the ESS.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. Remove the ESS. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| metal debris on the end of the sensor damage to the end of the sensor caused by contact with the flywheel oil leakage or insulation problems such as swelling damaged electrical potting in the sensing end of the sensor. | No damaged ESS | 1C |
| **Clean or replace the ESS** Clean the ESS. Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the ESS. Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 1C. Check for an open circuit in the ESS.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure resistance from pin A to pin B of the first ESS coil. Measure resistance from pin A to pin B of the second ESS coil. | Less than 1500 ohms | 1D |
| **Replace the ESS** Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 1D. Check for a short circuit to ground in the ESS.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure resistance from pin A of the first ESS coil to engine block ground. Measure resistance from pin A of the second ESS coil to engine block ground. | More than 10M ohms | 1E |
| **Replace the ESS** Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 1E. Check for a short circuit between coils of the ESS.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect ESS from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure resistance from pin A of the first ESS coil to pin A of second ESS coil. | More than 10M ohms | 2A |
| **Replace the ESS** Refer to Procedure 019-042 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect engine harness and ECM.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
| **Repair damaged pins** Repair or replace the engine harness adaptor cable or ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the ECM. Refer to OEM procedures. | 3A |  |

#### STEP 2A-1. Inspect engine harness connector and engine harness extension cables.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect engine harness extension cables from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
| **Repair damaged pins** Repair or replace the engine harness or engine harness extension cable, whichever has the damaged pins. Repair the engine harness or engine harness extension cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness or engine harness extension cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 2B. Check for an open circuit in the signal and return wires.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable connector from the ECM. Connect the ESS to the engine harness. Connect the engine harness to the engine harness adaptor cable. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 22 to pin 21 of the 40 pin on the engine harness adaptor connector. | Less than 1500 ohms | 2C |
|  | 2B-1 |  |

#### STEP 2B-1. Check for an open circuit in the engine harness adaptor cable and engine harness extension cables.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable connector from the ECM. Disconnect the engine harness from the engine harness extension cable. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the continuity of pin 22 of each cable used between the engine harness and the ECM. Measure the continuity of pin 21 of each cable used between the engine harness and the ECM. | Less than 10 ohms Repair or replace the engine harness. Repair the engine harness. Refer to Procedures 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |
| **Repair or replace the engine harness adaptor cable or an engine harness extension cable, whichever is found faulty** Repair the engine harness adaptor cable or an engine harness extension cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or an engine harness extension cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 2C. Check for a short circuit to ground in the signal and return wires with the engine harness adaptor cable, and any extension cables used, installed.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the ESS from the engine harness. Connect the engine harness to the engine harness adaptor cable. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 22 of the engine harness adaptor cable connector to engine block ground. Measure the resistance from pin 21 of the engine harness adaptor cable connector to engine block ground. | More than 10M ohms | 2D |
|  | 2C-1 |  |

#### STEP 2C-1. Check for a short circuit to ground in the signal and return wires.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the ESS from the engine harness. Disconnect the engine harness from the engine harness extension cables. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 22 of the engine harness to engine block ground. Measure the resistance from pin 21 of the engine harness to engine block ground. | More than 10M ohms | 2D-1 |
| **Repair or replace the engine harness** Repair the engine harness. Refer to Procedures 019-202 and 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

#### STEP 2D. Check for a short circuit from pin to pin in the engine harness adaptor cable, and any engine harness extension cables used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cables. Disconnect the ESS from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 22 of the engine harness connector to all other pins in the engine harness connector. Measure the resistance from pin 21 of the engine harness connector to all other pins in the engine harness connector. | More than 10M ohms | 3A |
|  | 2D-1 |  |

#### STEP 2D-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and the engine harness extension cables.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness extension cables from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 22 of the engine harness adaptor cable and engine harness extension cable to all other pins in the applicable cable. Measure the resistance from pin 21 of the engine harness adaptor cable and engine harness extension cable to all other pins in the applicable cable. | More than 10M ohms | 3A |
| **Repair or replace the engine harness adaptor cable or the engine harness extension cable, whichever is faulty** Repair the engine harness adaptor cable or the engine harness extension cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. Replace the engine harness adaptor cable or the engine harness extension cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual QST Fuel System QST30 G-Drive Engine Series, Bulletin No. 3666184. | 3A |  |

### STEP 3. Clear fault codes.

#### STEP 3A. Clear fault codes.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear Fault Code 115 using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | Fault Code 115 cleared | Repair complete |
| Refer to the appropriate troubleshooting charts for any remaining active fault codes. | Go to the appropriate troubleshooting charts |  |
