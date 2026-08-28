---
aliases:
  - "Ошибка блока управления Centinel™"
type: "Процедура"
doc: "96-fc111"
title_en: "Centinel™ Control Module Error"
title_ru: "Ошибка блока управления Centinel™"
modified: "2004-03-03"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Centinel™ Control Module Error
**Ошибка блока управления Centinel™**

> [!abstract] Процедура · `96-fc111`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-03-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-fc111.pdf)

### Fault Code: 111

### Centinel™ Control Module Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 111 PID(P): SPN: FMI: Lamp: None SRT: | Centinel™ Control Module Error. An error occurred during the diagnostic test of the Centinel™ control module internal hardware. | The Centinel™ system will **not** operate properly. |

![[05800058.png]]

### Circuit Description

The Centinel™ control module is a computer that is responsible for Centinel™ system control and diagnostics.

### Component Location

Heavy-duty: The Centinel™ control module is located on the Centinel™ system make-up oil tank.

High-horsepower: The Centinel™ control module is located on the Centinel™ system oil control valve mounting bracket.

### Shoptalk

This fault code can be caused **only** by an internal Centinel™ control module problem. **Only** on high-horsepower should you try to clear a fault code with use of the service plug. Repairs are **not** possible for the Centinel™ control module.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid damaging a new Centinel™ control module, all other active fault codes must be investigated prior to replacing the Centinel™ control module.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 111 inactive |
|  | **STEP 1B.** Check the fault codes. | Complete |

### STEP 1. Check the fault codes. (This step is for high-horsepower only. For heavy-duty, continue to Step 1B.)

#### STEP 1A. Read the fault codes.

| **Conditions:** High-horsepower only Connect all components. Turn the keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using diagnostic lamp. | Fault Code 111 inactive | Complete |
| High-horsepower **only**: Clear the fault codes with the service plug. Refer to Procedure [[96-209-001 — System Description\|209-001]]. | 1B |  |

#### STEP 1B. Check the fault codes.

| **Conditions:** Turn the keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault code. | Fault Code 111 inactive | Complete |
| Replace the Centinel™ control module Refer to Procedure [[96-019-130-tr — Centinel™ Control Module\|019-130]]. | Complete |  |
