---
type: "Процедура"
doc: "97-fc338int"
title_en: "Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source

> [!abstract] Процедура · `97-fc338int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338int.pdf)

### Fault Code: 338 (Integrated)

### Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 338 PID(P): S087, 3 SPN: 1267 FMI: 3 Lamp: Yellow SRT: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shortedd to High Source. High voltage detected at the ignition bus relay output circuit, ignition relay positive (+), when low voltage was expected by the ICON™ system. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. No power to the keyswitch ignition circuit. |

![[19803215.png]]

### Circuit Description

The ignition bus relay controls ignition circuits powering the heating/air conditioning controls and other equipment connected to the ignition bus relay(s) (optional second relay can be installed for additional accessories). This relay(s) is controlled by ignition relay positive (+) signal from the engine electronic control module (ECM) OEM 50-pin connector pin 35.

### Component Location

The ignition bus relay is located under the dash inside the vehicle cab.

### Shoptalk

This fault typically indicates a short circuit from the ignition relay positive (+) output of battery voltage. Ignition relay positive (+) pin outputs 12 VDC to open the ignition bus relay(s) when the ICON™ system has powered the vehicle down and needs to disconnect power going to the cab circuits. The ignition bus relay(s) is normally closed when no power is applied.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging a new engine ECM, all other active fault codes must be investigated prior to replacing the engine ECM. To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read all fault codes. |  |
|  | **STEP 1A.** Read fault codes with INSITE™ electronic service tool or flash out with ICON™ lamp. | Fault Code 338 inactive |
| STEP 2. | Perform the ignition bus relay test with INSITE™ electronic service tool. |  |
|  | **STEP 2A.** Perform the ignition bus relay test with INSITE™ electronic service tool. | Dashboard blowers turn off |
| STEP 3. | Inspect the OEM harness bulkhead connector, OEM engine harness ECM connector. |  |
|  | **STEP 3A.** Inspect the OEM engine harness connector pins. | No damaged pins |
|  | **STEP 3B.** Check for a short circuit from pin to pin. | More than 100k ohms |
| STEP 4. | Check the ignition bus relay. |  |
|  | **STEP 4A.** Check the ignition bus relay connector pins. | No damaged pins |
|  | **STEP 4B.** Check the ignition bus relay coil resistance. | Refer to the OEM troubleshooting and repair manual for specifications |
|  | **STEP 4C.** Check for a short circuit to the battery at ignition bus relay. | Less than 1.5 VDC |
| STEP 5. | Clear the fault code. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 338 inactive; Dashboard blowers turned off |

### STEP 1. Read all fault codes.

#### STEP 1A. Read fault codes with INSITE™ electronic service tool or flash out with ICON™ lamp.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read the fault codes with INSITE™ electronic service tool or flash out ICON™ lamp. | Fault Code 338 inactive | 2A |
| Fault Code 338 active | 2A |  |

### STEP 2. Perform the ignition bus relay test with INSITE™ electronic service tool.

#### STEP 2A. Perform the ignition bus relay test with INSITE™ electronic service tool.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure 019-305. | Dashboard/blowers turn off | 5A |
| Dashboard/blowers do **not** turn off | 3A |  |

### STEP 3. Inspect the OEM harness bulkhead connector, OEM engine harness ECM connector.

#### STEP 3A. Inspect the OEM engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness at the bulkhead. Disconnect the OEM harness to the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4A |
| Repair the damaged pins. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the OEM wiring harness. Refer to the OEM service manual. Replace the engine ECM. Refer to Procedure 019-031 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 3B. Check for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the OEM harness. Disconnect the OEM harness connector from the engine ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 35 of the OEM harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 4A |
| Repair or replace the OEM wiring harness. Refer to the OEM service manual. | 5A |  |

### STEP 4. Check the ignition bus relay.

#### STEP 4A. Check the ignition bus relay connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ignition bus relay. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
| Repair the damaged pins, replace ignition bus relay. Flush the dirt, debris, and moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair or replace the OEM wiring harness. Refer to the OEM service manual. Replace the engine ECM. Refer to Procedure 019-031 in Troubleshooting and Repair Manual, CELECT™ Plus, Bulletin 3666130, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 5A |  |

#### STEP 4B. Check the ignition bus relay coil resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect the OEM harness from the ignition bus relay. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 85 of the ignition relay coil to pin 86. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Refer to the OEM troubleshooting and repair manual for specifications | 4C |
| Replace the ignition bus relay. Refer to the OEM troubleshooting and repair manual. | 5A |  |

#### STEP 4C. Check for a short circuit to the battery at ignition bus relay.

| **Conditions:** Disconnect the ignition bus relay(s) from the OEM harness. Connect the OEM harness to the engine ECM. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 85 of the ignition bus relay(s) to pins 30, 87, and 87A of the relay(s). Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 5A |
| Refer to the OEM service manual. | 5A |  |

### STEP 5. Clear the fault code.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify Fault Code 338 is inactive using INSITE™ electronic service tool. Perform ignition bus relay test using INSITE™ electronic service tool. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 338 inactive; Dashboard blowers turned off | Repair complete |
| Return to the troubleshooting steps, or contact the nearest Cummins Authorized Repair Location if all the steps have been completed and rechecked. Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
