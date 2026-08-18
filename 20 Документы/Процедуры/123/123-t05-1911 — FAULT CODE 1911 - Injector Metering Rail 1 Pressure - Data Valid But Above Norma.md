---
aliases:
  - "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
type: "Процедура"
doc: "123-t05-1911"
title_en: "FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень"
modified: "2018-11-01"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1911.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-1911.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 1911 - Injector Metering Rail 1 Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Код 1911 — давление в топливной рампе 1 выше нормы — наивысший уровень**

> [!abstract] Процедура · `123-t05-1911`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-11-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-1911.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-1911.pdf)

Printable Version

## Warnings and Cautions

> [!danger] WARNING · Опасно
> Fuel is flammable. Keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on the fuel system.

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting personal injury, death or property damage, never smoke or allow sparks or flames (such as pilot lights, electrical switches, or welding equipment) in the work area.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823996 - female Weather Pack™ test lead, and Part Number 3824774 - breakout cable.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or inactive with more than one count in the last 25 engine hours? |
| STEP 2. | Clear the operation of the low pressure fuel system. |  |
|  | **STEP 2A.** Check for air in fuel. | Air present in the fuel flow line? |
|  | **STEP 2B.** Check the first stage fuel filter inlet pressure. | Fuel pressure greater than 0.35 bar \[5 psi\]? |
| STEP 3. | Check the operation of the fuel pump pressurizing assembly. |  |
|  | **STEP 3A.** Check fuel pump actuator. | Measured fuel rail pressure devated more than 200 bar \[2901 psi\] compared to the commanded fuel rail pressure? |
|  | **STEP 3B.** Inspect the fuel pump pressuring assembly o-ring. | O-ring cut or shaved? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault codes. | Fault Code 1911 inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 271, 272, 2311, 2261, 451, or 452 active or inactive with more than one count in the last 25 engine hours? **YES** | Appropriate troubleshooting tree. |
| Fault Code 271, 272, 2311, 2261, 451, or 452 active or inactive with more than one count in the last 25 engine hours? **NO** | 2A |  |

### STEP 2. Clear the operation of the low-pressure fuel system.

#### STEP 2A. Check for air in fuel.

| **Conditions:** Remove air bleed line from air bleed valve on the fuel drain manifold block. Route the air bleed line into a suitable container to collect fuel. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel flow for air. Use the following procedure in Service Manual, QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS. [[20-006-003 — Air in Fuel\|Refer to Procedure 006-003 in Section 6]]. | Air present in the fuel flow line? **YESRepair:** Repair or replace the damaged line or loose connection. Use the following procedure in the QSK19, QSK19 CM850 Modular Common Rail System, and QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin 4021592. [[20-006-024-tr — Fuel Supply Lines\|Refer to Procedure 006-024 in Section 6.]] | 4A |
| Air present in the fuel flow line? **NO** | 2B |  |

#### STEP 2B. Check the first stage fuel filter inlet pressure.

| **Conditions:** Turn keyswitch OFF Install the pressure gauge into fuel filter head port at inlet. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure inlet pressure. Turn keyswitch ON. Measure the inlet pressure to the first stage fuel filter. Refer to the equipment manufacturer service information. **Note**: If the engine will **not** start, perform this test while cranking the engine. | Fuel pressure greater than 0.35 bar \[5 psi\]? **YESRepair:** Refer to the equipment manufacturer service information. | 4A |
| Fuel pressure greater than 0.35 bar \[5 psi\]? **NO** | 3A |  |

### STEP 3. Check the operation of the fuel pump pressurizing assembly.

#### STEP 3A. Check the fuel pump actuator.

| **Conditions:** Turn keyswitch OFF. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel pump actuator. Run the engine at idle for at least one minute to purge air induced from previous steps. Use INSITE™ electronic service tool to monitor commanded fuel rail pressure and measured fuel rail pressure at idle. | Measured fuel rail pressure devated more than 200 bar \[2901 psi\] compared to the commanded fuel rail pressure? **YESRepair:** A malfunctioning fuel pump actuator has been detected. Replace the fuel pump actuator assembly. Refer to Procedure 019-117 in Section 19. | 4A |
| Measured fuel rail pressure devated more than 200 bar \[2901 psi\] compared to the commanded fuel rail pressure? **NO** | 3B |  |

#### STEP 3B. Inspect the fuel pump pressurizing assembly o-ring.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the fuel pump actuator. Remove the fuel pump actuator. Use the following procedure in the QSK19, QSK19 CM850 Modular Common Rail System, and QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin 4021592. Refer to Procedure 005-016 in Section 5. Inspect the fuel pump actuator and o-ring. If the o-ring is cut or shaved, fuel can be bypassing the fuel pump actuator and entering the high-pressure pump. | O-ring cut or shaved? **YESRepair:** Replace the damaged o-ring. Use the following procedure in the QSK19, QSK19 CM850 Modular Common Rail System, and QSK19 CM2150 Modular Common Rail System Service Manual, Bulletin 4021592. [[20-005-016-tr — Fuel Pump\|Refer to Procedure 005-016 in Section 5]]. | 4A |
| O-ring cut or shaved? **NO** | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault codes.

| **Conditions:** Connect all components Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault codes. Operate the engine within the “Conditions for Clearing the Fault Code” found in the Overview section of this troubleshooting procedure. Use INSITE™ electronic service tool to verify the inactive fault codes. | Fault Code 1911 inactive? **YES** | Repair complete |
| Fault Code 1911 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance |  |
