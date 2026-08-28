---
aliases:
  - "Код 235 — уровень ОЖ ниже нормы — наивысший уровень"
type: "Процедура"
doc: "122-t05-235"
title_en: "FAULT CODE 235 - Coolant Level - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Код 235 — уровень ОЖ ниже нормы — наивысший уровень"
modified: "2012-07-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 235 - Coolant Level - Data Valid But Below Normal Operating Range - Most Severe Level
**Код 235 — уровень ОЖ ниже нормы — наивысший уровень**

> [!abstract] Процедура · `122-t05-235`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-07-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-235.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for Fault Code 235. | Active or inactive counts of Fault Code 235? |
|  | **STEP 1B.** Check the coolant level. | Coolant level normal? |
| STEP 2. | Check the engine harness and ECM. |  |
|  | **STEP 2A.** Inspect the engine harness and ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the coolant level sensor 1 and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 2C.** Check for an open circuit in the engine harness. | Less than 10 ohms? |
|  | **STEP 2D.** Check for a pin-to-pin short circuit in the engine harness. | Greater than 100k ohms? |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 235 inactive? |
|  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for Fault Code 235.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active or inactive counts of Fault Code 235? **YES** | 1B |
| Active or inactive counts of Fault Code 235? **NO** | Repair complete |  |

#### STEP 1B. Check the coolant level.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

| **Conditions:** Engine coolant temperature below 50°C \[122°F\]. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant level in the radiator top tank or surge tank. Make sure the engine coolant temperature is below 50°C \[122°F\] before removing the radiator cap. | Coolant level normal? **YES** | 2A |
| Coolant level normal? **NORepair:** Fill the radiator top tank or surge tank with coolant. | 3A |  |

### STEP 2. Check the engine harness and ECM.

#### STEP 2A. Inspect the engine harness and ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the engine harness or ECM connector. Clean the connector and pins. Replace the damaged section of the engine harness or the ECM. Check all harnesses connected in series. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 3A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Inspect the coolant level sensor 1 engine harness and the connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the coolant level sensor 1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and the coolant level sensor 1 connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the engine harness or the coolant level sensor 1 connector. Clean the connector and pins. Replace the damaged section of the engine harness or the the coolant level sensor 1. Check all harnesses connected in series. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the harness. Refer to Procedure 019-043 in Section 19. Replace the coolant level sensor 1. Refer to Procedure 019-017 in Section 19. | 3A |
| Dirty or damaged pins? **NO** | 2C |  |

#### STEP 2C. Check for an open circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the coolant level 1 sensor connector from the engine harness. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the coolant level 1-5 volt supply (sensor supply1) SUPPLY pin of the coolant level sensor 1 engine harness connector and the coolant level 1-5 volt supply (sensor supply 1) SUPPLY pin of the engine harness ECM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Refer to the circuit diagram or wiring diagram for connector pin identification. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19]]. | Less than 10 ohms? **YES** | 2D |
| Less than 10 ohms? **NORepair:** An open SUPPLY wire has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 3A |  |

#### STEP 2D. Check for a pin-to-pin short circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance between the coolant level 1 SIGNAL pin and the battery 1 voltage (ECM1) pin of the ECM 4-pin OEM power harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** Return to the troubleshooting steps. A fault should have been detected. | 1A |
| Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit has been detected in the coolant level 1 SIGNAL wire of the engine harness. Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short circuit. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 235 inactive? **YES** | 2B |
| Fault Code 235 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Appropriate troubleshooting steps |  |
