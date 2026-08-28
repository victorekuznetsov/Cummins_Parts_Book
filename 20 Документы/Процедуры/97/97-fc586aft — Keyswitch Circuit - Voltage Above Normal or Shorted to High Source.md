---
type: "Процедура"
doc: "97-fc586aft"
title_en: "Keyswitch Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc586aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc586aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Keyswitch Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `97-fc586aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2007-01-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc586aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc586aft.pdf)

### Fault Code: 586 (Aftermarket and OEM)

### Keyswitch Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 586 PID(P): SPN: FMI: Lamp: SRT: | Keyswitch Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the keyswitch circuit output of the ICON™ idle control module when low voltage was expected by the ICON™ idle control module. | The ICON™ system will be disabled. Mandatory shutdown can also be disabled. Engine can be started normally. Engine will possibly **not** shut down. |

![[19c01536.png]]

### Circuit Description

The keyswitch output circuit provides the keyswitch input signal for the engine control module and starter relay. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The keyswitch signal connects to pin 26 of the actuator connector on the engine harness for CELECT™ Plus engines, and pin 39 for CM870, CM871, CM875, and CM876 electronic control modules (ECMs), and pin 38 of the OEM connector for ISM, ISX, and Signature engines. It also connects to pin 85 of the starter relay. This assumes the keyswitch input voltage from the keyswitch to pin 7 of the ICON™ idle control module A connector is present.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault typically indicates a short circuit or connection to battery voltage. The engine will possibly **not** be able to shut down due to voltage on the ICON™ idle control module keyswitch positive (+) output line (ICON™ idle control module B connector pin 5).

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
|  | **STEP 1A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 586 active |
| STEP 2. | Check for a short in the ICON™ idle control module. |  |
|  | **STEP 2A.** Check the ICON™ idle control module connector pins. | No damaged pins |
|  | **STEP 2B.** Determine if the ICON™ idle control module is operating properly. | Less than 1 VDC detected |
| STEP 3. | Check the ICON™ harnesses. |  |
|  | **STEP 3A.** Inspect the ICON™ engine harness connector pins. | No damaged pins |
|  | **STEP 3B.** Check the complete harness for a short circuit to the battery. | Less than 1 VDC. |
| STEP 4. | Check the keyswitch output circuit. |  |
|  | **STEP 4A.** Check the complete harness for a short to a voltage source. | Less than 1 VDC. |
|  | **STEP 4B.** Check the starter relay circuit for a short to voltage source. | Less than 1 VDC |
|  | **STEP 4C.** Check the engine ECM OEM or actuator harness connector pins. | No damaged pins |
|  | **STEP 4C-1.** Check for a pin to pin short in the ECM engine harness. | More than 100k ohms |
| STEP 5. | Clear the fault code. |  |
|  | **STEP 5A.** Disable the fault code. | Fault Code 586 cleared |

### STEP 1. Read the fault codes.

#### STEP 1A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 586 active. | 2A |
| Refer to Inactive or Intermittent Fault Codes, Procedure [[99-019-362 — Inactive or Intermittent Fault Code\|019-362]]. | 5A |  |

### STEP 2. Check for a short in the ICON™ idle control module.

#### STEP 2A. Check the ICON™ idle control module connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the ICON™ idle control module connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 2B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. | 5A |  |

#### STEP 2B. Determine if the ICON™ idle control module is operating properly.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage at pin 5 of the ICON™ idle control module B connector. Refer to the wiring diagram or the circuit diagram for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC | 3A |
| Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |  |

### STEP 3. Check the ICON™ harnesses.

#### STEP 3A. Inspect the ICON™ engine harness connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the ICON™ engine harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 3B |
| Repair the damaged pins. Flush the dirt, debris, or moisture from the connector pins using electrical contact cleaner, Part Number 3824510. Install the appropriate connector seal if it is damaged or missing. Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |

#### STEP 3B. Check the complete harness for a short circuit to the battery.

| **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage at pin 5 of the ICON™ engine harness B connector to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair complete |
|  | 4A |  |

### STEP 4. Check the keyswitch output circuit.

#### STEP 4A. Check the complete harness for a short to a voltage source.

| **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the engine ECM OEM or actuator harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage at pin 5 of the ICON™ engine harness B connector to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | More than 1 VDC | 4B |
|  | 4C |  |

#### STEP 4B. Check the starter relay circuit for a short to voltage source.

| **Conditions:** Turn keyswitch ON. Disconnect the ICON™ idle control module B connector from the ICON™ idle control module. Disconnect the starter relay. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage from pin 5 of the ICON™ engine harness B connector to engine block ground. Refer to the wiring diagram or the circuit diagram for connector pin identification. For multimeter usage techniques, refer to Multimeter Usage, Procedure [[99-019-359 — Multimeter Usage\|019-359]]. | Less than 1 VDC Replace the starter relay. Refer to Procedure [[97-019-302 — Starter Relay\|019-302]]. | 5A |
| Repair the ICON™ engine harness. Refer to Procedure 019-206 or 019-207. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 5A |  |

#### STEP 4C. Check the engine ECM OEM or actuator harness connector pins

| **Conditions:** Turn keyswitch OFF. Disconnect the engine ECM OEM or actuator harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the ECM engine harness connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris on or in the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. For general inspection techniques, refer to Component Connector and Pin Inspection, Procedure [[99-019-361 — Component Connector and Pin Inspection\|019-361]]. | No damaged pins | 4C-1 |
| Repair or replace the engine ECM engine harness connector. Refer to Procedure [[99-019-203 — AMP Connector Series\|019-203]] or [[99-019-204 — Deutsch DRC Connector Series\|019-204]]. | 5A |  |

#### STEP 4C-1. Check for a pin to pin short in the ECM engine harness.

| **Conditions:** Turn keyswitch OFF. Disconnect the engine harness ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for a pin to pin short. Measure the resistance from pin 38 on the ISM and ISX ECM engine harness connector to all other pins in the ECM engine harness connector. Measure the resistance from pin 26 of the CELECT™ Plus actuator connector to all other pins in the CELECT™ Plus actuator connector. Measure the resistance from pin 39 of the ISM CM870, ISX CM870, ISM CM875, ISX CM871, or ISM CM876 ECM engine harness connector to all other pins in the ECM engine harness connector. Refer to the wiring diagram or the circuit diagram for connector pin identification. For general resistance measurement techniques, refer to the Resistance Measurements Using a Multimeter and Wiring Diagram, Procedure [[99-019-360 — Resistance Measurement Using a Multimeter\|019-360]]. | More than 100k ohms Replace the engine ECM. Refer to one of the following troubleshooting and repair manuals: Procedure 019-031 in CELECT™ Plus, Bulletin 3666130. Procedure 019-031 in Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]]. Procedure 019-031 in Electronic Control System, Signature and ISX, Bulletin 3666259. Procedure 019-031 in Electronic Control System, CM870 ISM, Bulletin 4021381. Procedure 019-031 in Electronic Control System, CM870 Signature and ISX, Bulletin 4021334. Procedure 019-031 in Electronic Control System, CM875 ISM, Bulletin 4021477. Procedure 019-031 in CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. | 5A |
| Repair or replace the engine harness. Refer to one of the following troubleshooting and repair manuals: Procedure 019-043 in CELECT Plus Engines, Bulletin 3666084. Procedure 019-043 in Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]]. Procedure 019-043 in Electronic Control System, Signature and ISX, Bulletin 3666259. Procedure 019-043 in Electronic Control System, CM870 ISM, Bulletin 4021381. Procedure 019-043 in Electronic Control System, CM870 Signature and ISX, Bulletin 4021334. Procedure 019-043 in Electronic Control System, CM875 ISM, Bulletin 4021477. Procedure 019-031 in CM871 and CM876 Electronic Control Systems, ISX and ISM Engines, Bulletin 4021560. | 5A |  |

### STEP 5. Clear the fault code.

#### STEP 5A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Clear the inactive fault code. Cycle the keyswitch to verify the fault code is inactive. | Fault Code 586 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
