---
type: "Процедура"
doc: "97-fc414aft"
title_en: "SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc414aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc414aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate

> [!abstract] Процедура · `97-fc414aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc414aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc414aft.pdf)

### Fault Code: 414 (Aftermarket and OEM)

### SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 414 PID(P): SPN: FMI: Lamp: SRT: | SAE J1587/J1922 Datalink Circuit - Abnormal Update Rate. J1587 datalink information was **not** received by the ICON™ idle control module within the specified time. | The ICON™ system will be disabled. Engine will start normally. |

![[19802968.png]]

### Circuit Description

The J1587 datalink provides communication between the engine ECM and the ICON™ idle control module. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The J1587 datalink is located in the OEM wiring harness. The ICON™ idle control module typically connects into the J1587 wiring harness behind the in-cab datalink service connector. The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault is set when information that is required by the ICON™ idle control module is **not** received from the engine ECM on the J1587 datalink. It typically indicates an open circuit on the J1587 datalink. Check the engine ECM for active faults and troubleshoot those first.

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**NOTE:** A problem can exist with the vehicle wiring for the J1708 datalink.

**NOTE:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of damaging a new ICON™ idle control module, all other active fault codes must be investigated prior to replacing the ICON™ idle control module.**

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Confirm the fault status. |  |
|  | **STEP 1A.** Check the engine ICON™ idle control module for active fault codes. | Datalink operating properly |
| STEP 2. | Check the ICON™ engine harness. |  |
|  | **STEP 2A.** Inspect the ICON™ engine harness and ICON™ idle control module connector pins. | No damaged pins |
|  | **STEP 2B.** Check the complete harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 2B-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 2B-2.** Check the cab harness for a short circuit from pin to pin. | More than 100k ohms |
|  | **STEP 2C.** Check the complete harness for a short circuit to the battery. | Pin 7: 2.5 to 5.0 VDC; Pin 8: 0.0 to 2.5 VDC |
|  | **STEP 2C-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 2C-2.** Check the engine harness for a short circuit to the battery. | Less than 1 VDC |
|  | **STEP 2D.** Check the complete harness for a short circuit to ground. | More than 100k ohms |
|  | **STEP 2D-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 2D-2.** Check the engine harness for a short circuit to ground. | More than 100k ohms |
|  | **STEP 2E.** Check the complete harness for an open circuit. | Less than 10 ohms |
|  | **STEP 2E-1.** Identify whether the ICON™ system is an Aftermarket or an OEM. | ICON™ system is Aftermarket |
|  | **STEP 2E-3.** Check the engine harness for an open circuit. | Less than 10 ohms |
|  | **STEP 2F.** Check for an open circuit in the engine ECM harness. | Less than 10 ohms |
| STEP 3. | Check the J1587 device. |  |
|  | **STEP 3A.** Check for a malfunctioning J1587 datalink device. | Positive wire to chassis ground (J1587 only): 2.5 to 5.0 VDC, negative wire to chassis ground (J1587 only): 0.0 to 2.5 VDC |
| STEP 4. | Clear the fault code. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 414 cleared |

### STEP 1. Confirm the fault status.

#### STEP 1A. Check the engine ICON™ idle control module for active fault codes.

| **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Initiate the Datalink Test button with the service tool to determine if the datalink is operating properly. | Datalink operating properly Refer to Inactive or Intermittent Fault Code, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]] | 4A |
|  | 2A |  |

### STEP 2. Check the ICON™ engine harness.

#### STEP 2A. Inspect the ICON™ engine harness and ICON™ idle control module connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corroded pins Bent or broken pins Pushed back or expanded pins Wire insulation damage Moisture in or on the connector Missing or damaged connector seals Connector shell broken Dirt or debris in or on the connector pins. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair the damaged pins Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Replace the ICON™ idle control module. Refer to Procedure 019-358. Repair or replace the OEM wiring harness as necessary. | 4A |  |

#### STEP 2B. Check the complete harness for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to all other pins in the A and B harness connectors, except pin 8 in the B harness connector. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to all other pins in the A and B harness connectors, except pin 7 in the B harness connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2C |
|  | 2B-1 |  |

#### STEP 2B-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2B-2 |
| Check the OEM wiring harness pin to pin for a short in the datalink circuit. | 4A |  |

#### STEP 2B-2. Check the cab harness for a short circuit from pin to pin.

| **Conditions:** Turn keyswitch OFF. Disconnect the 14-pin pass-through connector. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin G of the 14-pin cab harness, cab harness side, to all other pins in the connector except pin H. Measure the resistance from pin H of the 14-pin cab harness, cab harness side, to all other pins in the connector except pin G. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |
| Repair or replace the ICON™ cab harness Repair the cab harness. Refer to Procedure 019-207. Replace the cab harness. Refer to Procedure 019-305. | 4A |  |

#### STEP 2C. Check the complete harness for a short circuit to the battery.

| **Conditions:** Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the voltage from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Pin 7: 2.5 to 5.0 VDC Pin 8: 0.0 to 2.5 VDC | 2D |
|  | 2C-1 |  |

#### STEP 2C-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2C-2 |
| Check the OEM wiring harness a short to battery in the datalink circuit. | 4A |  |

#### STEP 2C-2. Check the engine harness for a short circuit to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the 14-pin connector. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the voltage from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For multimeter usage techniques, refer to Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Troubleshoot per Procedure 019-166 or the OEM troubleshooting procedure. | 4A |
| Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |  |

#### STEP 2D. Check the complete harness for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the engine ECM OEM connector (containing the datalink output wire). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms | 2E |
|  | 2D-1 |  |

#### STEP 2D-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2D-2 |
| Check the OEM wiring harness short to ground in the datalink circuit. | 4A |  |

#### STEP 2D-2. Check the engine harness for a short circuit to ground.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the 14-pin pass-through connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to engine block ground. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to engine block ground. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Troubleshoot per Procedure 019-166 or the OEM troubleshooting procedure. | 4A |
| Repair or replace the ICON™ engine harness Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |  |

#### STEP 2E. Check the complete harness for an open circuit.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to positive (+) pin A of the J1587 datalink connector (for the 6-pin Deutsch connector), or pin F (for the 9-pin Deutsch connector). Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to negative (-) pin B of the J1587 datalink connector (for the 6-pin Deutsch connector), or pin G (for the 9-pin Deutsch connector). **NOTE:** The above-mentioned datalink positive and negative connections are typical for the 6-pin and 9-pin Deutsch connectors. Refer to the OEM manual for the appropriate datalink positive and negative pin numbers if your vehicle is configured differently. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 2F |
|  | 2E-1 |  |

#### STEP 2E-1. Identify whether the ICON™ system is an Aftermarket or an OEM.

| **Conditions:** None |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | ICON™ system is Aftermarket | 2E-2 |
| Check the OEM wiring harness for an open in the datalink circuit. | 4A |  |

#### STEP 2E-2. Check for an open circuit in the engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module A and B connectors from the ICON™ idle control module. Disconnect the 14-pin pass-through connector at the vehicle bulkhead. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 7 in the ICON™ idle control module B harness connector to pin G of the cab harness connector, engine harness side. Measure the resistance from pin 8 in the ICON™ idle control module B harness connector to pin H of the cab harness connector, engine harness side. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms Troubleshoot per Procedure 019-166 or the OEM troubleshooting procedure. | 4A |
| Repair or replace the ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. | 4A |  |

#### STEP 2F. Check for an open circuit in the engine ECM harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the ECM OEM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance from pin 27 on a CELECT™ Plus ECM OEM connector and pin A of the 6-pin or pin F of the 9-pin connector. Measure the resistance from pin 8 on a CELECT™ Plus ECM OEM connector and pin B of the 6-pin or pin G of the 9-pin connector. Measure the resistance from pin 26 on an ISM or ISX ECM OEM connector and pin A of the 6-pin or pin F of the 9-pin connector. Measure the resistance from pin 27 on an ISM or ISX ECM OEM connector and pin B of the 6-pin or pin G of the 9-pin connector. Measure the resistance from pin 10 on an ISM CM870, ISM CM875, or ISX CM870 ECM OEM connector and pin A of the 6-pin or pin F of the 9-pin connector. Measure the resistance from pin 20 on an ISM CM870, ISM CM875, or ISX CM870 ECM OEM connector and pin B of the 6-pin or pin G of the 9-pin connector. Refer to the wiring diagram or the circuit description at the beginning of this fault code for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | Less than 10 ohms | 3A |
| Repair or replace the OEM harness. Refer to the OEM troubleshooting manual. | 4A |  |

### STEP 3. Check the J1587 device.

#### STEP 3A. Check for a malfunctioning J1587 datalink device.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| **NOTE:** This device can be an automatic transmission, automatic braking system, or electronic dash. Locate the power fuse for the J1587 device(s). Pull out the fuses one at a time. As the fuse is pulled from the fuse-holder, measure the voltage from positive (+) pin A of the J1587 datalink connector, cab side (for the 6-pin Deutsch connector), or pin F (for the 9-pin Deutsch connector) to chassis ground. As the fuse is pulled from the fuse-holder, measure the voltage from negative (-) pin B of the J1587 datalink connector, cab side (for the 6-pin Deutsch connector), or pin G (for the 9-pin Deutsch connector) to chassis ground. **NOTE:** The J1587 device that typically will cause a problem is an electronic dash. The above-mentioned datalink positive and negative connections are typical for the 6-pin and 9-pin Deutsch connectors. Refer to the OEM manual for the appropriate datalink positive and negative pin numbers if your vehicle is configured differently. | Positive wire to chassis ground (J1587 only): 2.5 to 5.0 VDC Negative wire to chassis ground (J1587 only): 0.0 to 2.5 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |
| Datalink device is nonstandard or defective Repair or replace as necessary. Refer to the OEM troubleshooting manual. | 4A |  |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle the keyswitch to verify the fault code is inactive. | Fault Code 414 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
