---
type: "Процедура"
doc: "513-t02-1037"
title_en: "Display Data Incorrect"
modified: "2019-10-25"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1037.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1037.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Display Data Incorrect

> [!abstract] Процедура · `513-t02-1037`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1037.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1037.pdf)

Printable Version

### Symptoms

- Sensor parameters or data does **not** display correctly or is incorrect.

### How To Use This Tree

This symptom tree can be used to troubleshoot display data issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- Incorrect vessel personality file

- Vessel personality file setup improperly

- Incorrect engine calibration.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the ED-4 display. |  |
|  | **STEP 1A.** Check for active fault code. | Fault or alarm code active? |
|  | **STEP 1B.** Check the setup in the ED-4 display. | ED-4 display setup properly? |
|  | **STEP 1C.** Check the vessel personality file. | Vessel personality file correct for this vessel? |
| STEP 2. | Check the sensors. |  |
|  | **STEP 2A.** Check the sensor setup in the ED-4 display. | Affected sensor data turned on? |

### STEP 1. Check the ED-4 display.

#### STEP 1A. Check for active fault code.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for fault code. Check if fault is active in Advance Fault screen. | Fault or alarm code active? **YES** | Go to appropriate troubleshooting tree. |
| Fault or alarm code active? **NO** | 1B |  |

#### STEP 1B. Check the setup in the ED-4 display.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check vessel personality file. Verify correct vessel personality file is downloaded in the display. Refer to Procedure 015-044 in Section 15. | ED-4 display setup properly? **YES** | 1C |
| ED-4 display setup properly? **NORepair:** Configure the ED-4 display properly for this engine. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete. |  |

#### STEP 1C. Check the vessel personality file.

| **Conditions:** Turn enable switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check connections. Verify correct vessel personality file is downloaded in the display. Refer to Procedure 015-044 in Section 15. | Vessel personality file correct for this vessel? **YES** | 2A |
| Vessel personality file correct for this vessel? **NORepair:** Download correct vessel personality file to the display from Cummins QuickServe® Online. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |  |

### STEP 2. Check the sensors.

#### STEP 2A. Check the sensor setup in the ED-4 display.

| **Conditions:** Turn enable switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check voltage. In the ED-4 display, monitor I/O Configuration (under configuration) for affected sensor data. | Affected sensor data turned on? **YESRepair:** Go to the tree based off the sensor data that is incorrect. Transmission gear oil temperature, refer to Alarm Code 2562 in Section TA. Transmission gear oil pressure refer to Transmission Gear Oil Pressure Sensor Signal Wrong or Missing Troubleshooting Symptom Tree in Section TT. | Repair complete |
| Affected sensor data turned on? **NORepair:** Turn on data for affected sensor in the ED-4 display. Refer to Procedure 015-035 in Section 15. | Repair complete. |  |
