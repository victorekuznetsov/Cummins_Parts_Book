---
aliases:
  - "Расход топлива выше диапазона"
type: "Процедура"
doc: "96-fc327"
title_en: "Fuel Rate - Out of Range High"
title_ru: "Расход топлива выше диапазона"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc327.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc327.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Fuel Rate - Out of Range High
**Расход топлива выше диапазона**

> [!abstract] Процедура · `96-fc327`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc327.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc327.pdf)

### Fault Code: 327

### Fuel Rate - Out of Range High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 327 PID(P): SPN: FMI: Lamp: Red SRT: | Fuel Rate - Out of Range High. The Centinel™ control module detected a fuel rate out of range high signal from the electronic control module (ECM). | The Centinel™ system will **not** operate properly. |

![[05800058.png]]

### Circuit Description

The Centinel™ control module monitors the engine dynamics via information from the electronic control module (ECM). If the fuel rate is out of range, the Centinel™ control module will display a fault.

### Component Location

Heavy-Duty: The Centinel™ control module is located on the Centinel™ system make-up oil tank.

High-Horsepower: The Centinel™ control module is located on the Centinel™ system oil control valve mounting bracket.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fuel rate data OK |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 327 inactive |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for active fault codes.

| **Conditions:** Turn the keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify ECM fuel rate data using INSITE™ electronic service tool. | **Fuel rate data OK** | 2A |
| **Reprogram the ECM** Refer to Procedure [[105-019-032 — Engine Control Module Calibration Code\|019-032]] and the INSITE™ user manual. | 2A |  |

### STEP 2. Clear the fault code.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect all the components. Start the engine and let it idle for 1 minute. Verify Fault Code 327 is inactive. | **Fault Code 327 inactive** | Complete |
| Return to the troubleshooting step or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
