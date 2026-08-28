---
type: "Процедура"
doc: "97-fc199int"
title_en: "ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc199int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc199int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `97-fc199int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc199int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc199int.pdf)

### Fault Code: 199 (Integrated)

### ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 199 PID(P): S122, 4 SPN: 612 FMI: 4 Lamp: Yellow SRT: | ICON™ Lamp Circuit - Voltage Below Normal or Shorted to Low Source. Less than 6 VDC (low voltage) detected at the ICON™ lamp circuit when high voltage was expected by the engine electronic control module (ECM). | Will **not** allow ICON™ to activate, however if ICON™ is engaged and fault code 199 becomes active, ICON™ will **not** be disabled. |

![[19803214.png]]

### Circuit Description

The ICON™ lamp circuit illuminates the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ active fault codes will be flashed out on this lamp. The lamp circuit requires a specific flash timing (on or off timing). If the on or off voltage is incorrect, the ICON™ system will be disabled. The lamp circuit **must** be functional to enable the ICON™ system.

### Component Location

The ICON™ lamp is located in the vehicle cab on the dash panel.

### Shoptalk

This fault indicates a short circuit to ground or an open circuit.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read all fault codes. |  |
|  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool, or flash out engine lamp for active fault code. | Fault Code 199 inactive |
| STEP 2. | Check the ICON™ lamp. |  |
|  | **STEP 2A.** Check the bulb for continuity. | Less than 35 ohms |
|  | **STEP 2B.** Check for voltage to the ICON™ lamp. | More than 6 VDC |
| STEP 3. | Check the fuse. |  |
|  | **STEP 3A.** Check the 5-amp ignition fuse. | Fuse installed correctly |
|  | **STEP 3B.** Check if the 5-amp fuse is blown. | Fuse not blown |
| STEP 4. | Check the OEM cab harness connectors at the firewall and the OEM harness engine ECM connector. |  |
|  | **STEP 4A.** Inspect the OEM harness for damaged pins. | No damaged pins |
| STEP 5. | Check the ICON™ lamp circuit for an open or short circuit. |  |
|  | **STEP 5A.** Check the ICON™ lamp for an open circuit. | Less than 10 ohms |
|  | **STEP 5B.** Check for a short circuit. | More than 100k ohms |
|  | **STEP 5C.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 6. | Clear the fault code. |  |
|  | **STEP 6A.** Disable the fault code. | Fault Code 199 inactive |

### STEP 1. Read all fault codes.

#### STEP 1A. Read the fault codes with INSITE™ electronic service tool, or flash out engine lamp for active fault code.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™ electronic service tool, or flash out engine lamp for active fault codes. | Fault Code 199 inactive | 6A |
| Fault Code 199 active | 2A |  |

### STEP 2. Check the ICON™ lamp.

#### STEP 2A. Check the bulb for continuity.

| **Conditions:** Turn keyswitch OFF. Remove the bulb from the holder. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use a multimeter to check the resistance of the bulb. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 35 ohms | 2B |
| Replace the bulb for a 12-VDC system with a General Electric 1892 bulb or equivalent. | 6A |  |

#### STEP 2B. Check for voltage to the ICON™ lamp.

| **Conditions:** Remove the bulb from the holder. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use a multimeter to measure the voltage at the lamp bulb holder keyswitch side (power side) to chassis ground. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | More than 6 VDC | 4A |
| Less than 6 VDC | 3A |  |

### STEP 3. Check the fuse.

#### STEP 3A. Check the 5-amp ignition fuse.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | Fuse installed correctly | 3B |
| Install fuse correctly. Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | 6A |  |

#### STEP 3B. Check if the 5-amp fuse is blown.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | Fuse not blown | 4A |
| Replace the blown fuse. Refer to Procedure [[99-019-198 — Fuse, Harness In-Line\|019-198]]. | 6A |  |

### STEP 4. Check the OEM cab harness connectors at the fire wall and the OEM harness engine ECM connector.

#### STEP 4A. Inspect the OEM harness for damaged pins.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 5A |
| Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |

### STEP 5. Check the ICON™ lamp circuit for an open or short circuit.

#### STEP 5A. Check the ICON™ lamp for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine ECM. Remove the ICON™ lamp bulb from the bulb holder. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 4 of the OEM harness connector at the engine ECM to the return side (engine ECM side) of the ICON™ lamp bulb holder. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 5B |
| Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |

#### STEP 5B. Check for a short circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine ECM. Remove the ICON™ lamp bulb from the bulb holder. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 4 of the OEM harness connector at the engine ECM to ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 5C |
| Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |

#### STEP 5C. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness connector from the engine ECM. Remove the ICON™ lamp bulb from the bulb holder. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 4 of the OEM harness connector at the engine ECM to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 6A |
| Repair or replace the OEM harness. Refer to the OEM service manual. | 6A |  |

### STEP 6. Clear the fault code.

#### STEP 6A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that Fault Code 199 is inactive. Erase the inactive fault codes using INSITE™. | Fault Code 199 inactive | Repair complete |
| Return to the troubleshooting steps, or contact the nearest Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
