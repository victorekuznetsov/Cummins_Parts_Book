---
type: "Процедура"
doc: "97-fc199aft"
title_en: "ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2004-09-29"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc199aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc199aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc199aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc199aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc199aft.pdf)

### Fault Code: 199 (Aftermarket and OEM)

### ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 199 PID(P): SPN: FMI: Lamp: SRT: | ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source. Less than 6 VDC (low voltage) detected at the ICON™ lamp or LED circuit when high voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. |

![[19c01467.png]]

### Circuit Description

The ICON™ lamp or LED circuit turns on the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ fault codes will be flashed out on this lamp. The lamp or LED circuit requires a specific flash timing (on or off timing). If the on or off voltage is incorrect, the ICON™ system will be disabled. The lamp or LED circuit **must** be functional to enable the ICON™ system. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ system devices.

### Component Location

The ICON™ lamp is typically located in the vehicle cab on the dash panel.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault indicates an open circuit or a short circuit to ground.

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging a new ICON™ idle control module, all other active fault codes must be investigated prior to replacing the ICON™ idle control module.**

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read the fault codes. |  |
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 199 inactive |
| STEP 2. | Check the ICON™ lamp assembly. |  |
|  | **STEP 2A.** Check the ICON™ lamp assembly for continuity. | Bulb illuminates |
|  | **STEP 2B.** Check the ICON™ lamp assembly for continuity. | Less than 10 ohms |
| STEP 3. | Check the ICON™ lamp. |  |
|  | **STEP 3A.** Check the ICON™ lamp connector for damaged pins. | No damaged pins |
|  | **STEP 3B.** Check the ICON™ lamp for a short circuit to ground. | More than 100k ohms |
| STEP 4. | Check the ICON™ harnesses. |  |
|  | **STEP 4A.** Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins. | No damaged pins |
|  | **STEP 4B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 4B-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 4B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 4C.** Check the complete harness for a short circuit to ground. | More than 100k ohms |
|  | **STEP 4C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 4C-2.** Check the cab harness for a short circuit to ground. | More than 100k ohms |
|  | **STEP 4D.** Check the complete harness for an open circuit. | Less than 10 ohms |
|  | **STEP 4D-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 4D-2.** Check for an open circuit in the cab harness. | Less than 10 ohms |
| STEP 5. | Clear the fault code. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 199 cleared |

### STEP 1. Read the fault codes.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 199 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 5A |
|  | 2A |  |

### STEP 2. Check the ICON™ lamp assembly.

#### STEP 2A. Check the ICON™ lamp assembly for continuity.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure 019-047. | Bulb illuminates | 3A |
|  | 2B |  |

#### STEP 2B. Check the ICON™ lamp assembly for continuity.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ lamp connector from the cab harness. Remove the ICON™ lamp or LED. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A of the harness connector to the lamp socket. Measure the resistance from pin B of the harness connector to the lamp socket. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | Less than 10 ohms Replace the ICON™ lamp or LED. Refer to Procedure [[99-019-046 — Fault Lamp\|019-046]]. | 5A |
| Repair or replace the ICON™ lamp assembly. Refer to the OEM service manual. | 5A |  |

### STEP 3. Check the ICON™ lamp.

#### STEP 3A. Check the ICON™ lamp connector for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the lamp connector pins. Refer to Procedure 019-202 or 019-206. | 5A |  |

#### STEP 3B. Check the ICON™ lamp for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin B of the lamp connector to the engine block ground. Measure the resistance from pin A of the lamp connector to the engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | More than 100k ohms | 4A |
| Repair or replace the ICON™ lamp assembly. Repair the ICON™ lamp assembly. Refer to Procedure 019-202 or 019-206. Replace the ICON™ lamp assembly. Refer to Procedure 019-046. | 5A |  |

### STEP 4. Check the ICON™ harnesses.

#### STEP 4A. Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect any other connectors for the ICON™ system in order to check the connector pins. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair the cab harness. Refer to Procedure 019-200. Replace the cab harness. Refer to Procedure 019-305. Repair or replace the OEM wiring harness as necessary. | 5A |  |

#### STEP 4B. Check the complete harness for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 in the ICON™ idle control module A harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | More than 100k ohms | 4C |
|  | 4B-1 |  |

#### STEP 4B-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 4B-2 |
| Check the OEM wiring harness pin to pin for a short in the lamp output circuit. | 5A |  |

#### STEP 4B-2. Check the cab harness for a short circuit from pin to pin.

| **Conditions:** Disconnect the 14-pin connector. Disconnect the ICON™ lamp or LED. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin J in the 14-pin pass-through connector, cab harness side, to all other pins except pin K in the connector, cab harness side. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 5A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 5A |  |

#### STEP 4C. Check the complete harness for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 of the ICON™ idle control module A harness connector to engine block ground. Measure the resistance from pin 6 of the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | More than 100k ohms | 4D |
|  | 4C-1 |  |

#### STEP 4C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 4C-2 |
| Check the OEM wiring harness for a short to ground in the lamp output circuit. | 5A |  |

#### STEP 4C-2. Check the cab harness for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin connector. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin J in the 14-pin pass-through connector, cab harness side, to engine block ground. Measure the resistance from pin D of the 14-pin pass-through connector, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 5A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 5A |  |

#### STEP 4D. Check the complete harness for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 of the ICON™ idle control module A connector to pin B of the ICON™ lamp harness connector. Measure the resistance from pin 6 of the ICON™ idle control module A connector to pin A of the ICON™ lamp harness connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | Less than 10 ohms Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
|  | 4D-1 |  |

#### STEP 4D-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 4D-2 |
| Check the OEM wiring harness for an open in the lamp output circuit. | 5A |  |

#### STEP 4D-2. Check for an open circuit in the ICON™ cab harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin J of the 14-pin pass-through connector, cab harness side, to pin B of the ICON™ lamp harness connector. Measure the resistance from pin D of the 14-pin pass-through connector, cab harness side, to pin A of the ICON™ lamp harness connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure 019-360. | Less than 10 ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 5A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 5A |  |

### STEP 5. Clear the fault code.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle the keyswitch to verify the fault code is inactive. | Fault Code 199 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
