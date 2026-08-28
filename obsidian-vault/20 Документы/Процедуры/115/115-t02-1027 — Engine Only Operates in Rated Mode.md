---
aliases:
  - "Двигатель работает только в номинальном режиме"
type: "Процедура"
doc: "115-t02-1027"
title_en: "Engine Only Operates in Rated Mode"
title_ru: "Двигатель работает только в номинальном режиме"
modified: "2006-06-12"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Only Operates in Rated Mode
**Двигатель работает только в номинальном режиме**

> [!abstract] Процедура · `115-t02-1027`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1027.pdf)

Printable Version

### Symptoms

- The engine will **only** operate in rated mode.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected | Less than 10 ohms resistance? |
|  | **STEP 1B.** Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected | Less than 10 ohms resistance? |
| STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
|  | **STEP 2A.** Check Idle/Rated Switch Signal Wire | Less than 10 ohms resistance? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check idle/rated switch signal wire. Disconnect the idle/rated switch signal wire from the X4 connector. Place one test lead on the idle/rated switch signal pin in connector C3. Place the other test lead on idle rated switch signal pin on the X4 connector. | Less than 10 ohms resistance? **YES** | 1B |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 1B. Check Idle/Rated Switch Signal Wire with Engine Harness Disconnected

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check idle/rated switch return wire. Disconnect the idle/rated switch return wire from the X4 connector. Place one test lead on the idle/rated switch return terminal on the customer interface box logic unit. Place the other test lead on the idle rated switch return pin on the X4 connector. | Less than 10 ohms resistance? **YES** | 2A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 2. Check Engine Harness to Customer Interface Box Cable

#### STEP 2A. Check Idle/Rated Switch Signal Wire

| **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check idle/rated switch signal wire. Place one test lead in the idle/rated switch signal pin of the C3 connector. Place the other test lead in the idle/rated switch signal pin of the C10 connector. | Less than 10 ohms resistance? **YESRepair:** Replace to the OEM service manual or idle switch repair instructions. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
