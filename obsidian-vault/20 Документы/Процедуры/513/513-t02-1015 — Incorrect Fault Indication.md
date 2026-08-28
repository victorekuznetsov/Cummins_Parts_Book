---
aliases:
  - "Неверная индикация неисправности"
type: "Процедура"
doc: "513-t02-1015"
title_en: "Incorrect Fault Indication"
title_ru: "Неверная индикация неисправности"
modified: "2019-10-21"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Incorrect Fault Indication
**Неверная индикация неисправности**

> [!abstract] Процедура · `513-t02-1015`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1015.pdf)

Printable Version

### Symptoms

- Incorrect fault displayed on ED-4 screen.

### How To Use This Tree

This symptom tree can be used to troubleshoot Fault Display Software issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- Incorrect Vessel Personality File

- Vessel Personality File setup improperly.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the Vessel Personality File. |  |
|  | **STEP 1A.** Check Vessel Personality File. | Is Vessel Personality File correct? |
| STEP 2. | Check the engine control module (ECM) calibration. |  |
|  | **STEP 2A.** Check the ECM calibration. | ECM calibration setup properly? |
|  | **STEP 2B.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |

### STEP 1. Check the Vessel Personality File.

#### STEP 1A. Check Vessel Personality File.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify correct Vessel Personality File is downloaded in the display. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Is Vessel Personality File correct? **YES** | 2A |
| Is Vessel Personality File correct? **NORepair:** Download correct Vessel Personality File to the display from Cummins® QuickServe® On-line webpage. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete. |  |

### STEP 2. Check the ECM calibration.

#### STEP 2A. Check the ECM calibration.

| **Conditions:** Turn enable switch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine if components have been configured properly in the ECM. | ECM calibration setup properly? **YES** | 2B |
| ECM calibration setup properly? **NORepair:** Enable the proper components for multiplexing and make sure the SIM source addresses for each component are correct. | Repair complete. |  |

#### STEP 2B. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YESRepair:** Request a Cummins® Marine Application Engineer on site. | Repair complete. |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Reference Procedure 019-032 in Section 19 of the appropriate engine service manual. | Repair complete. |  |
