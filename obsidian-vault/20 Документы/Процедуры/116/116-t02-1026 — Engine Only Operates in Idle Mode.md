---
aliases:
  - "Двигатель работает только на холостом ходу"
type: "Процедура"
doc: "116-t02-1026"
title_en: "Engine Only Operates in Idle Mode"
title_ru: "Двигатель работает только на холостом ходу"
modified: "2007-03-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Engine Only Operates in Idle Mode
**Двигатель работает только на холостом ходу**

> [!abstract] Процедура · `116-t02-1026`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1026.pdf)

Printable Version

### Symptoms

- The engine will **only** operate in idle mode.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine idle symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check Idle/Rated Switch Signal Wire for Short Circuit | Less than 10 ohms resistance? |
| STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
|  | **STEP 2A.** Check Idle/Rated Switch Signal Wire | Less than 10 ohms resistance? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check Idle/Rated Switch Signal Wire for Short Circuit

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check idle/rated switch signal wire. Disconnect the idle/rated switch signal wire from the X4 connector. Place one test lead on the idle/rated switch signal pin in connector C3. Place the other test lead on the battery 1 voltage return terminal of the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the wire(s). Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| Less than 10 ohms resistance? **NO** | 2A |  |

### STEP 2. Check Engine Harness to Customer Interface Box Cable

#### STEP 2A. Check Idle/Rated Switch Signal Wire

| **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check idle/rated switch signal wire. Place one test lead in the idle/rated switch signal pin of the C3 connector. Place the other test lead on another pin in the C3 connector. Repeat for all other pins in the C3 connector. | Less than 10 ohms resistance? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual for idle switch repair instructions. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
