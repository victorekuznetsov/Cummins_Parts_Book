---
type: "Процедура"
doc: "300-t02-1109"
title_en: "Shutdown Unit Buzzer Does Not Activate With Fault"
modified: "2019-05-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1109.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1109.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Shutdown Unit Buzzer Does Not Activate With Fault

> [!abstract] Процедура · `300-t02-1109`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1109.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1109.pdf)

Printable Version

### Symptoms

- Fault code registered with no activation of shutdown unit buzzer.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The shutdown unit input signals are switches. These switches are normally open. They are closed when activated. The buzzer is internal to the shutdown unit and has no external wiring.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for active fault codes. | Active fault codes? |
| STEP 2. | Check the shutdown unit. |  |
|  | **STEP 2A.** Check for buzzer function at the shutdown unit. | Does buzzer function? |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for active fault codes.

| **Conditions:** Turn keyswitch ON. Check the control panel for active fault codes. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. | Active fault codes? **YESRepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |
| Active fault codes? **NO** | 2A |  |

### STEP 2. Check the shutdown unit.

#### STEP 2A. Check for buzzer function at the shutdown unit.

| **Conditions:** No fault code registered at the shutdown unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for buzzer function at the shutdown unit. | Does buzzer function? **YES** | 3A |
| Does buzzer function? **NORepair:** Replace the shutdown unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Clear the inactive fault codes.

| **Conditions:** Turn keyswitch ON. Check the control panel for inactive fault codes. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Check the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Contact a Cummins® Authorized Repair Location |  |
