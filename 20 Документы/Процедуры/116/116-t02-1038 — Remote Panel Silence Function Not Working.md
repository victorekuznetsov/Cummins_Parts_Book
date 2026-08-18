---
aliases:
  - "Не работает функция отключения звука на дистанционном пульте"
type: "Процедура"
doc: "116-t02-1038"
title_en: "Remote Panel Silence Function Not Working"
title_ru: "Не работает функция отключения звука на дистанционном пульте"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1038.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1038.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Remote Panel Silence Function Not Working
**Не работает функция отключения звука на дистанционном пульте**

> [!abstract] Процедура · `116-t02-1038`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1038.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1038.pdf)

Printable Version

### Symptoms

- Alarm will **not** silence when silence button is pushed on remote panel

- Alarm will silence when silence button is pushed on DCU410 unit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The DCU410 unit and remote panels each have a silence button. The ECM delivers alarm information to the customer interface box logic unit. The customer interface box logic unit delivers alarm information to the DCU410 unit and remote panel. The DCU410 unit and remote panel deliver alarm information to the operator in visual and audible format. A silence button allows the audible alarm to be silenced.

When an alarm condition occurs the audible alarm can be shut off at all panels by pressing the silence button at any remote panel location.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
| STEP 2. | Check the remote panel alarm. |  |
|  | **STEP 2A.** Check the silence button at the DCU410 unit and remote panel. |  |
| STEP 3. | Check the remote panel wiring. |  |
|  | **STEP 3A.** Check the remote panel power switch supply wire for an open. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 2A |
| DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 2A |  |

### STEP 2. Check the remote panel alarm.

#### STEP 2A. Verify the silence button is functioning.

| **Conditions:** Open the customer interface box. Turn the DCU410 and remote panel switch to the OFF position. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the silence button at the DCU410 unit and remote panel. Place one test lead on the remote panel power switch supply wire at the X4 connection. Place the other test lead on the remote panel alarm silence supply wire at the X4 connection. Press the silence button. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3A |
| Less than 10 ohms? **NORepair:** Replace the remote panel. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

### STEP 3. Check the remote panel wiring.

#### STEP 3A. Check the remote panel power switch supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the remote panel alarm supply wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel power switch supply wire for an open. Place one test lead on the remote panel silence alarm supply wire at the DCU410 unit. Place the other test lead on the remote panel silence alarm supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |
