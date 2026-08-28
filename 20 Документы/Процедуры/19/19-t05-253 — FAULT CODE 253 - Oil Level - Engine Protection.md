---
type: "Процедура"
doc: "19-t05-253"
title_en: "FAULT CODE 253 - Oil Level - Engine Protection"
modified: "2012-04-23"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-253.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-253.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# FAULT CODE 253 - Oil Level - Engine Protection

> [!abstract] Процедура · `19-t05-253`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-04-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-253.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-253.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for multiple fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 252 inactive? |
| STEP 2. | Check the oil level. |  |
|  | **STEP 2A.** Verify the oil level. | Oil level correct? |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 253 inactive? |
|  | **STEP 3B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check for multiple fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 252 not active? | 2A |
|  | Multiple fault code trees |  |

### STEP 2. Check the oil level.

#### STEP 2A. Verify the oil level.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the oil level using the oil dipstick. | Oil level correct? Replace the oil level sensor. [[19-019-056 — Lubricating Oil Level Sensor\|Refer to Procedure 019-056 in Section 19.]] | 3A |
| Fill the engine lubricating oil to the appropriate level. Reference the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098, the Troubleshooting and Repair Manual, QSK23 Series Engines, Bulletin [[4021375 — QSK23 Troubleshooting and Repair Manual\|4021375]], the Troubleshooting and Repair Manual, QSK45 and QSK60 Series Engines, Bulletin 3666261, or the Troubleshooting and Repair Manual, QSK78 Series Engines, Bulletin 3666727. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. Verify that Fault Code 253 is inactive. | Fault Code 253 inactive? | 3B |
| Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 3B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared. | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
