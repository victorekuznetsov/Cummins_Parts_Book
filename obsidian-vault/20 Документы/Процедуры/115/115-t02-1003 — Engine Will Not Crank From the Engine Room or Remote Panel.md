---
aliases:
  - "Двигатель не проворачивается ни из МО, ни с дистанционного пульта"
type: "Процедура"
doc: "115-t02-1003"
title_en: "Engine Will Not Crank From the Engine Room or Remote Panel"
title_ru: "Двигатель не проворачивается ни из МО, ни с дистанционного пульта"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1003.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Will Not Crank From the Engine Room or Remote Panel
**Двигатель не проворачивается ни из МО, ни с дистанционного пульта**

> [!abstract] Процедура · `115-t02-1003`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1003.pdf)

Printable Version

### Symptoms

- Engine will **not** crank when the start button is pushed at the engine room panel.

- Engine will **not** crank when the start button is pushed at the remote panel.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

To initiate engine crank from the engine room panel, the following panel parameters **must** be met:

- The engine room panel power switch on the lamp illuminated.

- The engine is stopped.

To initiate engine crank from the remote panel, the following panel parameters **must** be met:

- The remote panel power lamp illuminated.

- The local start **only** lamp is **not** illuminated

- The engine is stopped.

Prior to beginning the troubleshooting procedure, the following conditions **must** be active:

1. All circuit breakers in the customer interface box must be closed.

2. The engine stop switch **must** be disengaged.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Engine Room Panel Configuration |  |
|  | **STEP 1A.** Check Panel Power | Is the power switch on and lamp illuminated? |
|  | **STEP 1B.** Check Local Start Only Lamp | Local start **only** lamp illuminated? |
| STEP 2. | Check Remote Panel Configuration |  |
|  | **STEP 2A.** Check Panel Power | Local start **only** lamp illuminated? |
|  | **STEP 2B.** Check Local Start Only Lamp | Is remote panel local start **only** lamp illuminated? |
| STEP 3. | Check Engine Room Panel Start Button |  |
|  | **STEP 3A.** Check Start Button Input to Customer Interface Box Logic Unit | Crank lamp illuminated? |
|  | **STEP 3B.** Check Start Button Operation | Less than 10 ohms resistance? |
| STEP 4. | Check Remote Panel Start Button |  |
|  | **STEP 4A.** Check Start Button Input to Customer Interface Box Logic Unit | Crank lamp illuminated? |
|  | **STEP 4B.** Check Start Button Operation | Less than 10 ohms resistance? |
| STEP 5. | Check Panel Wiring |  |
|  | **STEP 5A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
|  | **STEP 5A-1.** Check Engine Room Power Switch Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 5A-2.** Check Engine Room Panel Start Supply Wire | Less than 10 ohms resistance? |
| STEP 6. | Check Panel System Cables |  |
|  | **STEP 6A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
|  | **STEP 6B.** Check Remote Panel Cable | Less than 10 ohms resistance? |
|  | **STEP 6C.** Check Starter Cable Prelubrication Signals | Less than 10 ohms resistance? |
|  | **STEP 6C-1.** Check Starter Cable Prelubrication System Jumper | Less than 10 ohm resistance? |
|  | **STEP 6C-2.** Check Starter Cable Prelubrication System Wires | Less than 10 ohm resistance? |
| STEP 7. | Check Customer Interface Box Wiring |  |
|  | **STEP 7A.** Check the Engine Room Panel Start Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 7B.** Check the Remote Panel Start Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 7C.** Check Customer Interface Box Logic Unit Prelube Activation Signal Wire | Less than 10 ohms resistance? |
|  | **STEP 7D.** Check Customer Interface Box Logic Prelube Complete Signal Wire | Less than 10 ohms resistance? |
|  | **STEP 7E.** Check Customer Interface Box Logic Unit Starter Relay Switch Signal Wire | Less than 10 ohms resistance? |
|  | **STEP 7F.** Check Customer Interface Box Logic Unit Starter Relay Return Wire | Less than 10 ohms resistance? |
| STEP 8. | Check Start Signal to Engine |  |
|  | **STEP 8A.** Check Starter Cable Starter Relay Switch Signals | Less than 10 ohms resistance? |
| STEP 9. | Check Customer Interface Box Logic Unit |  |
|  | **STEP 9A.** Check Customer Interface Box Logic Unit From the Engine Room Panel | 24 VDC? |
|  | **STEP 9B.** Check Customer Interface Box Logic Unit From the Remote Panel | 24 VDC? |
| STEP 10. | Check Engine Room Panel |  |
|  | **STEP 10A.** Check Start Signal from Engine Room Panel or Remote Panel | 24 VDC? |

### STEP 1. Check Engine Room Panel Configuration

#### STEP 1A. Check Panel Power

| **Conditions:** Locate engine room panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify power switch is on and lamp illuminated. | Is the power switch on and lamp illuminated? **YES** | 1B |
| Is the power switch on and lamp illuminated? **NORepair:** Turn on power switch and verify lamp is illuminated. If the power lamp is **not** on refer to the System Will **Not** Start After Shutdown Troubleshooting Symptom Tree. | Repair complete. |  |

