---
aliases:
  - "Код 2619 — вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
type: "Процедура"
doc: "123-t05-2619"
title_en: "FAULT CODE 2619 - Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions"
title_ru: "Код 2619 — вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
modified: "2012-05-04"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2619.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-2619.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 2619 - Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions
**Код 2619 — вход датчика вспомогательного оборудования 1, защита двигателя — особые указания**

> [!abstract] Процедура · `123-t05-2619`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2619.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-2619.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, and Part Number 3823995 - male Weather Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Verify if the engine stop button is in the STOP position. |  |
|  | **STEP 1A.** Verify if the engine stop button is in the STOP position. | Engine stop button in the STOP position? |
|  | **STEP 1B.** Check Diesel Control Unit (DCU) information. | DCU shows a stop button event or witness test? |
|  | **STEP 1C.** Check for other fault codes. | Active or inactive fault codes? |
| STEP 2. | Check for correct position of the air shutoff valves. |  |
|  | **STEP 2A.** Check for correct position of the air shutoff valves. | Air shutoff valves in the OPEN position? |
| STEP 3. | Check the engine stop button for short circuit. |  |
|  | **STEP 3A.** Check the engine stop button for short circuit. | Greater than 100k ohms? |
| STEP 4. | Check the engine harness. |  |
|  | **STEP 4A.** Inspect the engine harness and ECM connectors. | Dirty or damaged pins? |
|  | **STEP 4B.** Check for a short circuit to ground. | Greater than 100k ohms? |
|  | **STEP 4C.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
| STEP 5. | Check the OEM harness. |  |
|  | **STEP 5A.** Inspect the OEM harness and 23-pin connectors. | Dirty or damaged pins? |
|  | **STEP 5B.** Check for a short circuit to ground. | Greater than 100k ohms? |
|  | **STEP 5C.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
| STEP 6. | Check the Customer Interface Box (CIB) internal wiring. |  |
|  | **STEP 6A.** Check the Customer Interface Box (CIB) internal wiring between the E-stop button and the 23-pin OEM connector. | Dirty or damaged pins? |
|  | **STEP 6B.** Check for a short circuit to ground. | Greater than 100k ohms? |
|  | **STEP 6C.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
| STEP 7. | Clear the fault codes and check for progressive damage. |  |
|  | **STEP 7A.** Confirm conditions. | Snapshot data shows Fault Code 2619 was set at or below idle and 10 percent torque? |
|  | **STEP 7B.** Complete checks with engine off. | Hump hoses and turbochargers meet specifications? |
|  | **STEP 7C.** Disable the fault code. | Fault Code 2619 inactive? |
|  | **STEP 7D.** Check gaskets at load. | Damage to gaskets detected? |
|  | **STEP 7E.** Disable the fault code. | Fault Code 2619 inactive? |
|  | **STEP 7F.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Verify the engine stop button is in the STOP position.

#### STEP 1A. Verify the engine stop button is in the STOP position.

| **Conditions:** Turn keyswitch ON. All components connected. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the engine stop button is in the STOP position. | Engine stop button in the STOP position? **YESRepair:** Reset the engine stop button. | 8A |
| Engine stop button in the STOP position? **NO** | 1B |  |

#### STEP 1B. Check Diesel Control Unit (DCU) information (marine **only**).

| **Conditions:** Turn keyswitch ON. All components connected. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check DCU information. Check the event log in the DCU for an engine stop button event or an engine protection overspeed witness test. Use the following procedure in the Marine C Command Elite™ and C Command Elite Plus™ Panel Systems Master Repair Manual, Bulletin 4021617. [[116-101-013 — General Operating Instructions\|Refer to Procedure 101-013 in Section 1.]] | DCU shows a stop button event or witness test? **YESRepair:** Reset the engine stop button or move out of test mode. Use the following procedure in the Marine C Command Elite™ and C Command Elite Plus™ Panel Systems Master Repair Manual, Bulletin 4021617. [[116-101-013 — General Operating Instructions\|Refer to Procedure 101-013 in Section 1.]] | 7A |
| DCU shows a stop button event or witness test? **NO** | 1C |  |

#### STEP 1C. Check for other fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault codes. Use INSITE™ electronic service tool to read the fault code. | Active or inactive fault codes? **YES** | Troubleshoot other fault codes and return to this fault code. |
| Active or inactive fault codes? **NO** | 2A |  |

### STEP 2. Check for correct position of the air shutoff valves.

#### STEP 2A. Check for correct position of the air shutoff valves.

| **Conditions:** Turn keyswitch ON. All components connected. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check that all of the air shutoff valves are in the OPEN position. | Air shutoff valves in the OPEN position? **YES** | 3A |
| Air shutoff valves in the OPEN position? **NORepair:** Refer to the OEM service manual. | 7A |  |

### STEP 3. Check the engine stop button for short a circuit.

#### STEP 3A. Check the engine stop button for a short circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect wires from NO (Normally Open) engine stop switch terminals. The NO engine stop switch is the middle switch of the three terminals. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit. Measure the resistance between the NO (Normally Open) switch terminals. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4A |
| Greater than 100k ohms? **NORepair:** Replace the engine stop button. Use the procedure in the Marine C Command Elite™ and C Command Elite Plus™ Panel Systems Master Repair Manual, Bulletin 4021617. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | 7A |  |

