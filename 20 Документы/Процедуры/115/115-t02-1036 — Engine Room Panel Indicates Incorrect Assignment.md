---
aliases:
  - "Пульт машинного отделения показывает неверное назначение"
type: "Процедура"
doc: "115-t02-1036"
title_en: "Engine Room Panel Indicates Incorrect Assignment"
title_ru: "Пульт машинного отделения показывает неверное назначение"
modified: "2006-06-12"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021587"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1036.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1036.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# Engine Room Panel Indicates Incorrect Assignment
**Пульт машинного отделения показывает неверное назначение**

> [!abstract] Процедура · `115-t02-1036`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2006-06-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1036.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/115-t02-1036.pdf)

Printable Version

### Symptoms

- The remote panel indicates the engine room panel is in the local mode.

- The local mode lamp is **not** illuminated on the engine room control panel.

### How To Use This Tree

This symptom tree can be used to troubleshoot panel symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check Engine Room Panel Local Start Only Button Operation |  |
|  | **STEP 1A.** Check Remote Panel Local Start Only Lamp | Lamp illuminated? |
| STEP 2. | Check Engine Room Panel Control Panel |  |
|  | **STEP 2A.** Check for Voltage to Control Panel | Lamp illuminated? |

### STEP 1. Check Engine Room Panel Local Start Only Button Operation

#### STEP 1A. Check Remote Panel Local Start Only Lamp

| **Conditions:** Verify that engine room panel power switch is on and lamp illuminated. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that remote panel power lamp is illuminated. Press the local start only on button on the engine room panel. Verify that the local start only lamp is illuminated on the remote panel. | Lamp illuminated? **YES** | 2A |
| Lamp illuminated? **NORepair:** Refer to Remote Panel Indicates Incorrect Assignment symptom tree. | Repair complete. |  |

### STEP 2. Check Engine Room Panel Control Panel

#### STEP 2A. Check for Voltage to Control Panel

| **Conditions:** Press local start only on button on the engine room panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel local start only lamp. | Lamp illuminated? **YES** | Repair complete. |
| Lamp illuminated? **NORepair:** Replace the engine room panel control panel. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
