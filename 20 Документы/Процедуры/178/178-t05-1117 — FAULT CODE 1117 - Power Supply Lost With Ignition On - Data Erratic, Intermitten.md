---
type: "Процедура"
doc: "178-t05-1117"
title_en: "FAULT CODE 1117 - Power Supply Lost With Ignition On - Data Erratic, Intermittent, or Incorrect"
modified: "2017-04-20"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-1117.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-1117.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
---

# FAULT CODE 1117 - Power Supply Lost With Ignition On - Data Erratic, Intermittent, or Incorrect

> [!abstract] Процедура · `178-t05-1117`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-04-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-1117.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-1117.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3164133 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check for fault codes. |  |
|  | **STEP 1A.** Check for fault codes. | Fault Code 1117 active? |
| STEP 2. | Check the batteries and the power connector. |  |
|  | **STEP 2A.** Check the batteries and the power connector. | Connections tight and corrosion-free? |
|  | **STEP 2B.** Check the battery voltage. | Normal conditions: At least (+) 12 VDC \[(+) 24 VDC with 24 volt system\]; During cranking: At least (+) 6.2 VDC? |
| STEP 3. | Check the original equipment manufacturer (OEM) power harness. |  |
|  | **STEP 3A.** Inspect the harness and the ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit in the battery power circuit. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? |
|  | **STEP 3B-1.** Verify that the OEM fuse is installed correctly. | Fuse installed correctly? |
|  | **STEP 3B-2.** Check if the OEM fuse is blown. | Fuse blown? |
|  | **STEP 3B-3.** Check the add-on or accessory wiring at the (+) terminal of the battery. | Damaged wires? |
|  | **STEP 3C.** Check battery ground(s), engine block, and chassis ground. | Connections tight and corrosion-free? |
|  | **STEP 3D.** Check the resistance of the battery supply circuit. | Less than 1.0 ohms? |
|  | **STEP 3E.** Check the keyswitch input-to-ECM wire. | Keyswitch input wire uninterrupted? |
|  | **STEP 3F.** Check the keyswitch input circuit. | Less than 5 ohms? |
| STEP 4. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 4B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check for fault codes.

#### STEP 1A. Check for fault codes.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for active fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 1117 active? **YES** | 2A |
| Fault Code 1117 active? **NORepair:** If high inactive counts of Fault Code 1117 are found in the ECM, check the battery disconnect devices in the vehicle. If the keyswitch and ECM power are disconnected at the same time, Fault Code 1117 will be logged. | 4A |  |

### STEP 2. Check the batteries and the power connector.

#### STEP 2A. Check the batteries and the power connector.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery connections. Check the battery terminal connections. | Connections tight and corrosion-free? **YES** | 2B |
| Connections tight and corrosion-free? **NORepair:** Tighten the loose connections and clean the terminals. See the equipment manufacturer service information. | 4A |  |

#### STEP 2B. Check the battery voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage. Place the positive (+) probe of the multimeter on the positive battery terminal and touch the negative (-) probe to the negative battery terminal while trying to start the engine. | Normal conditions: At least (+) 12 VDC \[(+) 24 VDC with 24 volt system\]; During cranking: At least (+) 6.2 VDC? **YES** | 3A |
| Normal conditions: At least (+) 12 VDC \[(+) 24 VDC with 24 volt system\]; During cranking: At least (+) 6.2 VDC? **NORepair:** Charge or replace the battery. See the equipment manufacturer service information. | 4A |  |

### STEP 3. Check the OEM power harness.

#### STEP 3A. Inspect the harness and the ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM power harness/OEM harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the harness and the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM connector or OEM power harness/OEM harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit in the battery power circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM power harness/OEM harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the battery power circuits. Use a multimeter to measure the voltage from the ECM battery SUPPLY (+) pin of the OEM power harness/OEM harness connector and engine block ground. Reference the circuit diagram or the wiring diagram for connector pin identification. | At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **YES** | 3C |
| At least (+) 10 VDC \[(+) 20 VDC for a 24 volt system\]? **NO** | 3B-1 |  |

#### STEP 3B-1. Verify that the OEM fuse is installed correctly.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM fuse for correct installation.. | Fuse installed correctly? **YES** | 3B-2 |
| Fuse installed correctly? **NORepair:** Install the fuse correctly. [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19.]] | 4A |  |

#### STEP 3B-2. Check if the OEM fuse is blown.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that the OEM fuse is **not** blown.. | Fuse blown? **YESRepair:** Locate the short circuit. Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] Replace the blown fuse(s). [[99-019-198 — Fuse, Harness In-Line\|Refer to Procedure 019-198 in Section 19.]] | 4A |
| Fuse blown? **NO** | 3B-3 |  |

#### STEP 3B-3. Check the add-on or the accessory wiring at the (+) terminal of the battery.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the add-on or the accessory wiring at the (+) terminal of the battery. Starting at the (+) terminal, follow any add-on or accessory wiring and examine wire(s) for damaged insulation or an installation error that can cause the supply wire to be shorted to the engine block. | Damaged wires? **YESRepair:** Repair or replace the damaged wiring. | 4A |
| Damaged wires? **NORepair:** Repair or replace the OEM harness from the OEM power connector to the batteries. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3C. Check battery ground(s), engine block, and chassis ground.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check battery ground(s), engine block, and chassis ground. Check all battery ground(s), engine block, and chassis ground for properly grounded, tightened, and free of corrosion. See equipment manufacturer service information and wiring diagram for grounds information. | Connections tight and corrosion-free? **YES** | 3D |
| Connections tight and corrosion-free? **NORepair:** Tighten the loose connections and clean the terminals. See equipment manufacturer service information. | 4A |  |

#### STEP 3D. Check the resistance of the battery supply circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM power harness/OEM harness connector from the ECM. Disconnect the positive terminal from the battery. Digital multimeter set to low resistance mode and calibrated to zero. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the resistance of the battery supply circuit. Measure the resistance between the ECM battery SUPPLY (+) pin of the OEM power harness/OEM harness connector and the positive battery connector. Measure the resistance between the ECM battery SUPPLY (-) pin of the OEM power harness/OEM harness connector and the negative battery connector. Reference the circuit diagram or the wiring diagram for connector pin identification. Since the battery supply circuit resistance is normally very low, it is necessary to use a digital multimeter calibrated to zero on the low resistance setting to accurately measure the circuit resistance. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 1.0 ohms? **YES** | 3E |
| Less than 1.0 ohms? **NORepair:** Repair or replace the OEM power harness/OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |

#### STEP 3E. Check the keyswitch input-to-ECM wire.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the keyswitch input wire from the keyswitch ignition post in the keyswitch assembly to the ECM to make sure there are no interruptions in the wire, that is, no solenoids or relays. | Keyswitch input wire uninterrupted? **YES** | 4A |
| Keyswitch input wire uninterrupted? **NORepair:** Correct the wiring so the wire is uninterrupted. | 3F |  |

#### STEP 3F. Check the keyswitch input circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the keyswitch input circuit. Measure the resistance from the keyswitch ignition post in the keyswitch assembly to keyswitch input SIGNAL pin of the OEM harness connector. Reference the circuit diagram or the wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 5 ohms? **YES** | 4A |
| Less than 5 ohms? **NORepair:** Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |

### STEP 4. Check ECM calibration and clear fault codes.

#### STEP 4A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[105-019-032 — Engine Control Module Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 4B |  |

#### STEP 4B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
