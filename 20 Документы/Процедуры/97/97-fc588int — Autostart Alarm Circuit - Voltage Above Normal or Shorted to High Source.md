---
type: "Процедура"
doc: "97-fc588int"
title_en: "Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc588int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588int.pdf)

### Fault Code: 588 (Integrated)

### Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 588 PID(P): S121 SPN: 611 FMI: 3/3 Lamp: Yellow SRT: | Autostart Alarm Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the alarm circuit when low voltage was expected by the engine electronic control module (ECM). | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. |

![[19803489.png]]

### Circuit Description

The alarm circuit turns on the audible alarm to warn of an impending engine start.

### Component Location

The ICON™ alarm is mounted on the vehicle's fire wall on the intake side of the engine.

### Shoptalk

This fault typically indicates short circuit to battery or an open circuit. The fan 2 clutch feature is **not** used on ISM. ICON™ engine brake harness is required for Signature/ISX. **Only** 3-position engine brake switch is available for Signature/ISX with ICON™ installed.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read all fault codes. |  |
|  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp. | Fault Code 588 inactive |
|  | **STEP 1B.** Perform the ICON™ alarm test. | Alarm sounds |
| STEP 2. | Check the engine start alarm. |  |
|  | **STEP 2A.** Inspect the engine start alarm connector for damaged pins. | No damaged pins |
|  | **STEP 2B.** Check the engine start alarm resistance from pin to pin. | More than 800 and less than 1200 ohms |
| STEP 3. | Check the engine wiring harness. |  |
|  | **STEP 3A.** Inspect the engine wiring harness and the engine start alarm connector pins. | No damaged pins |
|  | **STEP 3B.** Check for a short circuit to battery voltage. | Less than positive (+) 1.5 VDC |
|  | **STEP 3B-1.** Check for a short circuit to battery voltage in the OEM harness. | Less than positive (+) 1.5 VDC |
| STEP 4. | Clear the fault codes. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 588 inactive |

### STEP 1. Read all fault codes.

#### STEP 1A. Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 588 inactive | 1B |
| Fault Code 588 active | 1B |  |

#### STEP 1B. Perform the ICON™ alarm test.

| **Conditions:** Connect the INSITE™ electronic service tool to the engine. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use INSITE™ to perform the ICON™ alarm test. | Alarm sounds | 4A |
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
| Measure the resistance from pin A (or 1) to pin B (or 2) of the engine start alarm connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 800 and less than 1200 ohms | 3A |
| Replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |

### STEP 3. Check the engine wiring harness.

#### STEP 3A. Inspect the engine wiring harness and the engine start alarm connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm from the engine harness. Disconnect the actuator harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. Repair or replace the engine start alarm. Refer to Procedure 019-293. | 4A |  |

#### STEP 3B. Check for a short circuit to battery voltage.

| **Conditions:** Disconnect the engine start alarm from the engine harness. Disconnect the actuator harness connector from the engine ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 25 of the actuator harness connector to engine block ground. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than positive (+) 1.5 VDC | 3B-1 |
| Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 4A |  |

#### STEP 3B-1. Check for a short circuit to battery voltage in the OEM harness.

| **Conditions:** Disconnect the 31-pin OEM connector. Disconnect the engine start alarm from the engine harness. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 29 of the 31-pin OEM connector, OEM harness side, to engine block ground. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than positive (+) 1.5 VDC | 4A |
| Does **not** meet specifications. Repair or replace the OEM harness. Refer to the OEM service manual. | 4A |  |

### STEP 4. Clear the fault codes.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that Fault Code 588 is inactive using INSITE™ electronic service tool. Perform alarm test with INSITE™ electronic service tool. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 588 inactive | Repair complete |
| Return to the troubleshooting steps, or contact the local Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
