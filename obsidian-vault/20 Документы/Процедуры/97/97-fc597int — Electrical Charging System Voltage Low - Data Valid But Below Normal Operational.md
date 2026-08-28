---
type: "Процедура"
doc: "97-fc597int"
title_en: "Electrical Charging System Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc597int.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc597int.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Electrical Charging System Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level

> [!abstract] Процедура · `97-fc597int`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2004-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-fc597int.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-fc597int.pdf)

### Fault Code: 597 (Integrated)

### Electrical Charging System Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 597 PID(P): P167 SPN: 67 FMI: 1/18 Lamp: Yellow SRT: | Electrical Charging System Voltage Low - Data Valid But Below Normal Operational Range - Moderately Severe Level. The ICON™ system has restarted the engine three times in 7 hours due to low battery voltage. | The engine will run continuously. The ICON™ system will **not** be disabled. Accessories will **not** be on. |

![[19803221.png]]

### Circuit Description

The engine electronic control module (ECM) receives unswitched battery input through the OEM harness. There are two in-line 15-amp fuses in the unswitched battery wire of the OEM harness to protect the engine harness from overheating. The battery return wires are connected directly to the negative (-) battery post.

### Component Location

The engine ECM is connected to the battery by the OEM harness. This direct link provides a constant power supply for the engine ECM. The location of the battery will vary with the OEM. Refer to the OEM troubleshooting and repair manual for the battery location.

### Shoptalk

Make certain that the engine ECM unswitched battery supply is coming directly from the battery and **not** the starter.

The following are possible causes of this fault:

- Undercharged batteries caused by a faulty alternator or regulator

- High-current devices on the vehicle such as refrigerators, citizens band radio amplifiers, numerous exterior lights, or other accessories.

## Warnings and Cautions

> [!danger] WARNING · Опасно
>

**Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.**

> [!warning] CAUTION · Осторожно
>

**To reduce the possibility of pin and harness damage, use the following test leads when taking a measurement: Part Number 3822758 - male Deutsch/AMP/Metri-Pack test lead Part Number 3822917 - female Deutsch/AMP/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Read all fault codes. |  |
|  | **STEP 1A.** Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp. | Fault Code 597 inactive |
| STEP 2. | Check the equipment battery charging system. |  |
|  | **STEP 2A.** Inspect the battery and alternator cable connections. | Connections clean and tight |
|  | **STEP 2B.** Monitor the battery voltage. | Less than 0.2 VDC |
|  | **STEP 2C.** Check the charging system. | See Procedure 209-017 |
| STEP 3. | Clear the fault codes. |  |
|  | **STEP 3A.** Disable the fault code. | Fault Code 597 inactive |

### STEP 1. Read all fault codes.

#### STEP 1A. Read the fault codes with INSITE™ electronic service tool or flash out with the ICON™ lamp.

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
|  | Fault Code 597 inactive | 3A |
| Fault Code 597 active | 3A |  |

### STEP 2. Check the equipment battery charging system.

#### STEP 2A. Inspect the battery and alternator cable connections.

| **Conditions:** Turn keyswitch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Corrosion Loose connections. | Connections clean and tight | 2B |
| Repair the damaged connections Tighten the battery and alternator connections, and clean the terminals, refer to the OEM troubleshooting and repair manual. | 3A |  |

#### STEP 2B. Monitor the battery voltage

| **Conditions:** Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Connect the INSITE™ electronic service tool Record the battery voltage on the monitor screen Connect a digital volt meter to the battery pack Record the voltage Calculate the difference between the INSITE™ electronic service tool reading and the digital volt meter reading. | Less than 0.25 VDC | 2C |
| Repair or replace the engine harness. Refer to Procedure 019-043 in Troubleshooting and Repair Manual, CELECT Plus Engines, Bulletin 3666084, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, ISM, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], or Procedure 019-031 in Troubleshooting and Repair Manual, Electronic Control System, Signature and ISX, Bulletin 3666259, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 ISM, Bulletin 4021381, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM870 Signature and ISX, Bulletin 4021334, or Procedure 019-043 in Troubleshooting and Repair Manual, Electronic Control System, CM875 ISM, Bulletin 4021477. | 3A |  |

#### STEP 2C. Check the charging system.

| **Conditions:** Start the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage output of the alternator. **Note:** Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | Refer to Procedure [[97-209-017 — ICON™ Idle Control System\|209-017]]. | 3A |
| Refer to the OEM to correct the problem. | 3A |  |

### STEP 3. Clear the fault codes.

#### STEP 3A. Disable the fault code.

| **Conditions:** Connect all components. Turn keyswitch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Start the engine, and let it idle. Verify that Fault Code 597 is inactive using INSITE™ electronic service tool. Erase the inactive fault codes using INSITE™ electronic service tool. | Fault Code 597 inactive | Repair complete |
| Return to the troubleshooting steps, or contact the local Cummins Authorized Repair Location if all the steps have been completed and rechecked. | Appropriate troubleshooting charts |  |
