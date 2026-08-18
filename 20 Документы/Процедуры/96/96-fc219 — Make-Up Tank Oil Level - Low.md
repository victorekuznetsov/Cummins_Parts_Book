---
aliases:
  - "Низкий уровень масла в баке подпитки"
type: "Процедура"
doc: "96-fc219"
title_en: "Make-Up Tank Oil Level - Low"
title_ru: "Низкий уровень масла в баке подпитки"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc219.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc219.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Make-Up Tank Oil Level - Low
**Низкий уровень масла в баке подпитки**

> [!abstract] Процедура · `96-fc219`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc219.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc219.pdf)

### Fault Code: 219

### Make-Up Tank Oil Level - Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 219 PID(P): SPN: FMI: Lamp: Red SRT: | Make-Up Tank Oil Level - Low. This fault code is displayed to indicate that the make-up oil tank oil is below specified levels. | The Centinel™ system will **not** operate. |

![[05800061.png]]

### Circuit Description

The make-up tank oil level low sensor monitors the oil level in the make-up oil tank and reports to the Centinel™ control module when the oil drops below the specified level.

### Component Location

The make-up tank oil level low sensor is located on the lower portion of the front of the Centinel™ system make-up oil tank.

### Shoptalk

Verify that the make-up tank has the appropriate level of oil.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test leads when taking measurements: Male Cannon, Metri-Pack, and Deutsch test lead, Part Number 3822758 Female AMP, Metri-Pack, and Deutsch test lead, Part Number 3822917 Male Deutsch test lead, Part Number 3823993 Female Deutsch test lead, Part Number 3823994 Male Weather-Pack test lead, Part Number 3823995 Female Weather-Pack test lead, Part Number 3823996.**

> [!warning] CAUTION · Осторожно
>

**The component can be damaged internally if dropped.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the make-up tank oil level low sensor. |  |
|  | **STEP 1A.** Inspect the make-up tank oil level low sensor and Centinel™ harness connectors. | No damaged pins |
|  | **STEP 1B.** Check the make-up tank oil level low sensor for an open. | Less than 100 ohms |
| STEP 2. | Check the Centinel™ harness. |  |
|  | **STEP 2A.** Inspect the Centinel™ harness and the Centinel™ control module connectors. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 2C.** Check for a short circuit from pin to pin. | More than 1k ohms |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 219 inactive |

### STEP 1. Check the make-up tank oil level low sensor.

#### STEP 1A. Inspect the make-up tank oil level low sensor and the Centinel™ harness connector.

| **Conditions:** Fill the make-up oil tank. Turn the keyswitch OFF. Disconnect the Centinel™ harness from the make-up tank oil level low sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 1B |
| **Repair the damaged pins** Repair or replace the Centinel™ harness or the make-up tank oil level low sensor, whichever has damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the make-up tank oil level low sensor. Refer to Procedure 019-056. Install the appropriate connector seal if damaged or missing. | 3A |  |

#### STEP 1B. Check the make-up tank oil level low sensor for an open.

| **Conditions:** Fill the make-up oil tank. Turn the keyswitch OFF. Disconnect the make-up tank oil level low sensor from the Centinel™ harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A to pin B of the make-up tank oil level low sensor connector while the sensor is covered with oil. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 100 ohms | 2A |
| **Replace the make-up tank oil level low sensor** Refer to Procedure [[96-019-056-tr — Lubricating Oil Level Sensor\|019-056]]. | 3A |  |

### STEP 2. Check the Centinel™ wiring harness.

#### STEP 2A. Inspect the Centinel™ wiring harness and Centinel™ control module connectors.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| **Repair the damaged pins** Repair or replace the Centinel™ harness or the Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Turn the keyswitch OFF. Disconnect the make-up tank oil level low sensor from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Heavy-duty: Measure the resistance from pin 7 of the Centinel™ harness connector to pin A of the make-up tank oil level low sensor, harness side. Heavy-duty: Measure the resistance from pin 3 of the Centinel™ harness connector to pin B of the make-up tank oil level low sensor, harness side. High-horsepower: Measure the resistance from pin 13 of the Centinel™ harness connector to pin A of the make-up tank oil level low sensor, harness side. High-horsepower: Measure the resistance from pin 26 of the Centinel™ harness connector to pin B of the make-up tank oil level low sensor, harness side. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C |
| **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |

#### STEP 2C. Check for a short circuit from pin to pin.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the make-up tank oil level low sensor. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Heavy-duty: Measure the resistance from pins 3 and 1 of the Centinel™ harness connector to all adjacent pins in the connector. High-horsepower: Measure the resistance from pins 13 and 22 of the Centinel™ harness connector to all adjacent pins in the connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
| **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start the engine and let it idle for at least 1 minute. Verify that Fault Code 219 is inactive. | Fault Code 219 inactive | Complete |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
