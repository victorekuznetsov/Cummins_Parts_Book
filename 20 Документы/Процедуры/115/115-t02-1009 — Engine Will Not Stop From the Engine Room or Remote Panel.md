---
aliases:
  - "Двигатель не останавливается ни из МО, ни с дистанционного пульта"
type: "Процедура"
doc: "115-t02-1009"
title_en: "Engine Will Not Stop From the Engine Room or Remote Panel"
title_ru: "Двигатель не останавливается ни из МО, ни с дистанционного пульта"
modified: "2007-01-08"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1009.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1009.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Will Not Stop From the Engine Room or Remote Panel
**Двигатель не останавливается ни из МО, ни с дистанционного пульта**

> [!abstract] Процедура · `115-t02-1009`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1009.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1009.pdf)

Printable Version

### Symptoms

- Engine will **not** stop when the stop button is pushed at the engine room panel.

- Engine will **not** stop when the stop button is pushed at the remote panel.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The engine can be stopped by pushing the stop button from the engine room panel or remote panel. The panel does **not** need to have start control to stop the engine.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Engine Room Panel Stop Button |  |
|  | **STEP 1A.** Check Stop Button Input to Customer Interface Box Logic Unit | Stop lamp illuminated? |
|  | **STEP 1B.** Check Stop Button Operation | Less than 10 ohms resistance? |
| STEP 2. | Check Remote Panel Stop Button |  |
|  | **STEP 2A.** Check Stop Button to Customer Interface Box Logic Unit | Stop lamp illuminated? |
|  | **STEP 2B.** Check Stop Button Operation | Less than 10 ohms resistance? |
| STEP 3. | Check Panel Wiring |  |
|  | **STEP 3A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
|  | **STEP 3A-1.** Check Engine Room Power Switch Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 3A-2.** Check Engine Room Panel Stop Supply Wire | Less than 10 ohms resistance? |
| STEP 4. | Check Panel System Cables |  |
|  | **STEP 4A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
|  | **STEP 4B.** Check Remote Panel Cable | Less than 10 ohms resistance? |
| STEP 5. | Check Customer Interface Box Wiring |  |
|  | **STEP 5A.** Check Engine Room Panel Stop Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 5B.** Check the Remote Panel Stop Supply Wire | Less than 10 ohms resistance? |

### STEP 1. Check Engine Room Panel Stop Button

#### STEP 1A. Check Stop Button Input to Customer Interface Box Logic Unit

| **Conditions:** Locate engine room panel Engine room panel power lamp illuminated Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine stop button input to customer interface box logic unit. Push the stop button. Verify stop lamp is illuminated on the customer interface box logic unit. | Stop lamp illuminated? **YES** | 2A |
| Stop lamp illuminated? **NO** | 1B |  |

#### STEP 1B. Check Stop Button Operation

| **Conditions:** Open engine room panel Disconnect engine room panel cable connetor from control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the stop button operation. Place one test lead on the engine room panel power switch supply terminal of the control panel connector. Place the other test lead on the engine room panel stop supply terminal of the control panel connector. Press the stop button. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 2. Check Remote Panel Stop Button

#### STEP 2A. Check Stop Button to Customer Interface Box Logic Unit

| **Conditions:** Locate remote panel Remote panel power lamp illuminated Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine stop button input to customer interface box logic unit. Press the stop button. Verify the stop lamp illuminated on the customer interface box logic unit. | Stop lamp illuminated? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| Stop lamp illuminated? **NO** | 2B |  |

#### STEP 2B. Check Stop Button Operation

| **Conditions:** Open remote panel Disconnect engine room panel cable connector from the control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the stop button operation. Place one test lead on the remote panel stop supply terminal of the control panel connector. Place the other test lead on the remote panel power switch supply terminal of the control panel connector. Press the stop button. | Less than 10 ohms resistance? **YES** | 4B |
| Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |

### STEP 3. Check Panel Wiring

#### STEP 3A. Check Engine Room Panel Wiring

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead to the engine room power switch supply pin at the C14 connector. Place the other test lead on the engine room panel stop supply pin at the C14 connector. Press the stop button. | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NO** | 3A-1 |  |

#### STEP 3A-1. Check Engine Room Power Switch Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room power switch supply pin on connector C14. Place the other test lead on the engine room power switch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 3A-2 |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 3A-2. Check Engine Room Panel Stop Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel stop supply pin on the C14 connector. Place the other test lead on the engine room panel stop supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 4. Check Panel System Cables

#### STEP 4A. Check Engine Room Panel Cable

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel cable. Install a jumper between engine room power switch supply pin and the engine room panel stop supply pin in connector C14. Place one test lead in the engine room power switch supply pin in connector C7. Place the other test lead in the engine room panel stop supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 5A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 4B. Check Remote Panel Cable

| **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect remote panel cable from customer interface box X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel cable. Install a jumper between remote panel power switch supply terminal and remote panel stop supply terminal on remote control panel X4 in the remote control panel. Place one test lead on the remote panel power switch supply wire. Place the other test lead on the remote panel stop supply wire. | Less than 10 ohms resistance? **YES** | 5B |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 5. Check Customer Interface Box Wiring

#### STEP 5A. Check Engine Room Panel Stop Supply Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel stop supply wire. Place one test lead on the engine room panel stop supply pin in connector C7. Place the other test lead on the engine room panel stop supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 2A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 5B. Check the Remote Panel Stop Supply Wire

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel stop supply wire. Place one test lead on the remote panel stop supply wire terminal in the customer interface box X4 connector. Place the other test lead on the remote panel stop supply wire terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
