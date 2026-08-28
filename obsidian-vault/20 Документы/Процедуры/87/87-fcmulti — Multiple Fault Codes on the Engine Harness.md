---
aliases:
  - "Множественные коды неисправностей на жгуте двигателя"
type: "Процедура"
doc: "87-fcmulti"
title_en: "Multiple Fault Codes on the Engine Harness"
title_ru: "Множественные коды неисправностей на жгуте двигателя"
modified: "2003-10-23"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fcmulti.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fcmulti.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Multiple Fault Codes on the Engine Harness
**Множественные коды неисправностей на жгуте двигателя**

> [!abstract] Процедура · `87-fcmulti`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-10-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fcmulti.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fcmulti.pdf)

### Fault Code: Multiple

### Multiple Fault Codes on the Engine Harness

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: Multiple PID(P): SPN: FMI: Lamp: SRT: | Multiple fault codes generated due to a common supply or a return wire failure in the engine harness. | Multiple fault codes. |

![[19900397.png]]

### Circuit Description

The electronic control module (ECM) supplies all of the engine pressure sensors on the engine harness with +5 VDC from pin 10. The ECM has common returns for all of the engine pressure sensors and temperature sensors on pin 19. A failure on either of these wires will cause multiple fault codes.

### Component Location

Consult the engine diagrams.

### Shoptalk

Look for an open circuit in the common supply and return wires and short circuits from battery or ground to the supply and return wires or defective ECM power supply.

A failed pressure sensor can cause multiple fault codes.

A failed pressure sensor can cause multiple active fault codes to go inactive once the engine has been started.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.**

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Determine the set of multiple fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Codes 122, 135, 144, 153, 221, and 719 are not active |
|  | **STEP 1B.** Read the fault codes. | Fault Codes 122, 135, 221, 231, and 719 are not active |
|  | **STEP 1C.** Read the fault codes. | Fault Codes 123, 141, 145, 154, 213, 222, 232, and 729 are not active |
|  | **STEP 1D.** Read the fault codes. | Fault Codes 123, 141, 222, 232, and 729 are not active |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the ECM and engine harness connectors. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 2C.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 3. | Check the engine harness. |  |
|  | **STEP 3A.** Inspect the ECM and engine harness connectors. | No damaged pins |
|  | **STEP 3B.** Check for an open circuit. | More than 100k ohms |
| STEP 4. | Check the engine harness. |  |
|  | **STEP 4A.** Inspect the ECM and engine harness connectors. | No damaged pins |
|  | **STEP 4B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 4C.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 4D.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 4E.** Check the battery supply voltage. | 17.0 to 35.0 VDC |
| STEP 5. | Check the engine harness. |  |
|  | **STEP 5A.** Inspect the ECM and engine harness connectors. | No damaged pins |
|  | **STEP 5B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 5C.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 5D.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 5E.** Check the battery supply voltage. | 17.0 to 35.0 VDC |
| STEP 6. | Clear the fault codes. |  |
|  | **STEP 6A.** Disable the fault code. | Multiple fault codes inactive |
|  | **STEP 6B.** Clear the inactive fault codes. | All fault codes cleared |

### STEP 1. Determine the set of multiple fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™. | Fault Codes 122, 135, 144, 153, 221, and 719 are not active | 1B |
| Fault Code 122, 135, 144, 153, 221, or 719 is active | 2A |  |

#### STEP 1B. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™. | Fault Codes 122, 135, 221, and 719 not active | 1C |
| Fault Code 122, 135, 221, or 719 is active | 3A |  |

#### STEP 1C. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™. | Fault Codes 123, 141, 145, 154, 222, 232, and 729 not active | 1D |
| Fault Code 123, 141, 145, 154, 222, 232, or 729 is active | 4A |  |

#### STEP 1D. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™. | Fault Codes 123, 141, 222, 232, and 729 not active | 2A |
| Fault Code 123, 141, 222, 232, or 729 is active | 5A |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect the ECM and engine harness connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 2B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. Dry the connector by using an electrical contact cleaner, Part Number 3824510. | 6A |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from the sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 19 in the engine harness connector to pin B on the engine wiring harness side of all sensors with active fault codes. | Less than 10 ohms | 2C |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-202 or 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

#### STEP 2C. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 19 of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | More than 100k ohms | 6A |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

### STEP 3. Check the engine harness.

#### STEP 3A. Inspect the ECM and engine harness connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 3B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 6A |  |

#### STEP 3B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 19 of the engine harness connector to pin B of the harness side of all sensors with active fault codes. | More than 100k ohms | 6A |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

### STEP 4. Check the engine harness.

#### STEP 4A. Inspect the ECM and engine harness connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 4B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 6A |  |

#### STEP 4B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the pressure sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 10 in the engine harness connector to pin A on the engine wiring harness side of a pressure sensor connector. | Less than 10 ohms | 4C |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

#### STEP 4C. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 10 of the engine harness connector to the engine block ground. Measure the resistance from pin 23 of the engine harness connector to the engine block ground. Measure the resistance from pin 34 of the engine harness connector to the engine block ground. | More than 100k ohms | 4D |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

#### STEP 4D. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 10 of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | More than 100k ohms | 4E |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

#### STEP 4E. Check the battery supply voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 50 of the engine harness connector to engine block ground. | 17.0 to 35.0 VDC | 5A |
| Correct battery supply voltage problem. | 6A |  |

### STEP 5. Check the engine harness.

#### STEP 5A. Inspect the ECM and engine harness connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins. | No damaged pins | 5B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. Replace the ECM. Refer to Procedure 019-031. | 6A |  |

#### STEP 5B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the pressure sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 10 in the engine harness connector to pin A on the engine wiring harness side of all pressure sensors with active fault codes. | Less than 10 ohms | 5C |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

#### STEP 5C. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 10 of the engine harness connector to the engine block ground. Measure the resistance from pin 23 of the engine harness connector to the engine block ground. Measure the resistance from pin 34 of the engine harness connector to the engine block ground. | More than 100k ohms | 5D |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

#### STEP 5D. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the OEM harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 10 of the engine harness connector to all other pins in the connector, and to all pins in the OEM harness connector. | More than 100k ohms | 5E |
| Repair or replace the engine harness Repair the engine harness. Refer to Procedure 019-204. Replace the engine harness. Refer to Procedure 019-043. | 6A |  |

#### STEP 5E. Check the battery supply voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness in the multiple fault code circuit from all the sensors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 50 of the engine harness connector to engine block ground. | 17.0 to 35.0 VDC | 6A |
| Correct battery supply voltage problem. | 6A |  |

### STEP 6. Clear the fault codes.

#### STEP 6A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start the engine and let it idle for 1 minute. Verify that multiple fault codes are inactive. | Multiple fault codes inactive | 6B |
| Return to the troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |

#### STEP 6B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase the inactive fault codes using INSITE™. | All fault codes cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
