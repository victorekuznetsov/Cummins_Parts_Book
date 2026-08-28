---
type: "Сервисный бюллетень"
doc: "5579553"
title_en: "FleetguardFIT™ Filtration Monitoring System Troubleshooting"
released: "2018-11-08"
modified: "2018-11-16"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5579553.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/5579553.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/QSK60"
---

# FleetguardFIT™ Filtration Monitoring System Troubleshooting

> [!abstract] Сервисный бюллетень · `5579553`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** выпущен 2018-11-08 · изменён 2018-11-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/5579553.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/bulletin/5579553.pdf)

## FleetguardFIT™ Filtration Monitoring System Troubleshooting

**Purpose:**

Troubleshooting of FleetguardFIT™ filtration monitoring system.

- FleetguardFIT™ system not working as expected.
- FleetguardFIT™ data not visible on telematics portal.
- FleetguardFIT™ power issue.
- FleetguardFIT™ data incorrect on portal.

This symptom tree can be used to troubleshoot the FleetguardFIT™ filtration monitoring system. Perform the list of troubleshooting steps in the sequence shown.

**Troubleshooting Summary**

| **STEPS** |  |
|---|---|
| STEP 1. Identify telematics portal state |  |
|  | STEP 1A. Check for faulty equipment visibility on telematics portal |
|  | STEP 1B. Check for visibility of other equipment on telematics portal |
| STEP 2. Confirm telematics device operating properly |  |
|  | STEP 2A. Telematics device power |
|  | STEP 2B. Telematics device data communication |
| STEP 3. Identify state of FleetguardFIT™ Filter Monitor System (FMS) LEDs |  |
|  | STEP 3A. LED operation |
|  | STEP 3B. Blue LED steady on |
|  | STEP 3C. Green and red LED flashing |
| STEP 4. Identify state of power supply |  |
|  | STEP 4A. Fuse condition |
|  | STEP 4B. Power supply, ignition, and ground wire condition |
|  | STEP 4C. Power supply, ignition, and chassis ground connections |
|  | STEP 4D. Datalink harness connection to FleetguardFIT™ FMS |
| STEP 5. Equipment J1939 connections |  |
|  | STEP 5A. Inspect equipment and FleetguardFIT™ J1939 connection |
|  | STEP 5B. Inspect equipment and telematics J1939 connection |
|  | STEP 5C. Equipment J1939 public connection |
|  | STEP 5D. Measure equipment resistance |
|  | STEP 5E. Inspect J1939 backbone terminal resistors |
| STEP 6. Identify FleetguardFIT™ FMS compatibility |  |
|  | STEP 6A. Communication baud rate |
| STEP 7. Identify state of FleetguardFIT™ sensor(s) |  |
|  | STEP 7A. Check telematics portal for FleetguardFIT™ oil quality sensor data |
|  | STEP 7B. Oil quality sensor data |
|  | STEP 7C. Check telematics portal for FleetguardFIT™ differential pressure and restriction sensor data |
|  | STEP 7D. differential pressure and restriction sensor data |
| STEP 8. Identify state of FleetguardFIT™ sensor installations |  |
|  | STEP 8A. Oil quality sensor |
|  | STEP 8B. Air restriction sensor |
|  | STEP 8C. differential pressure sensor hardware |
| STEP 9. Identify state of FleetguardFIT™ sensor extension harnesses and FMS |  |
|  | STEP 9A. Sensor breakout harness and extension harness condition |
|  | STEP 9B. Sensor breakout harness and extension harness connection |
|  | STEP 9C. Sensor breakout harness and extension harness continuity |
|  | STEP 9D. FMS module replacement |

STEP 1. Identify telematics portal state.

STEP 1A. Check for faulty equipment visibility on telematics portal.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Log on to telematics portal and check for operation | Is equipment in question visible on portal? **Yes** | **3A** |
| Is equipment in question visible on portal? **No** | **1B** |  |

STEP 1B. Check for visibility of other equipment on telematics portal.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check telematics portal for visibility of other equipment | Is other equipment visible on portal? **YesNote:** Not an issue with portal | **2A** |
| Is other equipment visible on portal? **No** | **Contact:** Telematics service provider support |  |

STEP 2. Confirm telematics device operating properly.

STEP 2A. Telematics device power.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check telematics device power supply | Does the telematics device have power? **YesNote:** Not an issue with telematics device power supply | **2B** |
| Does the telematics device have power? **No** | **Contact:** Telematics service provider support |  |

