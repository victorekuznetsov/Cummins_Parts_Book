---
aliases:
  - "Двигатель работает только на холостом ходу"
type: "Процедура"
doc: "300-t02-1026"
title_en: "Engine Only Operates in Idle Mode"
title_ru: "Двигатель работает только на холостом ходу"
modified: "2019-05-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Engine Only Operates in Idle Mode
**Двигатель работает только на холостом ходу**

> [!abstract] Процедура · `300-t02-1026`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1026.pdf)

Printable Version

### Symptoms

- The engine will **only** operate in idle mode.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine idle symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

None.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box (C.I.B.) |  |
|  | **STEP 1A.** Check the idle/rated switch SIGNAL wire for short circuit. | Greater than 100k ohms? |
| STEP 2. | Check the the engine harness to the C.I.B. cable. |  |
|  | **STEP 2A.** Check the idle/rated switch SIGNAL wire. | Less than 10 ohms? |

### STEP 1. Check the C.I.B. wiring.

#### STEP 1A. Check the idle/rated switch SIGNAL wire for short circuit.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check idle/rated switch SIGNAL wire. Disconnect the idle/rated switch SIGNAL wire from the X1 connector. Place one test lead on the idle/rated switch SIGNAL pin in connector C1. Place the other test lead on the battery 1 voltage return terminal of the cascade module. | Greater than 100k ohms? **YESRepair:** Replace the wire(s). [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
| Greater than 100k ohms? **NO** | 2A |  |

### STEP 2. Check the engine harness to the C.I.B. cable.

#### STEP 2A. Check the idle/rated switch SIGNAL wire.

| **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C4 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the idle/rated switch SIGNAL wire. Place one test lead in the idle/rated switch SIGNAL pin of the C1 connector. Place the other test lead on another pin in the C1 connector. Repeat for all other pins in the C1 connector. | Less than 10 ohms? **YESRepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or the ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or the X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
