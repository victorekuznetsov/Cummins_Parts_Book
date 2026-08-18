---
aliases:
  - "Код 237 — внешний вход задания частоты (синхронизация агрегатов) — данные нестабильны или неверны"
type: "Процедура"
doc: "122-t05-237"
title_en: "FAULT CODE 237 - External Speed Command Input (Multiple Unit Synchronization) - Data Erratic, Intermittent, or Incorrect"
title_ru: "Код 237 — внешний вход задания частоты (синхронизация агрегатов) — данные нестабильны или неверны"
modified: "2017-09-08"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-237.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-237.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 237 - External Speed Command Input (Multiple Unit Synchronization) - Data Erratic, Intermittent, or Incorrect
**Код 237 — внешний вход задания частоты (синхронизация агрегатов) — данные нестабильны или неверны**

> [!abstract] Процедура · `122-t05-237`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-09-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-237.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-237.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3823993 - male Deutsch™ test lead, and Part Number 3823994 - female Deutsch™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Determine which engine is shutting down. |  |
|  | **STEP 1A.** Check for multiple fault codes. | Fault Codes 426 and 497 active or inactive with more than one count in the last 25 engine hours? |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the output driver supply voltage. | 11.75 to 12.25-VDC? |
|  | **STEP 2C.** Check the 5 volt supply. | 4.75 to 5.25-VDC? |
|  | **STEP 2D.** Check for an open circuit. | Less than 10 ohms? |
|  | **STEP 2E.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
|  | **STEP 2F.** Check for a short circuit to engine block ground. | Greater than 100k ohms? |
| STEP 3. | Check the original equipment manufacturer (OEM) harness. |  |
|  | **STEP 3A.** Inspect the OEM harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit. | Less than 10 ohms? |
|  | **STEP 3C.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
|  | **STEP 3D.** Check for a short circuit to engine block ground. | Greater than 100k ohms? |
| STEP 4. | Check the engine harness. |  |
|  | **STEP 4A.** Inspect the engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 4B.** Check for an open circuit. | Less than 10 ohms? |
|  | **STEP 4C.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
|  | **STEP 4D.** Check for a short circuit to engine block ground. | Greater than 100k ohms? |
| STEP 5. | Clear the fault codes. |  |
|  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 5B.** Disable the fault code. | Fault Code 237 inactive? |

### STEP 1. Determine which engine is shutting down.

#### STEP 1A. Check for multiple fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for multiple fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Codes 426 and 497 active or inactive with more than one count in the last 25 engine hours? **YES** | Appropriate troubleshooting steps |
| Fault Codes 426 and 497 active or inactive with more than one count in the last 25 engine hours? **NO** | 2A |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect the engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness connector and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pin Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the connector. Refer to Procedure 019-204 Repair the engine harness. Refer to Procedure 019-043 Replace the ECM. Refer to Procedure 019-031 in Section 19. | 5A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the output driver supply voltage.

| **Conditions:** Disconnect the engine harness connector from the ECM on the secondary engine. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the output driver supply voltage. Measure the voltage from the external speed command input SIGNAL pin of the engine harness ECM connector to engine block ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | 11.75 to 12.25-VDC? **YES** | 2C |
| 11.75 to 12.25-VDC? **NO** | 2D |  |

#### STEP 2C. Check the 5 volt supply.

| **Conditions:** Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the 5 volt supply. Measure the voltage from the external speed input RETURN pin of the engine harness ECM connector to engine block ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | 4.75 to 5.25-VDC? **YES** | 5A |
| 4.75 to 5.25-VDC? **NO** | 2D |  |

#### STEP 2D. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Disconnect the engine harness ECM connector from the OEM harness connector on the secondary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from the external speed command input SIGNAL pin of the engine harness ECM connector to the external speed command input SIGNAL pin of the OEM connector. Measure the resistance from the frequency input RETURN (VSS)/auxiliary governor pin of the engine harness connector to the external speed command input RETURN pin of the OEM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 2E |
| Less than 10 ohms? **NORepair:** An open circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |

#### STEP 2E. Check for a short circuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Disconnect the engine harness ECM connector from the OEM harness connector on the secondary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from the external speed command input SIGNAL pin of the engine harness ECM connector to all other pins in the connector. Measure the resistance from the external speed command input RETURN pin of the engine harness ECM connector to all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 2F |
| More than 100k ohms? **NORepair:** A pin-to-pin short circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 inSection 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |

