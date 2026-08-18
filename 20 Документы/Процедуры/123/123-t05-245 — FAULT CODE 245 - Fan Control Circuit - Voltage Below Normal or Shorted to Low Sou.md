---
aliases:
  - "Код 245 — цепь управления вентилятором — напряжение ниже нормы или замыкание на массу"
type: "Процедура"
doc: "123-t05-245"
title_en: "FAULT CODE 245 - Fan Control Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Код 245 — цепь управления вентилятором — напряжение ниже нормы или замыкание на массу"
modified: "2012-05-14"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-245.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-245.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# FAULT CODE 245 - Fan Control Circuit - Voltage Below Normal or Shorted to Low Source
**Код 245 — цепь управления вентилятором — напряжение ниже нормы или замыкание на массу**

> [!abstract] Процедура · `123-t05-245`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-t05-245.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-t05-245.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3822917 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for an active fault code. | Fault Code 245 active? |
| STEP 2. | Check the fan control circuit. |  |
|  | **STEP 2A.** Inspect the fan control connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check for an internal short in the fan control. | Within the OEM resistance specification? |
|  | **STEP 2B-1.** Check for a pin-to-ground short circuit in the fan control. | Greater than 100k ohms? |
|  | **STEP 2C.** Check the fan control diagnostic supply voltage and supply wire. | Greater than 5-VDC? |
| STEP 3. | Check the ECM and OEM harness. |  |
|  | **STEP 3A.** Inspect the ECM and OEM harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for a pin-to-ground short circuit in the OEM harness. | Greater than 100k ohms? |
|  | **STEP 3C.** Check for a pin-to-pin short circuit in the OEM harness or engine harness. | Greater than 100k ohms? |
|  | **STEP 3D.** Check for an inactive fault code. | Fault Code 245 inactive? |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 245 inactive? |
|  | **STEP 4B.** Clear the inactive fault codes. | All fault codes cleared? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for an active fault code.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 245 active? **YES** | 2A |
| Fault Code 245 active? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |

### STEP 2. Check the fan control circuit.

#### STEP 2A. Inspect the fan control connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the fan control connector from the OEM harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness, engine harness, and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire or insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the solenoid or harness connector. Clean the connector and pins. Replace the damaged section of the harness or damaged sensor. Check all harnesses connected in series. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] Repair the engine harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Repair the connectors. [[99-019-199 — Connector, Butt Splice\|Refer to Procedure 019-199 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check for an internal short in the fan control.

| **Conditions:** Turn keyswitch OFF. Disconnect the fan control connector from the OEM harness connector or engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for low internal resistance of the fan control solenoid. Use a multimeter to measure the resistance between the fan control switch SIGNAL and RETURN pin of the fan control connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Refer to the OEM service manual for resistance specifications. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Within the OEM resistance specification? **YES** | 2B-1 |
| Within the OEM resistance specification? **NORepair:** Replace the fan control. Refer to the OEM service manual. | 4A |  |

#### STEP 2B-1. Check for a pin-to-ground short circuit in the fan control.

| **Conditions:** Turn keyswitch OFF. Disconnect the fan control connector from the OEM harness connector or engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Short circuit on one connector pin-to-ground check: Measure the resistance and check for a short circuit between the fan control SIGNAL connector pin and ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 2C |
| Greater than 100k ohms? **NORepair:** Replace the fan control. Refer to the OEM service manual. | 4A |  |

#### STEP 2C. Check the fan control diagnostic supply voltage and supply wire.

| **Conditions:** Turn keyswitch OFF. Disconnect the fan control connector from the OEM harness connector or engine harness connector. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage between the fan control SIGNAL pin and the fan control RETURN pin. Refer to the circuit diagram or wiring diagram for connector pin identification. | Greater than 5-VDC? **YES** | 3C |
| Greater than 5-VDC? **NO** | 3A |  |

### STEP 3. Check the ECM, engine harness, and OEM harness.

#### STEP 3A. Inspect all OEM and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the all harness connections. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the solenoid or harness connector. Replace the damaged section of the harness. Refer to the OEM service manual. Refer to the circuit diagram or wiring diagram for all harness interconnections. Repair the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] Repair the engine harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Replace the fan control circuit. Refer to Procedure 019-045 in Section 19. Repair the connectors. [[99-019-199 — Connector, Butt Splice\|Refer to Procedure 019-199 in Section 19.]] [[99-019-204 — Deutsch DRC Connector Series\|Refer to Procedure 019-204 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for a pin-to-ground short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the fan control connector from the OEM harness connector or engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Short circuit on one connector pin-to-ground check: Measure the resistance and check for a short circuit between the fan control SIGNAL pin of the ECM 60-pin OEM port connector and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3C |
| Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the engine harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Repair the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] Repair the connectors. [[99-019-199 — Connector, Butt Splice\|Refer to Procedure 019-199 in Section 19.]] | 4A |  |

#### STEP 3C. Check for a pin-to-pin short circuit in the OEM harness or engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the fan control connector from the OEM harness connector or engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Short circuit on one connector pin-to-pin check: Measure the resistance and check for a short circuit between the fan control SIGNAL pin of the ECM 60-pin OEM port connector pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3D |
| Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the pin-to-pin short. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the engine harness. [[123-019-043 — Engine Wiring Harness\|Refer to Procedure 019-043 in Section 19.]] Repair the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] Repair the connectors. [[99-019-199 — Connector, Butt Splice\|Refer to Procedure 019-199 in Section 19.]] | 4A |  |

#### STEP 3D. Check for an inactive fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 245 inactive? **YESRepair:** None: The removal and installation of the connector corrected the fault. | 4A |
| Fault Code 245 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Disconnect the fan control connector from the engine harness connector or OEM harness connector. Turn the keyswitch OFF. Connect the fan control connector to the engine harness connector or OEM harness connector. Turn keyswitch ON. Use INSITE™ electronic service tool to verify that the fault codes are inactive. | Fault Code 245 inactive? **YES** | 4B |
| Fault Code 245 inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

#### STEP 4B. Clear the inactive fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault codes. Use INSITE™ electronic service tool to clear the inactive fault codes. | All fault codes cleared? **YES** | Repair complete. |
| All fault codes cleared? **NORepair:** Troubleshoot any remaining active fault codes. | Go to the appropriate troubleshooting steps. |  |
