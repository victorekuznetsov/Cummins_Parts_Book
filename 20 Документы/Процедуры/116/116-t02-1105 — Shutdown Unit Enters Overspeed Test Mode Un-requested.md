---
aliases:
  - "Блок останова самопроизвольно входит в режим проверки разноса"
type: "Процедура"
doc: "116-t02-1105"
title_en: "Shutdown Unit Enters Overspeed Test Mode Un-requested"
title_ru: "Блок останова самопроизвольно входит в режим проверки разноса"
modified: "2008-04-15"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1105.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1105.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Shutdown Unit Enters Overspeed Test Mode Un-requested
**Блок останова самопроизвольно входит в режим проверки разноса**

> [!abstract] Процедура · `116-t02-1105`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1105.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1105.pdf)

Printable Version

### Symptoms

- Engine speed circuit has malfunctioned.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 input signals are switches. These switches are normally open and closed when activated.

Overspeed test mode is internal to SDU410 unit. No external wiring.

- The overspeed button **must** be pressed 2 seconds to enter the overspeed test mode

- The overspeed test mode times out after 4 minutes

- Can **not** enter an overspeed test mode if an actual overspeed condition exists.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for active fault codes. | Any fault codes active? |
| STEP 2. | Check engine speed. |  |
|  | **STEP 2A.** Check the engine speed reading on the SDU410 unit. | Engine speed above 1400 rpm? |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for active fault codes.

| **Conditions:** Turn keyswitch ON. Check the DCU410 for active fault codes. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. | Any active fault codes? **YESRepair:** Troubleshoot the appropriate fault code. For QSK19 engines, refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021490. For QSK38, QSK50 and QSK60 engines, refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 CM850 Modular Common Rail System, Bulletin 4021533. | Repair complete |
| Any active fault codes? **NO** | 2A |  |

### STEP 2. Check the engine speed.

#### STEP 2A. Check the engine speed reading on the SDU410 unit.

| **Conditions:** Check engine speed on the SDU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed reading on the SDU410 unit. Check the engine speed. Verify engine speed is above on the SDU410 unit display. | Engine speed above 1400 rpm? **YESRepair:** Check SDU410 configuration. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Engine speed above 1400 rpm? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Clear the inactive fault codes.

| **Conditions:** Turn keyswitch ON. Check the DCU410 unit for inactive fault codes. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Check the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Contact a Cummins® Authorized Repair Location. |  |
