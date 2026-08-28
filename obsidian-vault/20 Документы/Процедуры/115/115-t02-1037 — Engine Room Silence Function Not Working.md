---
aliases:
  - "Не работает функция отключения звука в машинном отделении"
type: "Процедура"
doc: "115-t02-1037"
title_en: "Engine Room Silence Function Not Working"
title_ru: "Не работает функция отключения звука в машинном отделении"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1037.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1037.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Room Silence Function Not Working
**Не работает функция отключения звука в машинном отделении**

> [!abstract] Процедура · `115-t02-1037`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1037.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1037.pdf)

Printable Version

### Symptoms

- Buzzer will **not** silence when silence button pushed at engine room panel.

- Buzzer will silence when silence button pushed at remote panel.

### How To Use This Tree

This symptom tree can be used to troubleshoot alarm silence symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The engine room panel and remote panel each have a silence button. The ECM delivers alarm information to the customer interface box logic unit. The customer interface box logic unit delivers alarm information to the engine room panel and remote panel. The engine room panel and remote panel deliver alarm information to the operator in visual and audible format. A silence button allows the audible alarm to be silenced.

When an alarm condition occurs the audible alarm can be shut off at all panels by pressing the silence button at any panel.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Engine Room Panel |  |
|  | **STEP 1A.** Check Silence Button | Less than 10 ohms resistance? |
| STEP 2. | Check Panel Wiring |  |
|  | **STEP 2A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
|  | **STEP 2A-1.** Check Engine Room Power Switch Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 2A-2.** Check the Engine Room Panel Alarm Silence Supply Wire | Less than 10 ohms resistance? |
| STEP 3. | Check Panel System Cable |  |
|  | **STEP 3A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
| STEP 4. | Check Customer Interface Box Wiring |  |
|  | **STEP 4A.** Check the Engine Room Alarm Silence Supply Wire | Less than 10 ohms resistance? |

### STEP 1. Check Engine Room Panel

#### STEP 1A. Check Silence Button

| **Conditions:** Locate engine room panel Turn engine room panel power switch off Disconnect control panel connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify silence button function: Place one test lead on the engine room power switch supply terminal of the control panel connector. Place the other test lead on the engine room panel alarm silence supply terminal of the control panel connector. Press the silence button. | Less than 10 ohms resistance? **YES** | 2A |
| Less than 10 ohms resistance? **NORepair:** Replace the engine room panel control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 2. Check Panel Wiring

#### STEP 2A. Check Engine Room Panel Wiring

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead to the engine room power switch supply pin at the C14 connector. Connect the other test lead to the engine room panel alarm silence supply pin at the C14 connector. Press the silence button. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NO** | 2A1 |  |

#### STEP 2A-1. Check Engine Room Power Switch Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room power switch supply pin on connector C14. Place the other test lead on the engine room power switch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 2A2 |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 2A-2. Check the Engine Room Panel Alarm Silence Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel alarm silence supply pin on connector C14. Place the other test lead on the engine room panel alarm silence supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** Replace the fault wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 3. Check Panel System Cable

#### STEP 3A. Check Engine Room Panel Cable

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Install a jumper between engine room power switch supply pin and the engine room panel alarm silence supply pin in connector C14. Place one test lead in the engine room power switch power switch supply pin in connector C7. Place the other test lead in the engine room power switch alarm silence supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 4. Check Customer Interface Box Wiring

#### STEP 4A. Check the Engine Room Panel Alarm Silence Supply Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel alarm silence supply wire. Place one test lead on the engine room panel alarm silence supply pin in connector C7. Place the other test lead on the engine room panel alarm silence supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
