---
aliases:
  - "Код 5121 — цепь датчика давления масла топливного насоса — напряжение ниже нормы"
type: "Процедура"
doc: "122-t05-5121"
title_en: "FAULT CODE 5121 - Fuel Pump Lubricating Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 5121 — цепь датчика давления масла топливного насоса — напряжение ниже нормы"
modified: "2020-05-21"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-5121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-5121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 5121 - Fuel Pump Lubricating Oil Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Код 5121 — цепь датчика давления масла топливного насоса — напряжение ниже нормы**

> [!abstract] Процедура · `122-t05-5121`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-05-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-5121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-5121.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3164596 - male Framatome™ test lead and Part Number 3822917 - female Deutsch™/Amp™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for sensor supply fault codes. | Fault Code 2186 active? |
| STEP 2. | Check the fuel pump lubricating oil pressure sensor and circuit. |  |
|  | **STEP 2A.** Inspect the pins and connectors for damage. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the sensor supply voltage and return circuit. | 4.75 to 5.25-VDC? |
|  | **STEP 2C.** Check the circuit response. Fuel pump lubricating oil pressure sensor circuit check. | Fault Code 5119 active? |
| STEP 3. | Fuel pump lubricating oil pressure sensor circuit check. |  |
|  | **STEP 3A.** Fuel pump lubricating oil pressure sensor circuit pin to ground check. | Resistance less than 100k ohms? |
|  | **STEP 3B.** Fuel pump lubricating oil pressure sensor circuit pin to pin check. | Resistance less than 100k ohms? |
| STEP 4. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 4B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for sensor supply fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | Go to the appropriate fault code troubleshooting tree. |
| Fault Code 2186 active? **NO** | 2A |  |

### STEP 2. Check the fuel pump lubricating oil pressure sensor and circuit.

#### STEP 2A. Inspect the fuel pump lubricating oil pressure sensor and engine wiring harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor connector from the engine wiring harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the pins and connectors for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Dirt or debris in or on the connector pins Wire insulation damage Missing or damaged connector seals Connector or shell broken Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair or replace only the components that were found to be out of specification. Replace the fuel pump lubricating oil pressure sensor. Refer to Procedure 019-679 in Section 19. Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the sensor supply voltage and return circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor connector from the engine wiring harness connector. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage and return circuit. Measure the voltage from the Fuel pump oil pressure, 5 volt SUPPLY pin to the Fuel pump oil pressure RETURN pin at the sensor connector of the engine wiring harness. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359]] in Section 19. | 4.75 to 5.25-VDC? **YES** | 2C |
| 4.75 to 5.52-VDC? **NO** | 3A |  |

#### STEP 2C. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor connector from the engine wiring harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the fuel pump lubricating oil pressure sensor SUPPLY pin and the fuel pump lubricating oil pressure sensor SIGNAL pin at the sensor connector of the engine wiring harness. Turn keyswitch ON. Connect the INSITE™ electronic service tool or equivalent. Check for appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 5119 active? **YESRepair:** A damaged fuel pump lubricating oil pressure sensor has been detected. Replace the fuel pump lubricating oil pressure sensor. Refer to Procedure 019-679 in Section 19. | 4A |
| Fault Code 5119 active? **NO** | 3A |  |

### STEP 3. Fuel pump lubricating oil pressure sensor circuit check.

#### STEP 3A. Fuel pump lubricating oil pressure sensor circuit pin to ground check.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor from the engine wiring harness. Disconnect the engine wiring harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the fuel pump lubricating oil pressure sensor SIGNAL pin at the engine wiring harness ECM connector and ground. | Resistance less than 100k ohms? **YESRepair:** A malfunctioning engine wiring harness has been detected. Repair or replace the engine wiring harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] in Section 19. | 4A |
| Resistance less than 100k ohms? **NO** | 3B |  |

#### STEP 3B. Fuel pump lubricating oil pressure sensor circuit pin to pin check.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel pump lubricating oil pressure sensor from the engine wiring harness. Disconnect the engine wiring harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance between the fuel pump lubricating oil pressure sensor SIGNAL pin at the engine wiring harness ECM connector and all other pins at the engine wiring harness ECM connector. | Resistance less than 100k ohms? **YESRepair:** A malfunctioning engine wiring harness has been detected. Repair or replace the engine wiring harness. [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] in Section 19. | 4A |
| Resistance less than 100k ohms? **NO** | 4A |  |

### STEP 4. Clear ECM calibration and clear fault codes.

#### STEP 4A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032]] in Section 19. | 4B |  |

#### STEP 4B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the ”Conditions for Clearing the Fault Code” found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow the technical escalation process. | Escalate or call for assistance. |  |
