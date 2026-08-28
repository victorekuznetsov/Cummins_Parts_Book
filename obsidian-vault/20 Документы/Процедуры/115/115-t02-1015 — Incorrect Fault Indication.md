---
aliases:
  - "Неверная индикация неисправности"
type: "Процедура"
doc: "115-t02-1015"
title_en: "Incorrect Fault Indication"
title_ru: "Неверная индикация неисправности"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Incorrect Fault Indication
**Неверная индикация неисправности**

> [!abstract] Процедура · `115-t02-1015`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1015.pdf)

Printable Version

### Symptoms

- Alarm lamp is **not** illuminated at the engine room panel or the remote panel when alarm condition is present.

### How To Use This Tree

This symptom tree can be used to troubleshoot panel fault symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Panel Alarm Lamp Indication |  |
|  | **STEP 1A.** Check Engine Room Panel Alarm Lamp Indication | Alarm lamp illuminated? |
|  | **STEP 1B.** Check Remote Panel Alarm Lamp Indication | Alarm lamp illuminated? |
| STEP 2. | Check Engine Room Panel Wiring |  |
|  | **STEP 2A.** Check Engine Room Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 2B.** Check Engine Room Panel Return Wire | Less than 10 ohms resistance? |
| STEP 3. | Check Panel System Cables |  |
|  | **STEP 3A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
|  | **STEP 3B.** Check Remote Panel Cable | Less than 10 ohms resistance? |
| STEP 4. | Check Customer Interface Box |  |
|  | **STEP 4A.** Check the Engine Room Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 4B.** Check Remote Panel Alarm (Red Lamp) Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 4C.** Check Red Lamp Signal Wire | Less than 10 ohms resistance? |
| STEP 5. | Check Customer Interface Box to Engine Harness Cable |  |
|  | **STEP 5A.** Check Red Lamp Signal Wire | Less than 10 ohms resistance? |
| STEP 6. | Check Customer Interface Box Logic Unit |  |
|  | **STEP 6A.** Check Engine Room Panel Alarm (Red Lamp) Supply Terminal | 24 VDC |

### STEP 1. Check Panel Alarm Lamp Indication

#### STEP 1A. Check Engine Room Panel Alarm Lamp Indication

| **Conditions:** Locate engine room panel |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify engine room panel alarm lamp is illuminated. | Alarm lamp illuminated? **YES** | 1B |
| Alarm lamp illuminated? **NO** | 2A |  |

#### STEP 1B. Check Remote Panel Alarm Lamp Indication

| **Conditions:** Locate remote panel |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify remote panel alarm lamp is illuminated. | Alarm lamp illuminated? **YES** | Repair complete. |
| Alarm lamp illuminated? **NO** | 3B |  |

### STEP 2. Check Engine Room Panel Wiring

#### STEP 2A. Check Engine Room Panel Alarm (Red Lamp) Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel Place one test lead on the engine room panel alarm (red lamp) supply pin on connector C14. Place the other test lead on the engine room panel alarm (red lamp) supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 2B |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 2B. Check Engine Room Panel Return Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel return pin on connector C14. Place the other test lead on the engine room panel return pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 3. Check Panel System Cables

#### STEP 3A. Check Engine Room Panel Cable

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Install a jumper between engine room panel alarm (red lamp) supply pin and the engine room panel return pin in connector C14. Place the other test lead in the engine room panel alarm (red lamp) supply pin in connector C7. Place the other test lead in the engine room panel return pin in connector C7. | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 3B. Check Remote Panel Cable

| **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect remote panel cable from customer interface box X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel cable. Install a jumper between remote panel alarm (red lamp) supply terminal and the remote panel return terminal on the remote control panel X4 in the remote control panel. Place one test lead on the remote panel alarm (red lamp) supply wire. Place the other test lead on the remote panel return wire. | Less than 10 ohms resistance? **YES** | 4B |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 4. Check Customer Interface Box

#### STEP 4A. Check the Engine Room Panel Alarm (Red Lamp) Supply Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel alarm (red lamp) supply wire. Place one test lead on the engine room panel alarm (red lamp) supply pin in connector C7. Place the other test lead on the engine room panel alarm (red lamp) supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 4C |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 4B. Check Remote Panel Alarm (Red Lamp) Supply Wire

| **Conditions:** Open the customer interface box |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel alarm (red lamp) supply wire. Place one test lead on the remote panel alarm (red lamp) supply wire terminal in customer interface box X4 connector. Place the other test lead on the remote panel alarm (red lamp) supply terminal of the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 4C |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 4C. Check Red Lamp Signal Wire

| **Conditions:** Open the customer interface box Disconnect the customer interface box to engine harness cable at the C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the red lamp signal wire. Place one test lead on the red lamp signal pin in connector C3. Place the other test lead on the red lamp signal terminal of the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 5A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 5. Check Customer Interface Box to Engine Harness Cable

#### STEP 5A. Check Red Lamp Signal Wire

| **Conditions:** Disconnect cable connector C10 from the engine harness Disconnect cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface box to engine harness cable. Place one test lead in the red lamp signal pin in connector C10. Place the other test lead in the red lamp signal pin in connector C3. | Less than 10 ohms resistance? **YES** | 6A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 6. Check Customer Interface Box Logic Unit

#### STEP 6A. Check Engine Room Panel Alarm (Red Lamp) Supply Terminal

| **Conditions:** Locate customer interface box Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the engine room panel alarm (red lamp) supply terminal of the customer interface box logic unit is 24 VDC. | 24 VDC **YESRepair:** Replace the faulty control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]] or [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
| 24 VDC **NORepair:** Replace customer interface box logic unit after verifying on-engine harness and engine control module are operating property. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
