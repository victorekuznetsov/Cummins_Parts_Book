---
aliases:
  - "Код 111 — критический внутренний отказ ЭБУ"
type: "Процедура"
doc: "178-t05-111"
title_en: "FAULT CODE 111 - Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component"
title_ru: "Код 111 — критический внутренний отказ ЭБУ"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
---

# FAULT CODE 111 - Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
**Код 111 — критический внутренний отказ ЭБУ**

> [!abstract] Процедура · `178-t05-111`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-111.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the ECM. |  |
|  | **STEP 1A.** Check the ECM. | Fault Code 111 inactive? |
|  | **STEP 1B.** Check the inactive counts of Fault Code 111. | Less than 3 counts? |
| STEP 2. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 2B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the ECM.

#### STEP 1A. Check the ECM.

| **Conditions:** Connect all components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM. Turn the keyswitch OFF and wait 5 seconds. Start the engine and let it idle for 1 minute. | Fault Code 111 inactive? **YES** | 1B |
| Fault Code 111 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 2A |  |

#### STEP 1B. Check the inactive counts of Fault Code 111.

| **Conditions:** Turn the keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the inactive counts of Fault Code 111. Use INSITE™ electronic service tool to read the inactive counts of Fault Code 111. | Less than 3 counts? **YES** | 2 |
| Less than 3 counts? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | Repair complete. |  |

### STEP 2. Check ECM calibration and clear fault codes.

#### STEP 2A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 2B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 2B |  |

#### STEP 2B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Engine Control Module | Refer to Procedure 019-031 | ISB3.9 CM2220 B107 | 4310792 |
| Engine Control Module | Refer to Procedure 019-031 | QSB4.5 CM2150 B108 | 4326163 |
| Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Engine Control Module | Refer to Procedure 019-031 | QSB7 CM2880 B117 | 4358390 |
| Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
| Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
| Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
| Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
| Engine Control Module | Refer to Procedure 019-031 | QSNT14 CM876 N102 | 4325993 |
| Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F104 | 4332741 |
| Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F108 | 4332746 |
| Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
| Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F116 | 4383664 |
| Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
| Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 F129 | 5411325 |
| Engine Control Module | Refer to Procedure 019-031 | ISF4.5 CM2220 F123 | 5411320 |
| Engine Control Module | Refer to Procedure 019-031 | QSG12 CM2880 G112 | 4388731 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F134B | 5504165 |
| Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
| Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
| Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
| Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
| Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
