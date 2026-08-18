---
aliases:
  - "Изменения конфигурации блока останова не записываются"
type: "Процедура"
doc: "116-t02-1111"
title_en: "Shutdown Unit Configuration Changes Not Recorded"
title_ru: "Изменения конфигурации блока останова не записываются"
modified: "2008-04-15"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Shutdown Unit Configuration Changes Not Recorded
**Изменения конфигурации блока останова не записываются**

> [!abstract] Процедура · `116-t02-1111`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1111.pdf)

Printable Version

### Symptoms

- The engine shuts down with no indication from the SDU410 Modicon™ communication bus circuit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 unit input signals are switches. These switches are normally open and closed when activated.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box wiring. |  |
|  | **STEP 1A.** Check shutdown unit Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1B.** Check shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1C.** Check shutdown unit Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire from the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | Troubleshooting procedures **must** be checked again. A fault mode should have been detected. |  |
