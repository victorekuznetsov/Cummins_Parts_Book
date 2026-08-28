---
aliases:
  - "Код 173 — заклинивание рейки управления подачей"
type: "Процедура"
doc: "87-t05-173"
title_en: "FAULT CODE 173 - Fuel Control Rack Stuck"
title_ru: "Код 173 — заклинивание рейки управления подачей"
modified: "2018-08-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-173.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-173.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# FAULT CODE 173 - Fuel Control Rack Stuck
**Код 173 — заклинивание рейки управления подачей**

> [!abstract] Процедура · `87-t05-173`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-08-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-173.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-t05-173.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for active fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 166 active |
| STEP 2. | Clear the fault codes. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 173 inactive |
|  | **STEP 2B.** Clear the inactive fault codes. | All fault codes cleared |

### STEP 1. Check for active fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 166 active | Fault Code 166 |
| Replace the fuel pump. Refer to Procedure 005-012 in Section 5. | 2A |  |

### STEP 2. Clear the fault codes.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault. | Fault Code 173 inactive | 2B |
| Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