STEP 2B. Telematics device data communication.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check telematics device for data communication | Is the telematics device sending / receiving data? **YesNote:** Not an issue with telematics device data communication | **3A** |
| Is the telematics device sending / receiving data? **No** | **Contact:** Telematics service provider support **Note:** May be issue with SIM card, data limits, internal device issue, device antenna, cell service, or other |  |

STEP 3. Identify state of FleetguardFIT™ FMS LEDs.

STEP 3A. LED operation.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect FMS module | Are any LEDs on? **YesNote:** FMS is receiving power | **3B** |
| Are any LEDs on? **No** | **4A** |  |

STEP 3B. Blue LED steady on.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect FMS module | Is blue LED steady on? **YesNote:** Ignition power source is wired correctly | **3C** |
| Is blue LED steady on? **NoNote:** Ignition power source needs to be connected or repaired | **4A** |  |

STEP 3C. Green and red LED flashing.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect FMS module | Are green and red LEDs flashing **YesNote:** FMS is sending / receiving data | **5B** |
| Are green and red LEDs flashing **No** | **5A** |  |

STEP 4. Identify state of power supply.

STEP 4A. Fuse condition.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect inline fuses for ignition and power supply | Is fuse open? **YesRepair:** Replace 10 ampere fuse | **Repair Complete** |
| Is fuse open? **No** | **4B** |  |

STEP 4B. Power supply, ignition, and ground wire condition.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Carefully inspect datalink harness | Are power supply, ignition, and ground wires in good condition with no damage, i.e. no tears? **Yes** | **4C** |
| Are power supply, ignition, and chassis ground wires in good condition with no damage? **NoRepair:** Replace or replace datalink harness | **Repair Complete** |  |

STEP 4C. Power supply, ignition, and chassis ground connections.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Carefully inspect datalink harness | Are power supply, ignition, and ground wires connected? **Yes** | **4D** |
| Are power supply, ignition, and chassis ground wires connected? **NoRepair:** Connect wire(s) that are not connected | **Repair Complete** |  |

STEP 4D. Datalink harness connection to FleetguardFIT™ FMS.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect datalink harness connection to FMS module | Is the datalink harness connected securely to FMS module? **Yes** | **5A** |
| Is the datalink harness connected securely to FMS module? **NoRepair:** Connect datalink harness to FMS module | **Repair Complete** |  |

STEP 5. Equipment J1939 connections.

STEP 5A. Inspect equipment and FleetguardFIT™ J1939 connection.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect FleetguardFIT™ J1939 connection with equipment | Is FleetguardFIT™ properly connected to equipment's J1939 public data connection? **Yes** | **5B** |
| Is FleetguardFIT™ properly connected to equipment's J1939 public data connection? **NoRepair:** Connect FleetguardFIT™ properly to J1939 public datalink | **Repair Complete** |  |

STEP 5B. Inspect equipment and telematics J1939 connection.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect telematics J1939 connection with equipment | Is telematics device properly connected to equipment's J1939 public data connection? **Note:** FleetguardFIT™ FMS and telematics should be on different nodes of the datalink backbone **Yes** | **5C** |
| Is telematics device properly connected to equipment's J1939 public data connection? **NoRepair:** Connect telematics properly to J1939 public datalink | **Repair Complete** |  |

STEP 5C. Equipment J1939 public connection.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure continuity from 9-pin service connector to 3-pin Deutsch connector **Note:** Needs to be completed for FleetguardFIT™ and telematics J1939 connections | Was continuity confirmed? **Yes** | **5D** |
| Was continuity confirmed? **NoRepair:** Locate different public J1939 public connection or repair wiring if 3 pin is known to be a public J1939 connection | **Repeat Step** |  |

STEP 5D. Measure equipment resistance.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the J1939 connection; using the equipment J1939 3 pin or 9 Pin service connector measure the equipment resistance | Is the measured resistance 55-65 Ohms? **Yes** | **6A** |
| Is the measured resistance 55-65 Ohms? **No** | **5E** |  |

STEP 5E. Inspect J1939 backbone terminal resistors.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect J1939 connection terminal resistors; measure resistance Note: ONLY two 120 Ohms resistors needed in parallel on backbone to achieve a total resistance of 60 Ohms | Is the measured resistance in each resistor 120 Ohms? **Yes** | **6A** |
| Is the measured resistance in each resistor 120 Ohms? **NoRepair:** Discard and replace resistor(s) | **Repair Complete** |  |

STEP 6. Identify FleetguardFIT™ FMS compatibility.