#### STEP 1B. Check Local Start Only Lamp

| **Conditions:** Locate engine room panel Power switch on and lamp illuminated. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify local start only lamp is illuminated. | Local start **only** lamp illuminated? **YES** | 2A |
| Local start **only** lamp illuminated? **NORepair:** Push local start **only** button and verify lamp is illuminated. If the lamp did not illuminate refer to the Engine Room Panel Local/Remote Switch Fails to Switch to Local Troubleshooting Symptom Tree. | Repair complete. |  |

### STEP 2. Check Remote Panel Configuration

#### STEP 2A. Check Panel Power

| **Conditions:** Locate remote panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify power lamp is illumintated. | Local start **only** lamp illuminated? **YES** | 2B |
| Local start **only** lamp illuminated? **NORepair:** If the lamp did **not** illuminate refer to the System Will Not Start After Shutdown Troubleshooting Symptom Tree. | Repair complete. |  |

#### STEP 2B. Check Local Start Only Lamp

| **Conditions:** Remote panel power lamp illuminated. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify remote panel local start only lamp is illuminated. | Is remote panel local start **only** lamp illuminated? **YESRepair:** Locate engine room panel and push local start **only** button and verify remote panel lamp is **not** illuminated. If the lamp is still illuminated refer to the Remote Panel Fails to Switch to Remote Troubleshooting Symptom Tree. | 3A |
| Is remote panel local start **only** lamp illuminated? **NORepair:** Refer to the Remote Panel Fails to Switch to Local Troubleshooting Symptom Tree. | Repair complete. |  |

### STEP 3. Check Engine Room Panel Start Button

#### STEP 3A. Check Start Button Input to Customer Interface Box Logic Unit

| **Conditions:** Locate engine room panel Engine room panel power lamp illuminated Engine room panel local start only lamp not illuminated Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine start button input to customer interface box logic unit. Press the start button. Verify crank lamp illuminated on customer interface box logic unit. | Crank lamp illuminated? **YES** | 7E |
| Crank lamp illuminated? **NO** | 3B |  |

#### STEP 3B. Check Start Button Operation

| **Conditions:** Open engine room panel Disconnect control panel X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the start button operation. Place one test lead on the engine room power switch supply terminal of the control panel X4 connector. Place the other test lead on the engine room panel start supply terminal of the control panel X4 connector. Press the start button. | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 4. Check Remote Panel Start Button

#### STEP 4A. Check Start Button Input to Customer Interface Box Logic Unit

| **Conditions:** Locate remote panel Remote panel power lamp illuminated Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine start button input to customer interface box logic unit. Press the start button. Verify the crank lamp illuminated on the customer interface box logic unit. | Crank lamp illuminated? **YES** | 7E |
| Crank lamp illuminated? **NO** | 4B |  |

#### STEP 4B. Check Start Button Operation

| **Conditions:** Open remote panel Disconnect control panel X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the start button operation. Place one test lead on the remote panel start supply terminal of the control panel X4 connector. Place the other test lead on the remote panel power switch supply terminal of the control panel X4 connector. Press the start button. | Less than 10 ohms resistance? **YES** | 5A |
| Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |  |

### STEP 5. Check Panel Wiring

#### STEP 5A. Check Engine Room Panel Wiring

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead to the engine room power switch supply pin at the C14 connector. Place the other test lead on the engine room panel start supply pin at the C14 connector. Press the start button. | Less than 10 ohms resistance? **YES** | 6A |
| Less than 10 ohms resistance? **NO** | 5A-1 |  |

#### STEP 5A-1. Check Engine Room Power Switch Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect on test lead on the engine room power switch supply pin on the engine room panel C14 connector. Place the other test lead on the engine room power switch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 5A-2 |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 5A-2. Check Engine Room Panel Start Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel start supply pin on the engine room panel C14 connector. Place the other test lead on the engine room panel start supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 6A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 6. Check Panel System Cables

#### STEP 6A. Check Engine Room Panel Cable

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Install a jumper between engine room power switch supply pin and the engine room panel start supply pin in connector C14. Place one test lead in the engine room panel power switch supply pin in connector C7. Place the other test lead in the engine room panel start supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 6B |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 6B. Check Remote Panel Cable

| **Conditions:** Locate and open customer interface box Locate and open remote panel Disconnect remote panel cable from customer interface box X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel cable. Install a jumper between the remote power switch supply terminal and the remote panel start supply terminal on the remote control panel X4 connector. Place one test lead on the remote panel power switch supply terminal in customer interface box X4 connector. Place the other test lead on the remote panel start supply terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 6C |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 6C. Check Starter Cable Prelubrication Signals

| **Conditions:** Disconnect cable connector C1 from the customer interface box Check that prelubrication system jumper is in place. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter cable. Place one test lead on the prelubrication activation signal pin in connector C1. Place the other test lead on the prelubrication complete signal pin in connector C1. | Less than 10 ohms resistance? **YES** | 7A |
| Less than 10 ohms resistance? **NO** | 6C-1 |  |

