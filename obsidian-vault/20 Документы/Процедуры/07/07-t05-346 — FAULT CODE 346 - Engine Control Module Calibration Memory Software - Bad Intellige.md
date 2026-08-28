---
aliases:
  - "Код 346 — ПО калибровочной памяти ЭБУ — неисправное устройство"
type: "Процедура"
doc: "07-t05-346"
title_en: "FAULT CODE 346 - Engine Control Module Calibration Memory Software - Bad Intelligent Device or Component"
title_ru: "Код 346 — ПО калибровочной памяти ЭБУ — неисправное устройство"
modified: "2016-10-07"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-t05-346.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-t05-346.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# FAULT CODE 346 - Engine Control Module Calibration Memory Software - Bad Intelligent Device or Component
**Код 346 — ПО калибровочной памяти ЭБУ — неисправное устройство**

> [!abstract] Процедура · `07-t05-346`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-t05-346.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-t05-346.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Read the fault codes. | Fault Code 346 active or inactive with more than one count logged in the last 25 engine hours? |
| STEP 2. | Check the ECM and engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness and ECM connectors. | Dirty or damaged pins? |
|  | **STEP 2B.** Check for an open circuit in the unswitched battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
|  | **STEP 2C.** Check for an open circuit in the unswitched battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
| STEP 3. | Check the batteries and fuses. |  |
|  | **STEP 3A.** Check the batteries. | Connections tight and corrosion-free? |
|  | **STEP 3B.** Check the battery voltage. | Battery voltage acceptable in normal and cranking conditions? |
|  | **STEP 3B-1.** Verify that the original equipment manufacturer (OEM) fuses are installed correctly. | Fuse installed correctly? |
|  | **STEP 3B-2.** Check if the OEM fuses are blown. | Fuse blown? |
| STEP 4. | Check the OEM power harness and 4 pin ECM power interface connector. |  |
|  | **STEP 4A.** Inspect the power harness and 4 pin ECM power interface connector pins. | Dirty or damaged pins? |
|  | **STEP 4B.** Check for an open circuit in the battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
|  | **STEP 4C.** Check for an open circuit in the battery power circuits. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
| STEP 5. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 5B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Read the fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to read the fault codes. | Fault Code 346 active or inactive with more than one count logged in the last 25 engine hours? **YES** | 2A |
| Fault Code 346 active or inactive with more than one count logged in the last 25 engine hours? **NO** | Use the following procedure for an inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19]]. |  |

### STEP 2. Check the ECM and engine harness.

#### STEP 2A. Inspect the ECM and engine harness connectors.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness from the 4 pin ECM power interface connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or the engine harness connector. Clean the connector and pins. Replace the damaged section of the harness. Reference the circuit diagram or wiring diagram for all harness interconnections. Replace the harness. Refer to 019-043 in the Associated Procedures Table. | 5A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check for an open circuit in the unswitched battery power circuits.

| **Conditions:** Turn keyswitch OFF Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage between the unswitched battery voltage SUPPLY pins and RETURN pins at the 50 pin ECM engine harness connector. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 5A |
| At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NO** | 2C |  |

#### STEP 2C. Check for an open circuit in the unswitched battery power circuits.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM. Disconnect the engine harness from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage between the unswitched battery voltage SUPPLY pins at the 50 pin engine harness connector and engine block ground. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** An open or high resistance circuit has been detected in the battery voltage return circuit. Troubleshoot the engine harness and all interconnects for the malfunction. Repair or replace the damaged component as necessary. | 5A |
| At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NO** | 3A |  |

### STEP 3. Check the batteries and fuses.

#### STEP 3A. Check the batteries and fuses.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery terminal connections. | Connections tight and corrosion-free? **YES** | 3B |
| Connections tight and corrosion-free? **NORepair:** Tighten the loose connections and clean the terminals. See the equipment manufacturer service information. | 5A |  |

#### STEP 3B. Check the battery voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place the positive (+) probe of the multimeter on the positive battery terminal and touch the negative (-) probe to the negative battery terminal while trying to start the engine. | Battery voltage acceptable in normal and cranking conditions? **YES** | 3B-1 |
| Battery voltage acceptable in normal and cranking conditions? **NORepair:** Charge or replace the battery. See the equipment manufacturer service information. | 5A |  |

#### STEP 3B-1. Verify that the OEM fuses are installed correctly.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that the OEM 10A fuses between the battery and 4 pin ECM power interface are installed correctly. Reference the circuit diagram or the wiring diagram for connector pin identification. | Fuses installed correctly? **YES** | 3B-2 |
| Fuses installed correctly? **NORepair:** Install the fuses correctly. [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19]]. | 5A |  |

#### STEP 3B-2. Check if the OEM fuses are blown.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that the OEM 10A fuses between the battery and 4 pin ECM power interface are **not** blown. Reference the circuit diagram or the wiring diagram for connector pin identification. | Fuses blown? **YESRepair:** Locate the short circuit. Replace the blown fuse(s). [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19]]. | 5A |
| Fuses blown? **NO** | 4A |  |

### STEP 4. Check the power harness and 4 pin ECM power interface connector.

#### STEP 4A. Inspect the power harness and the 4 pin ECM power interface connector pins.

| **Conditions:** Turn keyswitch OFF Disconnect power harness from the 4 pin ECM Power interface connector. Disconnect the power harness from the batteries. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the power harness and 4 pin ECM Power interface connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19]]. | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the power harness or 4 pin ECM power interface connection. Clean the connector and pins. Reference the circuit diagram or wiring diagram for all harness interconnections. Replace the harness or interface connector. | 5A |
| Dirty or damaged pins? **NO** | 4B |  |

#### STEP 4B. Check for an open circuit in the battery power circuits.

| **Conditions:** Turn keyswitch OFF. Disconnect the power harness from the 4 pin ECM power interface connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage between the power harness SUPPLY pins and the power harness RETURN pins at the power harness 4 pin power interface connector. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** Troubleshoot the engine harness and the interconnect for the malfunction. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 5A |
| At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NO** | 4C |  |

#### STEP 4C. Check for an open circuit in the battery power circuits.

| **Conditions:** Turn keyswitch OFF. Disconnect the power harness from the 4 pin ECM power interface connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage between the power harness SUPPLY pins on the power harness 4 pin ECM power interface connector and engine block ground. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. Refer to Procedure 019-359 in Section 19. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YESRepair:** An open or high resistance circuit has been detected in the battery voltage return circuit. Troubleshoot the power harness and all interconnects for the malfunction. Repair or replace the damaged component as necessary. | 5A |
| At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NORepair:** An open or high resistance circuit has been detected in the battery voltage return circuit. Troubleshoot the power harness and all interconnects for the malfunction. Repair or replace the damaged component as necessary. | 5A |  |

### STEP 5. Check ECM calibration and clear fault codes.

#### STEP 5A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. Refer to Procedure 019-032 in Section 19 in the Associated Procedure Table. | 5B |  |

#### STEP 5B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
| Fault code inactive? **NORepair:** Verify that all steps have been completed. If all steps have been completed, then follow your technical escalation process. | Repair complete |  |
