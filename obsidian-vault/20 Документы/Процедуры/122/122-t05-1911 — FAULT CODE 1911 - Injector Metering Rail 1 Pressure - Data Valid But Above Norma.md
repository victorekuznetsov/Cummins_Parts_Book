---
aliases:
  - "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
type: "Процедура"
doc: "122-t05-1911"
title_en: "FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
modified: "2015-04-10"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1911.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1911.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень**

> [!abstract] Процедура · `122-t05-1911`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-04-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1911.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-1911.pdf)

Printable Version

## Warnings and Cautions

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823996 - Female Weather-Pack™ test lead, and Part Number 3824774 - breakout cable.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of Fault Code 271, 272, 2311, 2261, 451, or 452? |
| STEP 2. | Clear the operation of the low-pressure fuel system. |  |
|  | **STEP 2A.** Check for air in fuel. | Air present in the fuel flow line? |
|  | **STEP 2B.** Check the first stage fuel filter inlet pressure. | Fuel pressure greater than 0.35 bar \[5 psi\]? |
|  | **STEP 2C.** Check the first stage fuel filter inlet pressure with the engine running. | Fuel pressure greater than 0.35 bar \[5 psi\]? |
| STEP 3. | Check the operation of the fuel pump pressurizing assembly. |  |
|  | **STEP 3A.** Inspect the fuel pump pressurizing assembly o-ring. | O-ring cut or shaved? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault codes. | Fault Code 1911 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of Fault Code 271, 272, 2311, 2261, 451, or 452? **YES** | Appropriate troubleshooting tree. |
| Fault Code 271, 272, 2311, 2261, 451, or 452 active or many inactive counts of Fault Code 271, 272, 2311, 2261, 451, or 452? **NO** | 2A |  |

### STEP 2. Clear the operation of the low-pressure fuel system.

#### STEP 2A. Check for air in fuel.

| **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel flow for air. Use the following procedure in Service Manual, K38, K50, QSK38 and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. [[28-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6.]] Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. [[56-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]]. | Air present in the fuel flow line? **YESRepair:** Repair or replace the damaged line or loose connection. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 006-024 in Section 6. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 006-024 in Section 6. | 4A |
| Air present in the fuel flow line? **NO** | 2B |  |

#### STEP 2B. Check the first stage fuel filter inlet pressure with the engine stopped.

| **Conditions:** Turn keyswitch OFF. Install the pressure gauge into the fuel filter head port at the inlet. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure inlet pressure. Measure the inlet pressure to the first stage fuel filter. | Fuel pressure greater than 0.35 bar \[5 psi\]? **YESRepair:** Refer to the equipment manufacturer service information. | 4A |
| Fuel pressure greater than 0.35 bar \[5 psi\]? **NO** | 2C |  |

#### STEP 2C. Check the first stage fuel filter inlet pressure with the engine running.

| **Conditions:** Turn keyswitch OFF. Install the pressure gauge into fuel filter head port at inlet. Turn keyswitch ON. Operate engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure inlet pressure. Measure the inlet pressure to the first stage fuel filter. If the engine will **not** start, perform this test while cranking the engine. | Fuel pressure greater than 0.35 bar \[5 psi\]? **YESRepair:** Refer to the equipment manufacturer service information. | 4A |
| Fuel pressure greater than 0.35 bar \[5 psi\]? **NO** | 3A |  |

### STEP 3. Check the operation of the fuel pump pressurizing assembly.

#### STEP 3A. Inspect the fuel pump pressurizing assembly o-ring.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel pump pressurizing assembly. Remove the fuel pump pressurizing assembly. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-232 in Section 5. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-232 in Section 5. Inspect the fuel pump pressurizing assembly o-ring. If the o-ring is cut or shaved; fuel can be bypassing the fuel pump pressuring assembly and entering the high-pressure pump. | O-ring cut or shaved? **YESRepair:** Replace the damaged o-ring. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-232 in Section 5. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-232 in Section 5. | 4A |
| O-ring cut or shaved? **NORepair:** Replace the fuel pump pressurizing assembly and mechanical dump valve. Use the following procedure in Service Manual, K38, K50, and QSK50, Bulletin [[4021528 — K38, K50, QSK38, and QSK50 Service Manual\|4021528]]. Refer to Procedure 005-232 in Section 5 and Refer to Procedure 006-061 in Section 6. Use the following procedure in Service Manual, QSK45 and QSK60, Bulletin [[4021530 — QSK45 and QSK60 Service Manual\|4021530]]. Refer to Procedure 005-232 in Section 5 and Refer to Procedure 006-061 in Section 6. | 4A |  |

### STEP 4. Clear the fault codes

#### STEP 4A. Disable the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. Operate engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault codes. Use INSITE electronic service tool to verify the fault code is inactive. | Fault Code 1911 inactive? **YES** | 4B |
| Fault Code 1911 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE electronic service tool to clear any inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Appropriate troubleshooting steps |  |
