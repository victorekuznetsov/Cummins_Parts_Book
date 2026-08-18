---
aliases:
  - "Код 1549 (QSK50/QSK60) — цепь электромагнита форсунки цилиндра 8 — ток ниже нормы или обрыв"
type: "Процедура"
doc: "122-t05-1549qsk50-60"
title_en: "FAULT CODE 1549 (QSK50 and QSK60) - Injector Solenoid Driver Cylinder 8 Circuit - Current Below Normal or Open Circuit"
title_ru: "Код 1549 (QSK50/QSK60) — цепь электромагнита форсунки цилиндра 8 — ток ниже нормы или обрыв"
modified: "2019-06-04"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1549qsk50-60.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-1549qsk50-60.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 1549 (QSK50 and QSK60) - Injector Solenoid Driver Cylinder 8 Circuit - Current Below Normal or Open Circuit
**Код 1549 (QSK50/QSK60) — цепь электромагнита форсунки цилиндра 8 — ток ниже нормы или обрыв**

> [!abstract] Процедура · `122-t05-1549qsk50-60`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-06-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1549qsk50-60.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-1549qsk50-60.pdf)

Printable Version

## Warnings and Cautions

> [!danger] WARNING · Опасно
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine contril module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3824811 - male Deutsch™test lead, Part Number 3824812 - female Deutsch™ test lead, Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for active fault codes. |  |
|  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool. | Fault Code 1557, 323, or 1549 active? |
|  | **STEP 1B.** Read the fault codes with INSITE™ electronic service tool. | **Only** Fault Code 1549 is active? |
|  | **STEP 1C.** Read the fault codes with INSITE™ electronic service tool. | Multiple injector fault codes active? |
| STEP 2. | Check the injector solenoid driver cylinder 8 for an open circuit. |  |
|  | **STEP 2A.** Inspect the engine harness connections. | Connectors properly connected? |
|  | **STEP 2A-1.** Inspect the engine harness and ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check for an open circuit. | Resistance between 0.5 and 5 ohms? |
|  | **STEP 2C.** Inspect the injector connector pins. | Dirty or damaged pins? |
|  | **STEP 2D.** Check for an open circuit. | Resistance between 0.5 and 5 ohms? |
|  | **STEP 2E.** Read the fault codes. | **Only** Fault Code 1549 is active? |
| STEP 3. | Check the engine harness. |  |
|  | **STEP 3A.** Inspect the engine harness and injector solenoid driver connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the injector solenoid drivers for a short circuit to ground. | Greater than 100k ohms? |
|  | **STEP 3C.** Inspect the engine harness. | Dirty or damaged pins, or damaged wire insulation? |
|  | **STEP 3C-1.** Check the engine harness for a short circuit to ground. | Greater than 100k ohms? |
|  | **STEP 3C-2.** Check the engine harness for a pin-to-pin short circuit. | Greater than 100k ohms? |
| STEP 4. | Disable and clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Same multiple injector fault codes active? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check for active fault codes.

#### STEP 1A. Read the fault codes with INSITE™ electronic service tool.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Operate the engine and observe the fault codes. Use INSITE™ electronic service tool to clear the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to clear the fault codes. | Fault Code 1549, 1557, or 323 active? **YES** | 1B |
| Fault Code 1549, 1557, or 323 active? **NO** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |

#### STEP 1B. Read the fault codes with INSITE™ electronic service tool.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | **Only** Fault Code 1549 is active? **YES** | 2A |
| **Only** Fault Code 1549 is active? **NO** | 1C |  |

#### STEP 1C. Read the fault codes with INSITE™ electronic service tool.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Multiple injector fault codes active? **YES** | 3A |
| Multiple injector fault codes active? **NO** | 2A |  |

### STEP 2. Check the injector and injector solenoid driver cylinder 8 for an open circuit.

#### STEP 2A. Inspect the engine harness connections.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Make sure the following engine harness connections are properly made: Engine harness connected to ECM Engine harness connected to the injector solenoid driver cylinder 8. | Connectors properly connected? **YES** | 2A-1 |
| Connectors properly connected? **NORepair:** Install the engine harness connectors properly. | 4A |  |

#### STEP 2A-1. Inspect the engine harness and ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for continuity in the injector circuit. Measure the resistance between the injector solenoid driver cylinder 8 SIGNAL pin and the injector solenoid driver cylinder 8 RETURN pin at the ECM 60 pin connector of the engine harness. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance between 0.5 and 5 ohms? **YES** | 2E |
| Resistance between 0.5 and 5 ohms? **NO** | 2C |  |

#### STEP 2C. Inspect the injector connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the engine harness connector from the injector solenoid driver cylinder 8 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and injector solenoid driver cylinder 8 connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire or insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness or damaged injector. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Replace the damaged injector. Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-026 in Section 6. | 4A |
| Dirty or damaged pins? **NO** | 2D |  |

#### STEP 2D. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the engine harness connector from the injector solenoid driver cylinder 8 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for continuity in the injector solenoid driver cylinder 8. Measure the resistance between the injector solenoid driver cylinder 8 SIGNAL pin and the injector solenoid driver cylinder 8 RETURN pin at the injector connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance between 0.5 and 5 ohms? **YESRepair:** Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |
| Resistance between 0.5 and 5 ohms? **NORepair:** Replace the damaged injector. Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual,, Bulletin 4021528. [[28-006-026-tr — Injector\|Refer to Procedure 006-026 in Section 6.]] Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-026 in Section 6. | 4A |  |

#### STEP 2E. Read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Operate the engine and observe the fault codes. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to read the fault codes. | **Only** Fault Code 1549 is active? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
| **Only** Fault Code 1549 is active? **NO** | 4A |  |

### STEP 3. Check the engine harness.

#### STEP 3A. Inspect the engine harness and injector solenoid driver connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connectors from the injector solenoid driver cylinder 8, 16, and 5 connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and injector solenoid driver cylinder 8, 16, and 5 connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire or insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Replace the damaged section of the harness or damaged injector(s). Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Replace the damaged injector. Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-026 in Section 6. | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the injector solenoid drivers for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connectors from the injector solenoid driver cylinder 8, 16, and 5 connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance between the injector solenoid driver cylinder 8 SIGNAL pin and engine block ground. Measure the resistance between the injector solenoid driver cylinder 16 SIGNAL pin and engine block ground. Measure the resistance between the injector solenoid driver cylinder 5 SIGNAL pin and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3C |
| Greater than 100k ohms? **NORepair:** Replace the damaged injector(s). Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-026 in Section 6. | 4A |  |

#### STEP 3C. Inspect the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the injector solenoid driver 8, 16, and 5 connectors from the engine harness connectors. Disconnect the engine harness connector from the ECM 60 pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connectors for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire or insulation damage Damaged locking tab connector. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins or damaged wire insulation? **YESRepair:** Replace the damaged section of the harness or damaged injector(s). Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Replace the damaged injector(s). Use the following procedure from the K38, K50, QSK38, and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 006-026 in Section 6. Use the following procedure from the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 006-026 in Section 6. | 4A |
| Dirty or damaged pins or damaged wire insulation? **NO** | 3C-1 |  |

#### STEP 3C-1. Check the engine harness for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the injector solenoid driver cylinder 8, 16, and 5 from the engine harness connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from the injector solenoid driver cylinder 8 SIGNAL pin at the ECM 60 pin connector of the engine harness to engine block ground. Repeat the check at the injector solenoid driver cylinder 16 SIGNAL and injector solenoid driver cylinder 5 SIGNAL pins. Measure the resistance from the injector solenoid driver cylinder 8 RETURN pin at the ECM 60 pin connector of the engine harness to engine block ground. Repeat the check for the injector solenoid driver cylinder 16 RETURN and injector solenoid driver cylinder 5 RETURN pins. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3C-2 |
| Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |

#### STEP 3C-2. Check the engine harness for a pin-to-pin short circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60 pin connector. Disconnect the injector solenoid driver cylinder 8, 16, and 5 connectors from the engine harness connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Measure the resistance from the injector solenoid driver cylinder 8 SIGNAL pin at the ECM 60 pin connector of the engine harness to all other pins in the connector. Repeat the check at the injector solenoid driver cylinder 16 SIGNAL and injector solenoid driver cylinder 5 SIGNAL pins. Measure the resistance from the injector solenoid driver cylinder 8 RETURN pin at the ECM 60 pin connector of the engine harness to all other pins in the connector. Repeat the check for the injector solenoid driver cylinder 16 RETURN and injector solenoid driver cylinder 5 RETURN pins. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4A |
| Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |

### STEP 4. Disable and clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic service tool to verify that the fault codes are inactive. | Same multiple injector fault codes active? **YESRepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |
| Same multiple injector fault codes active? **NO** | 4B |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
