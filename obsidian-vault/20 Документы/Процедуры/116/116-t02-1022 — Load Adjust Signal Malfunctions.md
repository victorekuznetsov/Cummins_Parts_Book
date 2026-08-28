---
aliases:
  - "Неисправности сигнала регулировки нагрузки"
type: "Процедура"
doc: "116-t02-1022"
title_en: "Load Adjust Signal Malfunctions"
title_ru: "Неисправности сигнала регулировки нагрузки"
modified: "2007-03-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1022.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1022.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Load Adjust Signal Malfunctions
**Неисправности сигнала регулировки нагрузки**

> [!abstract] Процедура · `116-t02-1022`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1022.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1022.pdf)

Printable Version

### Symptoms

- Engine does **not** respond to load adjust request.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check Droop Adjust Potentiometer Supply Wire | Less than 10 ohms? |
|  | **STEP 1B.** Check Droop Adjust Potentiometer Return Wire | Less than 10 ohms? |
|  | **STEP 1C.** Check Frequency Adjust Signal Wire | Less than 10 ohms? |
| STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
|  | **STEP 2A.** Check Frequency Adjust Supply and Signal Wires | Less than 10 ohms? |
|  | **STEP 2B.** Check Frequency Adjust Return and Signal Wires | Less than 10 ohms? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check Droop Adjust Potentiometer Supply Wire

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer supply wire. Place one test lead on the droop adjust potentiometer 5 volt supply (sensor supply 1) pin in connector C2. Place the other test lead on the droop adjust potentiometer 5 volt supply (sensor supply 1) terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 1B. Check Droop Adjust Potentiometer Return Wire

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer return wire. Place one test lead on the droop adjust potentiometer return (sensor return 1) pin in connector C2. Place the other test on droop adjust potentiometer return (sensor return 1) terminal on the X4 connector. | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 1C. Check Frequency Adjust Signal Wire

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the frequency adjust signal wire. Place one test lead on the generator output frequency adjust potentiometer signal pin in connector C2. Place the other test lead on the generator output frequency adjust potentiometer signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 2A |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 2. Check Engine Harness to Customer Interface Box Cable

#### STEP 2A. Check Frequency Adjust Supply and Signal Wires

| **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check frequency adjust supply and signal wires. Place a jumper between the droop adjust potentiometer 5 volt supply (sensor supply 1) pin and the generator output frequency adjust potentiometer signal pin in the C9 connector. Place one test lead in the droop adjust potentiometer 5 volt supply (sensor supply 1) pin of the C2 connector. Place the other test lead in the generator output frequency adjust potentiometer signal pin of the C2 connector. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 2B. Check Frequency Adjust Return and Signal Wires

| **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check frequency adjust return and signal wires. Place a jumper between the generator output frequency adjust potentiometer signal pin and the droop adjust potentiometer return (sensor return 1) pin in the C9 connector. Place one test lead in the droop adjust potentiometer return (sensor return 1) pin of the C2 connector. Place the other test lead in the generator output frequency adjust potentiometer signal pin of the C2 connector. | Less than 10 ohms? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System, Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533, or refer to the OEM service manual for potentiometer repair instructions. | Repair complete. |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete. |  |
