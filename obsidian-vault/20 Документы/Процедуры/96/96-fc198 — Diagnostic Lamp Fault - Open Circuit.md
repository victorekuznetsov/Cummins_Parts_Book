---
aliases:
  - "Неисправность диагностической лампы — обрыв"
type: "Процедура"
doc: "96-fc198"
title_en: "Diagnostic Lamp Fault - Open Circuit"
title_ru: "Неисправность диагностической лампы — обрыв"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc198.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc198.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Diagnostic Lamp Fault - Open Circuit
**Неисправность диагностической лампы — обрыв**

> [!abstract] Процедура · `96-fc198`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc198.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc198.pdf)

### Fault Code: 198

### Diagnostic Lamp Fault - Open Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 198 PID(P): SPN: FMI: Lamp: SRT: | Diagnostic Lamp Fault - Open Circuit. The diagnostic lamp is open. | Centinel™ system status or fault indications will **not** be properly displayed. |

![[05800060.png]]

### Circuit Description

The Centinel™ control module constantly monitors the operational parameters of the system. The status of the system is displayed by means of diagnostic lamps. There are two Centinel™ diagnostic lamps. They are green and red in color. The green lamp illuminates to indicate that the system's operational parameters are within specified tolerances for heavy-duty **only**. For high-horsepower, the green light indicates the system has power. The red lamp illuminates to indicate that a system parameter is out of specified tolerances.

### Component Location

Heavy-duty engines: The diagnostic lamps are located on the Centinel™ control module, located on the make up oil tank.

High-horsepower engines: The diagnostic lamps are located on the diagnostic lamp assembly on the oil make-up tank.

### Shoptalk

There is no repair procedure for the heavy-duty. The module **must** be replaced. The following procedure pertains to high-horsepower **only**. Be certain the voltage of the high-horsepower diagnostic lamp assembly matches the application.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test lead when taking measurements: Female AMP, Metri-Pack and Deutsch test lead, Part Number 3822917.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the diagnostic lamps. |  |
|  | **STEP 1A.** Inspect the diagnostic lamps and Centinel™ harness connectors (high-horsepower only.) | No damaged pins |
|  | **STEP 1B.** Check the diagnostic lamps for an open. | Less than 2M ohms |
|  | **STEP 1C.** Check the diagnostic lamps for a short. | More than 10 ohms |
| STEP 2. | Check the Centinel™ harness. |  |
|  | **STEP 2A.** Inspect the Centinel™ harness and the Centinel™ control module connectors. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 2C.** Check for a short circuit to ground. | More than 1k ohms |
|  | **STEP 2D.** Check for a short circuit from pin to pin. | More than 1k ohms |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Connect all the components. | Fault Codes 198 inactive |

### STEP 1. Check the diagnostic lamps.

#### STEP 1A. Inspect the diagnostic lamps and Centinel™ harness connectors (high-horsepower only.)

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the diagnostic lamp assembly for high-horsepower systems. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 1B |
| **Repair the damaged pins** Repair or replace the Centinel™ harness or the diagnostic lamp assembly, whichever has damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the diagnostic lamp assembly. Refer to Procedure 208-001. Install the appropriate connector seal if damaged or missing. | 3A |  |

#### STEP 1B. Check the diagnostic lamp assembly for an open.

| **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| High-horsepower: Measure the resistance from pin A to pin D on the diagnostic lamp assembly connector for the green lamp circuit and from pin D to pin B for the red lamp circuit. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 2M ohms | 1C |
| **Replace the diagnostic lamp assembly** Refer to Procedure [[96-208-001 — Component Identification\|208-001]]. | 3A |  |

#### STEP 1C. Check the diagnostic lamp assembly for a short.

| **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| High-horsepower: Measure the resistance from pin A to pin D on the diagnostic lamp assembly connector for the green lamp circuit and from pin D to pin B for the red lamp circuit. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 10 ohms | 2A |
| **Replace the diagnostic lamp assembly** Refer to Procedure [[96-208-001 — Component Identification\|208-001]]. | 3A |  |

### STEP 2. Check the high-horsepower Centinel™ harness.

#### STEP 2A. Inspect the Centinel™ harness and Centinel™ control module connectors.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the Centinel™ control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Wire insulation damage Connector shell broken Damaged locking tab connector. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| **Repair the damaged pins** Repair or replace the Centinel™ harness or the Centinel™ control module, whichever has the damaged pins. Repair the Centinel™ harness. Refer to Procedure 019-202. Replace the Centinel™ harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty applications only). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| High-horsepower: Measure the resistance from pin 1 of the Centinel™ harness connector to pin A of the diagnostic lamp assembly, harness side. High-horsepower: Measure the resistance from pin 25 of the Centinel™ harness connector to pin B of the diagnostic lamp assembly, harness side. High-horsepower: Measure the resistance from pin 22 of the Centinel™ harness connector to pin C of the diagnostic lamp assembly, harness side. High-horsepower: Measure the resistance from pin 10 of the Centinel™ harness connector to pin D of the diagnostic lamp assembly, harness side. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C |
| **Replace the Centinel™ wiring harness** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 3A |  |

#### STEP 2C. Check for a short circuit to ground.

| **Conditions:** Turn the keyswitch OFF. Disconnect the diagnostic lamp assembly from the Centinel™ harness. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty applications only). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| High-horsepower: Measure the resistance from pin 1 of the Centinel™ harness connector to pin 25. High-horsepower: Measure the resistance from pin 22 of the Centinel™ harness connector to pin 25. High-horsepower: Measure the resistance from pin 10 of the Centinel™ harness connector to pin 22. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 2D |
| **Replace the Centinel™ wiring harness or Centinel™ control module** Replace the Centinel™ wiring harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |

#### STEP 2D. Check for a short circuit from pin to pin.

| **Conditions:** Turn the keyswitch OFF. Disconnect the Centinel™ harness from the diagnostic lamp assembly. Disconnect the Centinel™ harness from the Centinel™ control module. Disconnect the power relay from the Centinel™ harness (heavy-duty engines only). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| High-horsepower: Measure the resistance from pins 1, 10, 22, and 25 of the Centinel™ harness connector to all other pins in the connector. Refer to the wiring diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 1k ohms | 3A |
| **Replace the Centinel™ wiring harness or Centinel™ control module** Replace the Centinel™ wiring harness. Refer to Procedure 019-131. Replace the Centinel™ control module. Refer to Procedure 019-130. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start the engine and let it idle for 1 minute. Verify that Fault Code 198 is inactive. | Fault Code 198 inactive | Complete |
| **Replace the Centinel™ control module** Replace the Centinel™ control module if the fault codes are active. Refer to Procedure 019-130. | Complete. |  |
