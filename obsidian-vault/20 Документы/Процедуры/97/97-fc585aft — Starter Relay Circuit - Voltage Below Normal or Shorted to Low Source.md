---
type: "Процедура"
doc: "97-fc585aft"
title_en: "Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2007-01-26"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc585aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc585aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc585aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc585aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc585aft.pdf)

### Fault Code: 585 (Aftermarket and OEM)

### Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 585 PID(P): SPN: FMI: Lamp: SRT: | Starter Relay Circuit - Voltage Below Normal or Shorted to Low Source. Less than 6-VDC detected at the starter relay circuit when high voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Can possibly **not** be able to start the engine normally. |

![[19c01537.png]]

### Circuit Description

The starter relay connects power to the starter magnetic switch for starting the engine. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The starter relay is typically mounted on the vehicle's bulkhead on the intake side of the engine.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault typically indicates an open circuit or a short circuit to ground. If there is a short circuit to ground on the starter relay (-) circuit, then the starter will continue to be engaged; otherwise the engine will **not** start.

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read the fault codes. |  |
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 585 inactive |
|  | **STEP 1B.** Check the output and input with the ICON™ electronic service tool. | Verify starter input is blank (not marked), verify starter relay is blank (not marked), verify keyswitch to engine ECM is marked |
| STEP 2. | Starter test. |  |
|  | **STEP 2A.** Run the starter test. | Starter operates properly |
| STEP 3. | Check the starter relay. |  |
|  | **STEP 3A.** Inspect the starter relay pins. | No damaged pins |
|  | **STEP 3B.** Check the starter relay coil resistance. | 30 to 99 ohms |
| STEP 4. | Check the ICON™ harnesses. |  |
|  | **STEP 4A.** Inspect the ICON™ engine harness and ICON™ idle control module connector pins. | No damaged pins |
|  | **STEP 4B.** Check for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 4C.** Check for a short circuit to ground. | More than 100k ohms |
|  | **STEP 4D.** Check for an open circuit. | Less than 100 ohms |
| STEP 5. | Clear the fault code. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 585 cleared |

### STEP 1. Read the fault codes.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the fault flashout feature or the ICON™ electronic service tool read the fault codes. | Fault Code 585 inactive. | 2A |
|  | 1B |  |

#### STEP 1B. Check the output and input with the ICON™ electronic service tool.

| **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter input, starter relay (closed) output, and keyswitch to the engine electronic control module (ECM) output. | Verify starter input is blank (not marked) Verify starter relay is blank (not marked) Verify keyswitch to engine ECM is marked | 3A |
| Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |

### STEP 2. Starter test.

#### STEP 2A. Run starter test.

| **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Run the starter test. | Starter operates properly. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 5A |
|  | 3A |  |

### STEP 3. Check the starter relay.

#### STEP 3A. Inspect the starter relay pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the starter relay from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the starter relay for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Replace the relay Flush the dirt, debris, or moisture from the relay connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the starter relay. Refer to Procedure 019-302. | 5A |  |

#### STEP 3B. Check the starter relay coil resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect the starter relay from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the stater relay coil resistance. Measure the resistance from pin 85 to pin 86 of the starter relay. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 30 to 99 ohms | 4A |
| Replace the starter relay. Refer to Procedure [[97-019-302 — Starter Relay\|019-302]]. | 5A |  |

### STEP 4. Check the ICON™ harnesses.

#### STEP 4A. Inspect the ICON™ engine harness and ICON™ idle control module connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the ICON™ engine harness and ICON™ idle control module connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |

#### STEP 4B. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the OEM electronic control module (ECM) connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit from pin to pin. Measure the resistance from pin 6 in the Aftermarket or OEM ICON™ B harness connector to all other pins in the connectors except pin 5 in the B harness connector. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4C |
| Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |

#### STEP 4C. Check for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a short circuit to ground. Measure the resistance from pin 5 of the Aftermarket or OEM ICON™ B harness connector to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4D |
| Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |

#### STEP 4D. Check for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Make sure the starter relay is installed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open circuit. Measure the resistance from pin 6 of the ICON™ idle control module B harness connector to pin 5 of the connector. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 100 ohms Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | 5A |
| Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | Repair complete |  |

### STEP 5. Clear the fault code.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault code. Cycle the keyswitch to verify the fault code is inactive. | Fault Code 585 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
