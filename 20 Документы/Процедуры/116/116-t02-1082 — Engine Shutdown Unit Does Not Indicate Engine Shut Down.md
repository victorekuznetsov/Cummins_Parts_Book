---
aliases:
  - "Блок останова не индицирует останов двигателя"
type: "Процедура"
doc: "116-t02-1082"
title_en: "Engine Shutdown Unit Does Not Indicate Engine Shut Down"
title_ru: "Блок останова не индицирует останов двигателя"
modified: "2008-04-04"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1082.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1082.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Engine Shutdown Unit Does Not Indicate Engine Shut Down
**Блок останова не индицирует останов двигателя**

> [!abstract] Процедура · `116-t02-1082`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1082.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1082.pdf)

Printable Version

### Symptoms

- The engine shuts down with no communication between the DCU410 and SDU410 Modicon™ communication bus circuit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

NOTE: Check the DCU410 troubleshooting manual before performing any of the following steps. If there is communication, then the engine shutdown was **not** caused by the SDU410. If the LED is illuminated on the SDU410 unit, then the problem is in the DCU410 or the SDU410 unit. If no LED is illuminated then the SDU410 is **not** the root of the cause.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box wiring |  |
|  | **STEP 1A.** Check the Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1B.** Check the Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1C.** Check the Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |

### STEP 1. Check customer interface box wiring

#### STEP 1A. Check the Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the Modicon™ communication bus supply and return wire at the SDU410 and DCU410 terminal strips. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the Modicon™ communication bus supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the Modicon™ communication bus supply and return wires at the SDU410 and DCU410 terminal strips. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on each of the other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on each of the other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on each of the other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on each of the other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the Modicon™ communication bus supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the Modicon™ communication bus supply wire at the SDU410 and DCU410 units. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply wire for short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Loaction |  |
