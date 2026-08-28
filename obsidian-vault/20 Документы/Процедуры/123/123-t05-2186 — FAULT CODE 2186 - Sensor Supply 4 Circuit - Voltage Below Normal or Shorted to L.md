---
aliases:
  - "Код 2186 — цепь питания датчиков 4 — напряжение ниже нормы"
type: "Процедура"
doc: "123-t05-2186"
title_en: "FAULT CODE 2186 - Sensor Supply 4 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 2186 — цепь питания датчиков 4 — напряжение ниже нормы"
modified: "2026-02-09"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2186.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2186.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 2186 - Sensor Supply 4 Circuit - Voltage Below Normal or Shorted to Low Source
**Код 2186 — цепь питания датчиков 4 — напряжение ниже нормы**

> [!abstract] Процедура · `123-t05-2186`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-2186.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-t05-2186.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new ECM, all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3164596 - male Framatome™ test lead, and Part Number 3164597 - female Framatome™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for an active fault code. | Fault Code 2186 active? |
| STEP 2. | Check the sensors and circuits connected to the sensor supply 4 and return. |  |
|  | **STEP 2A.** Inspect the engine camshaft speed/position sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
|  | **STEP 2A-1.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2B.** Inspect the intake manifold 1 pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
|  | **STEP 2B-1.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2C.** Inspect the injector metering rail 1 pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
|  | **STEP 2C-1.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2D.** Inspect the barometric pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
|  | **STEP 2D-1.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2E.** Inspect the fuel delivery pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
|  | **STEP 2E-1.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2F.** Inspect the oil rifle pressure sensor and circuit connected to the sensor supply 4 and return. | Dirty or damaged pins? |
|  | **STEP 2F-1.** Check the circuit response. | Fault Code 2186 active? |
|  | **STEP 2G.** Inspect the crankcase pressure sensor and circuit connected to the sensor supply 4 and return, if equipped. | Dirty or damaged pins? |
|  | **STEP 2G-1.** Check the circuit response. | Fault Code 2186 active? |
| STEP 3. | Check the ECM. |  |
|  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the ECM response. | Fault Code 2186 active? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 2186 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for an active fault code.

| **Conditions:** Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2A |
| Fault Code 2186 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |

### STEP 2. Check the sensors and circuits connected to the sensor supply 4 and return.

#### STEP 2A. Inspect the engine camshaft speed/position sensor and circuit connected to the sensor supply 4 and return.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine camshaft speed/position sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection had been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-218 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2A-1 |  |

#### STEP 2A-1. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine camshaft speed/position sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE ™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2B |
| Fault Code 2186 active? **NORepair:** Replace the engine camshaft speed/position sensor. Refer to Procedure 019-363 in Section 19. | 4A |  |

#### STEP 2B. Inspect the intake manifold 1 pressure sensor and circuit connected to the sensor supply 4 and return.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold 1 pressure sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2B-1 |  |

#### STEP 2B-1. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold 1 pressure sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2C |
| Fault Code 2186 active? **NORepair:** Replace the intake manifold 1 pressure sensor. Refer to Procedure 019-061 in Section 19. | 4A |  |

#### STEP 2C. Inspect the injector metering rail 1 pressure sensor and circuit connected to the sensor supply 4 and return.

| **Conditions:** Turn keyswitch OFF. Disconnect the injector metering rail 1 pressure sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-215 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2C-1 |  |

#### STEP 2C-1 Check the circuit response..

| **Conditions:** Turn keyswitch OFF. Disconnect the injector metering rail 1 pressure sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2D |
| Fault Code 2186 active? **NORepair:** Replace the injector metering rail 1 pressure sensor. [[123-019-115 — Rail Fuel Pressure Sensor\|Refer to Procedure 019-115 in Section 19.]] | 4A |  |

#### STEP 2D. Inspect the barometric pressure sensor and circuit connected to the sensor supply 4 and return.

| **Conditions:** Turn keyswitch OFF. Disconnect the barometric pressure sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-218 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2D-1 |  |

#### STEP 2D-1. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the barometric pressure sensor connector from the engine harness connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2E |
| Fault Code 2186 active? **NORepair:** A damaged barometric pressure sensor has been detected. Replace the barometric pressure sensor. Refer to Procedure 019-004 in Section 19. | 4A |  |

#### STEP 2E. Inspect the fuel delivery pressure sensor and circuit connected to the sensor supply 4 and return.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel delivery pressure sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2E-1 |  |

#### STEP 2E-1. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the fuel delivery pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2F |
| Fault Code 2186 active? **NORepair:** A damaged fuel delivery pressure sensor has been detected. Replace the fuel delivery pressure sensor. Refer to Procedure 019-398 in Section 19. | 4A |  |

#### STEP 2F. Inspect the oil rifle pressure sensor and circuit connected to the sensor supply 4 and return.

| **Conditions:** Turn keyswitch OFF. Disconnect the oil rifle pressure sensor connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2F-1 |  |

#### STEP 2F-1. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the oil rifle pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 2G |
| Fault Code 2186 active? **NORepair:** A malfunctioning or damaged oil rifle pressure sensor has been detected. Replace the oil rifle pressure sensor. Refer to Procedure 019-066 in Section 19. | 4A |  |

#### STEP 2G. Inspect the crankcase pressure sensor and circuit connected to the sensor supply 4 and return, if equipped.

| **Conditions:** Turn keyswitch OFF. Disconnect the crankcase pressure sensor connector from the engine harness connector, if equipped. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the engine harness or damaged sensor. Refer to the circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-209 in Section 19. Refer to Procedure 019-390 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2G-1 |  |

#### STEP 2G-1. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the crankcase pressure sensor from the engine harness, if equipped. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YES** | 3A |
| Fault Code 2186 active? **NORepair:** A malfunctioning or damaged crankcase pressure sensor has been detected. Replace the crankcase pressure sensor, if equipped. Refer to Procedure 019-445 in Section 19. | 4A |  |

### STEP 3. Check the ECM.

#### STEP 3A. Inspect the ECM and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or engine harness. Clean the connector and pins. Replace the damaged section of the engine harness. Refer to the circuit art or wiring diagram for all engine harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-204 in Section 19. Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the ECM response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2186 active? **YESRepair:** Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 4A |
| Fault Code 2186 active? **NORepair:** epair or replace the engine harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 2186 inactive? **YES** | 4B |
| Fault Code 2186 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components Turn keyswitch ON Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Appropriate troubleshooting steps |  |
