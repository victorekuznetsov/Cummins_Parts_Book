---
aliases:
  - "Код 465 — цепь управления перепускным клапаном турбины 1 — напряжение выше нормы"
type: "Процедура"
doc: "82-t05-465"
title_en: "FAULT CODE 465 - Turbocharger 1 Wastegate Control Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 465 — цепь управления перепускным клапаном турбины 1 — напряжение выше нормы"
modified: "2012-11-01"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-465.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-t05-465.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# FAULT CODE 465 - Turbocharger 1 Wastegate Control Circuit - Voltage Above Normal or Shorted to High Source
**Код 465 — цепь управления перепускным клапаном турбины 1 — напряжение выше нормы**

> [!abstract] Процедура · `82-t05-465`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-11-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-465.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-t05-465.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the wiring harness. |  |
|  | **STEP 1A.** Inspect the actuator harness and ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 1B.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
|  | **STEP 1C.** Check for a short circuit to the battery. | Less than (+) 1.5-VDC? |
| STEP 2. | Check the wastegate actuator. |  |
|  | **STEP 2A.** Inspect the wastegate actuator connector. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the actuator solenoid post for corrosion. | Corrosion found? |
|  | **STEP 2C.** Check the wastegate actuator resistance. | Resistance from 7 to 8 ohms for 12-VDC solenoids and 28 to 32 ohms for 24-VDC solenoids? |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 465 inactive? |
|  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the wiring harness.

#### STEP 1A. Inspect the actuator harness and ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the wastegate actuator number 1. Disconnect the actuator harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the appropriate circuit or wiring diagram for connector pin identification. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair or replace the engine harness or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Use electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 3A |
| Dirty or damaged pins? **NO** | 1B |  |

#### STEP 1B. Check for a pin-to-pin short circuit.

| **Conditions:** Turn keyswitch OFF Disconnect the actuator harness connector from the ECM Disconnect the engine harness from the wastegate actuator 1. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance from pin 24 in the actuator harness connector to all other pins in the connector. Use the following procedure for general resistance measurement techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19]]. | Greater than 100k ohms? **YES** | 1C |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

#### STEP 1C. Check for a short circuit to the battery.

| **Conditions:** Turn keyswitch OFF Disconnect the actuator harness connector from the ECM Disconnect the engine harness from the wastegate actuator 1. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to the battery. Measure the voltage from pin 1 of the wastegate actuator connector to engine block ground. Measure the voltage from pin 24 of the actuator harness connector to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19]]. | Less than (+) 1.5-VDC? **YES** | 2A |
| Less than (+) 1.5-VDC? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

### STEP 2. Check the wastegate actuator.

#### STEP 2A. Inspect the wastegate actuator connector.

| **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the wastegate actuator 1. Disconnect the actuator harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the wastegate actuator connector for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the appropriate circuit or wiring diagram for connector pin identification. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the actuator connector terminal. Flush the dirt, debris, or moisture from the connector pins. Use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if is is damaged or missing. Repair the actuator connector. Refer to Procedure 019-197 in Section 19. | 3A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the actuator solenoid post for corrosion.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the solenoid post for corrosion. | Corrosion found on solenoid post? Clean the solenoid post. **YES** | 3A |
| Corrosion found on solenoid post? **NO** | 2C |  |

#### STEP 2C. Check the wastegate actuator resistance.

| **Conditions:** Turn keyswitch OFF Disconnect the wastegate actuator from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the wastegate actuator resistance. Measure the resistance from the wastegate actuator to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Resistance from 7 to 8 ohms for 12-VDC solenoids and 28 to 32 for 24-VDC solenoids? **YESRepair:** Replace the ECM. [[82-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 3A |
| Resistance from 7 to 8 ohms for 12-VDC solenoids and 28 to 32 for 24-VDC solenoids? **NORepair:** Replace the actuator solenoid. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify Fault Code 465 is inactive. | Fault Code 465 inactive? **YES** | 3B |
| Fault Code 465 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 3B. Clear the inactive fault codes.

| **Conditions:** Connect all components Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | **Repair complete.** |
| All fault codes cleared? **NO** | **Troubleshoot any remaining active fault codes** |  |
