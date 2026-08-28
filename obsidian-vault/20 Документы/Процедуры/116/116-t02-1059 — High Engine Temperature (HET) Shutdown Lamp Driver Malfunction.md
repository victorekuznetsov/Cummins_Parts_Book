---
aliases:
  - "Неисправность драйвера лампы останова по перегреву (HET)"
type: "Процедура"
doc: "116-t02-1059"
title_en: "High Engine Temperature (HET) Shutdown Lamp Driver Malfunction"
title_ru: "Неисправность драйвера лампы останова по перегреву (HET)"
modified: "2007-03-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# High Engine Temperature (HET) Shutdown Lamp Driver Malfunction
**Неисправность драйвера лампы останова по перегреву (HET)**

> [!abstract] Процедура · `116-t02-1059`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-03-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1059.pdf)

Printable Version

### Symptoms

- The high engine temperature (HET) shutdown lamp is illuminated when a high engine temperature shutdown condition does **not** exist.

- The high engine temperature (HET) shutdown lamp is **not** illuminated when a pre-high engine temperature condition exists.

### How To Use This Tree

This symptom tree can be used to troubleshoot a high temperature (HET) shutdown lamp driver malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Wiring |  |
|  | **STEP 1A.** Check High Engine Temperature (HET) Shutdown Signal Wire for Open | Less than 10 ohms? |
|  | **STEP 1B.** Check High Engine Temperature (HET) Shutdown Signal Wire for Wire to Wire Short | Less than 10 ohms? |
|  | **STEP 1C.** Check High Engine Temperature Warning Signal Wire for Short to Ground | Less than 10 ohms? |
| STEP 2. | Check Engine Harness to Customer Interface Box Cable |  |
|  | **STEP 2A.** Check High Engine Temperature (HET) Shutdown Signal Wire for Open | Less than 10 ohms? |
|  | **STEP 2B.** Check High Engine Temperature (HET) Shutdown Signal Wire for Wire to Wire Short | Less than 10 ohms? |

### STEP 1. Check Customer Interface Box Wiring

#### STEP 1A. Check High Engine Temperature (HET) Shutdown Signal Wire for Open

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high engine temperature (HET) shutdown signal wire for an open. Place one test lead on the high engine temperature (HET) shutdown signal pin in connector C2. Place the other test lead on high engine temperature (HET) shutdown signal terminal on the X4 connector. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |  |

#### STEP 1B. Check High Engine Temperature (HET) Shutdown Signal Wire for Wire to Wire Short

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high engine temperature (HET) shutdown signal wire for wire to wire short. Place one test lead on the high engine temperature (HET) shutdown signal pin in connector C2. Place the other test lead on each of the remaining terminals in X4 connector. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check High Engine Temperature (HET) Shutdown Signal Wire for Short to Ground

| **Conditions:** Open the customer interface box Disconnect customer interface box to engine harness cable connector C2 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high engine temperature (HET) shutdown signal wire for short to ground. Place one test lead on the high engine temperature (HET) shutdown signal pin in connector C2. Place the other test lead on panel ground. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to Procedure [[116-015-023 — Customer Interface Box\|015-023]]. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check Engine Harness to Customer Interface Box Cable

#### STEP 2A. Check High Engine Temperature (HET) Shutdown Signal Wire for Open

| **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box Disconnect customer interface box to engine harness cable connector C9 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check high engine temperature (HET) shutdown signal wire for an open. Place a jumper between the pre-high engine temperature warning signal pin and the high engine temperature (HET) shutdown signal pin in the C9 connector. Place one test lead in the pre-high engine temperature warning signal pin of the C2 connector. Place the other test lead in the high engine temperature (HET) shutdown signal pin of the C2 connector. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |

#### STEP 2B. Check High Engine Temperature (HET) Shutdown Signal Wire for Wire to Wire Short

| **Conditions:** Disconnect customer interface box to engine harness cable connector C2 from the customer interface box Disconnect customer inteface box to engine harness cable connector C9 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check high engine temperature (HET) shutdown signal wire for wire to wire short. Place one test lead on the high engine temperature (HET) shutdown signal pin in connector C2. Place the other test lead on each of the remaining pins in the C2 connector. | Less than 10 ohms? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493, or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60, CM850 Modular Common Rail System Series Engines, Bulletin 4021533 or refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
