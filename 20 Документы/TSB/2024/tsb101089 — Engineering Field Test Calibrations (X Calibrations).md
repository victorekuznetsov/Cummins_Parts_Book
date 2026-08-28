---
type: "TSB"
doc: "tsb101089"
title_en: "Engineering Field Test Calibrations (X Calibrations)"
released: "2024-10-04"
modified: "2024-10-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
  - "82099327"
  - "93948840"
families:
  - "QSB6.7"
  - "QSM11"
  - "QSX15"
  - "QSZ13"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101089.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101089.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSB6.7"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "двигатель/QSZ13"
  - "год/2024"
---

# Engineering Field Test Calibrations (X Calibrations)

> [!abstract] TSB · `tsb101089`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]], [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]], [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** QSB6.7, QSM11, QSX15, QSZ13
> **Даты:** выпущен 2024-10-04 · изменён 2024-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101089.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb101089.pdf)

## Engineering Field Test Calibrations (X Calibrations)

### Core Issue

Engineering field test (or “X”) Calibrations are used by Cummins Inc. calibrations groups as preproduction field test calibrations, often used to test forthcoming corrective actions that will be released in warrantable production versions. X cals are also used as prototype calibrations for new equipment models. X calibrations are intended to be replaced by an appropriate production calibration when one becomes available.

### Confirmation

All Industrial Mid Range and Heavy Duty engines may be candidates for having an X calibration installed.

No fault codes will be active.

No potential component damage exists.

### Resolution

Having an X calibration in a machine does **not** represent a “failure”. However, X calibrations should immediately be replaced with appropriate production calibrations once they become available.

NOTE: Replacing an X calibration with a production calibration will require a Fleetcount password.

Verify if you have an X calibration installed by connecting to the ECM with INSITE™ electronic service tool and viewing “Features and Parameters”, then expanding “System ID and Dataplate”, and then expanding “Calibration Information”.

When troubleshooting any problem on an engine equipped with an X calibration, check the X Calibration Revision History and Released Calibration Cross Reference.

1. Insert the latest INCAL™ DVD into your computer.
2. Double click on “My Computer” on your Desktop.
3. Double click on the “E:” drive.
4. Double click on the “X cal” folder. Inside this folder will be an instruction file in PowerPoint format and the actual matrix in Excel format.

If a released calibration is available, install the released calibration in the ECM. X calibrations are temporary fixes and are not intended as permanent calibrations in any Cummins® engines. Service engineering recommends installing an appropriate released calibration whenever possible. Reference the X calibration cross reference, QSOL, or the OEM if you have questions about the availability of released calibrations.

If a released production calibration is **not** available, see if a more recent X calibration is available. If a more recent X calibration is **not** listed, troubleshoot the complaint using the appropriate published information and established troubleshooting procedures.

If a released calibration to replace the X cal is available, which resolves a complaint and is specified in the cal rev history as a warrantable corrective action, the claim should be filed to warranty.

If you are working on an engine that contains an X calibration or if a repair requires the recalibration of the engine with any X calibration, submit a Technical Service Request. See a Cummins® Distributor for support.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
