---
aliases:
  - "Неисправность сигнала промежуточной частоты 2"
type: "Процедура"
doc: "116-t02-1065"
title_en: "Intermediate Speed Control 2 Signal Malfunction"
title_ru: "Неисправность сигнала промежуточной частоты 2"
modified: "2007-03-02"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1065.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1065.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Intermediate Speed Control 2 Signal Malfunction
**Неисправность сигнала промежуточной частоты 2**

> [!abstract] Процедура · `116-t02-1065`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1065.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1065.pdf)

Printable Version

### Symptoms

- Intermediate speed control 2 signal is **not** available.

### How To Use This Tree

This symptom tree can be used to troubleshoot an intermediate speed control 2 signal malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check Intermediate Speed Control 2 Switch Signal Wire for Open | Less than 10 ohms? |
|  | **STEP 1B.** Check Intermediate Speed Control 2 Switch Signal Wire for Wire to Wire Short | Less than 10 ohms? |
|  | **STEP 1C.** Check Intermediate Speed Control 2 Switch Signal Wire for Short to Ground | Less than 10 ohms? |
| STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
|  | **STEP 2A.** Check Intermediate Speed Control 2 Switch Signal Wire for Open | Less than 10 ohms? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check Intermediate Speed Control 2 Switch Signal Wire for Open

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the intermediate speed control 2 switch signal wire for an open. Place one test lead on the intermediate speed control 2 switch signal pin in connector C3. Place the other test lead on intermediate speed control 2 switch signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |

#### STEP 1B. Check Intermediate Speed Control 2 Switch Signal Wire for Wire to Wire Short

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the intermediate speed control 2 switch signal wire for wire to wire short. Place one test lead on the intermediate speed control 2 switch signal pin in connector C3. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check Intermediate Speed Control 2 Switch Signal Wire for Short to Ground

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the intermediate speed control 2 switch signal wire for short to ground. Place one test lead on the intermediate speed control 2 switch signal pin in connector C3. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check Engine Harness to Customer Interface Box Cable

#### STEP 2A. Check Intermediate Speed Control 2 Switch Signal Wire for Open

| **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check intermediate speed control 2 switch signal wire. Place a jumper between the torque curve select signal pin and the intermediate speed control 2 switch signal pin in the C10 connector. Place one test lead in the torque curve select signal pin of the C3 connector. Place the other test lead in the intermediate speed control 2 switch signal pin of the C3 connector. | Less than 10 ohms? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troublehshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
