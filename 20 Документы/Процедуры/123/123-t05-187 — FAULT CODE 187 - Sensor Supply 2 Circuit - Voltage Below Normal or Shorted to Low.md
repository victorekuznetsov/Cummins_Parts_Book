---
aliases:
  - "Код 187 — цепь питания датчиков 2 — напряжение ниже нормы"
type: "Процедура"
doc: "123-t05-187"
title_en: "FAULT CODE 187 - Sensor Supply 2 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 187 — цепь питания датчиков 2 — напряжение ниже нормы"
modified: "2026-02-06"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-187.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-187.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 187 - Sensor Supply 2 Circuit - Voltage Below Normal or Shorted to Low Source
**Код 187 — цепь питания датчиков 2 — напряжение ниже нормы**

> [!abstract] Процедура · `123-t05-187`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-187.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-187.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead, Part Number 3164596 - male Framatome™ test lead, and Part Number 3164597 - female Framatome™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for an active fault code. | Fault Code 187 active? |
| STEP 2. | Check the sensors and circuits connected to the sensor supply 2 and return. |  |
|  | **STEP 2A.** Inspect the sensors and circuits connected to the sensor supply 2 and return. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the circuit response. | Fault Code 187 active? |
| STEP 3. | Check the ECM. |  |
|  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for a pin-to-pin short circuit. | Greater than 100k ohms? |
|  | **STEP 3B-1.** Check for a pin short circuit to ground. | Greater than 100k ohms? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 187 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for an active fault code.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 187 active? **YES** | 2A |
| Fault Code 187 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |

### STEP 2. Check the sensors and circuits connected to the sensor supply 2 and return.

#### STEP 2A. Inspect the sensors and circuits connected to the sensor supply 2 and return.

| **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Disconnect the engine harness connector from the 31-pin OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the harness connectors and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection had been detected in the sensor or harness connector. Clean the connector and pins. Replace the damaged section of the harness or damaged sensor. Refer to circuit diagram or wiring diagram for all harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-085 in Section 19. Refer to Procedure 019-071 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 187 active? **YES** | 3A |
| Fault Code 187 active? **NORepair:** Replace the accelerator pedal or lever position sensor, if equipped. Refer to Procedure 019-085 in Section 19. Replace the speed bias switch, if equipped. Refer to the OEM Service Manual. Replace the gain adjust potentiometer, if equipped. Refer to the OEM Service Manual. | 4A |  |

### STEP 3. Check the ECM.

#### STEP 3A. Inspect the ECM and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine harness. Clean the connector and pins. Replace the damaged section of harness. Refer to the circuit diagram or wiring diagram for all engine harness interconnections. Refer to Procedure 019-043 in Section 19. Refer to Procedure 019-199 in Section 19. Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for a pin-to-pin short circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and all other pins in the ECM connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3B-1 |
| Greater than 100k ohms? **NORepair:** A short circuit has been detected in the 5 volt SUPPLY (sensor supply 2) wire. Troubleshoot harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-199 in Section 19. Refer to Procedure 019-043 in Section 19. | 4A |  |

#### STEP 3B-1. Check for a pin short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 60-pin OEM port connector. Disconnect the accelerator pedal or lever position sensor connector from the OEM harness connector, if equipped. Disconnect the speed bias connector from the OEM harness connector, if equipped. Disconnect the gain adjust potentiometer connector from the OEM harness connector, if equipped. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance between the 5 volt SUPPLY (sensor supply 2) pin in the engine harness ECM connector and ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YESRepair:** Replace the ECM. [[123-019-031 — Engine Control Module\|Refer to Procedure 019-031 in Section 19.]] | 4A |
| Greater than 100k ohms? **NORepair:** A short circuit has been detected in the 5 volt SUPPLY (sensor supply 2) wire. Troubleshoot harnesses connected in series to determine which contains the short circuit to ground. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of harnesses. Refer to Procedure 019-071 in Section 19. Refer to Procedure 019-199 in Section 19. Refer to Procedure 019-043 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ electronic service tool to verify the fault code is inactive. | Fault Code 187 inactive? **YES** | 4B |
| Fault Code 187 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete |
| All fault codes cleared? **NO** | Appropriate troubleshooting steps |  |
