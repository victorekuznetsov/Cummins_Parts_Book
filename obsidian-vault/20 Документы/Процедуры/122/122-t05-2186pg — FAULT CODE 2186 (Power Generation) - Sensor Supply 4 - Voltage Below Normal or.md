---
aliases:
  - "Код 2186 (генераторные установки) — питание датчиков 4 — напряжение ниже нормы"
type: "Процедура"
doc: "122-t05-2186pg"
title_en: "FAULT CODE 2186 (Power Generation) - Sensor Supply 4 - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 2186 (генераторные установки) — питание датчиков 4 — напряжение ниже нормы"
modified: "2017-03-23"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2186pg.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-2186pg.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 2186 (Power Generation) - Sensor Supply 4 - Voltage Below Normal or Shorted to Low Source
**Код 2186 (генераторные установки) — питание датчиков 4 — напряжение ниже нормы**

> [!abstract] Процедура · `122-t05-2186pg`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-03-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-2186pg.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-t05-2186pg.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for an active fault code. | Fault Code 2186 active? |
|  | **STEP 1B.** Check the service model name. | Engine a QSK38 CM2150? |
|  | **STEP 1C.** Check the service model name. | Engine a QSK50 CM2150? |
|  | **STEP 1D.** Check the service model name. | Engine a QSK60 CM2150? |
| STEP 2. | Check the sensors and circuits connected to the sensor supply return. |  |
|  | **STEP 2A.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2B.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2C.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2D.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2E.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2F.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2G.** Check the circuit response | Fault Code 2186 active? |
|  | **STEP 2H.** Check the circuit response. | Fault Code 2186 active? |
| STEP 3. | Check the sensors and circuits connected to the sensor supply return. |  |
|  | **STEP 3A.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 3B.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 3C.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 3D.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 3E.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 3F.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 3G.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 3H.** Check the circuit response. | Fault Code 2186 active? |
| STEP 4. | Check the sensors and circuits connected to the sensor supply return. |  |
|  | **STEP 4A.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4B.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4C.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4D.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4E.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4F.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4G.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4H.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 4I.** Check the circuit response. | Fault Code 2186 active? |
| STEP 5. | Check the ECM and engine harness. |  |
|  | **STEP 5A.** Check for a pin-to-pin short circuit in the engine harness. | Greater than 100k ohms? |
|  | **STEP 5B.** Check for a pin-to-ground short circuit in the engine harness. | Greater than 100k ohms? |
| STEP 6. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 6A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 6B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for an active fault code.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 1B |
| Fault Code 2186 active? **NO** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |

#### STEP 1B. Check the service model name.

| **Conditions:** Not Applicable |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the service model name of the engine. | Engine a QSK38 CM2150? **YES** | 2A |
| Engine a QSK38 CM2150? **NO** | 1C |  |

#### STEP 1C. Check the service model name.

| **Conditions:** Not Applicable |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the service model name of the engine. | Engine a QSK50 CM2150? **YES** | 3A |
| Engine a QSK50 CM2150? **NO** | 1D |  |

#### STEP 1D. Check the service model name.

| **Conditions:** Not Applicable |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the service model name of the engine. | Engine a QSK60 CM2150? **YES** | 4A |
| Engine a QSK60 CM2150? **NO** | Repair complete |  |

### STEP 2. Check the sensors and circuits connected to the sensor supply return.

#### STEP 2A. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the rail fuel pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 2B |
| Fault Code 2186 active? **NORepair:** Replace the rail fuel pressure sensor. Refer to Procedure 019-115 in the Associated Procedures Table. | 6A |  |

#### STEP 2B. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the camshaft speed sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 2C |
| Fault Code 2186 active? **NORepair:** Replace the camshaft speed sensor. Refer to Procedure 019-363 in the Associated Procedures Table. | 6A |  |

