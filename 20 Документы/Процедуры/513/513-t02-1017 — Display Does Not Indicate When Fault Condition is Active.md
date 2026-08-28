---
type: "Процедура"
doc: "513-t02-1017"
title_en: "Display Does Not Indicate When Fault Condition is Active"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Display Does Not Indicate When Fault Condition is Active

> [!abstract] Процедура · `513-t02-1017`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1017.pdf)

Printable Version

### Symptoms

- No fault or alarm code displays on ED-4 screen when malfunction is present.

### How To Use This Tree

This symptom tree can be used to troubleshoot Fault Display issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- Incorrect Vessel Personality File

- Vessel Personality File setup improperly

- Incorrect engine calibration.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault. |  |
|  | **STEP 1A.** Check the display. | Fault or alarm code in advance alarm screen? |
|  | **STEP 1B.** Check the setup in the ED-4 display. | ED-4 display set up properly? |
| STEP 2. | Check the Vessel Personality File. |  |
|  | **STEP 2A.** Check ED-4 display. | Vessel Personality File correct for this vessel? |
| STEP 3. | Check the engine control module (ECM) calibration. |  |
|  | **STEP 3A.** Check the ECM calibration. | ECM calibration setup properly? |
|  | **STEP 3B.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |

### STEP 1. Check the fault.

#### STEP 1A. Check the display.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the display. Check if fault is active in advance fault screen. | Fault or alarm code in advance alarm screen? **YES** | 1B |
| Fault or alarm code in advance alarm screen? **NORepair:** Download correct Vessel Personality File to the display from Cummins® QuickServe® On-line webpage. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the setup in the ED-4 display.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the setup in the ED-4 display. Verify ED-4 display is properly configured with the engine. Refer to Procedure 015-108 in Section 15. | ED-4 display setup properly? **YES** | 2A |
| ED-4 display setup properly? **NORepair:** Configure the ED-4 display properly for this engine. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete |  |

### STEP 2. Check the Vessel Personality File.

#### STEP 2A. Check ED-4 display.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check ED-4 display. Verify correct Vessel Personality File is downloaded in the display. Refer to Procedure 015-044 in Section 15. | Indicator on? **YES** | 3A |
| Indicator on? **NORepair:** Download correct Vessel Personality File to the display from Cummins® QuickServe® On-line webpage. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |  |

### STEP 3. Check the ECM calibration.

#### STEP 3A. Check the ECM calibration.

| **Conditions:** Turn enable switch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM calibration. Determine if components have been configured properly in the ECM. | ECM calibration setup properly? **YES** | 3B |
| ECM calibration setup properly? **NORepair:** Enable the proper components for multiplexing and make sure the SIM source addresses for each component are correct. | Repair complete |  |

#### STEP 3B. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check if an ECM calibration update is available. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YESRepair:** Request a Cummins® Marine Application Engineer on site. | Repair complete |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Reference Procedure 019-032 in Section 19 of the appropriate engine service manual. | Repair complete |  |
