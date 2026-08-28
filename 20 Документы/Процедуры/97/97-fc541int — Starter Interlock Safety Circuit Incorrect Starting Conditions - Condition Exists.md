---
type: "Процедура"
doc: "97-fc541int"
title_en: "Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists"
modified: "2004-12-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc541int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc541int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists

> [!abstract] Процедура · `97-fc541int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-12-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc541int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc541int.pdf)

### Fault Code: 541 (Integrated)

### Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 541 PID(P): S123 SPN: 615 FMI: 11/31 Lamp: Yellow SRT: | Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists. Incorrect voltage detected at the ICON™ starter relay input circuit by the engine electronic control module (ECM). | The ICON™ system will be disabled. Mandatory shutdown can still be enabled. Engine can be started normally. |

![[19803483.png]]

### Circuit Description

Incorrect voltage detected at the ICON™ starter relay circuit by the engine ECM.

### Component Location

The ICON™ starter relay is located on the vehicle-side fire wall near the vehicle starter relay.

### Shoptalk

This fault indicates a short circuit to battery ground or an open ICON™ starter relay circuit. All interlock switches **must** be closed and the ICON™ lamp **must** be functional before the ICON™ system can be enabled for the engine to run while the ICON™ system is active. These circuits apply **only** when the ICON™ system is enabled.

**Note:** The parking brake switch is on a separate circuit. The interlock test in this fault code will **not** test the parking brake switch. It will **only** check the hood tilt switch and neutral switch. See to the wiring schematic.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging a new engine ECM, all other active fault codes must be investigated prior to replacing the engine ECM.**

To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read all fault codes. |  |
|  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp. | Fault Code 541 inactive |
|  | **STEP 1B.** Perform the starter relay/interlock test. | Starter relay engages starter |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness and engine ECM connector pins. | No damaged pins |
|  | **STEP 2B.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 2C.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 3C-1.** Check for an open circuit in the ICON™ shorting plug. | Less than 10 ohms |
|  | **STEP 2D.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 2E.** Check for a short circuit to the battery. | Less than positive (+) 1.5 VDC |
| STEP 3. | Check the OEM engine harness. |  |
|  | **STEP 3A.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 3B.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 3C.** Check for a short circuit to the battery. | Less than positive (+) 1.5 VDC |
|  | **STEP 3D.** Check for a short circuit to ground. | More than 100k ohms |
| STEP 4. | Check the ICON™ interlock switches. |  |
|  | **STEP 4A.** Check the hood tilt switch for a short circuit to ground. | More than 100k ohms |
|  | **STEP 4B.** Check the parking brake switch for a short circuit to ground. | More than 100k ohms |
|  | **STEP 4C.** Check the neutral position switch for a short circuit to ground. | More than 100k ohms |
|  | **STEP 4D.** Check the optional OEM interlock switches for a short circuit to ground. | More than 100k ohms |
| STEP 5. | Clear the fault codes. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 541 inactive |

### STEP 1. Read all fault codes.

#### STEP 1A. Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp. | Fault Code 541 inactive | 1B |
| **Fault Code 541 active** | 1B |  |

#### STEP 1B. Perform the starter relay/interlock test.

| **Conditions:** Connect the INSITE™ electronic service tool. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the starter relay or interlock test. Perform the starter relay and interlock test using INSITE™ electronic service tool. **Note:** The parking brake switch is on a separate circuit. The interlock test in this fault code will **not** test the parking brake switch. It will **only** check the hood tilt switch and neutral switch. Refer to the wiring schematic. | Starter relay engages starter | 6A |
| Starter does **not** engage | 2A |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect the engine harness and engine ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine ECM. Disconnect the actuator harness from the engine ECM. Disconnect the 31-pin connector from the OEM harness. Disconnect the sensor harness from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator, sensor harnesses, and engine ECM connector pins for the following: Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair or replace the engine harness or replace the engine ECM, whichever has the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or | 5A |  |

#### STEP 2A. Inspect the engine harness and engine ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine ECM. Disconnect the actuator harness from the engine ECM. Disconnect the 31-pin connector from the OEM harness. Disconnect the sensor harness from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator, sensor harnesses, and engine ECM connector pins for the following: Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair or replace the engine harness or replace the engine ECM, whichever has the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the engine wiring harness. Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 2A. Inspect the engine harness and engine ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine ECM. Disconnect the actuator harness from the engine ECM. Disconnect the 31-pin connector from the OEM harness. Disconnect the sensor harness from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator, sensor harnesses, and engine ECM connector pins for the following: Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair or replace the engine harness or replace the engine ECM, whichever has the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the engine ECM. Refer to Procedure 019-031 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or | 5A |  |

#### STEP 2A. Inspect the engine harness and engine ECM connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the engine ECM. Disconnect the actuator harness from the engine ECM. Disconnect the 31-pin connector from the OEM harness. Disconnect the sensor harness from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the actuator, sensor harnesses, and engine ECM connector pins for the following: Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair or replace the engine harness or replace the engine ECM, whichever has the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the engine ECM. Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 2B. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the 31-pin OEM connector from the OEM harness. Disconnect the actuator harness from the engine ECM. Verify that the ICON™ shorting plug is connected to the 6-pin engine harness connector. Disconnect the sensor harness from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 14 of the actuator harness connector to all other pins in the connector. Measure the resistance from pin 46 of the actuator harness connector to all other pins in the connector. Measure the resistance from pin 16 of the sensor harness connector to all other pins in the connector. For ISM Series engines only, measure the resistance from pin 21 of the sensor harness connector to all other pins in the connector. For Signature/ISX Series engines only, measure the resistance from pin 47 of the actuator harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2C |
| Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 2C. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the 31-pin OEM connector from the OEM harness. Disconnect the actuator harness from the engine ECM. Verify that the ICON™ shorting plug is connected to the 6-pin engine harness connector. Disconnect the sensor harness from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from pin 20 of the 31-pin OEM harness connector, engine harness side, to pin 46 of the actuator harness connector. Measure the resistance from pin 27 of the 31-pin OEM harness connector, engine harness side, to pin 14 of the actuator harness connector. Measure the resistance from pin 31 of the 31-pin OEM harness connector, engine harness side, to pin 16 of the sensor harness connector. For Signature/ISX Series engines only, measure the resistance from pin 24 of the 31-pin OEM harness connector, engine harness side, to pin 47 of the actuator harness connector. For ISM Series engines only, measure the resistance from pin 24 of the 31-pin OEM harness connector, engine harness side, to pin 21 of the sensor harness connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2C-1 |
| Repair or replace the OEM wiring harness. Refer to the OEM service manual. Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 2C-1. Check for an open circuit in the ICON™ shorting plug.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ shorting plug from the 6-pin engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit in the ICON™ shorting plug. Measure the resistance from pin 4 to pin 5 of the ICON™ shorting plug. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2D |
| Replace the shorting plug. | 5A |  |

#### STEP 2D. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the 31-pin OEM connector. Disconnect the actuator harness connector from the engine ECM. Verify that the ICON™ shorting plug is connected to the 6-pin engine harness connector. Disconnect the sensor harness from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from pin 14 of the actuator harness connector to engine block ground. Measure the resistance from pin 46 of the actuator harness connector to engine block ground. Measure the resistance from pin 16 of the sensor harness connector to engine block ground. For ISM Series engines only, measure the resistance from pin 21 of the sensor harness connector to engine block ground. For Signature/ISX Series engines only, measure the resistance from pin 47 of the actuator harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2E |
| Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 2E. Check for a short circuit to the battery.

| **Conditions:** Disconnect the 31-pin OEM connector. Disconnect the actuator harness connector from the engine ECM. Connect the shorting plug to the 6-pin OEM interface harness. Disconnect the sensor harness from the engine ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to the battery. Measure the voltage from pin 14 of the actuator harness connector to engine block ground. Measure the voltage from pin 46 of the actuator harness connector to engine block ground. Measure the voltage from pin 16 of the sensor harness connector to engine block ground. For ISM Series engines only, measure the voltage from pin 21 of the sensor harness connector to engine block ground. For Signature/ISX Series engines only, measure the voltage from pin 47 of the actuator harness to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than positive (+) 1.5 VDC | 3A |
| Repair or replace the engine wiring harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

### STEP 3. Check the OEM engine harness.

#### STEP 3A. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the 31-pin OEM connector from the OEM harness. Disconnect the OEM harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 33 of the OEM harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3B |
| Repair or replace the OEM harness. Refer to the OEM service manual. | 5A |  |

#### STEP 3B. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the 31-pin OEM connector. Disconnect the OEM harness connector from the engine ECM. Make certain that the interlock switches (hood tilt, parking brake, and neutral) are closed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from pin 20 of the 31-pin OEM connector, OEM side, to pin 33 of the 50-pin OEM harness connector. Measure the resistance from pin 27 of the 31-pin OEM connector, OEM side, to pin 33 of the 50-pin OEM harness connector. Measure the resistance from pin 31 to pin 24 on the 31-pin OEM connector, OEM side. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms When measuring pin 27 of the 31-pin connector, 100 ohms or less | 3C |
| Repair or replace the OEM wiring harness. Refer to the OEM service manual. Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 3C. Check for a short circuit to the battery.

| **Conditions:** Disconnect the 31-pin OEM connector. Disconnect the starter relay from the OEM harness. Make certain that all the interlock switches (hood tilt, parking brake, and neutral position) are closed. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to the battery. Measure the voltage from pin 20 of the 31-pin OEM harness connector, OEM harness side, to engine block ground. Measure the voltage from pin 27 of the 31-pin OEM harness connector, OEM harness side, to engine block ground. Measure the voltage from pin 31 of the 31-pin OEM harness connector, OEM harness side, to engine block ground. Measure the voltage from pin 24 of the 31-pin OEM harness connector, OEM side, to engine block ground. Measure the voltage from pin 33 of the 50-pin OEM harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than positive (+) 1.5 VDC | 3D |
| Repair or replace the OEM wiring harness. Refer to the OEM service manual. Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 3D. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine ECM. Disconnect the starter relay from the OEM harness. Make certain that all the interlock switches (hood tilt, parking brake, and neutral position) are closed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from pin 21 of the 50-pin OEM connector to engine block ground. Measure the resistance from pin 16 of the 50-pin OEM connector to engine block ground. Measure the resistance from pin 33 of the 50-pin OEM connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4A |
| Repair or replace the OEM wiring harness. Refer to the OEM service manual. Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

### STEP 4. Check the ICON™ interlock switches.

#### STEP 4A. Check the hood tilt switch for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the hood tilt switch for a short circuit to ground. Measure the resistance from hood tilt switch connector pin A (or 1), switch side of connector, to engine block ground. Measure the resistance from hood tilt switch connector pin B (or 2), switch side of connector, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4B |
| Replace the hood tilt switch. Refer to the OEM troubleshooting and repair manual. | 5A |  |

#### STEP 4B. Check the parking brake switch for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the parking brake switch from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the parking brake switch for a short circuit to ground. Measure the resistance from parking brake switch connector pin A (or 1), switch side of connector, to engine block ground. Measure the resistance from parking brake switch connector pin B (or 2), switch side of connector, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4C |
| Replace the parking brake switch. Refer to the OEM troubleshooting and repair manual. | 5A |  |

#### STEP 4C. Check the neutral position switch for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the neutral position switch from the OEM harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the neutral position switch for a short circuit to ground. Measure the resistance from neutral position switch connector pin A (or 1), switch side of connector, to engine block ground. Measure the resistance from neutral position switch connector pin B (or 2), switch side of connector, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4D |
| Replace the neutral position switch. Refer to the OEM troubleshooting and repair manual. | 5A |  |

#### STEP 4D. Check the optional OEM interlock switches for a short circuit to ground.

| **Conditions:** Disconnect any optional OEM interlock switches from the OEM harness. Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check any optional OEM interlock switches for a short circuit to ground, if applicable. Measure the resistance from OEM optional interlock switch connector pin A (or 1) to engine block ground. Measure the resistance from OEM optional interlock switch connector pin B (or 2) to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 5A |
| Replace the OEM optional interlock switch. Refer to the OEM troubleshooting and repair manual. | 5A |  |

### STEP 5. Clear the fault codes.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disable the fault code. Use INSITE™ to verify that Fault Code 541 is inactive. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 541 inactive | Repair complete |
| Return to the troubleshooting steps, or contact the local Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts. |  |
