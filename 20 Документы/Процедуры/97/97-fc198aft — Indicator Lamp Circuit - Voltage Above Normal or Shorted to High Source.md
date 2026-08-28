---
type: "Процедура"
doc: "97-fc198aft"
title_en: "Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2004-10-04"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc198aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198aft.pdf)

### Fault Code: 198 (Aftermarket and OEM)

### Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 198 PID(P): SPN: FMI: Lamp: SRT: | Indicator Lamp Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the ICON™ lamp or LED circuit when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. |

![[19802947.png]]

### Circuit Description

The ICON™ lamp or LED circuit turns on the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ fault codes will be flashed out on this lamp. The lamp or LED circuit requires a specific flash timing (on/off timing). If the on/off voltage is incorrect, the ICON™ system will be disabled. The lamp or LED circuit **must** be functional to enable the ICON™ system. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The ICON™ lamp or LED is typically located in the vehicle cab on the dash panel.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault indicates a short circuit to battery voltage.

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
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 198 inactive |
| STEP 2. | Check the ICON™ lamp. |  |
|  | **STEP 2A.** Check the ICON™ lamp connector for damaged pins. | No damaged pins |
|  | **STEP 2B.** Check for a short circuit to battery. | Less than 0.5 VDC |
| STEP 3. | Check the ICON™ harnesses. |  |
|  | **STEP 3A.** Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins. | No damaged pins |
|  | **STEP 3B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 3B-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 3B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 3C.** Check the complete harness for a short circuit to the battery. | Less than 0.5 VDC |
|  | **STEP 3C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 3C-2.** Check the cab harness for a short circuit to the battery. | Less than 0.5 VDC |
| STEP 4. | Clear the fault code. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 198 cleared |

### STEP 1. Read the fault codes.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 198 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |
|  | 2A |  |

### STEP 2. Check the ICON™ lamp.

#### STEP 2A. Check the ICON™ lamp connector for damaged pins.

| **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool to confirm the fault status. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the lamp connector pins. Refer to Procedures 019-202 or 019-206. Repair or replace the OEM wiring harness as necessary. | 4A |  |

#### STEP 2B. Check for a short circuit to battery.

| **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool to confirm the fault status. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin A of the ICON™ lamp connector pins to engine block ground. Measure the voltage from pin B of the ICON™ lamp connector pins to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC | 3A |
| Repair or replace the ICON™ lamp assembly. Refer to Procedure [[99-019-046 — Fault Lamp\|019-046]]. | 4A |  |

### STEP 3. Check the ICON™ harnesses.

#### STEP 3A. Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect all connectors between the lamp and ICON™ module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. Repair or replace the OEM wiring harness as necessary. | 4A |  |

#### STEP 3B. Check the complete harness for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the ICON™ lamp connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 in the ICON™ idle control module A harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
|  | 3B-1 |  |

#### STEP 3B-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3B-2 |
| Check the OEM wiring harness pin to pin for a short in the lamp output circuit. | 4A |  |

#### STEP 3B-2. Check the cab harness for a short circuit from pin to pin.

| **Conditions:** Disconnect the 14-pin connector. Disconnect the ICON™ lamp or LED. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin J in the 14-pin pass-through connector, cab harness side, to all other pins except pin K in the connector, cab harness side. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |

#### STEP 3C. Check the complete harness for a short circuit to the battery.

| **Conditions:** Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. NOTE: All other components must be connected. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 5 of the ICON™ idle control module A harness connector to engine block ground. Measure the voltage from pin 6 of the ICON™ idle control module A harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
|  | 3C-1 |  |

#### STEP 3C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3C-2 |
| Check the OEM wiring harness for a short circuit to battery in the lamp output circuit. | 4A |  |

#### STEP 3C-2. Check the cab harness for a short circuit to the battery.

| **Conditions:** Disconnect the 14-pin connector. NOTE: All other components must be connected. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin J in the 14-pin pass-through connector, cab harness side, to engine block ground. Measure the voltage from pin D in the 14-pin pass-through connector, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle the keyswitch to verify the fault code is inactive. | Fault Code 198 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
