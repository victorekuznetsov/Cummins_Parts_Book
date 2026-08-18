---
aliases:
  - "Код 2261 — давление подачи топливного насоса выше нормы — низший уровень"
type: "Процедура"
doc: "122-t05-2261"
title_en: "FAULT CODE 2261 - Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Least Severe Level"
title_ru: "Код 2261 — давление подачи топливного насоса выше нормы — низший уровень"
modified: "2017-04-19"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2261.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-2261.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 2261 - Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Least Severe Level
**Код 2261 — давление подачи топливного насоса выше нормы — низший уровень**

> [!abstract] Процедура · `122-t05-2261`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-04-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2261.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-2261.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated before replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3823993 - male Deutsch™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the low-pressure fuel system. |  |
|  | **STEP 1A.** Check for active fault codes. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? |
|  | **STEP 1B.** Check the fuel supply lines. | Any fuel lines damaged, kinked, or restricted? |
|  | **STEP 1C.** Check the Stage 2 fuel filter restriction. | Stage 2 fuel filter restriction within specification? |
|  | **STEP 1C-1.** Check the fuel filter head. |  |
|  | **STEP 1D.** Check the fuel supply pressure at the fuel inlet manifold. | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? |
| STEP 2. | Disable and clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 2261 inactive? |
|  | **STEP 2B.** Clear the inactive fault codes | All fault codes cleared? |

### STEP 1. Check the fuel supply pressure fuel system.

#### STEP 1A. Check the fuel supply pressure sensor.

| **Conditions:** Connect the Compuchek™ tool. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start and operate the engine at high idle. Record the fuel supply sensor reading in INSITE™ electronic service tool. Record the fuel supply pressure reading on a pressure gauge installed in place of the fuel supply pressure sensor. Use the following procedure for Stage 2 filters in the Measure section of the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-024 in in the Associated Procedures Table. Use the following procedure for Stage 2 filters in the Measure section in the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-024 in the Associated Procedures Table. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2psia\] of each other? **YES** | 1B |
| INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2psia\] of each other? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in the Associated Procedures Table. | 2A |  |

#### STEP 1B. Check the fuel supply lines.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure 006-024 in the Associated Procedures Table. | Any fuel lines damaged, kinked, or restricted? **YESRepair:** Replace the damaged fuel line(s). | 2A |
| Any fuel lines damaged, kinked, or restricted? **NO** | 1C |  |

#### STEP 1C. Check the Stage 2 fuel filter restriction.

| **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-020 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-020 in in the Associated Procedures Table. | Stage 2 fuel filter restriction within specification? **YES** | 1D |
| Stage 2 fuel filter restriction within specification? **NORepair:** Replace the Stage 2 fuel filters. Use the following procedure in the K38,K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-076 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-076 in the Associated Procedures Table. | 1C-1 |  |

#### STEP 1C-1. Check the fuel filter head.

| **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the following procedure in the K38, K50,QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-020 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-020 in Associated Procedures Table. | Stage 2 fuel filter restriction within specification? **YES** | 2A |
| Stage 2 fuel filter restriction within specification? **NORepair:** Replace the Stage 2 fuel filter head. Use the following procedure in the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-020 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-020 in Associated Procedures Table. | 2A |  |

#### STEP 1D. Check the fuel supply pressure at the fuel inlet manifold.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Close the fuel supply valve. Remove the M14 STOR plug from the fuel inlet manifold. Install a Compuchek™ fitting, Part Number 3824844, or equivalent, in the fuel inlet manifold. Connect the vacuum gauge and adapter, Part Number 3164491, or equivalent, and digital multimeter, Part Number 3164488 or 3164489,or equivalent, to the Compuchek™ fitting. Open the fuel supply valve. Start and operate the engine at low idle and high idle. Record the fuel inlet pressure readings. | Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? **YESRepair:** Replace the fuel pump. Use the following procedure the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 005-016 in the Associated Procedures Table. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 005-016 in the Associated Procedures Table. | 2A |
| Fuel inlet pressure always less than 34.5 kPaG \[5 psig\]? **NORepair:** Refer to the equipment manufacturer service information to reduce fuel inlet pressure. | 2A |  |

### STEP 2. Disable and clear the fault code.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. Start and operate the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 2261 inactive? **YES** | 2B |
| Fault Code 2261 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | 1A |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Fuel Pump | [[28-005-016-tr — Fuel Pump\|Refer to Procedure 005-016]] | K38, K50, QSK38 and QSK50 | 4021528 |
| Fuel Pump | Refer to Procedure 005-016 | QSK38 and QSK50 | 4021530 |
| Fuel Filter Head | [[28-006-017-tr — Fuel Filter Head\|Refer to Procedure 006-017]] | K38, K50, QSK38 and QSK50 | 4021528 |
| Fuel Filter Head | Refer to Procedure 006-017 | QSK38 and QSK50 | 4021530 |
| Fuel Inlet Restriction | [[28-006-020-tr — Fuel Inlet Restriction\|Refer to Procedure 006-020]] | K38, K50, QSK38 and QSK50 | 4021528 |
| Fuel Inlet Restriction | Refer to Procedure 006-020 | QSK38 and QSK50 | 4021530 |
| Fuel Supply Lines | [[28-006-024-tr — Fuel Supply Lines\|Refer to Procedure 006-024]] | K38, K50, QSK38 and QSK50 | 4021528 |
| Fuel Supply Lines | Refer to Procedure 006-024 | QSK38 and QSK50 | 4021530 |
| Fuel Filter (Stage 2) | Refer to Procedure 006-076 | K38, K50, QSK38 and QSK50 | 4021528 |
| Fuel Filter (Stage 2) | Refer to Procedure 006-076 | QSK45 and QSK60 | 4021530 |
| Fuel Supply Pump Pressure Sensor | Refer to Procedure 019-398 | QSK19 | 4022094 |
| Fuel Supply Pump Pressure Sensor | Refer to Procedure 019-398 | QSK38, QSK50, and QSK60 | 4022102 |
