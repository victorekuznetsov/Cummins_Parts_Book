---
type: "Процедура"
doc: "81-t05-1117"
title_en: "FAULT CODE 1117 - Power Supply Lost With Keyswitch ON - Data Erratic, Intermittent, or Incorrect"
modified: "2017-02-04"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-1117.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-1117.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# FAULT CODE 1117 - Power Supply Lost With Keyswitch ON - Data Erratic, Intermittent, or Incorrect

> [!abstract] Процедура · `81-t05-1117`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-02-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-t05-1117.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-t05-1117.pdf)

Printable Version

## Warnings and Cautions

> [!danger] WARNING · Опасно
> Batteries can emit explosive gasses. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead and Part Number 3824811 - female Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the battery. |  |
|  | **STEP 1A.** Check the battery connections. | Connections tight and corrosion-free? |
|  | **STEP 1B.** Check the battery 1 voltage. | Battery 1 voltage acceptable in normal and cranking conditions? |
|  | **STEP 1C.** Check the resistance of the original equipment manufacturer (OEM) power harness and engine harness. | Less than 10 ohms? |
| STEP 2. | Check the fuse. |  |
|  | **STEP 2A.** Verify that the fuse is installed correctly. | Fuse installed correctly? |
|  | **STEP 2B.** Check for a blown fuse. | Fuse blown? |
| STEP 3. | Check the OEM power harness and engine harness. |  |
|  | **STEP 3A.** Inspect the 4-pin power connector and the ECM connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit in the battery power circuits. | 10.0 and 15.0 VDC (12 volt system) or 21 to 27 VDC (24 VDC system)? |
|  | **STEP 3C.** Check battery supply for a short circuit from pin-to-pin. | Greater than 100k ohms? |
|  | **STEP 3D.** Check the add-on or accessory wiring at the positive (+) battery terminal. | Damaged wires? |
|  | **STEP 3E.** Check the ignition input-to-ECM wire. | Ignition input wire uninterrupted? |
|  | **STEP 3F.** Check the ignition input circuit. | Less than 5 ohms? |
| STEP 4. | Check the ECM calibration and clear the fault codes. |  |
|  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 4B.** Disable and clear the fault code. | Fault code inactive? |

### STEP 1. Check the battery.

#### STEP 1A. Check the battery connections.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery connections. Check the battery terminal connections on both positive (+) and negative (-) terminals. | Connections tight and corrosion-free? **YES** | 1B |
| Connections tight and corrosion-free? **NORepair:** Tighten the loose connections and clean the terminals. Refer to the equipment manufacturer service information. | 4A |  |

#### STEP 1B. Check the battery 1 voltage.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage. Measure the battery 1 voltage from the positive (+) battery terminal to the negative (-) battery terminal while trying to start the engine. Normal conditions: At least 12-VDC (+12 volt systems). At least 24-VDC (+24 volt systems). During Cranking: At least 6.2-VDC (+12 volt systems). At least 12-VDC (+24-volt systems). | Battery 1 voltage acceptable in normal and cranking conditions? **YES** | 1C |
| Battery 1 voltage acceptable in normal and cranking conditions? **NORepair:** Charge or replace the battery. Refer to the equipment manufacturer service information. | 4A |  |

#### STEP 1C. Check the resistance of the OEM power harness and engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the 4 pin power connector from the ECM connector. Disconnect the positive terminal connector from the battery connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the resistance of the battery supply circuit. Measure the resistance between the battery voltage SUPPLY pin in the ECM connector and the positive (+) battery connector. Measure the resistance between the battery voltage RETURN pin in the ECM connector and engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. Reference the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 2A |
| Less than 10 ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Repair the engine harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071]] in Section 19. | 4A |  |

### STEP 2. Check the fuse.

#### STEP 2A. Verify that the fuse is installed correctly.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that the fuse is installed correctly. Inspect the 10 fuse for correct installation. | Fuse installed correctly? **YES** | 2B |
| Fuse installed correctly? **NORepair:** Install the fuse correctly. Refer to Procedure 019-198 in Section 19. | 4A |  |

#### STEP 2B. Check for a blown fuse.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a blown fuse. Inspect the 10 fuse to see if it has blown. | Fuse blown? **YESRepair:** Replace the fuse. Refer to Procedure 019-198 in Section 19. | 4A |
| Fuse blown? **NO** | 3A |  |

### STEP 3. Check the OEM power harness and engine harness.

#### STEP 3A. Inspect the 4 pin power connector and the ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the 4 pin power connector from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the harness and the ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Reference the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Clean the connector and pins. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit in the battery power circuits.

| **Conditions:** Turn keyswitch OFF. Disconnect the 4 pin power harness connector from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the battery power circuits. Measure the voltage between the battery voltage SUPPLY pin in the 4 pin power connector to engine block ground. Refer to the circuit diagram or wiring diagram for connector pin identification. | 10.0 and 15.0 VDC (12 volt system) or 21 to 27 VDC (24 VDC system)? **YES** | 3C |
| 10.0 and 15.0 VDC (12 volt system) or 21 to 27 VDC (24 VDC system)? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3C. Check battery supply for a short circuit from pin-to-pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the 4 pin power harness connector from the ECMconnector. Disconnect the battery leads. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin-to-pin. Measure the resistance from battery voltage SUPPLY pin in the 4 pin power connector to all other pins in the connector. Measure the resistance from a battery voltage RETURN pin in the 4 pin power connector to all other pins in the connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Reference the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3D |
| Greater than 100k ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the short circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

#### STEP 3D. Check the add-on or accessory wiring at the positive (+) battery terminal.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the add-on or the accessory wiring at the positive (+) battery terminal. Starting at the positive (+) battery terminal, follow any add-on or accessory wiring, and examine the wire(s) for damaged insulation or an installation error that can cause the supply wire to be shorted the engine block. | Damaged wires? **YESRepair:** Repair or replace the damaged wires. Refer to the equipment manufacturer service information. | 4A |
| Damaged wires? **NO** | 3E |  |

#### STEP 3E. Check the ignition input-to-ECM wire.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition (keyswitch) input-to-ECM wire. Inspect the ignition wire from the ignition post in the ignition assembly to the ECM to make sure there are no interruptions in the wire, that is, no solenoids or relays. | Ignition wire uninterrupted? **YES** | 4A |
| Ignition wire uninterrupted? **NORepair:** Correct the wiring so the wire is uninterrupted. | 3F |  |

#### STEP 3F. Check the ignition input circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness connector from the ECM 50 pin connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the keyswitch input circuit. Measure the resistance from the ignition post in the ignition assembly to ignition input SUPPLY pin of the 50 pin engine harness connector. Refer to the circuit diagram or wiring diagram for connector pin identification. Reference the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 5 ohms? **YES** | 4A |
| Less than 5 ohms? **NORepair:** Troubleshoot all harnesses connected in series to determine which contains the open circuit. Refer to the circuit diagram or wiring diagram for all harness interconnections. Replace the damaged section of the harness. Refer to Procedure 019-043 in Section 19. Repair the OEM harness. Refer to Procedure 019-071 in Section 19. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Check if an ECM calibration update is available.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Compare the ECM code and revision number in the ECM to the calibration revisions listed in the ECM Calibration Revision History for applicable changes related to this fault code. Use INSITE™ electronic service tool to find the present ECM code and revision number in the ECM. The ECM code and revision number are found in the Calibration Information section of System ID and Dataplate in Features and Parameters. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? **YES** | 4B |
| If a calibration update for this fault code is available, does the ECM contain that revision or higher? **NORepair:** If necessary, calibrate the ECM. [[81-019-032 — ECM Calibration Code\|Refer to Procedure 019-032 in Section 19.]] | 4B |  |

#### STEP 4B. Disable the fault code.

| **Conditions:** Connect all components. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the overview Section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete. |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |
