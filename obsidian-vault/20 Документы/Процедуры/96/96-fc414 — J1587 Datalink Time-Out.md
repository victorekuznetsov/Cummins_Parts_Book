---
aliases:
  - "Тайм-аут шины данных J1587"
type: "Процедура"
doc: "96-fc414"
title_en: "J1587 Datalink Time-Out"
title_ru: "Тайм-аут шины данных J1587"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc414.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc414.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# J1587 Datalink Time-Out
**Тайм-аут шины данных J1587**

> [!abstract] Процедура · `96-fc414`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc414.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc414.pdf)

### Fault Code: 414

### J1587 Datalink Time-Out

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 414 PID(P): SPN: FMI: Lamp: SRT: | J1587 Datalink Time-Out. The data was **not** received by the Centinel™ control module within the specified time. | The Centinel™ system will **not** monitor engine dynamics and can **not** operate. |

![[19803802.png]]

### Circuit Description

The J1587 datalink provides communications capability between the parent engine electronic control module (ECM) and the Centinel™ control module. This allows the Centinel™ system the ability to monitor engine dynamics. Using these data, the Centinel™ system is able to function within the specified parameters.

### Component Location

### Shoptalk

Before proceeding with this fault code, make certain that the Centinel™ wiring harness connector is securely connected to the J1587 datalink.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test leads when taking measurements: Male Cannon, Merti-Pack, and Deutsch test lead, Part Number 3822758 Female AMP, Metri-Pack, and Deutsch test lead, Part Number 3822917 Male Deutsch test lead, Part Number 3823993 Female Deutsch test lead, Part Number 3823994.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the datalink. |  |
|  | **STEP 1A.** Inspect datalink connector. | No damaged pins |
| STEP 2. | Check the Centinel™ wiring harness. |  |
|  | **STEP 2A.** Check for reversed wires. | Pin A: 4 VDC; Pin B: 1 VDC |
|  | **STEP 2B.** Inspect Centinel™ control module connector pins. | No damaged pins |
|  | **STEP 2C.** Check for short circuit. | More than 1k ohms |
| STEP 3. | Clear the fault code. |  |
|  | **STEP 3A.** Disable fault code. | Fault Code 414 inactive |

### STEP 1. Check data link.

#### STEP 1A. Inspect datalink connector.

| **Conditions:** Turn the keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2A |
| **Repair damaged pins** Repair or replace the control datalink connector. Refer to Procedure [[99-019-207 — Deutsch HD10 Connector Series\|019-207]] or [[99-019-203 — AMP Connector Series\|019-203]]. | 3A |  |

### STEP 2. Check the Centinel™ wiring harness.

#### STEP 2A. Check for reversed wires.

| **Conditions:** Turn the keyswitch ON. Disconnect the Centinel™ wiring harness from the Centinel™ control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 8 on the harness side of the Centinel™ control module connector to pin 2. Measure the voltage from pin 9 on the harness side of the Centinel™ control module connector to pin 2. Refer to the wiring diagram for connector pin identification. | Pin 8 to pin 2: Approximately 4 VDC; Pin 9 to pin 2: Approximately 1 VDC | 2B |
| **If voltages are opposite of specification, reverse the wires** | 3A |  |

#### STEP 2B. Inspect the Centinel™ wiring harness and Centinel™ control module connectors.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ wiring harness from the Centinel™ control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2C |
| **Repair the damaged pins** Repair or replace the Centinel™ wiring harness or Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |

#### STEP 2C. Check for a short circuit from pin to pin.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ wiring harness from the Centinel™ control module. Disconnect the Centinel™ wiring harness from the datalink circuit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 8 of the Centinel™ module connector to all other pins. Measure the resistance from pin 9 of the Centinel™ module connector to all other pins. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
| **Replace the Centinel™ control module** Refer to Procedure [[96-019-130-tr — Centinel™ Control Module\|019-130]]. | 3A |  |

### STEP 3. Clear the fault code.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify Fault Code 414 is inactive. | Fault Code 414 inactive | Complete |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and rechecked. | 1A |  |
