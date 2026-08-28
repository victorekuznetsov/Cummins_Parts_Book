---
type: "Процедура"
doc: "97-fc441aft"
title_en: "Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc441aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc441aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level

> [!abstract] Процедура · `97-fc441aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc441aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc441aft.pdf)

### Fault Code: 441 (Aftermarket and OEM)

### Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 441 PID(P): SPN: FMI: Lamp: SRT: | Battery Number One Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level. Battery voltage below normal operating level. | The ICON™ system will be disabled. **Only** mandatory shutdown will be enabled. Engine will start normally. |

![[19803819.png]]

### Circuit Description

The ICON™ idle control module receives unswitched battery input through the ICON™ engine harness. There is one 5-amp in-line fuse in the unswitched battery wire to protect the ICON™ engine harness wire. The battery return wires are connected directly to the negative (-) battery post. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The ICON™ idle control module is connected directly to the batteries through the ICON™ engine harness. This direct link provides a constant power supply for the ICON™ idle control module. Refer to the OEM manual for the battery location. The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

The unswitched battery supply and return wires **must** be directly connected to the battery for the ICON™ system to function properly. During the ICON™ system start, this fault can be logged during engine cranking if there is a faulty ground connection.

This fault will be logged if the battery voltage falls below 9 VDC on a 12 VDC system. This is equivalent to a very low battery voltage on the engine electronic control module (ECM).

Perform a battery charging system test as described in Procedure [[97-210-001 — Installation Procedure|210-001]], Installation Guidelines, to verify the battery will have adequate voltage for the ICON™ system to function properly.

The ICON™ system can display **only** the present active fault code. If more than one fault code is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test lead when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the batteries and charging system. |  |
|  | **STEP 1A.** Check the batteries and alternator. | No damaged connections |
| STEP 2. | Check the fault status. |  |
|  | **STEP 2A.** Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes. | Fault Code 441 inactive |
| STEP 3. | Clear the fault code. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 441 cleared |

### STEP 1. Check the batteries and charging system.

#### STEP 1A. Check the batteries and alternator.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| For M11 engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin 3666139. For N14 engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin 3666142. For ISM engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]]. For Signature and ISX engines, refer to Procedure 013-001, Procedure 013-007, and Procedure 013-009 in the base engine Troubleshooting and Repair Manual, Bulletin [[3666239 — Signature™, ISX, and QSX15 Service Manual\|3666239]]. | More than 12 VDC | 2A |
| Troubleshoot any other fault codes. | 3A |  |

### STEP 2. Check the fault status.

#### STEP 2A. Use the fault flashout feature or the ICON™ electronic service tool to read the fault codes.

| **Conditions:** Connect all components. Turn keyswitch ON. Connect the ICON™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 441 inactive | 3A |
| Fault Code 441 active Replace the ICON™ idle control module. Refer to Procedure [[97-019-358 — ICON™ Idle Control Module\|019-358]]. | Repair Complete |  |

### STEP 3. Clear the fault code.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Cycle the keyswitch to verify the fault code is inactive. | Fault Code 441 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
