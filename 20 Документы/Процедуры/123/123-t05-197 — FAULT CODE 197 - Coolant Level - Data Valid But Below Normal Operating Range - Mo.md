---
aliases:
  - "Код 197 — уровень ОЖ ниже нормы — умеренный уровень"
type: "Процедура"
doc: "123-t05-197"
title_en: "FAULT CODE 197 - Coolant Level - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Код 197 — уровень ОЖ ниже нормы — умеренный уровень"
modified: "2015-03-10"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-197.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-197.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 197 - Coolant Level - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Код 197 — уровень ОЖ ниже нормы — умеренный уровень**

> [!abstract] Процедура · `123-t05-197`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-03-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-197.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-197.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for Fault Code 197. | Active or inactive counts of Fault Code 197? |
|  | **STEP 1B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
|  | **STEP 1C.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100k ohms? |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 197 inactive? |
|  | **STEP 2B.** Clear the inactive fault code. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for Fault Code 197.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for fault codes. Use INSITE™ electronic service tool to read the fault codes. | Active or inactive counts of Fault Code 197? **YES** | 1B |
| Active or inactive counts of Fault Code 197? **NO** | Repair complete |  |

#### STEP 1B. Check for an open circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM 60-pin port connector. Disconnect the engine coolant level sensor connector from the OEM harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the coolant level 1 5 volt (sensor supply 1) SUPPLY pin in the OEM harness ECM 60-pin port connector and the coolant level 1 5 volt supply (sensor supply 1) SUPPLY pin in the OEM harness engine coolant level sensor 1 connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** An open SUPPLY wire has been detected in the OEM harness. Troubleshoot each section of the OEM harness to determine which contains the pin-to-pin short. Check all harnesses connected in series. Replace the damaged section of the engine harness or OEM harness. Refer to Procedure 019-071 in Section 19. | 2A |  |

#### STEP 1C. Check for a pin-to-pin short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM 60-pin port connector. Disconnect the engine coolant level sensor 1 from the OEM harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the engine coolant level 1 SIGNAL pin of the OEM harness ECM connector and all other pins in the OEM harness ECM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** See the Coolant Loss troubleshooting symptom tree in the QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual, Bulletin 4021592. If Fault Code 197 is active and the coolant level is **not** low, a malfunctioning coolant level sensor is a likely cause. Refer to the OEM service manual before replacing the coolant level sensor. | Appropriate troubleshooting steps |
| Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the SIGNAL wire has been detected in the OEM harness. Troubleshoot each section of the OEM harness to determine which contains the pin-to-pin short circuit. Replace the damaged section of the engine harness or OEM harness. Refer to Procedure 019-071 in Section 19. | Repair complete |  |

### STEP 2. Clear the fault codes

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 197 inactive? **YES** | 2B |
| Fault Code 197 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair location if all steps have been completed and checked a second time. | 1A |  |

#### STEP 2B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service to clear the fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
