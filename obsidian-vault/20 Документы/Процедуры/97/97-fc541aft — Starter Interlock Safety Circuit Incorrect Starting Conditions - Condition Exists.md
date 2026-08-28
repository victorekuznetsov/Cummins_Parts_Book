---
type: "Процедура"
doc: "97-fc541aft"
title_en: "Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc541aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc541aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists

> [!abstract] Процедура · `97-fc541aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc541aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc541aft.pdf)

### Fault Code: 541 (Aftermarket and OEM)

### Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 541 PID(P): SPN: FMI: Lamp: SRT: | Starter Interlock Safety Circuit Incorrect Starting Conditions - Condition Exists. Signal **not** detected on the interlock input circuit when expected by the ICON™ idle control module while the ICON™ system is active, or the ICON™ system detected vehicle speed while parking brake switch is closed. | The ICON™ system will be disabled. Mandatory shutdown can still be enabled. Engine can be started normally. |

![[19803824.png]]

### Circuit Description

The interlock input circuit provides input to the ICON™ idle control module to determine the state of the interlock safety switches. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The ICON™ lamp is typically located in the vehicle cab on the dash panel. The parking brake switch or optional trailer brake switch is typically located behind the dash on the parking brake air line. The hood tilt switch is typically located on the hood behind the headlight housing. The neutral position switch is located on the top cover plate of the transmission near the gear shift. The ICON™ module can be located in a different location depending on the vehicle application. The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault indicates a short circuit to battery, an interlock switch was opened while the ICON™ system was active, or vehicle speed was greater than 0 mph while the parking brake switch was closed. All interlock switches **must** be closed and the ICON™ lamp functional before the ICON™ system can be enabled, or for the engine to run while the ICON™ system is active. These circuits apply **only** when the ICON™ system is enabled.

Question the driver to determine if the ICON™ system has been deactivating due to excessive engine vibration (engine being started or shutting down by the ICON™ system).

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Interview the driver. |  |
|  | **STEP 1A.** Interview the driver to determine any scenarios that could have caused a fault. | No qualifying events occurred |
| STEP 2. | Check the electronic control module (ECM) for calibration phase. |  |
|  | **STEP 2A.** Verify ECM calibration. | Calibration later than 9.3 on ISM and Signature/ISX/QSX15; Calibration 4.2 on CELECT™ Plus |
|  | **STEP 2B.** Check for active faults. | Fault Code 541 active |
| STEP 3. | Enable the ICON™ system. |  |
|  | **STEP 3A.** Verify the ICON™ system can be enabled. | ICON™ system can be enabled |
|  | **STEP 3B.** Monitor interlock switches. | Parking brake input changes status |
|  | **STEP 3C.** Verify transition of neutral switch. | Interlock (neutral and hood tilt) input changes status |
| STEP 4. | Check the neutral position switch. |  |
|  | **STEP 4A.** Check the neutral position switch for damaged pins. | No damaged pins |
|  | **STEP 4B.** Check for continuity in the neutral position switch circuit. | Less than 10 ohms |
|  | **STEP 4C.** Verify the neutral switch is working properly. | In Gear: more than 100k ohms; In Neutral: less than 10 ohms |
| STEP 5. | Check the hood tilt switch. |  |
|  | **STEP 5A.** Check the hood tilt switch for damaged pins. | No damaged pins |
|  | **STEP 5B.** Check for an open circuit in the hood tilt switch circuit. | Less than 10 ohms |
|  | **STEP 5B-1.** Check the continuity of the hood tilt switch to the ICON™ module. | Less than 10 ohms |
|  | **STEP 5B-2.** Verify the hood tilt switch is working properly. | Hood open, 100k ohms; hood closed, less than 10 ohms |
| STEP 6. | Check the parking brake switch. |  |
|  | **STEP 6A.** Check the parking brake switch connectors for damaged pins. | No damaged pins |
|  | **STEP 6B.** Check the installation of the parking brake switch in the parking brake line. | Installation is correct |
|  | **STEP 6C.** Check for an open circuit in the parking brake circuit. | Less than 10 ohms |
|  | **STEP 6D.** Check for an open circuit in the parking brake switch circuit. | Less than 10 ohms |
|  | **STEP 6E.** Verify the parking brake switch is working properly. | Parking brake switch disengaged, more than 100k ohms; parking brake switch engaged, less than 10 ohms |
| STEP 7. | Clear the fault code. |  |
|  | **STEP 7A.** Disable the fault code. | Fault Code 541 cleared |

### STEP 1. Interview the driver.

#### STEP 1A. Interview the driver to determine any scenarios that could have caused a fault.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Was the vehicle placed in gear? Was the parking brake released? Was the hood opened or left open? When did fault occur? | No qualifying events occurred | 2A |
| Correct the problem. | 8A |  |

### STEP 2. Check the electronic control module (ECM) for calibration phase.

#### STEP 2A. Verify ECM calibration.

| **Conditions:** Connect INSITE™ electronic service tool. Turn keyswitch on. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ECM calibration phase in monitor mode. | Calibration later than 9.3 on ISM and Signature/ISX/QSX15 Calibration 4.2 on CELECT™ Plus | 2B |
| Download latest ESDN calibration | 7A |  |

#### STEP 2B. Check for active faults.

| **Conditions:** Turn keyswitch OFF. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Read fault codes with the ICON™ electronic service tool or flash out the faults with the ICON™ lamp. Verify the ICON™ lamp flashes three times when keyswitch is turned on (lamp is not burned out). | Fault Code 541 active | 3A |
|  | Appropriate troubleshooting charts |  |

### STEP 3. Enable the ICON™ system.

#### STEP 3A. Verify the ICON™ system can be enabled.

| **Conditions:** Enabled ICON™ system. Connect ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Enable the ICON™ system and perform at least one autostart with cab thermostat or load batteries to less than 12.3 VDC. | ICON™ system can be enabled Clear the fault codes. | 7A |
| ICON™ system can **not** be enabled | 3B |  |

#### STEP 3B. Monitor interlock switches.

| **Conditions:** Engine running. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Parking brake input changes status. | 3C |
| ICON™ idle control module inputs are **not** active | 6A |  |

#### STEP 3C. Verify transition of neutral switch.

| **Conditions:** Turn the keyswitch OFF. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Move gear shift from in-gear to out-of-gear. Verify interlock (neutral and hood tilt) in monitor screen status changes from checked to unchecked. | Interlock (neutral and hood tilt) input changes status Note: Fault Code 541 can possibly have been caused by a momentary opening of the switch due to possible vibration. | 7A |
|  | 4A |  |

### STEP 4. Check the neutral position switch.

#### STEP 4A. Check the neutral position switch for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the neutral position switch connector from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4B |
| Repair the damaged pins, Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the neutral position switch connector pins. Refer to Procedure 019-202 or 019-206. | 7A |  |

#### STEP 4B. Check for continuity in the neutral position switch circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Set the parking brake. Close the hood. Vehicle in neutral. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin B of the neutral position switch connector to pin 2 of the ICON™ idle control module B connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 4C |
| Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |

#### STEP 4C. Verify the neutral switch is working properly.

| **Conditions:** Turn keyswitch OFF. Disconnect the neutral position switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance across the switch with the vehicle in gear and then back in neutral. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | In Gear: more than 100k ohms In Neutral: less than 10 ohms | 5A |
| Replace the neutral position switch. Refer to Procedure [[97-019-297 — Neutral Position Switch\|019-297]]. | 7A |  |

### STEP 5. Check the hood tilt switch.

#### STEP 5A. Check the hood tilt switch for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch connector from the ICON™ engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 5B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the hood tilt switch connector pins. Refer to Procedure 019-202 or 019-206. | 7A |  |

#### STEP 5B. Check for an open circuit in the hood tilt switch circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch connector from the ICON™ engine harness. Set the parking brake. Disconnect the neutral switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin B of the hood tilt switch harness connector to pin A of the neutral position switch connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 5B-1 |
| Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |

#### STEP 5B-1. Check the continuity of the hood tilt switch to the ICON™ Module.

| **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch. Disconnect the ICON™ idle control module connector A. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 5B-2 |
| Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |

#### STEP 5B-2. Verify the hood tilt switch is working properly.

| **Conditions:** Turn keyswitch OFF. Disconnect the hood tilt switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance across the hood tilt switch with the hood open and then with the hood closed. **Note:** The switch **must** close and open when the hood is tilted to an approximately 45 ± 15 degree angle. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Hood open: more than 100k ohms Hood closed: less than 10 ohms Note: Minor adjustment to the switch can possibly be needed to make sure the close or open angle is at 45 degrees. Disconnecting and reconnecting the connector has corrected the problem. | 7A |
| Replace the hood tilt switch or make minor adjustments so the switch will close or open properly and recheck. Refer to Procedure [[97-019-298 — Hood Tilt Switch\|019-298]]. | 7A |  |

### STEP 6. Check the parking brake switch.

#### STEP 6A. Check the parking brake switch connectors for damaged pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the parking brake switch from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 6B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the parking brake switch connector pins. Refer to Procedure 019-202 or 019-206. | 7A |  |

#### STEP 6B. Check the installation of the parking brake switch in the parking brake line.

| **Conditions:** Turn keyswitch OFF. Disconnect the parking brake switch connector from the cab harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify that connections are tight and there are no leaks from the line and vehicle air pressure is greater than 83 kPa \[12 psi\] ± 21 kPa \[3 psi\] with the parking brake engaged. | Installation is correct | 6C |
| Install the parking brake switch. Refer to Procedure [[97-019-299 — Parking Brake Switch\|019-299]]. | 7A |  |

#### STEP 6C. Check for an open circuit in the parking brake switch circuit.

| **Conditions:** Turn the keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Set the parking brake. Disconnect the parking brake switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 5 of the ICON™ idle control module A harness connector to pin B of the parking brake switch connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 6D |
| Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |

#### STEP 6D. Check for an open circuit in the parking brake switch circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the parking brake switch. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin A of the parking brake switch harness connector to pin 2 of the ICON™ idle control module B harness connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 6E |
| Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-202 or 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 7A |  |

#### STEP 6E. Verify the parking brake switch is working properly.

| **Conditions:** Engine running. Vehicle in neutral or park. Chock wheels. Disconnect parking brake switch. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance across the parking brake switch with the parking brake engaged and disengaged. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Parking brake switch disengaged: more than 100k ohms Parking brake switch engaged: less than 10 ohms Disconnecting and connecting fixes the problem. | 7A |
| Replace the parking brake switch. Refer to Procedure [[97-019-299 — Parking Brake Switch\|019-299]]. | 7A |  |

### STEP 7. Clear the fault code.

#### STEP 7A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 541 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
