---
aliases:
  - "Нет передачи данных от выносного блока ввода-вывода к блоку управления дизелем"
type: "Процедура"
doc: "116-t02-1115"
title_en: "No Data Link Transmission from Remote Input/Output Unit to Diesel Control Unit"
title_ru: "Нет передачи данных от выносного блока ввода-вывода к блоку управления дизелем"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# No Data Link Transmission from Remote Input/Output Unit to Diesel Control Unit
**Нет передачи данных от выносного блока ввода-вывода к блоку управления дизелем**

> [!abstract] Процедура · `116-t02-1115`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1115.pdf)

Printable Version

### Symptoms

- No communication between the remote input/output unit and the DCU410 unit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box wiring. |  |
|  | **STEP 1A.** Check the remote input/output unit Modicon™ communication bus supply and return wires for an open. |  |
|  | **STEP 1B.** Check the voltage at the remote input/output unit supply wire at the remote input/output unit. |  |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the remote input/output unit Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the remote input/output unit Modicon™ communication bus supply and return wires at the remote input/output unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply and return wires for an open Place one test lead on the remote input/output Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on the remote input/output Modicon™ communication bus supply wire at the remote input/output unit. Place one test lead on the remote input/output Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on the remote input/output Modicon™ communication bus return wire at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the voltage at the remote input/output unit supply wire at the remote input/output unit.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the remote input/output Modicon™ communication bus supply wire. Place one test lead on the remote input/output Modicon™ communication bus supply wire at the remote input/output unit. Place the other test lead on the remote input/output Modicon™ communication bus return wire at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check or replace the batteries. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than +24-VDC? **NO** | Repair complete |  |
