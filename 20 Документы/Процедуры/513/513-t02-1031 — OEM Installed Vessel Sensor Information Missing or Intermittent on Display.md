---
type: "Процедура"
doc: "513-t02-1031"
title_en: "OEM Installed Vessel Sensor Information Missing or Intermittent on Display"
modified: "2020-06-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1031.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1031.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# OEM Installed Vessel Sensor Information Missing or Intermittent on Display

> [!abstract] Процедура · `513-t02-1031`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TA - Troubleshooting Alarm Codes · Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2020-06-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1031.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1031.pdf)

Printable Version

### Symptoms

- Sensor parameters or data does **not** display correctly or is incorrect.

### How To Use This Tree

This symptom tree can be used to troubleshoot display data issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- Incorrect vessel personality file

- Customer interface box (C.I.B.)

- Original equipment manufacutrer (OEM) sensors.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the ED-4 display. |  |
|  | **STEP 1A.** Check for active fault code. | Fault or alarm code active? |
|  | **STEP 1B.** Check vessel personality file. | Vessel personality file correct for this vessel? |
|  | **STEP 1C.** Check the sensor connections. | All sensors and connections installed properly? |
| STEP 2. | Check the C.I.B. |  |
|  | **STEP 2A.** Check the sensor setup in the ED-4 display. | Approximately 5 volts? |

### STEP 1. Check the ED-4 display.

#### STEP 1A. Check for active fault code.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for fault code. Check if fault is active in Advanced fault screen. | Fault or alarm code active? **YES** | Go to appropriate troubleshooting tree or refer to procedure mentioned in fault code description on the Advanced Fault screen. |
| Fault or alarm code active? **NO** | 1B |  |

#### STEP 1B. Check vessel personality file.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check vessel personality file. Verify correct vessel personality file is downloaded in the display. Refer to Procedure 015-044 in Section 15. | Vessel personality file correct for this vessel? **YES** | 1C |
| Vessel personality file correct for this vessel? **NORepair:** Download correct vessel personality file to the display from Cummins QuickServe® Online. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |  |

#### STEP 1C. Check the sensor connections.

| **Conditions:** Turn enable switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check connections. Inspect sensor, harness, and terminal block connections on OEM sensor wiring harness. | All sensor and connections installed properly? **YES** | 2A |
| All sensor and connections installed properly? **NORepair:** Repair or fix connections or installation. | Repair complete |  |

### STEP 2. Check the C.I.B.

#### STEP 2A. Check the sensor setup in the ED-4 display.

| **Conditions:** Turn enable switch OFF. Disconnect the OEM sensor wiring harness from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check voltage. Place one lead on sensor SUPPLY pin 1 on the C.I.B. connector (mating to the OEM sensor harness). Place the other lead on sensor RETURN pin 2 on the C.I.B. connector (mating to the OEM sensor harness). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Approximately 5 volts? **YESRepair:** Repair or replace the OEM sensor wiring harness. Refer to Procedure 015-103 in Section 15. | Repair complete |
| Approximately 5 volts? **NORepair:** Replace the C.I.B. Refer to Procedure 015-023 in Section 15. | Repair complete |  |
