---
type: "Процедура"
doc: "97-fc338aft"
title_en: "Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc338aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc338aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc338aft.pdf)

### Fault Code: 338 (Aftermarket and OEM)

### Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 338 PID(P): SPN: FMI: Lamp: SRT: | Idle Shutdown Vehicle Accessories Relay Driver Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the ignition bus relay output circuit (ignition relay positive (+)) when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. No power to the keyswitch ignition circuit. |

![[19802960.png]]

### Circuit Description

The ignition bus relay controls ignition circuits powering the heating/air conditioning controls and other equipment connected to the ignition bus relay 1 and ignition bus relay 2. These outputting relays are controlled by the ignition relay positive (+) signal from the ICON™ idle control module B connector pin 4. Some OEM installations will possibly **not** have the second ignition bus relay. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The ignition bus relay is typically located under the dash inside the vehicle cab.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault typically indicates a short circuit from the ICON™ idle control module B connector pin 4 (ignition relay positive (+)) output to battery voltage. Ignition relay positive (+) (pin 4) outputs 12 VDC to open the ignition bus 1 and 2 relays when the ICON™ system has powered the vehicle down and needs to disconnect power going to the cab circuits. The ignition bus 1 and 2 relays are normally closed when no power is applied.

The ICON™ system can display **only** the present active fault code. If more than one fault is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

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
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 338 inactive |
| STEP 2. | Check the ignition bus relay. |  |
|  | **STEP 2A.** Inspect the ignition bus relay connector pins. | No damaged pins |
|  | **STEP 2B.** Check the ignition bus relay coil resistance. | 70 to 100 ohms |
|  | **STEP 2C.** Check for a short circuit in the ignition bus relay. | More than 100k ohms |
| STEP 3. | Check the ICON™ harnesses. |  |
|  | **STEP 3A.** Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins. | No damaged pins |
|  | **STEP 3B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 3B-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 3B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 3C.** Check the complete harness for a short circuit to the battery. | Less than 0.5 VDC |
|  | **STEP 3C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 3C-2.** Check the cab harness for a short circuit to the battery. | Less than 0.5 VDC |
| STEP 4. | Clear the fault code. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 338 cleared |

### STEP 1. Read the fault codes.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the service tool to check the ignition bus relay. Initiate the Ignition Bus Relay Test button with the keyswitch ON and determine if the relay will turn the fans OFF. | Fault Code 338 inactive. Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 4A |
|  | 2A |  |

### STEP 2. Check the ignition bus relay.

#### STEP 2A. Inspect the ignition bus relay(s) pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Replace the relay(s). Flush the dirt, debris, or moisture from the relay pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Replace the ignition bus relay(s). Refer to Procedure 019-301. | 4A |  |

#### STEP 2B. Check the ignition bus relay coil resistance.

| **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 85 to pin 86 of the relay(s). Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | 70 to 100 ohms | 2C |
| Replace the relay(s). Refer to Procedure [[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4A |  |

#### STEP 2C. Check for a short circuit in the ignition bus relay.

| **Conditions:** Turn keyswitch OFF. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 85 of the ignition bus relay(s) to pins 30, 87, and 87A of the relay(s). Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3A |
| Replace the relay(s). Refer to Procedure [[97-019-301 — Ignition Bus Relay 1 and 2\|019-301]]. | 4A |  |

### STEP 3. Check the ICON™ harnesses.

#### STEP 3A. Inspect the ICON™ engine harness, cab harness, and ICON™ idle control module connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect any other connectors for the ICON™ system in order to check the connector pins. Disconnect the cab harness from the ignition bus relay(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair the cab harness. Refer to Procedure 019-211 or 019-207. Replace the cab harness. Refer to Procedure 019-305. Replace the ICON™ idle control module. Refer to Procedure 019-358. Repair or replace the OEM wiring harness as necessary. | 4A |  |

#### STEP 3B. Check the complete harness for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 4 in the ICON™ idle control module B harness connector to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 3C |
|  | 3B-1 |  |

#### STEP 3B-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3B-2 |
| Check the OEM wiring harness pin to pin for a short in the ignition bus relay circuit. | 4A |  |

#### STEP 3B-2. Check the cab harness for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector. Disconnect the ignition bus relay(s) from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin F of the 14-pin cab harness, cab harness side, to all other pins in the connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |

#### STEP 3C. Check the complete harness for a short circuit to the battery.

| **Conditions:** Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 4 of the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
|  | 3C-1 |  |

#### STEP 3C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 3C-2 |
| Check the OEM wiring harness pin to pin for a short to battery in the ignition bus relay circuit. | 4A |  |

#### STEP 3C-2. Check the cab harness for a short circuit to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the 14-pin pass-through connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin F of the 14-pin cab harness, cab harness side, to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 0.5 VDC Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle the keyswitch to verify the fault code is inactive. | Fault Code 338 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
