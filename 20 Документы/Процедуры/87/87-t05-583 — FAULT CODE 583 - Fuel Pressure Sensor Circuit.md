---
aliases:
  - "Код 583 — цепь датчика давления топлива"
type: "Процедура"
doc: "87-t05-583"
title_en: "FAULT CODE 583 - Fuel Pressure Sensor Circuit"
title_ru: "Код 583 — цепь датчика давления топлива"
modified: "2012-08-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-583.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-t05-583.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# FAULT CODE 583 - Fuel Pressure Sensor Circuit
**Код 583 — цепь датчика давления топлива**

> [!abstract] Процедура · `87-t05-583`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-08-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-t05-583.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-t05-583.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated before replacing the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check fuel pressure sensor and engine harness connector. |  |
|  | **STEP 1A.** Inspect the fuel pressure sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 1B.** Check the fuel pressure sensor resistance. | Greater than 800k ohms? |
| STEP 2. | Check if engine will not start or engine starts and dies. |  |
|  | **STEP 2A.** Attempt to start engine. | Engine starts and continues running? |
| STEP 3. | Check the low pressure side of the fuel system. |  |
|  | **STEP 3A.** Check for external fuel leaks. | Fuel leaking externally? |
|  | **STEP 3B.** Check fuel inlet restriction. | Is the fuel restriction at the lift pump inlet greater than the maximum fuel inlet restriction specifications? |
|  | **STEP 3C.** Check for air in fuel. | Air present in the fuel flow? |
|  | **STEP 3D.** Measure the resistance across the fuel lift pumps. | Does the resistance indicate a short or open circuit? |
|  | **STEP 3E.** Check the fuel lift pumps individually. | Does fuel flow from both lift pumps meet specification? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 583 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fuel pressure sensor and engine harness connector.

#### STEP 1A. Inspect the fuel pressure sensor and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine wiring harness connector from the fuel pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness connector and fuel pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Repair the damaged harness, connector, or pins. Use the following procedures. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-199 in Section 19. Replace the fuel pressure sensor. | 4A |
| Dirty or damaged pins? **NO** | 1B |  |

#### STEP 1B. Check the fuel pressure sensor resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel pressure sensor connector from the engine wiring harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel pressure sensor resistance. Measure the resistance between the fuel pressure SIGNAL pin and the fuel pressure RETURN pin at the fuel pressure sensor connector. Use a wiring diagram for connector pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 800k ohms? **YESRepair:** Replace the fuel pressure sensor. | 4A |
| Greater than 800k ohms? **NO** | 2A |  |

### STEP 2. Check if engine will not start or engine starts and dies.

#### STEP 2A. Attempt to start engine.

| **Conditions:** Start engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Try to start the engine. Check if engine will **not** start or engine starts and dies. | Engine starts and continues running? **YES** | 3A |
| Engine starts and continues running? **NO** | Reference troubleshooting symptom trees Engine Difficult to Start or Will Not Start and Engine Will Starts But Will Not Keep Running in Section TS. |  |

### STEP 3. Check the low pressure side of the fuel system.

#### STEP 3A. Check for external fuel leaks.

| **Conditions:** Engine running. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start the engine and check for external fuel leaks. Check for external fuel leaks. | Fuel leaking externally? **YESRepair:** Repair all fuel leaks. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-024 in Section 6. | 4A |
| Fuel leaking externally? **NO** | 3B |  |

#### STEP 3B. Check the fuel inlet restriction.

| **Conditions:** Turn keyswitch OFF. Install a quick connecting fitting and vacuum gauge. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the fuel restriction at the fuel lift pump inlet. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-020 in Section 6. | Fuel restriction at the lift pump inlet greater than the maximum fuel inlet restriction specifications? Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-020 in Section 6. **YESRepair:** Tighten loose connections, check OEM suction side of system for damage or debris, check OEM fuel tank for debris or damage, clean screens, replace plugged fuel pre-filter. Refer to the OEM service manual. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-020 in Section 6. | 4A |
| Fuel restriction at the lift pump inlet greater than the maximum fuel inlet restriction specifications? Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-020 in Section 6. **NO** | 3C |  |

#### STEP 3C. Check for air in fuel.

| **Conditions:** Install a sight glass at the fuel filter outlet. Operate the engine at high idle. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for air in fuel. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-003 in Section 6. | Air present in the fuel flow? **YESRepair:** Tighten loose connections and check OEM suction side of system for damage or debris. Replace plugged fuel filter. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-015 in Section 6. | 4A |
| Air present in the fuel flow? Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 006-003 in Section 6. **NO** | 3D |  |

#### STEP 3D. Measure resistance across the fuel lift pumps.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Unplug both fuel lift pumps and measure the resistance across the pins. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. | Does the resistance indicate a short or open circuit? Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. **YESRepair:** Replace the damaged fuel lift pump. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. | 4A |
| Does the resistance indicate a short or open circuit? **NORepair:** Remove both electric fuel lift pumps from the engine. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. | 3E |  |

#### STEP 3E. Check the fuel lift pumps individually.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Remove electric lift pumps from engine and measure fuel pumping capability. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. | Does fuel flow from each lift pump meet specification? Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. **YES** | 4A |
| Does fuel flow from each lift pump meet specification? Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. **NORepair:** Replace the damaged fuel lift pump. Use the following procedure in Service Manual, QST30, Bulletin 4021539. Refer to Procedure 005-045 in Section 5. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 583 inactive? **YES** | 4B |
| Fault Code 583 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair location if all steps have been completed and checked a second time. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
