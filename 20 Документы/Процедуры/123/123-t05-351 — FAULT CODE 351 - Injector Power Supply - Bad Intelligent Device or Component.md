---
aliases:
  - "Код 351 — питание форсунок — неисправное устройство"
type: "Процедура"
doc: "123-t05-351"
title_en: "FAULT CODE 351 - Injector Power Supply - Bad Intelligent Device or Component"
title_ru: "Код 351 — питание форсунок — неисправное устройство"
modified: "2021-11-03"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-351.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-351.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 351 - Injector Power Supply - Bad Intelligent Device or Component
**Код 351 — питание форсунок — неисправное устройство**

> [!abstract] Процедура · `123-t05-351`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-11-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-351.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-351.pdf)

Printable Version

## Warnings and Cautions

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3164133 - male Deutsch test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Codes 322, 323, 324, 325, 331, and 332 active during engine operation? |
| STEP 2. | Check the battery 1 voltage. |  |
|  | **STEP 2A.** Inspect the battery 1 voltage connectors and fuses. | Damage observed? |
|  | **STEP 2B.** Check for an open circuit. | Less than 0.5 ohms? |
|  | **STEP 2C.** Check for an open circuit in the battery 1 voltage circuit. | Less than 10 ohms? |
| STEP 3. | Validate the occurrence of this fault code. |  |
|  | **STEP 3A.** Operate the engine and determine if fault code condition exists. | Fault Code 351 reoccurs during engine operation, while injector Fault Codes 322, 323, 324, 325, 331, and 332 do not occur? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 351 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Connect the INSITE™ electronic service tool Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 322, 323, 324, 325, 331, and 332 active during engine operation? **YES** | Appropriate fault code troubleshooting tree |
| Fault Codes 322, 323, 324, 325, 331, and 332 active during engine operation? **NO** | 2A |  |

### STEP 2. Check the battery 1 voltage.

#### STEP 2A. Inspect the ECM 4-pin power connector and fuses.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM 4-pin power connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the ECM 4-pin power connector and fusess for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Damage observed? **YESRepair:** Clean the connector and pins. Repair or replace the damaged harness, pins, fuses, or connectors. | 4A |
| Damage observed? **NO** | 2B |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM 4-pin power connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the battery 1 voltage pins at the ECM 4-pin power connector SUPPLY harness and the battery positive (+) pins at the battery positive (+) connection. Use a wiring diagram for connector pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 0.5 ohms? **YES** | 2C |
| Less than 0.5 ohms? **NORepair:** Repair or replace the ECM power supply harness, fuses, or fuse holders, or clean the battery terminal connections. Refer to Procedure 019-206 in Section 19. Refer to Procedure 019-198 in Section 19. | 4A |  |

#### STEP 2C. Check for an open circuit in the battery 1 voltage circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM 4-pin power connector harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the ECM power supply circuit. Measure the resistance between the battery negative (-) pins at the ECM 4-pin power connector to engine block ground. Use a wiring diagram for connector pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3A |
| Less than 10 ohms? **NORepair:** Repair or replace the ECM power supply harness, fuses, or fuse holders, or clean the battery terminal connections. Refer to Procedure 019-206 in Section 19. Refer to Procedure 019-198 in Section 19. | 4A |  |

### STEP 3. Validate the occurrence of this fault code.

#### STEP 3A. Operate the engine and determine if fault code condition exists.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Operate the engine and determine whether the fault code condition still exists. Operate the engine at high idle, no load. Use INSITE™ electronic service tool to read the fault codes. Note: INSITE™ electronic service tool can also be used to monitor ECM power supply and injector power supply voltages. | Fault Code 351 reoccurs during engine operation, while injector Fault Codes 322, 323, 324, 325, 331, and 332 do **not** occur? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
| Fault Code 351 reoccurs during engine operation, while injector Fault Codes 322, 323, 324, 325, 331, and 332 do **not** occur? **NORepair:** A marginal battery voltage condition is possible. Make sure that the batteries are fully charged. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 351 inactive? **YES** | 4B |
| Fault Code 351 inactive? **NORepair:** Return to the troubleshooting steps or contact a local Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to erase the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
