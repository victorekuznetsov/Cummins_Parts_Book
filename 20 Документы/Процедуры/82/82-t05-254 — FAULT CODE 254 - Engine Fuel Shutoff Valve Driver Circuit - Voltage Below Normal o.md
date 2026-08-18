---
aliases:
  - "Код 254 — цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
type: "Процедура"
doc: "82-t05-254"
title_en: "FAULT CODE 254 - Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 254 — цепь драйвера клапана отсечки топлива — напряжение ниже нормы"
modified: "2019-05-31"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-t05-254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# FAULT CODE 254 - Engine Fuel Shutoff Valve Driver Circuit - Voltage Below Normal or Shorted to Low Source
**Код 254 — цепь драйвера клапана отсечки топлива — напряжение ниже нормы**

> [!abstract] Процедура · `82-t05-254`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-05-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-t05-254.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fuel shutoff solenoid. |  |
|  | **STEP 1A.** Check for extra wires on the fuel shutoff solenoid post. | Extra wires? |
|  | **STEP 1B.** Check for corrosion on the solenoid post. | Corrosion found? |
|  | **STEP 1C.** Check the supply voltage at the fuel shutoff solenoid. | Greater than positive +6 VDC? |
|  | **STEP 1C-1.** Check the actuator harness and the ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 1C-2.** Check for an open circuit. | Less than 10 ohms? |
|  | **STEP 1C-3.** Check for a short circuit from pin-to-pin. | Greater than 100k ohms? |
|  | **STEP 1C-4.** Measure the voltage from the ECM. | Greater than positive +6 VDC? |
|  | **STEP 1D.** Check the fuel shutoff solenoid resistance. | 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? |
| STEP 2. | Check the ECM calibration and clear fault codes. |  |
|  | **STEP 2A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 2B.** Diable the fault code. | Fault code inactive? |

### STEP 1. Check the fuel shutoff solenoid.

#### STEP 1A. Check for extra wires on the fuel shutoff solenoid post.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for extra wires. Check for extra wires on the fuel shut off solenoid post. | Extra wires? **YES** | 1B |
| Extra wires? **NORepair:** Remove extra wires and connect to positive +12 VDC supply. | 2A |  |

#### STEP 1B. Check for corrosion on the solenoid post.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel shutoff control wire from the fuel shutoff solenoid. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for corrosion. Check for corrosion on the solenoid post. | Corrosion found? **YES** | 1C |
| Corrosion found? **NORepair:** Clean the solenoid post and wiring terminal. Refer to Procedure 019-050 in the Associated Procedures Table. | 2A |  |

#### STEP 1C. Check the supply voltage at the fuel shutoff solenoid.

| **Conditions:** Disconnect the actuator harness from the fuel shutoff solenoid. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage at the fuel shutoff solenoid. Measure the voltage from the fuel shutoff control wire connectors on the harness side to engine block ground. | Greater than positive +6-VDC? **YES** | 1D |
| Greater than positive +6-VDC? **NO** | 1C-1 |  |

#### STEP 1C-1. Check the actuator harness and the ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator harness and the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YES** | 1C-2 |
| Dirty or damaged pins? **NORepair:** Repair or replace the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 1D |  |

#### STEP 1C-2. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness from the fuel shutoff solenoid. Disconnect the actuator harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit at pin 33. Measure the resistance from pin 33 of the actuator harness to the fuel shutoff control wire. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 1C-3 |
| Less than 10 ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 2A |  |

#### STEP 1C-3. Check for a short sircuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness from the fuel shutoff solenoid. Disconnect the actuator harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from pin 33 of the actuator harness connector to all other pins in the connector. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 1C-4 |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 2A |  |

#### STEP 1C-4. Measure the voltage from the ECM.

| **Conditions:** Disconnect the actuator harness connector from the ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage out of the ECM. Measure the voltage at the ECM from pin 33 of the actuator harness connector port to engine block ground. | Greater than positive +6-VDC? **YESRepair:** Repair or replace the engine harness. Repair the engine harness. Refer to Procedure 019-204 in Section 19. Replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 2A |
| Greater than positive +6-VDC? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 2A |  |

#### STEP 1D. Check the fuel shutoff solenoid resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect the actuator harness from the fuel shutoff solenoid. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel shutoff solenoid resistance. Measure the resistance from the fuel shutoff solenoid to engine block ground. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? **YES** | 2A |
| 1 to 5 ohms for 6-VDC solenoids, 6 to 15 ohms for 12-VDC solenoids, 24 to 50 ohms for 24-VDC solenoids, 42 to 80 ohms for 32-VDC solenoids, 46 to 87 ohms for 36-VDC solenoids, 92 to 145 ohms for 48-VDC solenoids, 315 to 375 ohms for 74-VDC solenoids, 645 to 735 ohms for 115-VAC solenoids? **NORepair:** Replace the fuel shutoff solenoid. Refer to Procedure 019-050 in the Associated Procedures Table. | 2A |  |

### STEP 2. Check ECM calibration and clear fault codes.

#### STEP 2A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 2B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 2B |  |

#### STEP 2B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Engine Control Module | [[82-019-031 — Engine Control Module\|Refer to Procedure 019-031]] | ISM and QSM11 Engines | 3666266 |
| Engine Wiring Harness | [[82-019-043-tr — Engine Wiring Harness\|Refer to Procedure 019-043]] | ISM and QSM11 Engines | 3666266 |
| Fuel Shutoff Valve | [[82-019-050 — Fuel Shutoff Valve\|Refer to Procedure 019-050]] | ISM and QSM11 Engines | 3666266 |
