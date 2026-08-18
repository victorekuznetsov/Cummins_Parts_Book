---
aliases:
  - "Неисправность выходного сигнала тахометра ЭБУ"
type: "Процедура"
doc: "116-t02-1068"
title_en: "ECM Tachometer Output Signal Malfunction"
title_ru: "Неисправность выходного сигнала тахометра ЭБУ"
modified: "2007-03-02"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1068.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1068.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# ECM Tachometer Output Signal Malfunction
**Неисправность выходного сигнала тахометра ЭБУ**

> [!abstract] Процедура · `116-t02-1068`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1068.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1068.pdf)

Printable Version

### Symptoms

- The tachometer output signal is **not** available.

### How To Use This Tree

This symptom tree can be used to troubleshoot an ECM tachometer output signal malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check Tachometer Output Signal Wire for Open | Less than 10 ohms? |
|  | **STEP 1B.** Check Tachometer Output Signal Wire for Wire to Wire Short | Less than 10 ohms? |
|  | **STEP 1C.** Check Tachometer Output Signal Wire for Short to Ground | Less than 10 ohms? |
| STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
|  | **STEP 2A.** Check Tachometer Output Signal Wire for Open | Less than 10 ohms? |
|  | **STEP 2B.** Check Tachometer Output Signal Wire for Wire to Wire Short | Less than 10 ohms? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check Tachometer Output Signal Wire for Open

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the tachometer output signal wire for an open. Place one test lead on the tachometer output signal pin in connector C3. Place the other test lead on tachometer output signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |

#### STEP 1B. Check Tachometer Output Signal Wire for Wire to Wire Short

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the tachometer output signal wire for wire to wire short. Place one test lead on the tachometer output signal wire pin in connector C3. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check Tachometer Output Signal Wire for Short to Ground

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the tachometer output signal wire for short to ground. Place one test lead on the tachometer output signal pin in connector C3. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check Engine Harness to Customer Interface Box Cable

#### STEP 2A. Check Tachometer Output Signal Wire for Open

| **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check tachometer output signal wire for an open. Place a jumper between the tachometer output signal wire pin and the common warning signal pin in the C10 connector. Place one test lead in the tachometer output signal pin of the C3 connector. Place the other test lead in the common warning signal pin of the C3 connector. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |

#### STEP 2B. Check Tachometer Output Signal Wire for Wire to Wire Short

| **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C10 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check tachometer output signal wire for a wire to wire short. Place one test lead in the tachometer output signal pin in connector C3. Place the other test lead on each of the remaining pins in the C3 connector. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual. | Repair complete |  |
