---
aliases:
  - "Код 1852 — индикатор воды в топливе выше нормы — умеренный уровень"
type: "Процедура"
doc: "00-t05-1852"
title_en: "FAULT CODE 1852 - Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Код 1852 — индикатор воды в топливе выше нормы — умеренный уровень"
modified: "2021-06-14"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
  - "41353297"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
manuals:
  - "4022094"
  - "4022102"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-t05-1852.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-t05-1852.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "группа/00"
---

# FAULT CODE 1852 - Water in Fuel Indicator - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Код 1852 — индикатор воды в топливе выше нормы — умеренный уровень**

> [!abstract] Процедура · `00-t05-1852`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-06-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-t05-1852.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-t05-1852.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check the fault codes. | Active or inactive counts of Fault Code 1852? |
| STEP 2. | Check the engine control module (ECM) calibration and clear the fault codes. |  |
|  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 2B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check the fault codes.

| **Conditions:** Turn keyswitch ON. Connect the recommended Cummins® electronic service tool, or equivalent. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for Fault Code 1852. Use the electronic service tool to read the fault codes. | Active or inactive counts of Fault Code 1852? **YESRepair:** Drain water from the fuel filter(s). If the fault code persists, check the sensor and harness connector for water intrusion. Clean or replace the connector or sensor, as necessary. | 2A |
| Active or inactive counts of Fault Code 1852? **NO** | Repair complete. |  |

### STEP 2. Check the ECM calibration and clear the fault codes.

#### STEP 2A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect the electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use the electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 2B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 2B |  |

#### STEP 2B. Disable the fault code.

| **Conditions:** Connect all components. Connect the electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
