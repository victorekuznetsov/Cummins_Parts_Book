---
type: "Процедура"
doc: "97-fc766aft"
title_en: "Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2004-10-15"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc766aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc766aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc766aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc766aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc766aft.pdf)

### Fault Code: 766 (Aftermarket and OEM)

### Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 766 PID(P): SPN: FMI: Lamp: SRT: | Starter Interlock Safety Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the interlock/lamp output positive (+) circuit when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. |

![[19803824.png]]

### Circuit Description

The interlock and lamp output circuit provides power to the ICON™ lamp and to the interlock switches. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The ICON™ lamp is typically located in the vehicle cab on the dash panel. The parking brake switch is typically located behind the dash on the parking brake air line. The hood tilt switch is typically located on the hood behind the left headlight housing. The neutral position switch is located on the top cover plate of the transmission near the gear shift.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault indicates a short circuit to battery voltage. This circuit outputs a pulse width modulated (PWM) voltage at pin 5 of the ICON™ idle control module A connector

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read the fault codes. |  |
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 766 active |
| STEP 2. | Check the ICON™ idle control module. |  |
|  | **STEP 2A.** Check the ICON™ idle control module A connector for damaged pins. | No damaged pins |
|  | **STEP 2B.** Check the hood tilt switch for a short circuit to the battery. | Less than 1 VDC |
|  | **STEP 2C.** Check the ICON™ system for a short to the battery. | Less than 1 VDC |
| STEP 3. | Identify the ICON™ system. |  |
|  | **STEP 3A.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
| STEP 4. | Check the ICON™ engine harness. |  |
|  | **STEP 4A.** Inspect the ICON™ engine harness 14-pin connector pins. | No damaged pins |
|  | **STEP 4B.** Check the ICON™ engine harness for a short to the battery. | Less than 1 VDC |
| STEP 5. | Check the ICON™ cab harness. |  |
|  | **STEP 5A.** Inspect the ICON™ cab harness 14-pin connector pins. | No damaged pins |
|  | **STEP 5B.** Check the ICON™ cab harness for a short to the battery. | Less than 1 VDC |
|  | **STEP 5C.** Check the ICON™ lamp for a short to the battery. | Less than 1 VDC |
|  | **STEP 5D.** Check the parking brake switch for a short circuit to the battery. | Less than 1 VDC |
| STEP 6. | Check the neutral position switch. |  |
|  | **STEP 6A.** Check the neutral position switch for a short circuit to the battery. | Less than 1 VDC |
| STEP 7. | Clear the fault code. |  |
|  | **STEP 7A.** Disable the fault code. | Fault Code 766 cleared |

### STEP 1. Read the fault codes.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 766 active. | 2A |
| Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 7A |  |

### STEP 2. Check the ICON™ idle control module.

#### STEP 2A. Check the ICON™ idle control module A connector for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B harness connectors from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |

#### STEP 2B. Check the hood tilt switch for a short circuit to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the ICON™ hood tilt switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin B of the ICON™ tilt switch connector to engine block ground. Measure the voltage from pin A of the ICON™ tilt switch connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 2C |
| Replace the hood tilt switch. Refer to Procedure [[97-019-298 — Hood Tilt Switch\|019-298]]. | 7A |  |

#### STEP 2C. Check the ICON™ system for a short to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Set the parking brake. Put the vehicle in neutral. Close or bypass the hood tilt switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 5 in the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
|  | 3A |  |

### STEP 3. Identify the ICON™ system.

#### STEP 3A. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 4A |
| Check the OEM wiring harness for a short circuit to battery in the lamp output circuit. | 7A |  |

### STEP 4. Check the ICON™ engine harness.

#### STEP 4A. Inspect the ICON™ engine harness 14-pin connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 7A |  |

#### STEP 4B. Check the ICON™ engine harness for a short to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module A and B harness connectors from the ICON™ idle control module. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 5 in the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 5A |
| Replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness\|019-043]]. | 7A |  |

### STEP 5. Check the ICON™ cab harness.

#### STEP 5A. Inspect the ICON™ cab harness 14-pin connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 5B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 7A |  |

#### STEP 5B. Check the ICON™ cab harness for a short to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. Set the parking brake. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin J in the cab harness 14 pin pass-through connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 6A |
|  | 5C |  |

#### STEP 5C. Check the ICON™ lamp for a short to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin B of the ICON™ lamp connector to engine block ground. Measure the voltage from pin A of the ICON™ lamp connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 5D |
| Replace the ICON™ lamp. Refer to Procedure [[99-019-046 — Fault Lamp\|019-046]]. | 7A |  |

#### STEP 5D. Check the parking brake switch for a short circuit to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the parking brake switch connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin B of the ICON™ parking brake switch connector to engine block ground. Measure the voltage from pin A of the ICON™ parking brake switch connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the cab harness. Refer to Procedure [[97-019-305 — Cab Wiring Harness\|019-305]]. | 7A |
| Replace the parking brake switch. Refer to Procedure [[97-019-299 — Parking Brake Switch\|019-299]]. | 7A |  |

### STEP 6. Check the neutral position switch.

#### STEP 6A. Check the neutral position switch for a short circuit to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the neutral position switch connector from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin B of the neutral position switch connector to engine block ground. Measure the voltage from pin A of the neutral position switch connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the ICON™ engine harness. Refer to Procedure [[97-019-043 — Engine Wiring Harness\|019-043]]. | 7A |
| Replace the neutral position switch. Refer to Procedure [[97-019-297 — Neutral Position Switch\|019-297]]. | 7A |  |

### STEP 7. Clear the fault code.

#### STEP 7A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle the keyswitch, start the engine, and drive the vehicle for 1 minute at more than 10 mph to verify the fault code is inactive. | Fault Code 766 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
