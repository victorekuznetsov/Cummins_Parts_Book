---
type: "Процедура"
doc: "178-t05-132"
title_en: "FAULT CODE 132 - Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-132.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-132.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
---

# FAULT CODE 132 - Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `178-t05-132`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-132.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-132.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3823995 - male Weather Pack™ test lead, Part Number 3823996 - female Weather Pack™ test lead, and Part Number 3822758 - male Deutsch™/AMP™/Metri-Pack™ test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for sensor supply fault codes. | Fault Code 2185 or 2186 active? |
|  | **STEP 1B.** Check for an active fault code. | Fault Code 132 active? |
| STEP 2. | Check the accelerator pedal or lever position sensor and circuit. |  |
|  | **STEP 2A.** Inspect the accelerator pedal position sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the accelerator pedal position sensor supply voltage and return circuit. | Between 4.75 VDC and 5.25 VDC? |
|  | **STEP 2C.** Check the circuit response. | Fault Code 131 active and Fault Code 132 inactive? |
|  | **STEP 2D.** Check the fault codes and verify accelerator pedal or lever condition. | Fault Code 132 is active? |
| STEP 3. | Check the ECM and original equipment manufacturer (OEM) harness. |  |
|  | **STEP 3A.** Inspect the ECM and OEM harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
|  | **STEP 3C.** Check for an open circuit in the OEM harness. | Less than 10 ohms? |
|  | **STEP 3D.** Check for a pin-to-pin short circuit in the OEM harness. | Greater than 100k ohms? |
|  | **STEP 3E.** Check for a pin-to-ground short circuit in the OEM harness. | Greater than 100k ohms? |
|  | **STEP 3F.** Check for an inactive fault code. | Fault Code 132 inactive? |
| STEP 4. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 4B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for sensor supply fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 2185 or 2186 active? **YES** | Appropriate fault code troubleshooting tree |
| Fault Code 2185 or 2186 active? **NO** | 1B |  |

#### STEP 1B. Check for an active fault code.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an active fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 132 active? **YES** | 2A |
| Fault Code 132 active? **NO** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |  |

### STEP 2. Check the accelerator pedal position sensor and circuit.

#### STEP 2A. Inspect the accelerator pedal position sensor and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal position sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the accelerator pedal position sensor supply voltage and return circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal position sensor from the OEM harness. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the sensor supply voltage and return circuit. Measure the voltage from the accelerator pedal position +5 volt SUPPLY pin to the accelerator pedal position RETURN pin at the sensor connector of the OEM harness. Use a wiring diagram and the following procedure for general multimeter usage. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Between 4.75 VDC and 5.25 VDC? **YES** | 2C |
| Between 4.75 VDC and 5.25 VDC? **NO** | 3A |  |

#### STEP 2C. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the accelerator pedal position sensor from the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the circuit response. Place a jumper wire between the accelerator pedal position +5 volt SUPPLY pin and the accelerator pedal position SIGNAL pin at the sensor connector of the OEM harness. Refer to the circuit diagram or the wiring diagram for connector pin identification. Check for the appropriate ECM response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 131 active and Fault Code 132 inactive? **YES** | 2D |
| Fault Code 131 active and Fault Code 132 inactive? **NO** | 3A |  |

#### STEP 2D. Check the fault codes and verify accelerator pedal condition.

| **Conditions:** Turn keyswitch OFF. Connect the accelerator pedal to the OEM harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 132 is active? **YESRepair:** A damaged accelerator pedal has been detected. See equipment manufacturer service information for repair instructions. Replace the accelerator pedal. See equipment manufacturer service information. | 4A |
| Fault Code 132 is active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |

### STEP 3. Check the ECM and OEM harness.

#### STEP 3A. Inspect the ECM and OEM harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the OEM harness and ECM connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins if possible. Repair or replace the OEM wiring harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check for an open circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the accelerator pedal position sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the OEM harness ECM connector accelerator pedal or lever SUPPLY pin and the OEM harness accelerator pedal or lever connector SUPPLY pin. Use a wiring diagram for pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3C |
| Less than 10 ohms? **NORepair:** An open supply circuit has been detected in the OEM harness. Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |

#### STEP 3C. Check for an open circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the accelerator pedal from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance between the OEM harness ECM connector accelerator pedal or lever SIGNAL pin and the OEM harness accelerator pedal connector SIGNAL pin. Use a wiring diagram for pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YES** | 3D |
| Less than 10 ohms? **NORepair:** An open signal circuit has been detected in the OEM harness. Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |

#### STEP 3D. Check for a pin-to-pin short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the accelerator pedal position sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-pin short. Measure the resistance between the accelerator pedal SIGNAL pin in the OEM harness ECM connector and all other pins in the OEM connector. Use a wiring diagram for pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3E |
| Greater than 100k ohms? **NORepair:** Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |

#### STEP 3E. Check for a pin-to-ground short circuit in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ECM connector. Disconnect the accelerator pedal position sensor from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin-to-ground short. Measure the resistance between the accelerator pedal SIGNAL pin in the OEM harness ECM connector and ground. Use a wiring diagram for pin identification and the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Greater than 100k ohms? **YES** | 3F |
| Greater than 100k ohms? **NORepair:** A pin-to-ground short circuit on the SIGNAL wire has been detected in the OEM harness. Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness\|Refer to Procedure 019-071 in Section 19.]] | 4A |  |

#### STEP 3F. Check for an inactive fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 132 inactive? **YESRepair:** The removal and installation of the connector corrected the fault. | 4A |
| Fault Code 132 inactive? **NORepair:**. Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |

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
| Disable and clear the fault code. Operate the engine within the "Conditions for Clearing the Fault Code" found in the Overview section of this troubleshooting procedure. | Fault code inactive? **YES** | Repair complete |
| Fault code inactive? **NORepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 1A |  |

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
| Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Engine Control Module | Refer to Procedure 019-031 | ISL9.5 CM2150 SN | 4310608 |
| Engine Control Module | Refer to Procedure 019-031 | ISB3.9 CM2220 B107 | 4310792 |
| Engine Control Module | Refer to Procedure 019-031 | QSB4.5 CM2150 B108 | 4326163 |
| Engine Control Module | Refer to Procedure 019-031 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Engine Control Module | Refer to Procedure 019-031 | QSB7 CM2880 B117 | 4358390 |
| Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G106 | 4332695 |
| Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G107 | 4332690 |
| Engine Control Module | Refer to Procedure 019-031 | ISG11 CM2880 G108 | 4332901 |
| Engine Control Module | Refer to Procedure 019-031 | ISG12 CM2880 G109 | 4332906 |
| Engine Control Module | Refer to Procedure 019-031 | QSNT14 CM876 N102 | 4325993 |
| Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F104 | 4332741 |
| Engine Control Module | Refer to Procedure 019-031 | QSF2.8 CM2880 F108 | 4332746 |
| Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
| Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F116 | 4383664 |
| Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
| Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 F129 | 5411325 |
| Engine Control Module | Refer to Procedure 019-031 | ISF4.5 CM2220 F123 | 5411320 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F134B | 5504165 |
| Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
| Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
| Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
| Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
| Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
