---
type: "Процедура"
doc: "97-fc588aft"
title_en: "Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source"
modified: "2004-10-07"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc588aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc588aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc588aft.pdf)

### Fault Code: 588 (Aftermarket and OEM)

### Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 588 PID(P): SPN: FMI: Lamp: SRT: | Auto Start Alarm Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the alarm circuit when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine will start normally. |

![[19803013.png]]

### Circuit Description

The alarm circuit turns on the audible alarm to warn of an impending engine start. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The engine start alarm is typically mounted on the vehicle's bulkhead on the intake side of the engine.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault typically indicates a short circuit to battery voltage on pin A of the alarm connector. This fault can cause the alarm to **not** sound. The alarm can sound for 14 seconds before an engine start. The alarm is activated by applying a ground from pin 3 of the ICON™ idle control module B connector to pin A of the alarm connector.

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Perform the alarm test. |  |
|  | **STEP 1A.** Test the ICON™ start alarm. | Alarm sounds |
|  | **STEP 1B.** Check the ICON™ idle control module operation. | Alarm sounds and fault code inactive |
| STEP 2. | Check the engine start alarm. |  |
|  | **STEP 2A.** Inspect the engine start alarm connector pins. | No damaged pins |
|  | **STEP 2A-1.** Inspect the engine harness start alarm connector pins. | No damaged pins |
|  | **STEP 2B.** Check the engine start alarm resistance. | 800 to 1200 ohms |
| STEP 3. | Check the ICON™ engine or OEM harness. |  |
|  | **STEP 3A.** Inspect the ICON™ engine harness and ICON™ idle control module connector pins. | No damaged pins |
|  | **STEP 3B.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 3C.** Check for a short circuit to the battery. | Less than 0.5 VDC |
| STEP 3. | Clear the fault code. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 588 cleared |

### STEP 1. Perform the alarm test.

#### STEP 1A. Test the ICON™ start alarm.

| **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Alarm sounds | 1B |
|  | 2A |  |

#### STEP 1B. Check the ICON™ idle control module operation.

| **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. Start the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Alarm sounds and fault code inactive Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |
| Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |  |

### STEP 2. Check the engine start alarm.

#### STEP 2A. Inspect the engine start alarm connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm connector from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2A-1 |
| Repair the connector pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the connector pins. Refer to Procedure 019-202 or 019-206. | 4A |  |

#### STEP 2A-1. Inspect the engine harness start alarm connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ start alarm from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |

#### STEP 2B. Check the engine start alarm resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine start alarm connector from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A of the engine start alarm connector to pin B of the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 800 to 1200 ohms | 3A |
| Replace the engine start alarm. Refer to Procedure [[97-019-293 — Engine Start Alarm\|019-293]]. | 4A |  |

### STEP 3. Check the ICON™ engine or OEM harness.

#### STEP 3A. Inspect the ICON™ engine harness and ICON™ idle control module connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |

#### STEP 3B. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B harness connectors from the ICON™ idle control module. Disconnect the engine start alarm connector from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 3 of the ICON™ idle control module B harness connector to all pins in the A and B harness connectors. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
| Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |

#### STEP 3C. Check for a short circuit to the battery.

| **Conditions:** Disconnect the engine start alarm connector from the ICON™ engine harness. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 3 of the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. | Less than 0.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
| Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 4A |  |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle the keyswitch to verify the fault code is inactive. | Fault Code 588 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
