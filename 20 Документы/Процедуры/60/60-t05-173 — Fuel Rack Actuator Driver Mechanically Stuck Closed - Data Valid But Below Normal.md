---
aliases:
  - "Привод рейки механически заклинил в закрытом положении — ниже нормы — умеренный уровень"
type: "Процедура"
doc: "60-t05-173"
title_en: "Fuel Rack Actuator Driver Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Привод рейки механически заклинил в закрытом положении — ниже нормы — умеренный уровень"
modified: "2018-08-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-t05-173.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-t05-173.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Fuel Rack Actuator Driver Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Привод рейки механически заклинил в закрытом положении — ниже нормы — умеренный уровень**

> [!abstract] Процедура · `60-t05-173`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-08-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-t05-173.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-t05-173.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for active fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 173 active |
| STEP 2. | Clear the fault codes. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 173 inactive? |
|  | **STEP 2B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check for active fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 173 active? **YES** | Go to Fault Code 173. |
| Fault Code 173 active? **NORepair:** Replace the fuel pump. Refer to Procedure 005-012 in Section 5 (Fuel Injection Pumps, In-Line) in the QST30 Service Manual, Bulletin 4021539. | 2A |  |

### STEP 2. Clear the fault codes.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 173 inactive? **YES** | 2B |
| Fault Code 173 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Go to the appropriate troubleshooting charts. |  |
