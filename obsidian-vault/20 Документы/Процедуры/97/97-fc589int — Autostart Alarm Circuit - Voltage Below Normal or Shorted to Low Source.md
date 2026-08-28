---
type: "Процедура"
doc: "97-fc589int"
title_en: "Autostart Alarm Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2004-09-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc589int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc589int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Autostart Alarm Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc589int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc589int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc589int.pdf)

### Fault Code: 589 (Integrated)

### Autostart Alarm Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 589 PID(P): S121 SPN: 611 FMI: 4/4 Lamp: Yellow SRT: | Autostart Alarm Circuit - Voltage Below Normal or Shorted to Low Source. Less than positive (+) 6 VDC detected at the engine start alarm circuit when high voltage was expected by the engine electronic control module (ECM). | The ICON™ idle control system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. |

![[19803489.png]]

### Circuit Description

The engine start alarm circuit turns on the audible engine start alarm to warn of an impending automatic engine start.

### Component Location

The engine start alarm is located on the vehicle's firewall on the intake side of the engine.

### Shoptalk

This fault typically indicates an open circuit between the alarm coil (pins A and B), or from pin B of the alarm to battery voltage, or from pin A of the alarm to pin 32 of the engine electronic control module (ECM). Another typical cause for this fault code is a short circuit from pin A or B of the alarm, or from engine ECM pin 32 to ground. The alarm **must** sound for 14 seconds before an engine start. The alarm is actuated by supplying a signal from pin 25 of the engine ECM connector to pin B of the alarm connector.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read all fault codes. |  |
|  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp. | Fault Code 589 inactive |
|  | **STEP 1B.** Perform the ICON™ alarm test. | Alarm sounds |
| STEP 2. | Check the engine start alarm. |  |
|  | **STEP 2A.** Inspect the engine start alarm connector for damaged pins. | No damaged pins |
|  | **STEP 2B.** Check the engine start alarm resistance from pin to pin. | More than 800 and less than 1200 ohms |
|  | **STEP 2C.** Check the engine start alarm resistance to engine block ground. | More than 100k ohms |
| STEP 3. | Check the engine wiring harness. |  |
|  | **STEP 3A.** Inspect the engine wiring harness and the engine start alarm connector pins. | No damaged pins |
|  | **STEP 3B.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 3B-1.** Check for a short circuit to ground in the OEM harness. | More than 100k ohms |
|  | **STEP 3C.** Check for an open circuit. | Less than 10 ohms |
|  | **STEP 3C-1.** Check for an open circuit from the alarm connector to the engine ECM actuator connector. | Less than 10 ohms |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 589 inactive |

### STEP 1. Read all fault codes.

#### STEP 1A. Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 589 inactive | 1B |
| Fault Code 589 active | 1B |  |

#### STEP 1B. Perform the ICON™ alarm test.

| **Conditions:** Connect the INSITE™ electronic service tool to the engine. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Perform the ICON™ alarm test using INSITE™ electronic service tool. | Alarm sounds | 4A |
| Alarm does **not** sound | 2A |  |

### STEP 2. Check the engine start alarm.

#### STEP 2A. Inspect the engine start alarm connector for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair or replace the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the engine start alarm connector. Refer to Procedure 019-202 or 019-206. Replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |

#### STEP 2B. Check the engine start alarm resistance from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A (or 1) to pin B (or 2) of the engine start alarm connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 800 and less than 1200 ohms | 2C |
| Replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |

#### STEP 2C. Check the engine start alarm resistance to engine block ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A (or 1) of the engine start alarm connector to engine block ground. Measure the resistance from pin B (or 2) of the engine start alarm connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3A |
| Replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |

### STEP 3. Check the engine wiring harness.

#### STEP 3A. Inspect the engine wiring harness and the engine start alarm connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. Disconnect the actuator harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair or replace the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. Repair or replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |

#### STEP 3B. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. Disconnect the actuator harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 25 of the actuator harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3B-1 |
| Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 4A |  |

#### STEP 3B-1. Check for a short circuit to ground in the OEM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the 31-pin OEM connector. Disconnect the engine start alarm from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 29 of the 31-pin OEM connector, OEM harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
| Does **not** meet specifications Repair or replace the OEM harness. Refer to the OEM service manual. | 4A |  |

#### STEP 3C. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ engine start alarm from the OEM harness. Disconnect the actuator harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 32 of the actuator harness connector to pin A (or 1) of the ICON™ alarm connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 3C-1 |
| Does **not** meet specifications Repair or replace the OEM harness. Refer to the OEM service manual. | 4A |  |

#### STEP 3C-1. Check for an open circuit from the alarm connector to the engine ECM actuator connector.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ engine start alarm from the OEM harness. Disconnect the actuator harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 25 of the actuator harness connector to pin B (or 2) of the ICON™ alarm connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 4A |
| Does **not** meet specifications Repair or replace the OEM harness. Refer to the OEM service manual. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that Fault Code 589 is inactive use INSITE™ electronic service tool. Perform the ICON™ alarm test. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 589 inactive | Repair complete |
| Return to the troubleshooting steps, or contact the local Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
