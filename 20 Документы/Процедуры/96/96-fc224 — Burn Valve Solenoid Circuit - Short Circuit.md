---
aliases:
  - "Цепь электромагнита клапана впрыска — короткое замыкание"
type: "Процедура"
doc: "96-fc224"
title_en: "Burn Valve Solenoid Circuit - Short Circuit"
title_ru: "Цепь электромагнита клапана впрыска — короткое замыкание"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc224.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc224.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Burn Valve Solenoid Circuit - Short Circuit
**Цепь электромагнита клапана впрыска — короткое замыкание**

> [!abstract] Процедура · `96-fc224`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc224.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc224.pdf)

### Fault Code: 224

### Burn Valve Solenoid Circuit - Short Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 224 PID(P): SPN: FMI: Lamp: Red SRT: | Burn Valve Solenoid Circuit - Short Circuit. The burn solenoid is shorted. | The Centinel™ system will **not** operate. |

![[07800053.png]]

### Circuit Description

The burn valve solenoid controls the flow of oil in the oil control valve during the burn cycle.

### Component Location

The burn valve solenoid is located on top of the oil control valve.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test leads when taking measurements: Male Cannon, Metri-Pack, and Deutsch test lead, Part Number 3822758 Female AMP, Metri-Pack, and Deutsch test lead, Part Number 3822917 Male Deutsch test lead, Part Number 3823993 Female Deutsch test lead, Part Number 3823994 Male Weather-Pack test lead, Part Number 3823995 Female Weather-Pack test lead, Part Number 3823996.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the burn valve solenoid. |  |
|  | **STEP 1A.** Verify the burn valve solenoid is connected to the Centinel™ harness. | Solenoid is connected |
|  | **STEP 1B.** Inspect the burn valve solenoid and Centinel™ harness connectors. | No damaged pins |
|  | **STEP 1C.** Check the Centinel™ control module burn valve solenoid supply voltage. | Battery voltage |
|  | **STEP 1D.** Check the burn valve solenoid for an open. | Less than 120 ohms |
| STEP 2. | Check the Centinel™ harness. |  |
|  | **STEP 2A.** Inspect the Centinel™ harness and the Centinel™ control module connectors. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 2C.** Check for a short circuit to ground. | More than 1k ohms |
|  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 1k ohms |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 224 inactive |

### STEP 1. Check the burn valve solenoid.

#### STEP 1A. Verify the burn valve solenoid is connected to the Centinel™ harness.

| **Conditions:** Turn the keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[96-007-076 — Burn Solenoid\|007-076]]. | Solenoid is connected | 1B |
| **Connect the solenoid to the Centinel™ harness** | 3A |  |

#### STEP 1B. Inspect the burn valve solenoid and the Centinel™ harness connector.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the burn valve solenoid. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 1C |
| **Repair the damaged pins** Repair or replace the Centinel™ harness or the burn valve solenoid, whichever has damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the burn valve solenoid. Refer to Procedure 007-076. Install the appropriate connector seal if damaged or missing. | 3A |  |

#### STEP 1C. Check the Centinel™ control module burn valve solenoid supply voltage.

| **Conditions:** Start the engine. Enter the service mode. Refer to Procedure 007-999. Disconnect the burn valve solenoid from the Centinel™ harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the supply voltage from pin A to pin B on the harness side of the burn valve solenoid within 15 seconds of entering the service mode. Refer to the wiring diagram for connector pin identification. | Approximately = normal battery voltage within 15 seconds after entering the service mode. | 1D |
| **Replace the Centinel™ control module or wiring harness** Replace the Centinel™ control module. Refer to Procedure 019-130. Replace the Centinel™ wiring harness. Refer to Procedure 019-131. | 3A |  |

#### STEP 1D. Check the burn valve solenoid for an open.

| **Conditions:** Turn the keyswitch OFF. Disconnect the burn valve solenoid from the Centinel™ harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A to pin B of the burn valve solenoid connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 120 ohms | 2A |
| **Replace the burn valve solenoid** Refer to Procedure [[96-007-076 — Burn Solenoid\|007-076]]. | 3A |  |

### STEP 2. Check the Centinel™ harness.

#### STEP 2A. Inspect the Centinel™ harness and Centinel™ control module connectors.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| **Repair the damaged pins** Repair or replace the Centinel™ harness or the Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Turn the keyswitch OFF. Disconnect the burn valve solenoid from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Heavy-duty: Measure the resistance from pin 4 of the power relay connector, harness side, to pin A of the burn valve solenoid, harness side. Heavy-duty: Measure the resistance from pin 12 of the Centinel™ harness connector to pin B of the burn valve solenoid, harness side. High-horsepower: Measure the resistance from pin 21 of the Centinel™ harness connector to pin A of the burn valve solenoid, harness side. High-horsepower: Measure the resistance from pin 25 of the Centinel™ harness connector to pin B of the burn valve solenoid, harness side. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C |
| **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |

#### STEP 2C. Check for a short circuit to ground.

| **Conditions:** Turn the keyswitch OFF. Disconnect the burn valve solenoid from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Heavy-duty: Measure the resistance between pin 12 and pin 2 of the Centinel™ harness connector. High-horsepower: Measure the resistance between pin 21 and pin 22 of the Centinel™ harness connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 2D |
| **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |

#### STEP 2D. Check for a short circuit from pin to pin.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the burn valve solenoid. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Heavy-duty: Measure the resistance from pin 12 of the Centinel™ harness connector to all adjacent pins in the connector, excluding pins 1 and 11. High-horsepower: Measure the resistance from pin 21 of the Centinel™ harness connector to all adjacent pins in the connector, excluding pins 1, 20, 22, and 23. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
| **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle power. Start the engine and let it idle for 1 minute. Use the service plug to check output. Verify that Fault Code 224 is inactive. | Fault Code 224 inactive | Complete |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
