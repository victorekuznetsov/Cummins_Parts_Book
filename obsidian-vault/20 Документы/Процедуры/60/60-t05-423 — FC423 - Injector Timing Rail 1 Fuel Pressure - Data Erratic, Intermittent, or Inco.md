---
aliases:
  - "FC423 — давление топлива в рампе опережения 1 — данные нестабильны или неверны"
type: "Процедура"
doc: "60-t05-423"
title_en: "FC423 - Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect"
title_ru: "FC423 — давление топлива в рампе опережения 1 — данные нестабильны или неверны"
modified: "2016-12-12"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-t05-423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-t05-423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# FC423 - Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect
**FC423 — давление топлива в рампе опережения 1 — данные нестабильны или неверны**

> [!abstract] Процедура · `60-t05-423`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-12-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-t05-423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-t05-423.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for multiple fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Codes 113 and 114 active? |
| STEP 2. | Measure fuel inlet restriction. |  |
|  | **STEP 2A.** Measure restriction. | Fuel restriction within specification? |
| STEP 3. | Check for a mechanical failure of the pump. |  |
|  | **STEP 3A.** Check the sleeve current. | Sleeve current changing? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 423 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check for multiple fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 113 and 114 active? **YES** | Appropriate troubleshooting tree |
| Fault Codes 113 and 114 active? **NO** | 2A |  |

### STEP 2. Measure fuel inlet restriction.

#### STEP 2A. Measure restriction.

| **Conditions:** Turn keyswitch ON. Start the engine and let it idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the fuel inlet restriction. Refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, QST30 Series Engines, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Fuel inlet restriction within specification? **YES** | 3A |
| Fuel inlet restriction within specification? **NORepair:** Refer to Procedure 006-020 (Fuel Inlet Restriction) in Section 6 of the Service Manual, QST30 Series Engines, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | Appropriate troubleshooting tree |  |

### STEP 3. Check for mechanical failure of the pump.

#### STEP 3A. Check the sleeve current.

| **Conditions:** Turn keyswitch ON. Start the engine and let it idle. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the sleeve current. Use INSITE™ electronic service tool to monitor the sleeve current while varying the engine rpm. | Sleeve current changing? **YESRepair:** Repair or replace the fuel pump. Refer to Procedure 005-016 (Fuel Pump) in Section 5 of the Service Manual, QST30 Series Engines, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. | 4A |
| Sleeve current changing? **NORepair:** Call for pre-authorization. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that Fault Code 423 is inactive. | Fault Code 423 inactive? **YES** | 4B |
| Fault Code 423 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Appropriate troubleshooting charts |  |
