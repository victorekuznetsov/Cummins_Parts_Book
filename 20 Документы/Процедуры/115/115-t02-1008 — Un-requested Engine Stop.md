---
aliases:
  - "Самопроизвольный останов двигателя"
type: "Процедура"
doc: "115-t02-1008"
title_en: "Un-requested Engine Stop"
title_ru: "Самопроизвольный останов двигателя"
modified: "2006-06-12"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Un-requested Engine Stop
**Самопроизвольный останов двигателя**

> [!abstract] Процедура · `115-t02-1008`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1008.pdf)

Printable Version

### Symptoms

- The engine stops without the operator pushing the stop button on the engine room panel or remote panel.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine stop symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Customer Interface Box |  |
|  | **STEP 1A.** Check Customer Interface Box Logic Unit | Is stop lamp illuminated? |
| STEP 2. | Check Engine Room Panel |  |
|  | **STEP 2A.** Check Engine Room Panel Control Panel | Less than 10 ohms resistance? |
| STEP 3. | Check Remote Panel |  |
|  | **STEP 3A.** Check Remote Panel Control Panel | Less than 10 ohms resistance? |

### STEP 1. Check Customer Interface Box

#### STEP 1A. Check Customer Interface Box Logic Unit

| **Conditions:** Locate customer interface box Open customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify stop lamp is illuminated. | Is stop lamp illuminated? **YES** | 2A |
| Is stop lamp illuminated? **NORepair:** Refer to the Engine Executes Un-requested Engine Stop Troubleshooting Tree | Repair complete. |  |

### STEP 2. Check Engine Room Panel

#### STEP 2A. Check Engine Room Panel Control Panel

| **Conditions:** Locate engine room panel Open engine room panel door Disconnect control panel connector X4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel control panel. Place one test lead in the engine room panel stop supply pin on the control panel X4 connector. Place the other test lead in the engine room power switch supply pin on the control panel X4 connector. | Less than 10 ohms resistance? **YESRepair:** Replace the engine room panel control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |
| Less than 10 ohms resistance? **NO** | 3A |  |

### STEP 3. Check Remote Panel

#### STEP 3A. Check Remote Panel Control Panel

| **Conditions:** Locate remote panel Open remote panel Disconnect remote panel control panel connector X4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel control panel. Place one test lead in the remote panel power switch supply pin on the control panel X4 connector. Place the other test lead on the remote panel stop supply pin of the control panel X4 connector. | Less than 10 ohms resistance? **YESRepair:** Replace the remote control panel control panel. Refer to Procedure [[115-015-025 — Remote Panel\|015-025]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace customer interface box logic unit. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |
