---
type: "Процедура"
doc: "97-fc198int"
title_en: "ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc198int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc198int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc198int.pdf)

### Fault Code: 198 (Integrated)

### ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 198 PID(P): S122, 3 SPN: 612 FMI: 3 Lamp: Yellow SRT: | ICON™ Lamp Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the ICON™ lamp circuit when low voltage was expected by the engine electronic control module (ECM). | Will **not** allow ICON™ to activate, however if ICON™ is engaged and fault code 198 becomes active, ICON™ will **not** be disabled. |

![[19803214.png]]

### Circuit Description

The ICON™ lamp circuit illuminates the ICON™ lamp to indicate when the ICON™ system is active. In addition, ICON™ fault codes will be flashed out on this lamp. The lamp circuit requires a specific flash timing (on/off timing). If the on/off voltage is incorrect, the ICON™ system will be disabled. The lamp circuit **must** be functional to enable ICON™.

### Component Location

The ICON™ lamp is located in the vehicle cab on the dash panel.

### Shoptalk

This fault indicates a short circuit to battery voltage. The ICON™ lamp will **only** flash out the active fault codes.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read all fault codes. |  |
|  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool or flash out ICON™ lamp for ICON™ fault codes. | Fault Code 198 inactive |
| STEP 2. | Check the OEM engine wiring harness and engine ECM connector pins. |  |
|  | **STEP 2A.** Inspect the OEM engine wiring harness and engine ECM connector for damaged pins. | No damaged pins |
|  | **STEP 2B.** Check for a short circuit to the battery. | Less than 0.5 VDC |
|  | **STEP 2C.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 3. | Check the ICON™ lamp. |  |
|  | **STEP 3A.** Check the ICON™ lamp connector for damaged pins. | No damaged pins |
| STEP 4. | Clear the fault code. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 198 inactive |

### STEP 1. Read all fault codes.

#### STEP 1A. Read the fault codes with INSITE™ electronic service tool or flash out ICON™ lamp for ICON™ fault codes.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes using INSITE™ electronic service tool or flash out ICON™ lamp. | Fault Code 198 inactive | 4A |
| Fault Code 198 active | 2A |  |

### STEP 2. Check the OEM engine wiring harness and engine ECM connector pins.

#### STEP 2A. Inspect the OEM engine wiring harness and engine ECM connector for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM engine wiring harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair the damaged pins. Flush the dirt, debris, and moisture from the connector pins using the electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. Repair or replace the OEM harness. Refer to the OEM service manual. | 4A |  |

#### STEP 2B. Check for a short circuit to the battery.

| **Conditions:** Disconnect the OEM engine wiring harness connector from the engine ECM. Remove the bulb from the ICON™ lamp holder. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 4 in the OEM engine wiring harness connector at the engine ECM to ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. | Less than 0.5 VDC | 2C |
| Repair or replace the OEM engine wiring harness. Refer to the OEM service manual. | 4A |  |

#### STEP 2C. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM engine wiring harness connector from the engine ECM. Remove the bulb from the ICON™ lamp holder. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 4 in the OEM engine wiring harness connector at the engine ECM to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3A |
| Repair or replace the OEM wiring harness. Refer to the OEM service manual. | 4A |  |

### STEP 3. Check the ICON™ lamp.

#### STEP 3A. Check the ICON™ lamp connector for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ lamp connector from the OEM cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4A |
| Repair the damaged pins Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the lamp connector pins. Refer to Procedures 019-202 or 019-206. | 4A |  |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that Fault Code 198 is inactive. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 198 inactive | Repair complete |
| Return to the troubleshooting steps, or contact the nearest Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
