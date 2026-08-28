---
type: "Процедура"
doc: "19-t05-2364"
title_en: "FAULT CODE 2364 - Engine Cold Start Aid - Condition Exists"
modified: "2020-01-27"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-2364.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-2364.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# FAULT CODE 2364 - Engine Cold Start Aid - Condition Exists

> [!abstract] Процедура · `19-t05-2364`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-01-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-t05-2364.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-t05-2364.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the ether injection solenoid. |  |
|  | **STEP 1A.** Inspect the injector solenoid connector post and OEM wiring harness connector. | No damage to post or connector |
|  | **STEP 1B.** Check the supply voltage at the ether injection solenoid. | More than 17.0 VDC |
|  | **STEP 1C.** Check the resistance of the ether injection solenoid. | Refer to OEM manual for specification |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Inspect the OEM wiring harness and OEM interface wiring harness connector pins. | No damaged pins |
|  | **STEP 2B.** Check for a short circuit to engine block ground. | More than 100k ohms |
|  | **STEP 2C.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 2D.** Check for an open circuit. | Less than 10 ohms |
| STEP 3. | Check the engine wiring harness. |  |
|  | **STEP 3A.** Inspect the engine wiring harness connector and ECM connector pins. | No damaged pins |
|  | **STEP 3B.** Check for a short circuit to engine block ground. | More than 100k ohms |
|  | **STEP 3C.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 3D.** Check for an open circuit. | Less than 10 ohms |
| STEP 4. | Check the supply voltage at the ECM. |  |
|  | **STEP 4A.** Check the supply voltage at the ECM. | More than 17.0 VDC |
| STEP 5. | Clear the fault codes. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 2364 inactive |

### STEP 1. Check the ether injection solenoid.

#### STEP 1A. Inspect the injector solenoid connector post and OEM wiring harness connector.

| **Conditions:** Turn keyswitch OFF. Disconnect the ether injection solenoid from the OEM wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the injector solenoid connector post and OEM wiring harness connector for the following: Bent or broken OEM wiring harness connector terminal Corroded terminal post on the solenoid Multiple wires on the terminal post Moisture in or on the connector. | No damage to post or connector | 1B |
| Repair the damaged connection. Flush the dirt, debris, or moisture from the connector post and ring terminal. Repair or replace the ether injection solenoid or the OEM wiring harness, whichever has the damaged part. Flush the dirt, debris, or moisture from the connector post and ring terminal using electronic contact cleaner, Part Number 3824510. Remove any additional wires connected to the solenoid terminal post. Replace the damaged solenoid. Refer to the OEM manual for procedure. Repair the OEM wiring harness ring terminal. Refer to Procedure 019-197 in Section 19. Replace the OEM wiring harness. Refer to Procedure 019-071 in Section 19. | 5A |  |

#### STEP 1B. Check the supply voltage at the ether injection solenoid.

| **Conditions:** Disconnect the ether injection solenoid from the OEM wiring harness. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage at the ether injection solenoid. Measure the voltage from the OEM wiring harness connector to engine block ground. | More than 17.0 VDC. Replace the ether injection solenoid. Refer to the OEM service manual. | 5A |
|  | 1C |  |

#### STEP 1C. Check the resistance of the ether injection solenoid.

| **Conditions:** Turn keyswitch OFF. Disconnect the ether injection solenoid from the OEM wiring harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the resistance of the ether injection solenoid. Measure the resistance from the connector post to engine block ground. | Refer to OEM manual for specification | 2A |
| Replace the ether injection solenoid. Refer to the OEM service manual. | 5A |  |

### STEP 2. Check the OEM harness.

#### STEP 2A. Inspect the OEM wiring harness and OEM interface wiring harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness from the ether injection solenoid. Disconnect the OEM wiring harness from the engine wiring harness at the 31-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM wiring harness and OEM interface wiring harness connectors for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | No damaged pins | 2B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the OEM wiring harness or the OEM wiring interface harness, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the OEM wiring harness. Refer to Procedure 019-208 in Section 19. Replace the OEM wiring harness. Refer to Procedure 019-071 in Section 19. Repair the OEM wiring interface harness. Refer to Procedure 019-208 in Section 19. Replace the OEM wiring interface harness. Refer to Procedure 019-072 in Section 19. | 5A |  |

#### STEP 2B. Check for a short circuit to engine block ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness from the ether injection solenoid. Disconnect the OEM wiring harness from the engine wiring harness at the 31-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short to ground in the OEM wiring harness. Measure the resistance from the ether solenoid harness connector (ring terminal) to engine block ground. | More than 100k ohms | 2C |
| Replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in section 19]]. | 5A |  |

#### STEP 2C. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness from the ether injection solenoid. Disconnect the OEM wiring harness from the engine wiring harness at the 31-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 26 of the OEM 31-pin connector, engine wiring harness side, to all other pins in the connector. | More than 100k ohms | 2D |
| Replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19]]. | 5A |  |

#### STEP 2D. Check for an open circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM wiring harness from the ether injection solenoid. Disconnect the OEM wiring harness from the engine wiring harness at the 31-pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from the OEM wiring harness solenoid connector (ring terminal) to pin 26 of the OEM wiring harness 31-pin connector, OEM side. | Less than 10 ohms | 3A |
| Replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19]]. | 5A |  |

### STEP 3. Check the engine wiring harness.

#### STEP 3A. Inspect the engine wiring harness and ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine wiring harness from the OEM harness at the 31-pin connector. Disconnect the engine wiring harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine wiring harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | No damaged pins | 3B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins. Repair or replace the engine wiring harness, or replace the ECM, whichever has the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electronic contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine wiring harness. Refer to Procedure 019-208 in Section 19. Replace the engine wiring harness. Refer to Procedure 019-043 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |  |

#### STEP 3B. Check for a short circuit to engine block ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine wiring harness from the OEM wiring harness at the 31-pin connector. Disconnect the engine wiring harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to engine block ground. Measure the resistance from pin 2 of the engine wiring harness ECM connector to engine block ground. | More than 100k ohms | 3C |
| Replace the engine wiring harness. [[19-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19]]. | 5A |  |

#### STEP 3C. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine wiring harness from the OEM wiring harness at the 31-pin connector. Disconnect the engine wiring harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 2 of the engine wiring harness ECM connector to all other pins in the connector. | More than 100k ohms | 3D |
| Replace the engine wiring harness. [[19-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19]]. | 5A |  |

#### STEP 3D. Check for an open circuit in the engine wiring harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine wiring harness from the OEM wiring harness at the 31-pin connector. Disconnect the engine wiring harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the engine wiring harness. Measure the resistance from pin 26 of the 31-pin OEM wiring harness connector to pin 2 of the engine wiring harness ECM connector. | Less than 10 ohms | 4A |
| Replace the engine wiring harness. [[19-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19]]. | 5A |  |

### STEP 4. Check the supply voltage at the ECM.

#### STEP 4A. Check the supply voltage at the ECM.

| **Conditions:** Ether injection system enabled. Coolant temperature below the ECM-calibrated threshold. Disconnect the engine wiring harness from the ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage at the ECM. Measure the supply voltage from pin 2 of the ECM engine wiring harness connector port to engine block ground. | More than 17.0 VDC | 5A |
| Replace the ECM. [[19-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19]]. | 5A |  |

### STEP 5. Disable the fault codes.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Start the engine. This **must** be a cold start. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 2364 inactive | Repair complete |
| Verify that all steps have been completed. If all steps have been completed, then follow your technical escalation process. | Escalate or call for assistance |  |
