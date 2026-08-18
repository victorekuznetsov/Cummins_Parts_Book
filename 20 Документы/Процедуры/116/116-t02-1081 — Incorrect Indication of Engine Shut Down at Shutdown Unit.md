---
aliases:
  - "Неверная индикация останова двигателя на блоке останова"
type: "Процедура"
doc: "116-t02-1081"
title_en: "Incorrect Indication of Engine Shut Down at Shutdown Unit"
title_ru: "Неверная индикация останова двигателя на блоке останова"
modified: "2008-03-20"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1081.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1081.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Incorrect Indication of Engine Shut Down at Shutdown Unit
**Неверная индикация останова двигателя на блоке останова**

> [!abstract] Процедура · `116-t02-1081`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-03-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1081.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1081.pdf)

Printable Version

### Symptoms

- No communication between the SDU410 unit and DCU410 unit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box |  |
|  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
|  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
| STEP 2. | Check customer interface box wiring |  |
|  | **STEP 2A.** Check the engine protection override signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 2B.** Check the engine protection override relay for an open. | Less than 10 ohms? |
|  | **STEP 2C.** Check the shutdown unit Modicon™ communication bus supply and return wires for an open | Less than 10 ohms? |

### STEP 1. Check customer interface box

#### STEP 1A. Check the customer interface box logic unit LED illumination.

| **Conditions:** Check the DCU410 unit for alarms and LED illumination. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for alarms and LED illumination on the DCU410 unit. | Are any alarms active or LEDs illuminated? **YES** | Contact a Cummins® Authorized Repair Location |
| Are any alarms active or LEDs illuminated? **NO** | 1B |  |

#### STEP 1B. Check the DCU410 power supply wire for +24-VDC.

| **Conditions:** Open the customer interface box |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the shutdown unit supply 24-VDC at the SDU410 unit. Place one test lead on the shutdown unit supply 24-VDC supply wire at the SDU410 unit. Place the other test lead on the shutdown unit return wire at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than +24-VDC? **NO** | 2A |  |

### STEP 2. Check customer interface box wiring

#### STEP 2A. Check the engine protection override signal and return wires for an open.

| **Conditions:** Open the customer interface box Disconnect the engine protection override signal and return wires at the SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engne protection override signal and return wires for an open. Place one test lead on the engine protection override signal wire at the SDU410 unit. Place the other test lead on the engine protection override signal wire at the DCU410 unit. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | 2B |  |

#### STEP 2B. Check the engine protection override relay for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override signal and return wires at the engine protection override relay contact. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override relay contacts for an open. Place one test lead on the engine protection override relay signal wire at the SDU410 unit. Place the other test lead on the engine protection override signal wire at the relay contact. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override return wire at the relay contact. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the relay. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location for replacement of the customer interface box relay. | 2C |  |

#### STEP 2C. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override relay contacts for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location for replacement of the customer interface box relay. | Contact a Cummins® Authorized Repair Location |  |
