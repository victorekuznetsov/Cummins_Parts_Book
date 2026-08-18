---
aliases:
  - "Переключатель «местный/дистанционный» пульта МО не переходит в дистанционный режим"
type: "Процедура"
doc: "115-t02-1032"
title_en: "Engine Room Panel Local/Remote Switch Does Not Switch to Remote"
title_ru: "Переключатель «местный/дистанционный» пульта МО не переходит в дистанционный режим"
modified: "2007-01-08"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1032.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1032.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Room Panel Local/Remote Switch Does Not Switch to Remote
**Переключатель «местный/дистанционный» пульта МО не переходит в дистанционный режим**

> [!abstract] Процедура · `115-t02-1032`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1032.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1032.pdf)

Printable Version

### Symptoms

- Engine will **not** crank when the start button is pushed at the remote panel.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

To initiate engine crank from the engine room panel, the following panel parameters **must** be met:

- The engine room panel power switch on and lamp illuminated.

- The engine **must** be stopped.

To initiate engine crank from the remote panel, the following panel parameters **must** be met:

- The remote panel power lamp illuminated.

- The local start **only** lamp is **not** illuminated.

- The engine **must** be stopped.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the Customer Interface Box Logic Unit |  |
|  | **STEP 1A.** Check Local Mode Lamp | Is the local mode lamp illuminated? |
|  | **STEP 1B.** Shut Off Local Mode Lamp | Is the local mode lamp illuminated? |
| STEP 2. | Check Engine Room Panel |  |
|  | **STEP 2A.** Check Local Start Only Button | Greater than 100k ohms resistance? |
| STEP 3. | Check Panel Wiring |  |
|  | **STEP 3A.** Check Engine Room Panel Wiring | Greater than 100k ohms resistance? |
|  | **STEP 3A-1.** Check Engine Room Panel Wiring | Greater than 100k ohms resistance? |
| STEP 4. | Check Panel System Cables |  |
|  | **STEP 4A.** Check Engine Room Panel Cable | Greater than 100k ohms resistance? |
| STEP 5. | Check Customer Interface Box Wiring |  |
|  | **STEP 5A.** Check the Local Mode Supply Wire | +24 VDC? |

### STEP 1. Check Customer Interface Box Logic Unit

#### STEP 1A. Check Local Mode Lamp

| **Conditions:** Locate engine room panel Power switch on and lamp illuminated Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local mode lamp. Push the local start only button. Verify local mode lamp illuminated on the customer interface box logic unit. | Is the local mode lamp illuminated? **YES** | 1B |
| Is the local mode lamp illuminated? **NO** | Engine Room Panel Local/Remote Switch Fails to Switch to Local. |  |

#### STEP 1B. Shut Off Local Mode Lamp

| **Conditions:** Locate engine room panel Power switch on and lamp illuminated Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local mode lamp. Push the local start only button. Verify local mode lamp not illuminated on the customer interface box logic unit. | Is the local mode lamp illuminated? **YES** | 2A |
| Is the local mode lamp illuminated? **NO** | Repair complete. |  |

### STEP 2. Check Engine Room Panel

#### STEP 2A. Check Local Start Only Button

| **Conditions:** Locate engine room panel Disconnect control panel connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify local start only button function. Place one test lead on the engine room power switch supply terminal of the control panel connector. Place the other test lead on the local mode supply terminal of the control panel connector. | Greater than 100k ohms resistance? **YES** | 3A |
| Greater than 100k ohms resistance? **NORepair:** Replace the control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 3. Check Panel Wiring

#### STEP 3A. Check Engine Room Panel Wiring

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable connector C14 from the engine room panel. Connect one test lead to the engine room power switch supply pin at the C14 connector on the panel. Place the other test lead on the local mode supply pin at the C14 connector on the panel. | Greater than 100k ohms resistance? **YES** | 4A |
| Greater than 100k ohms resistance? **NO** | 3A-1 |  |

#### STEP 3A-1. Check Engine Room Panel Wiring

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable connector C14 from the engine room panel. Place one test lead on the engine room power switch supply pin on the engine room panel C14 connector. Place the other test lead on the local mode supply pin on the engine room panel C14 connector. | Greater than 100k ohms resistance? **YES** | 4A |
| Greater than 100k ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 4. Check Panel System Cables

#### STEP 4A. Check Engine Room Panel Cables

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Place one test lead in the engine room power switch supply pin in connector C7. Place the other test lead in the local mode supply pin in connector C7. | Greater than 100k ohms resistance? **YES** | 5A |
| Greater than 100k ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 5. Check Customer Interface Box Wiring

#### STEP 5A. Check the Local Mode Supply Wire

| **Conditions:** Open the customer interface box Engine room panel power switch on the lamp illuminated Engine room panel not in local start only mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check customer interface box wiring. Place positive test lead on the local mode supply pin on the customer interface box logic unit. Place negative test lead on the battery voltage return pin on the customer interface box logic unit. | 24 VDC? **YESRepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |
| 24 VDC? **NORepair:** Replace the customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