STEP 6A. Communication baud rate.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine engine, Telematics Service Provider(TSP), and FleetguardFIT™ FMS baud rate **Note:** FleetguardFIT™ FMS modules options are 250 kbps and 500 kbps | Do engine, TSP, and FleetguardFIT™ FMS baud rates match? **Yes** | **7A** |
| Do engine, TSP, and FleetguardFIT™ FMS baud rates match? **NoRepair:** Replace with proper FleetguardFIT™ FMS module | **Repair Complete** |  |

STEP 7. Identify state of FleetguardFIT™ sensor(s).

STEP 7A. Check telematics portal for FleetguardFIT™ oil quality sensor data.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Log on to telematics portal and check for FleetguardFIT™ oil quality sensor data | Is any oil quality sensor data visible on portal? **Yes** | **7B** |
| Is any oil quality sensor data visible on portal? **No** | **9A** |  |

STEP 7B. Oil quality sensor data.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Log on to telematics portal and check for FleetguardFIT™ oil quality sensor data | Is oil quality sensor data within expected ranges? **Yes** | **7C** |
| Is oil quality sensor data within expected ranges? **No** | **8A** |  |

STEP 7C. Check telematics portal for FleetguardFIT™ differential pressure and restriction sensor data.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Log on to telematics portal and check for FleetguardFIT™ differential pressure and restriction sensor data | Is any differential pressure and restriction sensor data visible on portal? **Yes** | **7D** |
| Is any differential pressure and restriction sensor data visible on portal? **No** | **9A** |  |

STEP 7D. differential pressure and restriction sensor data.

| **Conditions:** While equipment is on |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Log on to telematics portal and check for FleetguardFIT™ differential pressure and restriction sensor data | Is differential pressure and restriction sensor data within expected ranges? **Yes** | **Repair Complete** |
| Is differential pressure and restriction sensor data within expected ranges? **No** | **8B** |  |

STEP 8. Identify state of FleetguardFIT™ sensor installations.

STEP 8A. Oil quality sensor.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect oil quality sensor installation | Is the sensor tip located in an area with hot pressurized flowing oil and no leaks? **Yes** | **9A** |
| Is the sensor tip located in an area with hot pressurized flowing oil and no leaks? **NoRepair:** Relocate oil quality sensor according to FleetguardFIT™ instructions | **Repair Complete** |  |

STEP 8B. Air restriction sensor.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect air restriction sensor installation | Is the sensor visibly in good condition and connected to air intake system with no leaks? **Yes** | **8C** |
| Is the sensor visibly in good condition and connected to air intake system with no leaks? **NoRepair:** Replace restriction sensor | **Repair Complete** |  |

STEP 8C. differential pressure sensor(s).

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect differential pressure sensor installation | Is the sensor properly connected to an inlet and outlet port of the filter head with no leaks? **Yes** | **9A** |
| Is the sensor properly connected to an inlet and outlet port of the filter head with no leaks? **NoRepair:** Properly connect differential pressure sensor to inlet/outlet ports of the filter head. Replace hardware if needed. | **Repair Complete** |  |

STEP 9. Identify state of FleetguardFIT™ sensor extension harnesses and FMS.

STEP 9A. Sensor breakout harness and extension harness condition.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Carefully inspect sensor breakout harness and extension harness | Are electrical harnesses in good condition with no damage, i.e. no tears? **Yes** | **9B** |
| Are electrical harnesses in good condition with no damage, i.e. no tears? **NoRepair:** Replace or repair harness | **Repair Complete** |  |

STEP 9B. Sensor breakout harness and extension harness connection.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Carefully inspect sensor breakout harness and extension harness | Are electrical harnesses connected properly to FMS, breakout harness, and each sensor? **Yes** | **9C** |
| Are electrical harnesses connected properly to FMS, breakout harness, and each sensor? **NoRepair:** Connect wire(s) that are not connected | **Repair Complete** |  |

STEP 9C. Sensor breakout harness and extension harness continuity.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure continuity from end to end for breakout harness and each extension harness | Was continuity confirmed? **YesRepair:** Replace sensor | **9D** |
| Was continuity confirmed? **NoRepair:** Fix or replace harnesses | **Repair complete** |  |

STEP 9D. FMS module replacement.

| **Conditions:** While equipment is off |  |  |
|---|---|---|
| **Specification/Repair** | **Action** | **Next Step** |
| Is data available and within expected ranges? **Yes** | Log on to telematics portal and check faulty equipment for FleetguardFIT™ data | **Repair Complete** |
| Is data available and within expected ranges? **NoRepair:** Replace FMS module | **Contact:FIT.Support@cummins.com** |  |

### Document History
