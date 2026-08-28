---
aliases:
  - "Подтверждение неисправностей ЭБУ не работает"
type: "Процедура"
doc: "115-t02-1013"
title_en: "ECM Fault Acknowledge Not Operational"
title_ru: "Подтверждение неисправностей ЭБУ не работает"
modified: "2006-06-12"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# ECM Fault Acknowledge Not Operational
**Подтверждение неисправностей ЭБУ не работает**

> [!abstract] Процедура · `115-t02-1013`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1013.pdf)

Printable Version

### Symptoms

- The alarm silence function works but the ECM does **not** receive a fault acknowledge signal.

- The ECM has active faults even after fault condition has been corrected and alarm silence button has been pressed.

### How To Use This Tree

This symptom tree can be used to troubleshoot ECM fault acknowledge symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

After an alarm is received and the silence button is pushed, the buzzers on the engine room panel and remote panel silence. The customer interface box logic unit also sends a fault acknowledge signal to the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check the Fault Acknowledge Signal Wire | Less than 10 ohms resistance? |
| STEP 2. | Check Customer Interface Box to Engine Harness Cable |  |
|  | **STEP 2A.** Check Fault Acknowledge Signal Wire | Less than 10 ohms resistance? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check the Fault Acknowledge Signal Wire

| **Conditions:** Open the customer interface box Disconnect the customer interface box to engine harness cable C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault acknowledge signal wire. Place one test lead on the fault acknowledge signal wire in connector C3. Place the other test lead on the fault acknowledge signal terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 2A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 2. Check Customer Interface Box to Engine Harness Cable

#### STEP 2A. Check Fault Acknowledge Signal Wire

| **Conditions:** Disconnect cable connector C3 from the customer interface box Disconnect cable connector C10 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check fault acknowledge signal wire. Place one test lead in the fault acknowledge signal pin of the C3 connector. Place the other test lead in the fault acknowledge signal pin of the C10 connector. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit after verifying on-engine harness and engine control module are operating properly. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
