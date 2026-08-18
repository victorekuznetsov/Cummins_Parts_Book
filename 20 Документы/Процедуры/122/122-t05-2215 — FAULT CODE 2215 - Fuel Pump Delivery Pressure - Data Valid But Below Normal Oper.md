---
aliases:
  - "Код 2215 — давление подачи топливного насоса ниже нормы — умеренный уровень"
type: "Процедура"
doc: "122-t05-2215"
title_en: "FAULT CODE 2215 - Fuel Pump Delivery Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Код 2215 — давление подачи топливного насоса ниже нормы — умеренный уровень"
modified: "2015-04-07"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2215.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-2215.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 2215 - Fuel Pump Delivery Pressure - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Код 2215 — давление подачи топливного насоса ниже нормы — умеренный уровень**

> [!abstract] Процедура · `122-t05-2215`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-04-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2215.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-2215.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check if engine will start or engine starts and dies. |  |
|  | **STEP 1A.** Attempt to start the engine. | Engine starts and continues operating? |
| STEP 2. | Check the low pressure side of the fuel system. |  |
|  | **STEP 2A.** Check for external fuel leaks. | Fuel leaking externally? |
|  | **STEP 2B.** Check for air in the fuel. | Air present in fuel flow? |
|  | **STEP 2C.** Check the fuel supply pressure sensor. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? |
|  | **STEP 2D.** Inspect the original equipment manufacturer (OEM) fuel supply hose and fuel tank. | Stage 1 inlet restriction greater than specification? |
|  | **STEP 2E.** Check the Stage 1 filter restriction. | Stage 1 filter restriction less than specification? |
| STEP 3. | Disable and clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 2215 inactive? |
|  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check if engine will start or engine starts and dies.

#### STEP 1A. Attempt to start engine.

| **Conditions:** Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Attempt to start the engine. Check if the engine will **not** start or if the engine starts and stalls. | Engine starts and continues operating? **YES** | 2A |
| Engine starts and continues operating? **NO** | Reference the Engine Performance troubleshooting symptom tree |  |

### STEP 2. Check the low pressure side of the fuel system.

#### STEP 2A. Check for external fuel leaks.

| **Conditions:** Operate the engine at idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start the engine and check for external fuel leaks. Check for external fuel leaks. | Fuel leaking externally? **YESRepair:** Repair all fuel leaks. Use the following procedure from the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-024 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-024 in Section 6. | 3A |
| Fuel leaking externally? **NO** | 2B |  |

#### STEP 2B. Check for air in fuel.

| **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Direct the fuel flow from the air bleed line into a container. Inspect fuel flow for air. Use the following procedure in Service Manual, K38, K50, QSK38 and QSK50, Bulletin 4021528. [[28-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]]. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin 4021530. Refer to Procedure 006-003 in Section 6. | Air present in the fuel flow? **YESRepair:** Repair or replace the damaged line or loose connection. Use the following procedure from the K38, K50, QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-024 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-024 in Section 6. | 3A |
| Air present in the fuel flow? **NO** | 2C |  |

#### STEP 2C. Check the fuel supply pressure sensor.

| **Conditions:** Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel supply pressure sensor accuracy. Start and operate the engine at high idle. Record the fuel supply sensor reading in INSITE™ electronic service tool. Shut the engine down and remove the fuel supply pressure sensor. Refer to Procedure 019-398 in Section 19. Install a pressure gauge. Start and operate the engine at high idle. Record the fuel supply pressure reading on a pressure gauge installed in place of the fuel supply pressure sensor. | INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? **YESRepair:** Install the fuel supply pressure sensor that was removed. Refer to Procedure 019-398 in Section 19. | 2D |
| INSITE™ electronic service tool and pressure gauge readings within 14 kPa \[2 psia\] of each other? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in Section 19. | 3A |  |

#### STEP 2D. Inspect the OEM fuel supply hose and fuel tank.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure fuel inlet restriction at the Stage 1 fuel filter inlet. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin 4021528. Refer to Procedure 006-020 in Section 6. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin 4021530. Refer to Procedure 006-020 in Section 6. | Stage 1 inlet restriction greater than specification? **YESRepair:** Refer to the equipment manufacturer service information for repair instructions. | 3A |
| Stage 1 inlet restriction greater than specification? **NO** | 2E |  |

#### STEP 2E. Check the Stage 1 filter restriction.

| **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the Stage 1 fuel filter restriction. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin 4021528. Refer to Procedure 006-020 in Section 6. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin 4021530. Refer to Procedure 006-020 in Section 6. | Stage 1 filter restriction less than specification? **YESRepair:** Replace the high pressure pump assembly. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin 4021528. Refer to Procedure 005-016 in Section 5. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin 4021530. Refer to Procedure 005-016 in Section 5. | 3A |
| Stage 1 filter restriction less than specification? **NORepair:** Replace the Stage 1 fuel filter. For K38, K50, and QSK50 Series Engines, use the following procedure in Bulletin 4021528. Refer to Procedure 006-075 in Section 6. For QSK45 and QSK60 Series Engines, use the following procedure in Bulletin 4021530. Refer to Procedure 006-075 in Section 6. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 2215 inactive? **YES** | 3B |
| Fault Code 2215 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 3B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
