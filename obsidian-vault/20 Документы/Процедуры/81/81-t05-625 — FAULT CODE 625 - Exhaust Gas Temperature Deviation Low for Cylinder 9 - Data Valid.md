---
type: "Процедура"
doc: "81-t05-625"
title_en: "FAULT CODE 625 - Exhaust Gas Temperature Deviation Low for Cylinder 9 - Data Valid But Below Normal Operating Range - Least Severe Level"
modified: "2014-06-03"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-625.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-625.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# FAULT CODE 625 - Exhaust Gas Temperature Deviation Low for Cylinder 9 - Data Valid But Below Normal Operating Range - Least Severe Level

> [!abstract] Процедура · `81-t05-625`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-625.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-625.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the exhaust sensor circuit cylinder 9 accuracy. |  |
|  | **STEP 1A.** Verify the exhaust gas temperature sensor circuit cylinder 9 accuracy. | Temperature measurement from the infrared thermometer within 15 percent of the exhaust gas temperature sensor circuit cylinder 9 reading with INSITE™ electronic service tool? |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 625 inactive? |
|  | **STEP 2B.** Clear any inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the exhaust gas temperature sensor circuit cylinder 9 accuracy.

#### STEP 1A. Verify the exhaust gas temperature sensor circuit cylinder 9 accuracy.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the exhaust gas temperature sensor circuit cylinder 9 accuracy with an infrared thermometer. Start the engine. Connect INSITE™ electronic service tool. Use an infrared thermometer to measure and record the surface temperature at the exhaust port side of the cylinder head. Compare the infrared thermometer temperature measurement with the exhaust gas temperature sensor circuit cylinder 9 reading on INSITE™ electronic service tool monitor screen. | Temperature measurement from the infrared thermometer within 15 percent of the exhaust gas temperature sensor circuit cylinder 9 reading with INSITE™ electronic service tool? **YESRepair:** Possible cylinder or injector damage **must** be investigated. | Engine Performance Troubleshooting Tree |
| Temperature measurement from the infrared thermometer within 15 percent of the exhaust gas temperature sensor circuit cylinder 9 reading with INSITE™ electronic service tool? **NORepair:** A damaged exhaust gas temperature sensor has been detected. Replace the exhaust gas temperature sensor. Refer to Procedure 019-013 in Section 19. | 2A |  |

### STEP 2. Clear the fault codes.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 625 inactive? **YES** | 2B |
| Fault Code 625 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear any inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
