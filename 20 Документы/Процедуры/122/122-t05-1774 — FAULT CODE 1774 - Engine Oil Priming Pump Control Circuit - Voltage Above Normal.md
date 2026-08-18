---
aliases:
  - "Код 1774 — цепь управления насосом прокачки масла — напряжение выше нормы"
type: "Процедура"
doc: "122-t05-1774"
title_en: "FAULT CODE 1774 - Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Код 1774 — цепь управления насосом прокачки масла — напряжение выше нормы"
modified: "2012-07-31"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1774.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-1774.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 1774 - Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source
**Код 1774 — цепь управления насосом прокачки масла — напряжение выше нормы**

> [!abstract] Процедура · `122-t05-1774`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-07-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1774.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-1774.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for active fault codes. | Fault Code 1774 active? |
| STEP 2. | Check the engine oil priming pump circuit and sensors. |  |
|  | **STEP 2A.** Inspect the oil pressure sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Inspect the OEM pump switch input connector pins. | Dirty or damaged pins? |
|  | **STEP 2C.** Check the OEM pump switch input voltage. | 4.75 to 5.25-VDC? |
| STEP 3. | Check the engine oil priming pump. |  |
|  | **STEP 3A.** Check the engine priming pump operation. | Pump operating? |
| STEP 4. | Clear the fault code. |  |
|  | **STEP 4A.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes

#### STEP 1A. Check for active fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1774 active? **YES** | 2A |
| Fault Code 1774 active? **NO** | 3A |  |

### STEP 2. Check the engine oil priming circuit and sensors

#### STEP 2A. Inspect the oil pressure sensor and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the oil pressure sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and crankcase pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the oil pressure sensor or harness connector. Clean the connector and pins. Replace the damaged section of harness or damaged oil pressure sensor. Check all harnesses connected in series. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Inspect the OEM pump switch input connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the oil pressure sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and crankcase pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the oil pressure sensor or harness connector. Clean the connector and pins. | 4A |
| Dirty or damaged pins? **NO** | 3A |  |

#### STEP 2C. Check the OEM pump switch input voltage.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM pump switch input connector from the OEM harness connector. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the input voltage. Measure the voltage between the OEM pump switch input pin and OEM pump switch return. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | 4.75 to 5.25-VDC? **YES** | 4A |
| 4.75 to 5.25-VDC? **NORepair:** Refer to the OEM service manual. | 4A |  |

### STEP 3. Check the engine oil priming pump

#### STEP 3A. Check the engine oil priming pump operation.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check if the engine oil priming pump is operating. | Pump operating? **YES** | 4A |
| Pump operating? **NORepair:** Troubleshoot the engine oil priming pump. | 4A |  |

### STEP 4. Clear the fault code

#### STEP 4A. Clear the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the fault codes. Use INSITE™ electronic service tool to clear the fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Appropriate troubleshooting steps. |  |