#### STEP 6C-1. Check Starter Cable Prelubrication System Jumper

| **Conditions:** Disconnect the prelubrication system jumper from the starter cable. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication system jumper. Place one test lead on the prelubrication activation signal pin in the prelubrication system jumper. Place the other test lead on the prelubrication complete signal pin in the prelubrication system jumper. | Less than 10 ohm resistance? **YES** | 6C-2 |
| Less than 10 ohm resistance? **NORepair:** Replace the jumper. | Repair complete. |  |

#### STEP 6C-2. Check Starter Cable Prelubrication System Wires

| **Conditions:** Disconnect cable connector C1 from the customer interface box Disconnect the prelubrication system jumper from the starter cable. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter cable. Install a jumper between the prelubrication activation signal pin and the prelubrication complete signal pin in the prelubrication system connector. Place one test lead on the prelubrication activation signal pin in connector C1. Place the other test lead on the prelubrication complete signal pin in connector C1. | Less than 10 ohm resistance? **YES** | 7A |
| Less than 10 ohm resistance? **NORepair:** Replace the jumper. | Repair complete. |  |

### STEP 7. Check Customer Interface Box Wiring

#### STEP 7A. Check the Engine Room Panel Start Supply Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel start supply wire. Place one test lead on the engine room panel start supply pin in connector C7. Place the other test lead on the engine room panel start supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 7B |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 7B. Check the Remote Panel Start Supply Wire

| **Conditions:** Open the customer interface box Disconnect remote panel cable at connector X4 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel start supply wire. Place one test lead on the remote panel start supply wire terminal in customer interface box X4 connector. Place the other test lead on the remote panel start supply wire terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 7C |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 7C. Check Customer Interface Box Logic Unit Prelube Activation Signal Wire

| **Conditions:** Open the customer interface box Disconnect cable C1 connector from the connector interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelube activation signal wire. Place one test lead on the prelube activation signal terminal on the customer interface box logic unit. Place the other test lead in the prelube activation signal pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 7D |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 7D. Check Customer Interface Box Logic Prelube Complete Signal Wire

| **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelube complete signal wire. Place one test lead on the prelube complete signal terminal on the customer interface box logic unit. Place the other test lead in the prelube complete signal pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 7E |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 7E. Check Customer Interface Box Logic Unit Starter Relay Switch Signal Wire

| **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the start relay switch signal wire. Place one test lead on the starter relay switch signal terminal on the customer interface box logic unit. Place the other test lead in the starter relay switch signal pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 7F |
| Less than 10 ohms resistance? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 7F. Check Customer Interface Box Logic Unit Starter Relay Return Wire

| **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay return wire. Place one test lead on the starter relay return terminal on the customer interface box logic unit. Place the other test lead in the starter relay return pin in the C1 connector. | Less than 10 ohms resistance? **YES** | 8A |
| Less than 10 ohms resistance? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 8. Check Start Signal to Engine

#### STEP 8A. Check Starter Cable Starter Relay Switch Signals

| **Conditions:** Disconnect cable connector C1 from the customer interface box Disconnect cable ring terminals from the starter relay switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter cable. Install a jumper between the starter relay switch signal pin and the starter relay switch return pin in connector C1. Place one test lead on the starter relay switch signal ring terminal. Place the other test lead on the starter relay switch return ring terminal. | Less than 10 ohms resistance? **YES** | 9A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 9. Check Customer Interface Box Logic Unit

#### STEP 9A. Check Customer Interface Box Logic Unit From the Engine Room Panel

| **Conditions:** Open the customer interface box Disconnect cable C1 connector from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel start supply wire. Place the positive test lead on the starter relay switch signal terminal on the customer interface box logic unit. Place the negative test lead on the starter relay switch return terminal on the customer interface box logic unit. Press the start button at the engine room panel. | 24 VDC? **YES** | 9B |
| 24 VDC? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 9B. Check Customer Interface Box Logic Unit From the Remote Panel

| **Conditions:** Open the customer interface box Basic system is configured for start from remote panel (local start only lamp is not illuminated) Disconnect cable C1 connector from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel start supply wire. Place the positive test lead on the starter relay switch signal terminal on the customer interface box logic unit. Place the negative test lead on the starter relay switch return terminal on the customer interface box logic unit. Press the start button at the remote panel. | 24 VDC? **YES** | 10A |
| 24 VDC? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 10. Check Engine Room Panel

#### STEP 10A. Check Start Signal from Engine Room Panel or Remote Panel

| **Conditions:** Configure panel system to start from remote or engine room panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check start signal from engine room panel or remote panel. Place the positive test lead on the starter relay switch signal ring terminal. Place the negative test lead on the starter relay switch return ring terminal. Press the start button. | 24 VDC? **YESRepair:** Refer to Service Manual, QSK19 and QSK19 CM850 Modular Common Rail System Series Engines, Bulletin [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual\|4021592]]. | Repair complete. |
| 24 VDC? **NORepair:** Replace the cable. | Repair complete. |  |
