---
aliases:
  - "Код 1543 — цепь вспомогательного датчика давления 1 — напряжение ниже нормы"
type: "Процедура"
doc: "122-t05-1543"
title_en: "FAULT CODE 1543 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 1543 — цепь вспомогательного датчика давления 1 — напряжение ниже нормы"
modified: "2012-07-29"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1543.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-1543.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# FAULT CODE 1543 - Auxiliary Pressure Sensor Input 1 Circuit - Voltage Below Normal or Shorted to Low Source
**Код 1543 — цепь вспомогательного датчика давления 1 — напряжение ниже нормы**

> [!abstract] Процедура · `122-t05-1543`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-t05-1543.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-t05-1543.pdf)

Printable Version

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for sensor supply fault codes. | Fault Code 352 active? |
| STEP 2. | Check the OEM pressure sensor and circuit. |  |
|  | **STEP 2A.** For Marine applications, check if a a resistive jumper is installed when a pressure sensor is **not** being used. | Resistive jumper installed in wiring harness extension when OEM pressure sensor is **not** being used? |
|  | **STEP 2B.** For Marine applications, check the resistive jumper. | Resistance within specifications across all pins? |
|  | **STEP 2C.** Inspect the OEM pressure sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 2D.** Check the sensor supply voltage and return circuit. | Voltage between 4.75 and 5.25-VDC? |
|  | **STEP 2E.** Check the circuit response. | Fault Code 297 active and Fault Code 298 inactive? |
|  | **STEP 2F.** Check the fault codes and verify sensor condition. | Fault Code 298 active? |
| STEP 3. | Check the ECM and OEM harness. |  |
|  | **STEP 3A.** Inspect ECM and OEM harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
|  | **STEP 3C.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
|  | **STEP 3D.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100K ohms? |
|  | **STEP 3E.** Check for a pin-to-ground short circuit. | Greater than 100K ohms? |
|  | **STEP 3F.** Check for an inactive fault code. | Fault Code 298 inactive? |
| STEP 4. | Clear fault codes. |  |
|  | **STEP 4A.** Disable the fault codes. | Fault Code 1543 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for sensor supply fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for sensor supply fault codes. Use INSITE™ electronic service to tool read the fault codes. | Fault Code 352 active? **YES** | Reference Fault Code 352. |
| Fault Code 352 active? **NO** | 2A |  |

### STEP 2. Check the OEM pressure sensor and circuit.

#### STEP 2A. For Marine applications, check if a resistive jumper is installed when a pressure sensor is **not** being used.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check if an OEM pressure sensor is installed. If an OEM pressure sensor is not installed, check to make sure a resistive jumper is installed in the wiring harness extension. | Resistive jumper installed in wiring harness extension when OEM pressure sensor is **not** being used? **YES** | 2B |
| Resistive jumper installed in wiring harness extension when OEM pressure sensor is **not** being used? **NORepair:** Install the resistive jumper in the wiring harness extension. | 4A |  |

#### STEP 2B. For Marine applications, check the resistive jumper.

| **Conditions:** Turn keyswitch OFF. Disconnect the wiring extension harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the resistance across the pins. Pin 1 to Pin 2: 1.2k Ohms Pin 2 to Pin 3: 1.5k Ohms Pin 1 to Pin 3: 270 Ohms Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Resistance within specifications across all pins? **YES** | 2C |
| Resistance within specifications across all pins? **NORepair:** Replace the resistive jumper. | 4A |  |

#### STEP 2C. Inspect the OEM pressure sensor and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and OEM pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2D |  |

#### STEP 2D. Check the sensor supply voltage and return circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage and return circuit. Measure the voltage between the OEM pressure +5 volt SUPPLY pin and the OEM pressure RETURN pin at the sensor connector of the OEM harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Voltage between 4.75 and 5.25-VDC? **YES** | 2E |
| Voltage between 4.75 and 5.25-VDC? **NO** | 3A |  |

#### STEP 2E. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM pressure sensor from the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Place a jumper wire between the OEM pressure SUPPLY pin and the OEM pressure SIGNAL pin at the OEM pressure sensor connector of the OEM harness. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 297 active and Fault Code 298 inactive? **YES** | 2F |
| Fault Code 297 active and Fault Code 298 inactive? **NO** | 3A |  |

#### STEP 2F. Check the fault codes and verify sensor condition.

| **Conditions:** Turn keyswitch OFF. Connect the OEM pressure sensor to the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 298 is active? **YESRepair:** A damaged sensor has been detected. Replace the OEM pressure sensor. Refer to the OEM service manual. | 4A |
| Fault Code 298 is active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |

### STEP 3. Check the ECM and OEM harness.

#### STEP 3A. Inspect ECM and OEM harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or OEM harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the OEM harness ECM connector OEM pressure RETURN pin and the OEM harness OEM pressure sensor connector RETURN pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
| Less than 10 ohms? **NORepair:** An open return circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open return circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3C. Check for an open circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the OEM harness ECM connector OEM pressure SIGNAL pin and the OEM harness OEM pressure sensor connector SIGNAL pin. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms **YES** | 3D |
| Less than 10 ohms? **NORepair:** An open signal circuit has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the open signal circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3D. Check for a pin-to-pin short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short. Measure the resistance between the OEM pressure SIGNAL pin in the OEM harness ECM connector and all other pins in the OEM connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3E |
| Greater than 100k ohms? **NORepair:** A pin-to-pin short circuit on the signal wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the shorted signal circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3E. Check for a pin-to-ground short circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the OEM pressure sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-ground short. Measure the resistance between the OEM pressure SIGNAL pin in the OEM harness ECM connector and ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3F |
| Greater than 100k ohms? **NORepair:** A pin-to-ground short circuit on the signal wire has been detected in the OEM harness. Troubleshoot each harness connected in series to determine which contains the shorted signal circuit. Repair or replace the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3F. Check for an inactive fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 298 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
| Fault Code 298 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify that the fault code is inactive. | Fault Code 1543 inactive? **YES** | 4B |
| Fault Code 1543 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining fault codes. | Go to the appropriate troubleshooting steps. |  |