#### STEP 2C. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine coolant pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 2D |
| Fault Code 2186 active? **NORepair:** Replace the engine coolant pressure sensor. Refer to Procedure 019-016 in the Associated Procedures Table. | 6A |  |

#### STEP 2D. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold air temperature/pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 2E |
| Fault Code 2186 active? **NORepair:** Replace the intake manifold air temperature sensor. Refer to Procedure 019-059 in the Associated Procedures Table. Replace the intake manifold air pressure sensor. Refer to Procedure 019-061 in the Associated Procedures Table. | 6A |  |

#### STEP 2E. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine oil pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 2F |
| Fault Code 2186 active? **NORepair:** Replace the engine oil pressure sensor. Refer to Procedure 019-066 in the Associated Procedures Table. | 6A |  |

#### STEP 2F. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the crankcase pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 2G |
| Fault Code 2186 active? **NORepair:** Replace the crankcase pressure sensor. Refer to Procedure 019-445 in the Associated Procedures Table. | 6A |  |

#### STEP 2G. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel supply pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 2H |
| Fault Code 2186 active? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in the Associated Procedures Table. | 6A |  |

#### STEP 2H. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 5A |
| Fault Code 2186 active? **NORepair:** Replace the ambient air pressure sensor. Refer to Procedure 019-004 in the Associated Procedures Table. | 6A |  |

### STEP 3. Check the sensors and circuits connected to the sensor supply return.

#### STEP 3A. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the rail fuel pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 3B |
| Fault Code 2186 active? **NORepair:** Replace the rail fuel pressure sensor. Refer to Procedure 019-115 in the Associated Procedures Table. | 6A |  |

#### STEP 3B. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the camshaft speed sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 3C |
| Fault Code 2186 active? **NORepair:** Replace the camshaft speed sensor. Refer to Procedure 019-363 in the Associated Procedures Table. | 6A |  |

#### STEP 3C. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine coolant pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 3D |
| Fault Code 2186 active? **NORepair:** Replace the engine coolant pressure sensor. Refer to Procedure 019-016 in the Associated Procedures Table. | 6A |  |

#### STEP 3D. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold air temperature/pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 3E |
| Fault Code 2186 active? **NORepair:** Replace the intake manifold air temperature sensor. Refer to Procedure 019-059 in the Associated Procedures Table. Replace the intake manifold air pressure sensor. Refer to Procedure 019-061 in the Associated Procedures Table. | 6A |  |

#### STEP 3E. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine oil pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 3F |
| Fault Code 2186 active? **NORepair:** Replace the engine oil pressure sensor. Refer to Procedure 019-066 in the Associated Procedures Table. | 6A |  |

#### STEP 3F. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the crankcase pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 3G |
| Fault Code 2186 active? **NORepair:** Replace the crankcase pressure sensor. Refer to Procedure 019-445 in the Associated Procedures Table. | 6A |  |

#### STEP 3G. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 3H |
| Fault Code 2186 active? **NORepair:** Replace the ambient air pressure sensor. Refer to Procedure 019-004 in the Associated Procedures Table. | 6A |  |

#### STEP 3H. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel supply pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 5A |
| Fault Code 2186 active? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in the Associated Procedures Table. | 6A |  |

### STEP 4. Check the sensors and circuits connected to the sensor supply return.

#### STEP 4A. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the rail fuel pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 4B |
| Fault Code 2186 active? **NORepair:** Replace the rail fuel pressure sensor. Refer to Procedure 019-115 in the Associated Procedures Table. | 6A |  |

#### STEP 4B. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the camshaft speed sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 4C |
| Fault Code 2186 active? **NORepair:** Replace the camshaft speed sensor. Refer to Procedure 019-363 in the Associated Procedures Table. | 6A |  |

#### STEP 4C. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine coolant pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 4D |
| Fault Code 2186 active? **NORepair:** Replace the engine coolant pressure sensor. Refer to Procedure 019-016 in the Associated Procedures Table. | 6A |  |

