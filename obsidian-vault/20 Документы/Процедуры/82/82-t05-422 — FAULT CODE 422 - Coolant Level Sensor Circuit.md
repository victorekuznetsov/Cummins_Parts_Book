---
aliases:
  - "Код 422 — цепь датчика уровня охлаждающей жидкости"
type: "Процедура"
doc: "82-t05-422"
title_en: "FAULT CODE 422 - Coolant Level Sensor Circuit"
title_ru: "Код 422 — цепь датчика уровня охлаждающей жидкости"
modified: "2019-01-22"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-422.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-422.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# FAULT CODE 422 - Coolant Level Sensor Circuit
**Код 422 — цепь датчика уровня охлаждающей жидкости**

> [!abstract] Процедура · `82-t05-422`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-01-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-422.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-422.pdf)

Printable Version

## Warnings and Cautions

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[122°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3823995 - male Weather-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for multiple fault codes and the presence of the coolant level sensor. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 187 active or inactive with more than one count logged in the last 25 engine hours? |
|  | **STEP 1B.** Check if vehicle has a coolant level sensor. | Coolant level sensor present? |
|  | **STEP 1B-1.** Check if a coolant level sensor is used in the application, or if a shorting plug is installed in the coolant level sensor harness connection. | Shorting plug installed? |
| STEP 2. | Check the coolant level sensor. |  |
|  | **STEP 2A.** Inspect the engine harness and coolant level sensor connectors. | Dirty or damaged pins? |
|  | **STEP 2B.** Inspect the engine harness and the engine control module (ECM) connectors. | Dirty or damaged pins? |
|  | **STEP 2C.** Check for an open circuit in the coolant level sensor circuit. | Less than 10 ohms? |
|  | **STEP 2C-1.** Inspect the original equipment manufacturer (OEM) harness sensor connector and 31 pin OEM connector pins. | Dirty or damaged pins? |
|  | **STEP 2C-2.** Check for an open circuit in the engine harness. | Less than 10 ohms? |
|  | **STEP 2C-3.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
| STEP 3. | Check for a short circuit to ground in the SIGNAL wires. |  |
|  | **STEP 3A.** Check for a short circuit to ground in the coolant level sensor SIGNAL wires. | Greater than 100k ohms? |
|  | **STEP 3A-1.** Check for a short circuit to ground in the engine harness. | Greater than 100k ohms? |
|  | **STEP 3A-2.** Check for a short circuit to ground in the OEM harness. | Greater than 100k ohms? |
| STEP 4. | Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness. |  |
|  | **STEP 4A.** Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness. | Greater than 100k ohms? |
|  | **STEP 4A-1.** Check for a short circuit in the engine harness. | Greater than 100k ohms? |
|  | **STEP 4A-2.** Check for a short circuit in the OEM harness. | Greater than 100k ohms? |
| STEP 5. | Check for a short circuit to ground in the SUPPLY wire. |  |
|  | **STEP 5A.** Check for a short circuit to ground in the SUPPLY wire. | Greater than 100k ohms? |
|  | **STEP 5A-1.** Check for a short circuit in the engine harness. | Greater than 100k ohms? |
|  | **STEP 5A-2.** Check for a short circuit in the OEM harness. | Greater than 100k ohms? |
| STEP 6. | Clear the fault codes. |  |
|  | **STEP 6A.** Disable the fault code. | Fault Code 422 inactive? |
|  | **STEP 6B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check for multiple fault codes and the presence of the coolant level sensor.

#### STEP 1A. Read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Start the engine and idle for one minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 187 active or inactive with more than one count logged in the last 25 engine hours? **YES** | Go to Fault Code 187 troubleshooting tree |
| Fault Code 187 active or inactive with more than one count logged in the last 25 engine hours? **NO** | 1B |  |

#### STEP 1B. Check if vehicle has a coolant level sensor.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check to see if the vehicle has a coolant level sensor. | Coolant level sensor present? **YES** | 2A |
| Coolant level sensor present? **NO** | 1B-1 |  |

#### STEP 1B-1. Check if a coolant level sensor is used in the application, or if a shorting plug is installed in the coolant level sensor harness connection.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check if a shorting plug is installed in the coolant level sensor harness connection. Note: Check the OEM wiring from the shorting plug to the engine harness connection for problems. Reference the OEM and the engine harness wiring diagrams. | If a Shorting plug is used in the application, is it present and properly installed? **YES** | 2A |
| If a Shorting plug is used in the application, is it present and properly installed? **NORepair:** Install the shorting plug. | 6A |  |

### STEP 2. Check the coolant level sensor.

#### STEP 2A. Inspect the harness and the coolant level sensor connectors.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the harness and the coolant level sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the OEM harness, or replace the coolant level sensor, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-208 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. Replace the coolant level sensor. Refer to Procedure 019-017 in Section 19. | 6A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Inspect the engine harness and the ECM connectors.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedures Table. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 6A |
| Dirty or damaged pins? **NO** | 2C |  |

#### STEP 2C. Check for an open circuit in the coolant level sensor circuit.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the coolant level sensor circuit. Measure the resistance from pin 25 in the sensor harness connector to pin C (or 3) on the harness side of the coolant level sensor connector. Measure the resistance from pin 23 in the sensor harness connector to pin B (or 2) on the harness side of the coolant level sensor connector. Measure the resistance from pin 24 in the sensor harness connector to pin D (or 4) on the harness side of the coolant level sensor connector. Measure the resistance from pin 22 in the sensor harness connector to pin A (or 1) on the harness side of the coolant level sensor connector. | Less than 10 ohms? **YES** | 3A |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness or OEM harness. Repair the engine harness. Refer to Procedure 019-208 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedures Table. Replace the OEM harness. Refer to the OEM service manual. | 2C-1 |  |

#### STEP 2C-1. Inspect the OEM harness sensor connector and 31 pin OEM connector pins.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness sensor connector and 31 pin OEM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Repair or replace the engine harness or the OEM harness, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-208 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedure Tables. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-208 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |
| Dirty or damaged pins? **NO** | 2C-2 |  |

#### STEP 2C-2. Check for an open circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the engine harness. Measure the resistance from pin 22 in the sensor harness connector to pin 6 on the engine harness side of the 31 pin OEM connector. Measure the resistance from pin 23 in the sensor harness connector to pin 19 on the engine harness side of the 31 pin OEM connector. Measure the resistance from pin 24 in the sensor harness connector to pin 5 on the engine harness side of the 31 pin OEM connector. Measure the resistance from pin 25 in the sensor harness connector to pin 7 on the engine harness side of the 31 pin OEM connector. | Less than 10 ohms? **YES** | 2C-3 |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness or OEM harness. Repair the engine harness. 019-208 in Section 19. 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedures Table. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |

#### STEP 2C-3. Check for an open circuit in OEM harness.

| **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the OEM harness at the 31 pin OEM connector Disconnect the OEM harness at the Weather-Pack™ four-way connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the OEM harness. Measure the resistance from pin 6 on the OEM harness side of the 31 pin OEM connector to pin A (or 1) on the OEM harness side of the 4 pin connector. Measure the resistance from pin 19 on the OEM harness side of the 31 pin OEM connector to pin B (or 2) on the OEM harness side of the 4 pin connector. Measure the resistance from pin 7 on the OEM harness side of the 31 pin OEM connector to pin C (or 3) on the OEM harness side of the 4 pin connector. Measure the resistance from pin 5 on the OEM harness side of the 31 pin OEM connector to pin D (or 4) on the OEM harness side of the 4 pin connector. | Less than 10 ohms? **YES** | 3A |
| Less than 10 ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Refer to Procedure 019-208 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |

### STEP 3. Check for a short circuit to ground in the SIGNAL wires.

#### STEP 3A. Check for a short circuit to ground in the coolant level sensor SIGNAL wires.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground in the coolant level sensor signal wires. Measure the resistance from pin 22 of the sensor harness connector to engine block ground. Measure the resistance from pin 24 of the sensor harness connector to engine block ground. Measure the resistance from pin 25 of the sensor harness connector to engine block ground. | Greater than 100k ohms? **YES** | 4A |
| Greater than 100k ohms? **NORepair:** Does **not** meet specifications. | 3A-1 |  |

#### STEP 3A-1. Check for a short circuit to ground in the engine harness.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground in the engine harness. Measure the resistance from pin 22 of the sensor harness connector to engine block ground. Measure the resistance from pin 24 of the sensor harness connector to engine block ground. | Greater than 100k ohms? **YES** | 3A-2 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section. Replace the engine harness. Refer to Procedure 019-043 in Section 19 in the Associated Procedure Table. | 6A |  |

#### STEP 3A-2. Check for a short circuit to ground in the OEM harness.

| **Conditions:** Turn keyswitch OFF Disconnect the OEM harness from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground in OEM harness. Measure the resistance from pin A (or 1) on the OEM harness side of the 4 pin connector to engine block ground. Measure the resistance from pin C (or 3) on the OEM harness side of the 4 pin connector to engine block ground. Measure the resistance from pin D (or 4) on the OEM harness side of the 4 pin connector to engine block ground. | Greater than 100k ohms? **YES** | 4A |
| Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |

### STEP 4. Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness.

#### STEP 4A. Check for a short circuit between the SIGNAL wires and any other wires in the engine harness or OEM harness.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM connector from the coolant level sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit between the SIGNAL wires and any other wires in the OEM harness or engine harness. Measure the resistance from pin 22 of the sensor harness connector to all other pins in the connector. Measure the resistance from pin 24 of the sensor harness connector to all other pins in the connector. | Greater than 100k ohms? **YESRepair:** Replace the coolant level sensor. Refer to Procedure 019-017 in the Associated Procedure Table. | 4A-1 |
| Greater than 100k ohms? **NO** | 6A |  |

#### STEP 4A-1. Check for a short circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM connector from the coolant level sensor Disconnect the engine harness from the OEM harness at the 31 pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit in the engine harness. Measure the resistance from pin 22 of the sensor harness connector to pins 24, 23, and 25 of the connector. Measure the resistance from pin 24 of the sensor harness connector to pins 22, 23, and 25 of the connector. | Greater than 100k ohms? **YES** | 4A-2 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associate Procedures Table. | 6A |  |

#### STEP 4A-2. Check for a short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF Disconnect the OEM harness from the coolant level sensor Disconnect the OEM harness at the OEM side of the 31 pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit in the OEM harness. Measure the resistance from pin A (or 1) in the OEM harness connector to pins B (or 2), C (or 3), and D (or 4). Measure the resistance from pin D (or 4) in the OEM harness connector to pins A (or 1), B (or 2), and C (or 3). | Greater than 100k ohms? **YES** | 5A |
| Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |

### STEP 5. Check for a short circuit to ground in the SUPPLY wire.

#### STEP 5A. Check for a short circuit to ground in the SUPPLY wire.

| **Conditions:** Turn keyswitch OFF Disconnect the sensor harness connector from the ECM Disconnect the OEM harness from the coolant level sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground in the SUPPLY wire. Measure the resistance from pin 25 in the sensor harness connector to engine block ground. | Greater than 100k ohms? **YES** | 5A-1 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedure Table. | 6A |  |

#### STEP 5A-1. Check for a short circuit in the sensor harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the sensor harness connector from the ECM. Disconnect the OEM harness from the coolant level sensor. Disconnect the sensor harness from the OEM harness at the 31 pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit in the sensor harness. Measure the resistance from pin 25 of the sensor harness connector to pin 22 of the connector. Measure the resistance from pin 25 of the sensor harness connector to pin 23 of the connector. Measure the resistance from pin 25 of the sensor harness connector to pin 24 of the connector. | Greater than 100k ohms? **YES** | 5A-2 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 6A |  |

#### STEP 5A-2. Check for a short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the sensor harness connector from the ECM. Disconnect the OEM harness from the coolant level sensor. Disconnect the sensor harness from the OEM harness at the 31 pin OEM connector. Disconnect the OEM harness at the Weather-Pack™ four-way connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit in the OEM harness. Measure the resistance from pin C (or 3) in the OEM harness connector to pins A (or 1), B (or 2), and D (or 4). | Greater than 100k ohms? **YES** | 6A |
| Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 6A |  |

### STEP 6. Clear the fault codes.

#### STEP 6A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and idle for one minute. Use INSITE™ electronic service tool to verify that Fault Code 422 is inactive. | Fault Code 422 inactive? **YES** | 6B |
| Fault Code 422 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |

#### STEP 6B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
