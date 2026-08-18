---
aliases:
  - "Нет передачи данных от блока останова к блоку управления дизелем"
type: "Процедура"
doc: "116-t02-1107"
title_en: "No Data Link Transmission from Shutdown Unit to Diesel Control Unit"
title_ru: "Нет передачи данных от блока останова к блоку управления дизелем"
modified: "2008-04-15"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1107.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1107.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# No Data Link Transmission from Shutdown Unit to Diesel Control Unit
**Нет передачи данных от блока останова к блоку управления дизелем**

> [!abstract] Процедура · `116-t02-1107`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1107.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1107.pdf)

Printable Version

### Symptoms

- No supply voltage (+24-VDC) at SDU410 unit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 unit input signals are switches. These switches are normally open and closed when activated.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box wiring. |  |
|  | **STEP 1A.** Check shutdown unit supply and return wires for an open. | Less than 10 ohms? |
|  | **STEP 3A-1.** Check shutdown unit Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
|  | **STEP 3A-2.** Check the battery voltage 1 supply and return wires for an open. | Less than 10 ohms? |
|  | **STEP 3B.** Check the battery voltage 1 supply and return circuits for supply voltage +24-VDC. | Less than +24-VDC? |
|  | **STEP 3C.** Check the shutdown unit supply +24-VDC and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 3C-1.** Check shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 3C-2.** Check the battery voltage 1 supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 3D.** Check the shutdown unit supply +24-VDC wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 3D-1.** Check shutdown unit Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 3D-2.** Check the battery voltage 1 supply wire for a short to ground. | Less than 10 ohms? |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the shutdown unit supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the supply and return wires at the SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply and return wires for an open. Place one test lead on the shutdown unit supply +24-VDC wire at the SDU410 unit. Place the other test lead on the shutdown unit supply +24-VDC wire at the customer interface box logic unit. Place one test lead on the shutdown unit supply +24-VDC wire at the SDU410 unit. Place the other test lead on the shutdown unit supply +24-VDC pin at the X4 connector. Place one test lead on the shutdown unit return wire at the SDU410 unit. Place the other test lead on the shutdown unit return wire at the customer interface box logic unit. Place one test lead on the shutdown unit return wire at the SDU410 unit. Place the other test lead on the shutdown unit return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 1A-1 |  |

#### STEP 1A-1. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 1A-2 |  |

#### STEP 1A-2. Check the battery voltage 1 supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 supply and return wires at the customer interface box logic unit and the X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 supply and return wires for an open. Place one test lead at the battery voltage 1 supply wire at the customer interface box logic unit. Place the other test lead on the battery voltage 1 supply pin at the X4 connector. Place one test lead at the battery voltage return wire at the customer interface box logic unit. Place the other test lead on the battery voltage return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 1B |  |

#### STEP 1B. Check the battery voltage 1 supply and return circuits for supply voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 supply and return circuits for supply voltage +24-VDC. Place one test lead on the battery voltage 1 supply pin at the X4 connector. Place the other test lead on the battery voltage 1 return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Replace the batteries. Refer to the OEM service manual. | 1C |
| Less than +24-VDC? **NO** | Repair complete |  |

#### STEP 1C. Check the shutdown unit supply +24-VDC and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit supply +24-VDC and return wires from the SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit supply +24-VDC and return wires for a wire-to-wire short. Place one test lead on the shutdown unit supply +24-VDC wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C-1 |  |

#### STEP 1C-1. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C-2 |  |

#### STEP 1C-2. Check the battery voltage 1 supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 supply and return wires from the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the battery voltage 1 supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the battery voltage return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1D |  |

#### STEP 3D. Check the shutdown unit supply +24-VDC wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit supply +24-VDC wire from the SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit supply +24-VDC wire for a short to ground. Place one test lead on the shutdown unit supply +24-VDC at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1D-1 |  |

#### STEP 1D-1. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire from the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1D-2 |  |

#### STEP 1D-2. Check the battery voltage 1 supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 supply wire from the customer interface box logic unit and X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 supply wire for a short to ground. Place one test lead on the battery voltage 1 supply wire at the customer interface box logic unit. Place the other test lead on panel ground. Place one test lead on the battery voltage 1 supply pin at the X4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location |  |