#### STEP 4D. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold air temperature/pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 4E |
| Fault Code 2186 active? **NORepair:** Replace the intake manifold air temperature sensor. Refer to Procedure 019-059 in the Associated Procedures Table. Replace the intake manifold air pressure sensor. Refer to Procedure 019-061 in the Associated Procedures Table. | 6A |  |

#### STEP 4E. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine oil pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 4F |
| Fault Code 2186 active? **NORepair:** Replace the engine oil pressure sensor. Refer to Procedure 019-066 in the Associated Procedures Table. | 6A |  |

#### STEP 4F. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the crankcase pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 4G |
| Fault Code 2186 active? **NORepair:** Replace the crankcase pressure sensor. Refer to Procedure 019-445 in the Associated Procedures Table. | 6A |  |

#### STEP 4G. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the ambient air pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 4H |
| Fault Code 2186 active? **NORepair:** Replace the ambient air pressure sensor. Refer to Procedure 019-004 in the Associated Procedures Table. | 6A |  |

#### STEP 4H. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel supply pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Use INSITE™ electronic service tool to read the fault codes | Fault Code 2186 active? **YES** | 5A |
| Fault Code 2186 active? **NORepair:** Replace the fuel supply pressure sensor. Refer to Procedure 019-398 in the Associated Procedures Table. | 6A |  |

### STEP 5. Check the ECM and engine harness.

#### STEP 5A. Check for a pin-to-pin short circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Disconnect the camshaft speed sensor from the engine harness. Disconnect the rail fuel pressure sensor from the engine harness. Disconnect the intake manifold air temperature and pressure sensor from the engine harness. Disconnect the crankcase pressure sensor from the engine harness. Disconnect the engine oil pressure sensor from the engine harness. Disconnect the ambient air pressure sensor from the engine harness. Disconnect the engine coolant pressure sensor from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short circuit. Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Measure the resistance and check for a short circuit between the sensor supply 4 ECM harness connector pin and all other pins in the engine harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 5B |
| Greater than 100k ohms? **NORepair:** Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 6A |  |

#### STEP 5B. Check for a pin-to-ground short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Disconnect the camshaft speed sensor from the engine harness. Disconnect the rail fuel pressure sensor from the engine harness. Disconnect the intake manifold air temperature and pressure sensor from the engine harness. Disconnect the crankcase pressure sensor from the engine harness. Disconnect the engine oil pressure sensor from the engine harness. Disconnect the ambient air pressure sensor from the engine harness. Disconnect the engine coolant pressure sensor from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-ground short circuit. Inspect the sensor pins and engine harness connector for damage. Refer to Procedure 019-361 in Section 19. Measure the resistance and check for a short circuit between the sensor supply 4 ECM harness connector pin and all other pins in the engine harness ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 6A |
| Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 6A |  |

### STEP 6. Check ECM calibration and clear fault codes.

#### STEP 6A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 6B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 6B |  |

#### STEP 6B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Ambient Air Pressure Sensor | [[122-019-004 — Barometric Pressure Sensor\|Refer to Procedure 019-004]] | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Engine Coolant Pressure Sensor | Refer to Procedure 019-016 | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Engine Wiring Harness | [[122-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043]] | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Intake Manifold Air Temperature Sensor | Refer to Procedure 019-059 | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Intake Manifold Air Pressure Sensor | Refer to Procedure 019-061 | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Engine Oil Pressure Sensor | Refer to Procedure 019-066 | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Rail Fuel Pressure Sensor | [[122-019-115 — Rail Fuel Pressure Sensor\|Refer to Procedure 019-115]] | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Camshaft Position Sensor | Refer to Procedure 019-363 | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Fuel Supply Pressure Sensor | Refer to Procedure 019-398 | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
| Crankcase Pressure Sensor | Refer to Procedure 019-445 | QSK38, QSK50, and QSK60 CM2150 | [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M\|4022102]] |
