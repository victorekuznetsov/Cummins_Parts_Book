---
aliases:
  - "Двигатель самопроизвольно останавливается"
type: "Процедура"
doc: "115-t02-1030"
title_en: "Engine Executes Un-requested Engine Stop"
title_ru: "Двигатель самопроизвольно останавливается"
modified: "2007-01-08"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1030.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1030.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Executes Un-requested Engine Stop
**Двигатель самопроизвольно останавливается**

> [!abstract] Процедура · `115-t02-1030`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1030.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1030.pdf)

Printable Version

### Symptoms

- The engine shut down without operator request.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Prior to starting this troubleshooting tree, verify the engine did **not** shut down because of ECM generated or mechanical engine problems. This troubleshooting procedure **only** addresses the panel side of the system.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Engine Room Panel |  |
|  | **STEP 1A.** Check Engine Room Panel Wiring | Less than 10 ohms resistance? |
|  | **STEP 1A-1.** Check Keyswitch Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 1A-2.** Check Ignition (Engine Stop) Supply Wire | Less than 10 ohms resistance? |
| STEP 2. | Check Panel System Cables |  |
|  | **STEP 2A.** Check Engine Room Panel Cable | Less than 10 ohms resistance? |
| STEP 3. | Check Customer Interface Box |  |
|  | **STEP 3A.** Check the Keyswitch Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 3B.** Check the Ignition (Engine Stop) Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 3C.** Check Engine Stop Switch | Less than 10 ohms resistance? |
|  | **STEP 3D.** Check Ignition (Engine Stop) Supply Wire from Engine Stop Switch | Less than 10 ohms resistance? |
| STEP 4. | Check Customer Interface Box to Engine Harness Cable |  |
|  | **STEP 4A.** Check Ignition (Engine Stop) Supply Wire | Less than 10 ohms resistance? |

### STEP 1. Check Engine Room Panel

#### STEP 1A. Check Engine Room Panel Wiring

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel power switch. Disconnect cable C14 from the engine room panel. Disconnect the control panel connector. Place one test lead on the keyswitch supply terminal of the control panel connector. Place the other test lead on the ignition (engine stop) supply terminal of the control panel connector. Turn on the power switch. | Less than 10 ohms resistance? **YES** | 1A-1 |
| Less than 10 ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 1A-1. Check Keyswitch Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the keyswitch supply pin on connector C14. Place the other test lead on the keyswitch supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 1A-2 |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 1A-2. Check Ignition (Engine Stop) Supply Wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Connect one test lead on the ignition (engine stop) supply pin on the on connector C14. Place the other test lead on the ignition (engine stop) supply pin on the control panel connector. | Less than 10 ohms resistance? **YES** | 2A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 2. Check Panel System Cables

#### STEP 2A. Check Engine Room Panel Cable

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Install a jumper between keyswitch supply pin and the ignition (engine stop) supply pin in connector C14. Place one test lead in the keyswitch supply pin in connector C7. Place the other test lead in the ignition (engine stop) supply pin in connector C7. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 3. Check Customer Interface Box

#### STEP 3A. Check the Keyswitch Supply Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the keyswitch supply wire. Place one test lead on the keyswitch supply pin in connector C7. Place the other test lead on the keyswitch supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YES** | 3B |
| Less than 10 ohms resistance? **NORepair:** Replace the fautly wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 3B. Check the Ignition (Engine Stop) Supply Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition (engine stop) supply wire. Place one test lead on the ignition (engine stop) supply pin in connector C7. Place the other test lead on the ignition (engine stop) supply terminal on the engine stop switch. | Less than 10 ohms resistance? **YES** | 3C |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 3C. Check Engine Stop Switch

| **Conditions:** Open the customer interface box Disconnect ignition (engine stop) supply wires from the engine stop switch Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine stop switch. Place one test lead on the ignition (engine stop) supply terminal of the engine stop switch. Place the other test lead on the other side of the engine stop switch at the ignition (engine stop) supply terminal. Make sure the switch is not engaged. | Less than 10 ohms resistance? **YES** | 3D |
| Less than 10 ohms resistance? **NORepair:** Replace the engine stop switch. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 3D. Check Ignition (Engine Stop) Supply Wire from Engine Stop Switch

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box to engine harness cable at connector C1 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition (engine stop) supply wire. Place one test lead on the ignition (engine stop) supply wire on the engine stop switch. Place the other test lead on the ignition (engine stop) supply pin in the C1 connector | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 4. Check Customer Interface Box to Engine Harness Cable

#### STEP 4A. Check Ignition (Engine Stop) Supply Wire

| **Conditions:** Disconnect cable connector C1 from the customer interface box Disconnect cable connector C8 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check ignition (engine stop) supply wire. Place one test lead in the ignition (engine stop) supply pin of the C1 connector. Place the other test lead in the ignition (engine stop) supply pin of the C8 connector. | Less than 10 ohms resistance? **YESRepair:** Replace customer interface box logic unit after verifying on-engine harness and engine control module are operating properly. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |
