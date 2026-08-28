---
type: "Процедура"
doc: "178-t05-122"
title_en: "FAULT CODE 122 - Intake Manifold 1 Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2019-08-22"
engines:
  - "82099327"
families:
  - "QSB6.7"
manuals:
  - "4326169"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSB6.7"
  - "группа/178"
---

# FAULT CODE 122 - Intake Manifold 1 Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `178-t05-122`
> **Двигатели:** [[82099327 — QSB6.7 CM2150 B109 CPL 4375|82099327]]
> **Семейство:** QSB6.7
> **Входит в руководства:** [[4326169 — QSB6.7 CM2150 B109 Fault Code Troubleshooting Manual|4326169]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-08-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/178/178-t05-122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/178-t05-122.pdf)

Printable Version

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damaging a new engine control module (ECM), all other active fault codes must be investigated prior to replacing the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the fault codes. |  |
|  | **STEP 1A.** Check for sensor supply fault codes. | Sensor supply fault codes active? |
|  | **STEP 1B.** Check for an inactive fault code. | Fault Code 122 inactive? |
| STEP 2. | Check the intake manifold pressure sensor and circuit. |  |
|  | **STEP 2A.** Inspect the intake manifold pressure sensor and connector pins. | Dirty or damaged pins? |
|  | **STEP 2B.** Check the circuit response. | Fault Code 123 active and Fault Code 122 inactive? |
|  | **STEP 2C.** Check the sensor supply voltage and return circuit. | Between 4.75 VDC and 5.25 VDC? |
|  | **STEP 2D.** Check the fault codes and verify sensor condition. | Fault Code 122 active? |
| STEP 3. | Check the ECM and engine harness. |  |
|  | **STEP 3A.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3A-1.** Check the ECM response. | Fault Code 123 active and Fault Code 122 inactive? |
|  | **STEP 3A-2.** Check for an active fault code. | Fault Code 122 inactive? |
|  | **STEP 3B.** Inspect the ECM and engine harness connector pins. | Dirty or damaged pins? |
|  | **STEP 3B-1.** Check the sensor supply voltage and return circuit. | Between 4.75 VDC and 5.25 VDC? |
|  | **STEP 3B-2.** Check for an active fault code. | Fault Code 122 inactive? |
| STEP 4. | Check ECM calibration and clear fault codes. |  |
|  | **STEP 4A.** Check if an ECM calibration update is available. | If a calibration update for this fault code is available, does the ECM contain that revision or higher? |
|  | **STEP 4B.** Disable the fault code. | Fault code inactive? |

### STEP 1. Check the fault codes.

#### STEP 1A. Check for sensor supply fault codes.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for sensor supply fault codes. Use INSITE™ electronic service tool to read the fault codes. | Sensor supply fault codes active? **YES** | Appropriate fault code troubleshooting tree |
| Sensor supply fault codes active? **NO** | 1B |  |

#### STEP 1B. Check for an inactive fault code.

| **Conditions:** Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an inactive fault code. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 122 inactive? **YES** | Use the following procedure for inactive or intermittent fault code. [[99-019-362 — Inactive or Intermittent Fault Code\|Refer to Procedure 019-362 in Section 19.]] |
| Fault Code 122 inactive? **NO** | 2A |  |

### STEP 2. Check the intake manifold pressure sensor and circuit.

#### STEP 2A. Inspect the intake manifold pressure sensor and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold pressure sensor from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and intake manifold pressure sensor connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the sensor or harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
| Dirty or damaged pins? **NO** | 2B |  |

#### STEP 2B. Check the circuit response.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold pressure sensor from the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 123 active and Fault Code 122 inactive? **YES** | 2C |
| Fault Code 123 active and Fault Code 122 inactive? **NO** | 3A |  |

#### STEP 2C. Check the sensor supply voltage and return circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the intake manifold pressure sensor from the engine harness. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage and return circuit. Measure the voltage from the intake manifold pressure +5 VOLT SUPPLY pin to the intake manifold pressure RETURN pin at the sensor connector of the engine harness. Use a wiring diagram for pin identification and the following procedure for general multimeter usage. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Between 4.75 VDC and 5.25 VDC? **YES** | 2D |
| Between 4.75 VDC and 5.25 VDC? **NO** | 3B |  |

#### STEP 2D. Check the fault codes and verify sensor condition.

| **Conditions:** Turn keyswitch OFF. Connect the intake manifold pressure sensor to the engine harness. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 122 active? **YESRepair:** A damaged sensor has been detected. Replace the intake manifold pressure sensor. Refer to Procedure 019-159 in the Associated Procedures Table. | 4A |
| Fault Code 122 active? **NORepair:** None. The removal and installation of the connector corrected the fault. | 4A |  |

### STEP 3. Check the ECM and engine harness.

#### STEP 3A. Inspect the ECM and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
| Dirty or damaged pins? **NO** | 3A-1 |  |

#### STEP 3A-1. Check the ECM response.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 123 active and Fault Code 122 inactive? **YES** | 3A-2 |
| Fault Code 123 active and Fault Code 122 inactive? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |

#### STEP 3A-2. Check for an active fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 122 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
| Fault Code 122 inactive? **NORepair:** A pin-to-pin short circuit has been detected on the SIGNAL wire of the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |

#### STEP 3B. Inspect the ECM and engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the engine harness and ECM engine connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the ECM engine connector or engine harness connector. Clean the connector and pins. Repair the damaged harness, connector, or pins, if possible. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |
| Dirty or damaged pins? **NO** | 3B-1 |  |

#### STEP 3B-1. Check the sensor supply voltage and return circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness from the ECM connector. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the supply voltage and return circuit. Measure the voltage from the intake manifold pressure +5 VOLT SUPPLY pin to the intake manifold pressure RETURN pin at the ECM engine connector. Use a wiring diagram for pin identification and the following procedure for general multimeter usage. [[99-019-359 — Multimeter Usage\|Refer to Procedure 019-359 in Section 19.]] | Between 4.75 VDC and 5.25 VDC? **YES** | 3B-2 |
| Between 4.75 VDC and 5.25 VDC? **NORepair:** Replace the ECM. Refer to Procedure 019-031 in the Associated Procedures Table. | 4A |  |

#### STEP 3B-2. Check for an active fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for the appropriate circuit response after 30 seconds. Use INSITE™ electronic service tool to read the fault codes. | Fault Code 122 inactive? **YESRepair:** None. The removal and installation of the connector corrected the fault. | 4A |
| Fault Code 122 inactive? **NORepair:** An open return circuit has been detected in the engine harness. Repair or replace the engine harness. Refer to Procedure 019-043 in the Associated Procedures Table. | 4A |  |

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

## Associated Procedures

| Associated Procedures |  |  |  |
|---|---|---|---|
| Procedure Title | Procedure Number | Service Model Name | Bulletin Number |
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
| Engine Control Module | Refer to Procedure 019-031 | ISL8.9 CM2880 L112 | 4358493 |
| Engine Control Module | Refer to Procedure 019-031 | QSF3.8 CM2880 F112 | 4383825 |
| Engine Control Module | Refer to Procedure 019-031 | ISB5.9 CM2880 B127 | 4383645 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F116 | 4383664 |
| Engine Control Module | Refer to Procedure 019-031 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Engine Control Module | Refer to Procedure 019-031 | QSL9.3 CM2880 L113 | 4383811 |
| Engine Control Module | Refer to Procedure 019-031 | QSC8.3 CM2880 C102 | 4388785 |
| Engine Control Module | Refer to Procedure 019-031 | QSB5.9 CM2880 B139 | 4388870 |
| Engine Control Module | Refer to Procedure 019-031 | QSB3.9 CM2880 B138 | 5411050 |
| Engine Control Module | Refer to Procedure 019-031 | ISD6.7 CM2880 D101 | 5411372 |
| Engine Control Module | Refer to Procedure 019-031 | ISF2.8 CM2220 F129 | 5411325 |
| Engine Control Module | Refer to Procedure 019-031 | ISF4.5 CM2220 F123 | 5411320 |
| Engine Control Module | Refer to Procedure 019-031 | QSG12 CM2880 G112 | 4388731 |
| Engine Control Module | Refer to Procedure 019-031 | ISF3.8 CM2220 F134B | 5504165 |
| Engine Control Module | Refer to Procedure 019-031 | Z14 CM2670 Z103B | 5504577 |
| Engine Control Module | Refer to Procedure 019-031 | D6.7 CM2670 D102B | 5504515 |
| Engine Control Module | Refer to Procedure 019-031 | B6.2 CM2670 B156B | 5579510 |
| Engine Control Module | Refer to Procedure 019-031 | X12 CM2670 X121B | 5504455 |
| Engine Control Module | Refer to Procedure 019-031 | L9 CM2670 L128B | 5504589 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISL9.5 CM2150 SN | 4310608 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISB3.9 CM2220 B107 | 4310792 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSB4.5 CM2150 B108 | 4326163 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSB7 CM2880 B117 | 4358390 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G106 | 4332695 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G107 | 4332690 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISG11 CM2880 G108 | 4332901 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISG12 CM2880 G109 | 4332906 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSNT14 CM876 N102 | 4325993 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSF2.8 CM2880 F104 | 4332741 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSF2.8 CM2880 F108 | 4332746 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISL8.9 CM2880 L112 | 4358493 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSF3.8 CM2880 F112 | 4383825 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISB5.9 CM2880 B127 | 4383645 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISF3.8 CM2220 F116 | 4383664 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSL9.3 CM2880 L113 | 4383811 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSC8.3 CM2880 C102 | 4388785 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSB5.9 CM2880 B139 | 4388870 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSB3.9 CM2880 B138 | 5411050 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISD6.7 CM2880 D101 | 5411372 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISF2.8 CM2220 F129 | 5411325 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISF4.5 CM2220 F123 | 5411320 |
| Engine Wiring Harness | Refer to Procedure 019-043 | QSG12 CM2880 G112 | 4388731 |
| Engine Wiring Harness | Refer to Procedure 019-043 | ISF3.8 CM2220 F134B | 5504165 |
| Engine Wiring Harness | Refer to Procedure 019-043 | Z14 CM2670 Z103B | 5504577 |
| Engine Wiring Harness | Refer to Procedure 019-043 | D6.7 CM2670 D102B | 5504515 |
| Engine Wiring Harness | Refer to Procedure 019-043 | B6.2 CM2670 B156B | 5579510 |
| Engine Wiring Harness | Refer to Procedure 019-043 | X12 CM2670 X121B | 5504455 |
| Engine Wiring Harness | Refer to Procedure 019-043 | L9 CM2670 L128B | 5504589 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISL9.5 CM2150 SN | 4310608 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISB3.9 CM2220 B107 | 4310792 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB4.5 CM2150 B108 | 4326163 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB6.7 CM2150 B109 | [[4326168 — QSB6.7 CM2150 B109 Service Manual\|4326168]] |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB7 CM2880 B117 | 4358390 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG11 CM2880 G106 | 4332695 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG12 CM2880 G107 | 4332690 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG11 CM2880 G108 | 4332901 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISG12 CM2880 G109 | 4332906 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSNT14 CM876 N102 | 4325993 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSF2.8 CM2880 F104 | 4332741 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSF2.8 CM2880 F108 | 4332746 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISL8.9 CM2880 L112 | 4358493 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSF3.8 CM2880 F112 | 4383825 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISB5.9 CM2880 B127 | 4383645 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF3.8 CM2220 F116 | 4383664 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISB/ISD6.7 CM2880 B126 | 4383693 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSL9.3 CM2880 L113 | 4383811 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSC8.3 CM2880 C102 | 4388785 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB5.9 CM2880 B139 | 4388870 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSB3.9 CM2880 B138 | 5411050 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISD6.7 CM2880 D101 | 5411372 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF2.8 CM2220 F129 | 5411325 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF4.5 CM2220 F123 | 5411320 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | QSG12 CM2880 G112 | 4388731 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | ISF3.8 CM2220 F134B | 5504165 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | Z14 CM2670 Z103B | 5504577 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | D6.7 CM2670 D102B | 5504515 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | B6.2 CM2670 B156B | 5579510 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | X12 CM2670 X121B | 5504455 |
| Intake Manifold Pressure/Temperature Sensor | Refer to Procedure 019-159 | L9 CM2670 L128B | 5504589 |