### STEP 4. Check the engine harness.

#### STEP 4A. Inspect the engine harness and ECM connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine wiring harness. Refer to Procedure 019-204 in Section 19. Replace the engine wiring harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 7A |
| Dirty or damaged pins? **NO** | 5B |  |

#### STEP 4B. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from the OEM switch/dual output B pin of the engine harness connector to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 4C |
| Greater than 100k ohms? **NORepair:** Replace the engine wiring harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 7A |  |

#### STEP 4C. Check for a short circuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from the OEM switch/dual output B pin of the engine harness connector to all other pins in the connector. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 5A |
| Greater than 100k ohms? **NORepair:** Replace the engine wiring harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 7A |  |

### STEP 5. Check the OEM harness.

#### STEP 5A. Inspect the OEM harness and 23-pin connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and 23-pin connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the OEM harness. Flush the dirt, debris, or moisture from the connector pins. Use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 7A |
| Dirty or damaged pins? **NO** | 5B |  |

#### STEP 5B. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the OEM harness from the OEM switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from the OEM switch/dual output B pin of the 23-pin OEM harness connector, OEM side, to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 5C |
| Greater than 100k ohms? **NORepair:** Replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |

#### STEP 5C. Check for a short circuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the OEM harness from the OEM switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from the OEM switch/dual output B pin of the 23-pin OEM harness connector, OEM side, to all other pins in the connector. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 6A |
| Greater than 100k ohms? **NORepair:** Replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |

### STEP 6. Check the Customer Interface Box (CIB) internal wiring.

#### STEP 6A. Check the CIB internal wiring between the E-stop button and the 23-pin OEM connector (Marine).

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the 23-pin connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the OEM harness. Flush the dirt, debris, or moisture from the connector pins. Use electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the OEM harness. Refer to Procedure 019-204 in Section 19. Replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 7A |
| Dirty or damaged pins? **NO** | 6B |  |

#### STEP 6B. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine harness at the 23-pin connector. Disconnect the OEM harness from the OEM switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from the OEM switch/dual output B pin of the 23-pin OEM harness connector, OEM side, to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 6C |
| Greater than 100k ohms? **NORepair:** Replace the CIB harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |

#### STEP 6C. Check for a short circuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the CIB at the 23-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from the OEM switch/dual output B pin of the 23-pin OEM harness connector, OEM side, to all other pins in the connector. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 7A |
| Greater than 100k ohms? **NORepair:** Replace the CIB harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 7A |  |

### STEP 7. Clear the fault codes and check for progressive damage.

#### STEP 7A. Confirm conditions.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Confirm the conditions of the engine. Use INSITE™ electronic service tool to view the fault code snapshot data to verify the conditions of the engine when Fault Code 2619 occured. | Snapshot data shows that Fault Code 2619 was set at or below idle and 10 percent torque? **YES** | 7E |
| Snapshot data shows that Fault Code 2619 was set at or below idle and 10 percent torque? **NORepair:** Check the engine for progressive damage. | 7B |  |

#### STEP 7B. Complete checks with engine OFF.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the following inspections: Inspect the hump hoses for signs of damage or leakage. Check the turbocharger shaft end clearance. Use the following procedure in the QSK45 and QSK60 Service Manual, Bulletin 4021530. Refer to Procedure 010-033 in Section 10. Use the following procedure in the QSK38 and QSK50 Service Manual, Bulletin 4021528. Refer to Procedure 010-033 in Section 10. Inspect the turbocharger compressor impeller wheel. | Hump hoses and turbochargers meet specifications? **YES** | 7C |
| Hump hoses and turbochargers meet specifications? **NORepair:** Replace the damaged components. Use the following procedures in the QSK45 and QSK60 Service Manual, Bulletin 4021530: Refer to Procedure 010-034 in Section 10. Refer to Procedure 010-035 in Section 10. | 7C |  |

#### STEP 7C. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine, and let it idle for 1 minute. Use INSITE™ electronic service tool to verify Fault Code 2619 is inactive. | Fault Code 2619 inactive? **YES** | 7D |
| Fault Code 2619 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |

#### STEP 7D. Check gaskets at load.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Operate the engine with load and check the gaskets. Start the engine and load it. Check and listen for any noise associated with head gasket or aftercooler gasket leaks. | Damage to gaskets detected? **YESRepair:** Replace gaskets as necessary. Use the following procedures in the QSK45 and QSK60 Service Manual, Bulletin 4021530: For head gasket repair: Refer to Procedure 002-021 in Section 2. For aftercooler gasket repair: Refer to Procedure 010-002 in Section 10. Use the following procedures in the QSK38 and QSK50 Service Manual, Bulletin 4021528: For head gasket repair: Refer to Procedure 002-021 in Section 2. For aftercooler gasket repair: Refer to Procedure 010-002 in Section 10. | 7E |
| Damage to gaskets detected? **NO** | 7E |  |

#### STEP 7E. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine and let it idle for 1 minute. Use INSITE™ electronic serivce tool to verify Fault Code 2619 is inactive. | Fault Code 2619 inactive? **YES** | 7F |
| Fault Code 2619 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all the steps have been completed and checked again. | 1A |  |

#### STEP 7F. Clear the inactive fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting tree |  |
