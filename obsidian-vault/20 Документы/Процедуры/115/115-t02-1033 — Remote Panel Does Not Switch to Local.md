---
aliases:
  - "Дистанционный пульт не переключается в местный режим"
type: "Процедура"
doc: "115-t02-1033"
title_en: "Remote Panel Does Not Switch to Local"
title_ru: "Дистанционный пульт не переключается в местный режим"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1033.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1033.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Remote Panel Does Not Switch to Local
**Дистанционный пульт не переключается в местный режим**

> [!abstract] Процедура · `115-t02-1033`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1033.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1033.pdf)

Printable Version

### Symptoms

- Engine will crank when the start button is pushed at the remote panel.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine start symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

To initiate engine crank from the engine room panel the following panel parameters **must** be met:

- The engine room power switch on and lamp illuminated.

- The engine **must** be stopped.

To initiate engine crank from the remote panel the following panel parameters **must** be met:

- The remote panel power lamp illuminated.

- The local start **only** lamp is **not** illuminated.

- The engine **must** be stopped.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box Logic Unit |  |
|  | **STEP 1A.** Check Local Mode Lamp | Is the local mode lamp illuminated? |
|  | **STEP 1B.** Check Local Start Only Lamp at Remote Panel | Local start **only** lamp illuminated? |
| STEP 2. | Check Panel System Cable |  |
|  | **STEP 2A.** Check Remote Panel Cable | Less than 10 ohms resistance? |
| STEP 3. | Check Customer Interface Box Wiring |  |
|  | **STEP 3A.** Check the Remote Panel Local Mode Supply Wire | Less than 10 ohms resistance? |

### STEP 1. Check Customer Interface Box Logic Unit

#### STEP 1A. Check Local Mode Lamp

| **Conditions:** Locate engine room panel Power switch on and lamp illuminated Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local mode lamp. Push the local start only button. Verify local mode lamp illuminated on the customer interface box logic unit. | Is the local mode lamp illuminated? **YES** | 1B |
| Is the local mode lamp illuminated? **NORepair:** Refer to Engine Room Panel Fails to Switch to Local symptom tree. | Repair complete. |  |

#### STEP 1B. Check Local Start Only Lamp at Remote Panel

| **Conditions:** Locate remote panel Power lamp illuminated. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local start only lamp. | Is local start **only** lamp illuminated? **YES** | Repair complete. |
| Is local start **only** lamp illuminated? **NO** | 2A |  |

### STEP 2. Check Panel System Cable

#### STEP 2A. Check Remote Panel Cable

| **Conditions:** Locate and open customer interface box Locate and open remote panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel cable. Install a jumper between remote panel local mode supply terminal and the remote panel return terminal on remote panel control panel connector. Place one test lead on the remote panel local mode supply terminal in customer interface box X4 connector. Place the other test lead on the remote panel return terminal in the customer interface box X4 connector. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. Refer to the OEM service manual. | Repair complete. |  |

### STEP 3. Check Customer Interface Box Wiring

#### STEP 3A. Check the Remote Panel Local Supply Wire

| **Conditions:** Open the customer interface box Disconnect remote panel cable at X4 connector of the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel local mode supply wire. Place one test lead on the remote panel local mode supply pin in connector X4 of the customer interface box. Place the other test lead on the local mode supply terminal on the customer interface box logic unit. | Less than 10 ohms resistance? **YESRepair:** Replace the remote panel control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
