---
aliases:
  - "Напряжение АКБ выше диапазона"
type: "Процедура"
doc: "96-fc442"
title_en: "Battery Voltage Out of Range - High"
title_ru: "Напряжение АКБ выше диапазона"
modified: "2004-02-25"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Battery Voltage Out of Range - High
**Напряжение АКБ выше диапазона**

> [!abstract] Процедура · `96-fc442`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-02-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/96-fc442.pdf)

### Fault Code: 442

### Battery Voltage Out of Range - High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 442 PID(P): SPN: FMI: Lamp: Red SRT: | Battery Voltage Out of Range - High. Battery voltage is more than the high threshold detected by the Centinel™ control module. | The Centinel™ control module voltage supply approaching a level at which unpredictable operation will occur. |

![[05800058.png]]

### Circuit Description

The Centinel™ control module receives unswitched battery voltage from the starter for heavy-duty. For high-horsepower, the Centinel™ control module receives switched power from the fuel shutoff valve solenoid. There are two in-line 5-amp fuses in the Centinel™ control module heavy-duty harness to protect the Centinel™ control module. The high-horsepower has **only** one 5-amp fuse. The battery return wires in the engine harness are connected to the engine block ground.

### Component Location

The location of the battery will vary with the OEM. Refer to the OEM manual for the battery location.

### Shoptalk

This fault can be caused by loose or corroded battery connections.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the equipment battery system. |  |
|  | **STEP 1A.** Inspect the battery cable connections. | No damaged connections |
|  | **STEP 1B.** Check the battery voltage. | Heavy-duty: 9 to 32 VDC 12-VDC High-horsepower: 8.2 - 17.3 VDC 24-VDC High-horsepower: 15.5 - 30.3 VDC |
|  | **STEP 1C.** Check the Centinel™ control module battery voltage. |  |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 442 inactive |

### STEP 1. Check the equipment battery system.

#### STEP 1A. Inspect the battery cable connections.

| **Conditions:** Turn the keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corrosion Loose connection. | No damaged connections | 1B |
| **Repair or replace the damaged connections** Repair the battery or starter connections. Replace the battery or starter connections. Refer to the OEM service manual. | 2A |  |

#### STEP 1B. Check the battery voltage.

| **Conditions:** Turn the keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the battery voltage. | Heavy-duty: 9 - 32 VDC 12VDC High-horsepower: 8.2 - 17.3 VDC 24VDC High-horsepower: 15.5 - 30.3 VDC | 1C |
| **Replace the battery.** Refer to the OEM service manual. | 2A |  |

#### STEP 1C. Check the Centinel™ control module battery voltage.

| **Conditions:** Turn the keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Heavy-duty: Measure the voltage between pins 1 (+) and 2 (-) of the Centinel™ control module harness connector. High-horsepower: Measure the voltage between pins 22 (+) and 25 (-) of the Centinel™ control module connector. | Reading must match Step 1B. | Complete |
| **Replace the Centinel™ wiring harness.** Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness\|019-131]]. | 2A |  |

### STEP 2. Clear the fault code.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect all the components. Start the engine and let it idle for 1 minute. Verify that Fault Code 442 is inactive. | Fault Code 442 inactive | Complete |
| Return to the troubleshooting step or contact your local Cummins Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |
