---
aliases:
  - "Код 343 — предупреждение о внутреннем аппаратном отказе ЭБУ"
type: "Процедура"
doc: "82-t05-343"
title_en: "FAULT CODE 343 - Engine Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component"
title_ru: "Код 343 — предупреждение о внутреннем аппаратном отказе ЭБУ"
modified: "2014-01-22"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-343.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-343.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# FAULT CODE 343 - Engine Control Module Warning Internal Hardware Failure - Bad Intelligent Device or Component
**Код 343 — предупреждение о внутреннем аппаратном отказе ЭБУ**

> [!abstract] Процедура · `82-t05-343`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2014-01-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-t05-343.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-t05-343.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3164133 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for fault codes. | Fault Code 343 active or more than three inactive counts? |
| STEP 2. | Check the batteries and the power connector. |  |
|  | **STEP 2A.** Check the batteries and the power connector. | Connections tight and corrosion-free? |
|  | **STEP 2B.** Check the battery voltage. | Normal conditions: At least (+) 12-VDC \[(+) 24-VDC with 24 volt system\]; During Cranking: At least (+) 6.2-VDC? |
| STEP 3. | Check the original equipment manufacturer (OEM) power harness. |  |
|  | **STEP 3A.** Inspect the harness and the ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit in the battery power circuit. | At least (+) 10-VDC \[(+) 20-VDC for a 24 volt system\]? |
|  | **STEP 3B-1.** Verify that the OEM fuse is installed correctly. | Fuse installed correctly? |
|  | **STEP 3B-2.** Check if the OEM fuse is blown. | Fuse blown? |
|  | **STEP 3B-3.** Check the add-on or accessory wiring at the (+) terminal of the battery. | Any damaged wires? |
|  | **STEP 3C.** Check the resistance of the battery supply circuit. | Less than 1.0 ohms? |
|  | **STEP 3D.** Check the keyswitch input-to-ECM wire. | Keyswitch input wire uninterrupted? |
|  | **STEP 3E.** Check the keyswitch input circuit. | Less than 5 ohms? |
| STEP 4. | Recalibrate the ECM. |  |
|  | **STEP 4A.** Recalibrate the ECM. | Fault Code 343 active after recalibrating the ECM? |
| STEP 5. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 5A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 5B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Read the fault codes.

#### STEP 1A. Check for fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 343 active or more than three inactive counts? **YES** | 2A |
| Fault Code 343 active or more than three inactive counts? **NO** | 5A |  |

### STEP 2. Check the batteries and the power connector.

#### STEP 2A. Check the batteries and the power connector.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery connections. Check the battery terminal connections. | Connections tight and corrosion-free? **YES** | 2B |
| Connections tight and corrosion-free? **NORepair:** Tighten the connections. Tighten the loose connections and clean the terminals. Refer to the OEM service manual. | 5A |  |

#### STEP 2B. Check the battery voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage. Place the positive (+) probe of the multimeter on the positive battery terminal and touch the negative (-) probe to the negative battery terminal while trying to start the engine. | Normal conditions: At least (+) 12-VDC \[(+) 24-VDC with 24 volt system\]; During cranking: At least (+) 6.2-VDC? **YES** | 3A |
| Normal conditions: At least (+) 12-VDC \[(+) 24-VDC with 24 volt system\]; During cranking: At least (+) 6.2-VDC? **NORepair:** Charge or replace the battery. Refer to the OEM service manual. | 5A |  |

### STEP 3. Check the OEM power harness.

#### STEP 3A. Inspect the harness and the ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM power harness connector from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the OEM harness. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 5A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit in the battery power circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM battery supply stub from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the battery power circuits. Use a multimeter to measure the voltage from the ECM battery supply (+) pin of the engine harness ECM battery supply stub connector and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general multimeter usage techniques. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | At least (+) 10-VDC \[(+) 20-VDC for a 24 volt system\]? **YES** | 3C |
| At least (+) 10-VDC \[(+) 20-VDC for a 24 volt system\]? **NO** | 3B-1 |  |

#### STEP 3B-1. Verify that the OEM fuse is installed correctly.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM fuse for correct installation. | Fuse installed correctly? **YES** | 3B-2 |
| Fuse installed correctly? **NORepair:** Install the fuse correctly. [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19.]] | 5A |  |

#### STEP 3B-2. Check if the OEM fuse is blown.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that the OEM fuse is not blown. | Fuse blown? **YESRepair:** Locate the short circuit. Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] Replace the blown fuse(s). [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19.]] | 5A |
| Fuse blown? **NO** | 3B-3 |  |

#### STEP 3B-3. Check the add-on or the accessory wiring at the (+) terminal of the battery.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the add-on or the accessory wiring at the (+) terminal of the battery. Starting at the (+) terminal, follow any add-on or accessory wiring and examine wire(s) for damaged insulation or an installation error that can cause the supply wire to be shorted to the engine block. | Any damaged wires? **YESRepair:** Repair or replace the damaged wiring. | 5A |
| Any damaged wires? **NORepair:** Repair or replace the OEM power harness from the OEM power connector to the batteries. Refer to the OEM service manual. | 5A |  |

#### STEP 3C. Check the resistance of the battery supply circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM battery supply stub from the ECM connector. Disconnect the positive terminal from the battery. Digital multimeter set to low resistance mode and calibrated to zero. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the resistance of the battery supply circuit. Measure the resistance between the ECM battery SUPPLY (+) pin of the engine harness ECM battery supply stub connector and the positive battery connector. Measure the resistance between the ECM battery SUPPLY (-) pin of the engine harness ECM battery supply stub connector and the negative battery connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Since the battery supply circuit resistance is normally very low, it is necessary to use a digital multimeter calibrated to zero on the low resistance setting to accurately measure the circuit resistance. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 1.0 ohms? **YES** | 3D |
| Less than 1.0 ohms? **NORepair:** Repair or replace the ECM power harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 5A |  |

#### STEP 3D. Check the keyswitch input-to-ECM wire.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the keyswitch input. Inspect the keyswitch input wire from the keyswitch ignition post in the keyswitch assembly to the ECM to make sure there are no interruptions in the wire, that is, no solenoids or relays. | Keyswitch input wire uninterrupted? **YESRepair:** Correct the wiring so the wire is uninterrupted. | 5A |
| Keyswitch input wire uninterrupted? **NO** | 3E |  |

#### STEP 3E. Check the keyswitch input circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the keyswitch input circuit. Measure the resistance from the keyswitch ignition post in the keyswitch assembly to keyswitch input SIGNAL pin of the OEM harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 5 ohms? **YES** | 4A |
| Less than 5 ohms? **NORepair:** Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 5A |  |

### STEP 4. Recalibrate the ECM.

#### STEP 4A. Recalibrate the ECM

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Use INSITE™ electronic service tool to recalibrate the ECM with the latest engine calibration. | Fault Code 343 active after recalibrating the ECM? **YESRepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 5A |
| Fault Code 343 active after recalibrating the ECM? **NO** | 5A |  |

### STEP 5. Check ECM calibration and clear fault codes.

#### STEP 5A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 5B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 5B |  |

#### STEP 5B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 E ISF2.8 CM2220 AN ISF2.8 CM2220 IAN | 4022178 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 ISF3.8 CM2220 AN ISF3.8 CM2220 IAN | 4021704 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F103 | 4310839 |
| Engine Control Module | Refer to Procedure 019-031 | ISB4.5, ISB6.7, ISD4.5, and ISD6.7 CM2150 SN | 4022188 |
| Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2150 SN | 4022190 |
| Engine Control Module | Refer to Procedure 019-031 | ISM11 CM876 SN | 4022196 |
| Engine Control Module | Refer to Procedure 019-031 | ISZ13 CM2150 | 4022133 |
| Engine Control Module | Refer to Procedure 019-031 | ISX15 CM2250 GX CM2250 | 4022250 |
| Engine Control Module | Refer to Procedure 019-031 | ISX12/ISX11.9 CM2250 | 2883445 |
| Engine Control Module | Refer to Procedure 019-031 | QSL9 CM2250 | 4022256 |
| Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2250 | 4022255 |
| Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2350 B105 | 4332778 |
| Engine Control Module | Refer to Procedure 019-031 | QSL9 CM2350 L102 | 4332796 |
| Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2250 EC | 2883621 |
| Engine Control Module | Refer to Procedure 019-031 | QSB3.3 CM2250 EC | 2883647 |
| Engine Control Module | Refer to Procedure 019-031 | QSK78 CM2250 K104 | 4332682 |
| Engine Control Module | Refer to Procedure 019-031 | QSX15 CM2250 ECF | 2883557 |
| Engine Control Module | Refer to Procedure 019-031 | PowerGen QSX15 CM2250 ECF | 4310661 |
| Engine Control Module | Refer to Procedure 019-031 | PowerGen QSX15 CM2250 | 4310664 |
| Engine Control Module | Refer to Procedure 019-031 | QSX11.9 CM2250 ECF | 2883561 |
| Engine Control Module | Refer to Procedure 019-031 | ISB6.7 CM2350 B101 | 2883567 |
| Engine Control Module | Refer to Procedure 019-031 | ISL9 CM2350 L101 | 4310787 |
| Engine Control Module | Refer to Procedure 019-031 | ISX12 CM2350 X102 | 4310646 |
| Engine Control Module | Refer to Procedure 019-031 | ISX15 CM2350 X101 | 4310641 |
| Engine Control Module | Refer to Procedure 019-031 | ISX15 CM2250 SN | 4310736 |
| Engine Control Module | Refer to Procedure 019-031 | ISB4.5 CM2350 B104 | 4332646 |
| Engine Control Module | Refer to Procedure 019-031 | ISB6.7 CM2350 B103 | 4332641 |
| Engine Control Module | Refer to Procedure 019-031 | ISB/ISD4.5 CM2150 B119 | 4358465 |
| Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2150 B120 | 4358470 |
| Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2150 L110 | 4358475 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F110 | 4358480 |
