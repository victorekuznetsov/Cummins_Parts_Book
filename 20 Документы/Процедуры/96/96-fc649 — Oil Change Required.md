---
aliases:
  - "Требуется замена масла"
type: "Процедура"
doc: "96-fc649"
title_en: "Oil Change Required"
title_ru: "Требуется замена масла"
modified: "2004-03-03"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc649.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc649.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Oil Change Required
**Требуется замена масла**

> [!abstract] Процедура · `96-fc649`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc649.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc649.pdf)

### Fault Code: 649

### Oil Change Required

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 649 PID(P): SPN: FMI: Lamp: Red SRT: | Oil Change Required. The Centinel™ control module detected an Oil Change Required signal from the ECM. | The Centinel™ system will **not** operate. |

![[05800058.png]]

### Circuit Description

The Centinel™ control module monitors the engine dynamics via information from the electronic control module (ECM). If the oil requires changing, the Centinel™ control module will display a fault.

### Component Location

Heavy-duty: The Centinel™ control module is located on the Centinel™ system make-up oil tank.

High-horsepower: The Centinel™ control module is located on the Centinel™ system oil control valve mounting bracket.

### Shoptalk

The oil change required is set if another fault existed for some time. Make certain all faults have been cleared and make certain the oil and filter are changed before clearing the fault.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 649 active. |
| STEP 2. | Clear the fault codes. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 649 inactive. |

### STEP 1. Check the fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn the keyswitch ON. Engine is not running |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Heavy-duty and high-horsepower: Change the oil and filter. High-horsepower: Check oil versus fuel usage. | Heavy-Duty: change oil and filter High-Horsepower: change oil and filter Standard oil = 300 gallons of fuel to 1 gallon of oil Advanced oil = 400 gallons of fuel to 1 gallon of oil. | 2A |
| **High-horsepower: Check oil usage versus fuel usage** Recalibrate the Centinel™ control module duty cycle parameter using INSITE™, raising the duty cycle up one level. Three levels, light 45 percent, medium 75 percent, and heavy 95 percent. | Heavy-duty: Complete High-horsepower: 2A |  |

### STEP 2. Clear the fault codes,

#### STEP 2A. Disable the fault codes,

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the oil change required fault. Refer to 007-999. Connect all the components. Start the engine and let idle for 1 minute. Verify that Fault Code 649 is inactive. | Fault Code 649 inactive | Complete |
| Return to the troubleshooting step or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
