---
aliases:
  - "Неисправности сигнала регулировки статизма"
type: "Процедура"
doc: "115-t02-1021"
title_en: "Droop Adjust Signal Malfunctions"
title_ru: "Неисправности сигнала регулировки статизма"
modified: "2006-08-09"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1021.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1021.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Droop Adjust Signal Malfunctions
**Неисправности сигнала регулировки статизма**

> [!abstract] Процедура · `115-t02-1021`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1021.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1021.pdf)

Printable Version

### Symptoms

- Droop adjust signal **not** available from customer interface box.

### How To Use This Tree

This symptom tree can be used to troubleshoot droop adjust symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check Droop Adjust Potentiometer Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 1B.** Check Droop Adjust Potentiometer Return Wire | Less than 10 ohms resistance? |
|  | **STEP 1C.** Check Droop Adjust Potentiometer Signal Wire | Less than 10 ohms resistance? |
| STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
|  | **STEP 2A.** Check Droop Adjust Potentiometer Supply and Signal Wires | Less than 10 ohms resistance? |
|  | **STEP 2B.** Check Droop Adjust Potentiometer Return and Signal Wires | Less than 10 ohms resistance? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check Droop Adjust Potentiometer Supply Wire

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer supply wire. Place one test lead on the droop adjust potentiometer 5 volt supply (sensor supply 1) pin in connector C3. Place the other test lead on droop adjust potentiometer 5 volt supply (sensor supply 1) terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 1B |
| Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 1B. Check Droop Adjust Potentiometer Return Wire

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer return wire. Place one test lead on the droop adjust potentiometer return (sensor return 1) pin in connector C3. Place the other test lead on droop adjust potentiometer return (sensor return 1) terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 1C |
| Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 1C. Check Droop Adjust Potentiometer Signal Wire

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer signal wire. Place one test lead on the droop adjust potentiometer signal pin in connector C3. Place the other test lead on droop adjust potentiometer signal terminal on the X4 connector. | Less than 10 ohms resistance? **YES** | 2A |
| Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 2. Check Engine Harness to Customer Interface Box Cable

#### STEP 2A. Check Droop Adjust Potentiometer Supply and Signal Wires

| **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer supply and signal wires. Place a jumper between the droop adjust potentiometer 5 volt supply (sensor supply 1) pin and the droop adjust potentiometer signal pin in the C9 connector. Place one test lead in the droop adjust potentiometer 5 volt supply (sensor supply 1) pin of the C3 connector. Place the other test lead in the droop adjust potentiometer signal pin of the C3 connector. | Less than 10 ohms resistance? **YES** | 2B |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 2B. Check Droop Adjust Potentiometer Return and Signal Wires

| **Conditions:** Disconnect customer interface box to engine harness cable connector C3 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer retrun and signal wires. Place a jumper between the droop adjust potentiometer signal pin and the droop adjust potentiometer return (sensor return 1) pin in the C9 connector. Place one test lead in the droop adjust potentiometer return (sensor return 1) pin of the C3 connector. Place the other test lead in the droop adjust potentiometer signal pin of the C3 connector. | Less than 10 ohms resistance? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493 or refer to the OEM Service Manual for potentiometer repair instructions. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