#### STEP 2F. Check for a short circuit to engine block ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector from the ECM connector on the secondary engine. Disconnect the engine harness ECM connector from the OEM harness connector on the secondary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to engine block ground. Measure the resistance from the external speed command input SIGNAL pin of the engine harness ECM connector to engine block ground. Measure the resistance from the external speed command input RETURN pin of the engine harness ECM connector to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 3A |
| More than 100k ohms? **NORepair:** A short circuit to ground has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |

### STEP 3. Check the OEM harness.

#### STEP 3A. Inspect the OEM harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the OEM harness connector on the secondary engine. Disconnect the engine harness connector from the OEM harness connector on the primary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness connector and engine harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pin Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. Repair the connector. Refer to Procedure 019-207 in Section 19. | 5A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the 31 pin OEM connector from the engine harness on the secondary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from the auxiliary PWM driver SIGNAL pin on the 23 pin OEM connector of the primary engine to the external speed command input SIGNAL pin on the 31 pin OEM connector of the secondary engine. Measure the resistance from the OEM-provided 5 volt SUPPLY to the external speed command input RETURN pin on the 31-pin OEM connector of the secondary engine. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
| Less than 10 ohms? **NORepair:** An open circuit has been detected in the OEM harness. Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the OEM service manual. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 5A |  |

#### STEP 3C. Check for a short circuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the 31 pin OEM connector from the engine harness on the secondary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from the auxiliary PWM driver SIGNAL pin on the 23 pin OEM connector of the primary engine to all other pins in the connector. Measure the resistance from the OEM-provided 5 volt SUPPLY to all other pins in the 23 pin OEM connector of the primary engine. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 3D |
| More than 100k ohms? **NORepair:** A pin-to-pin short circuit has been detected in the OEM harness. Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short circuit. Refer to the OEM service manual. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 5A |  |

#### STEP 3D. Check for a short circuit to engine block ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the 31 pin OEM connector from the engine harness on the secondary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to engine block ground. Measure the resistance from the OEM actuator pulse width modulation output pin on the 23 pin OEM connector of the primary engine to engine block ground. Measure the resistance from the OEM-provided 5 volt SUPPLY to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 4A |
| More than 100k ohms? **NORepair:** A short circuit to ground has been detected in the OEM harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit to ground. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 5A |  |

### STEP 4. Check the engine harness.

#### STEP 4A. Inspect the engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine harness connector on the primary engine. Disconnect the engine harness ECM connector from the ECM connector on the primary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness connector and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pin Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the engine harness connector. Clean the connector and pins. Replace the damaged section of the harness. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-204 in Section 19. | 5A |
| Dirty or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness on the primary engine. Disconnect the engine harness ECM connector from the ECM on the primary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from the auxiliary pulse width moduled (PWM) driver 1 SIGNAL pin on the 23 pin OEM connector to the auxiliary PWM driver 1 SIGNAL pin on the ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 4C |
| Less than 10 ohms? **NORepair:** An open circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |

#### STEP 4C. Check for a short circuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness connector on the primary engine. Disconnect the engine harness ECM connector from the ECM connector on the primary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from the auxiliary PWM driver 1 SIGNAL pin on the engine harness ECM connector all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 4D |
| More than 100k ohms? **NORepair:** A pin-to-pin short circuit has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |

#### STEP 4D. Check for a short circuit to engine block ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the 23 pin OEM connector from the engine harness connector on the primary engine. Disconnect the engine harness ECM connector from the ECM connector on the primary engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to engine block ground. Measure the resistance from the auxiliary PWM driver 1 SIGNAL pin on the ECM connector to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | More than 100k ohms? **YES** | 5A |
| More than 100k ohms? **NORepair:** A short circuit to ground has been detected in the engine harness. Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the connector. Refer to Procedure 019-199 in Section 19. | 5A |  |

### STEP 5. Check ECM calibration and clear fault codes.

#### STEP 5A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19]]. | 5B |  |

#### STEP 5B. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify Fault Code 237 is inactive. | Fault Code 237 inactive? **YES** | Repair complete. |
| Fault Code 237 inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |
