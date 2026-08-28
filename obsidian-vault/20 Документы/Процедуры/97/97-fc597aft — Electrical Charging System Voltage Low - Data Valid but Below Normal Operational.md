---
type: "Процедура"
doc: "97-fc597aft"
title_en: "Electrical Charging System Voltage Low - Data Valid but Below Normal Operational Range - Moderately Severe Level"
modified: "2004-10-11"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc597aft.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc597aft.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Electrical Charging System Voltage Low - Data Valid but Below Normal Operational Range - Moderately Severe Level

> [!abstract] Процедура · `97-fc597aft`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-10-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc597aft.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc597aft.pdf)

### Fault Code: 597 (Aftermarket and OEM)

### Electrical Charging System Voltage Low - Data Valid but Below Normal Operational Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 597 PID(P): SPN: FMI: Lamp: SRT: | Electrical Charging System Voltage Low - Data Valid but Below Normal Operational Range - Moderately Severe Level. The ICON™ system has restarted the engine three times within 5 hours because of low battery voltage. | Engine will run continuously. |

![[19803019.png]]

### Circuit Description

The ICON™ idle control module receives unswitched battery input through the ICON™ engine harness. There is one 5-amp in-line fuse in the unswitched battery wire to protect the ICON™ engine harness wire. The battery return wires are connected directly to the negative battery post. The above circuit diagram can vary, such as connector or pins, depending on the vehicle make or model. OEM installations can possibly provide the harnessing between the idle control module and other ICON™ devices.

### Component Location

The ICON™ idle control module is connected directly to the batteries through the ICON™ engine harness. This direct link provides a constant power supply for the ICON™ idle control module. Refer to the OEM manual for the battery location.

The ICON™ module can be located in a different location depending on the vehicle application.

### Shoptalk

This fault typically indicates a problem with the battery, alternator, or too much voltage drop from the alternator to the battery. The unswitched battery supply and return wires **must** be directly connected to the battery for the ICON™ system to function properly. To clear this fault, the ICON™ system needs to function properly for 3 hours or the power needs to be disconnected from the ICON™ idle control module for 5 seconds and then replaced.

The ICON™ system can display **only** the present active fault code. If more than one fault is active at the same time, the ICON™ system flashes out the highest priority fault. After the fault has been corrected then the next active fault will be flashed out.

**Note:** The ICON™ electronic service tool can display more than one active and or inactive fault codes at the same time.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the equipment battery system. |  |
|  | **STEP 1A.** Inspect the battery cable connections. | No damaged, corroded or loose connections |
|  | **STEP 1B.** Monitor the battery voltage. | Less than 0.25 VDC |
|  | **STEP 1C.** Check the charging system. | Alternator output correct |
|  | **STEP 1C-1.** Check the batteries. | Batteries pass check |
| STEP 2. | Clear the fault code. |  |
|  | **STEP 2A.** Disable the fault code. | Fault Code 597 cleared |

### STEP 1. Check the equipment battery system.

#### STEP 1A. Inspect the battery cable connections.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[99-013-009 — Battery Cables and Connections\|013-009]] in the base engine troubleshooting and repair manual. | No damaged, corroded or loose connections | 1B |
| Repair or replace the battery connections. Refer to the OEM troubleshooting and repair manual. | 2A |  |

#### STEP 1B. Monitor the battery voltage.

| **Conditions:** Turn keyswitch ON. Connect the ICON™ electronic service tool Connect a multimeter to the battery pack. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Record the battery voltage on the monitor screen. Record the voltage from the multimeter. Calculate the difference between the electronic service tool reading and the digital volt meter reading. | Less than 0.25 VDC | 1C |
| Repair or replace ICON™ engine harness. Repair the ICON™ engine harness. Refer to Procedure 019-206. Replace the ICON™ engine harness. Refer to Procedure 019-043. Repair or replace the OEM wiring harness as necessary. | 2A |  |

#### STEP 1C. Check the charging system.

| **Conditions:** Start the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage output of the alternator. Refer to Procedure [[97-210-001 — Installation Procedure\|210-001]]. | Alternator output correct | 1C-1 |
| Refer to the OEM to correct the problem. | 2A |  |

#### STEP 1C-1. Check the batteries.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Refer to Procedure [[97-210-001 — Installation Procedure\|210-001]]. | Batteries pass check **NOTE:** The fault can occur due to batteries being discharged prior to ICON™ system engagement. | 2A |
| Refer to OEM service manual to correct the problem. | 2A |  |

### STEP 2. Clear the fault code.

#### STEP 2A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Use the ICON™ electronic service tool to clear the faults. Cycle the keyswitch. Verify the fault code is inactive (it does not flash out on the ICON™ lamp). | Fault Code 597 cleared | Repair complete |
| Troubleshoot any remaining active fault codes. | Appropriate troubleshooting charts |  |
