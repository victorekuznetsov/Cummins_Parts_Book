---
aliases:
  - "Память ЭБУ — неисправности областей"
type: "Процедура"
doc: "94-fc342"
title_en: "Electronic Control Module (ECM) Memory - Area Faults"
title_ru: "Память ЭБУ — неисправности областей"
modified: "2003-03-19"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc342.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc342.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Electronic Control Module (ECM) Memory - Area Faults
**Память ЭБУ — неисправности областей**

> [!abstract] Процедура · `94-fc342`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2003-03-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-fc342.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-fc342.pdf)

### Fault Code: 342 or 346

### Electronic Control Module (ECM) Memory - Area Faults

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 342 or 346 PID(P): SPN: FMI: Lamp: SRT: | FC 342 - The ECM has detected a memory check sum error in the memory containing critical engine parameters. FC 346 - The ECM has detected a memory check sum error in the memory containing non-critical engine parameters. | FC 342 - Engine will shutdown. Common Alarm output is energized. FC 346 - None on performance. Common Warning output is energized. **NOTE:** ECM data may be lost, including fault code data, adjustable parameter settings, ECM time, and engine run time). |

![[19a00014.png]]

### Circuit Description

The QST30 G-Drive ECM is a computer that is responsible for engine control, diagnostics, and engine features.

### Component Location

The QST30 G-Drive ECM is installed by the generator set OEM. It can usually be found mounted near the generator utility panel.

### Shoptalk

This is a fault with the internal memory of the ECM. This fault can be caused by a power interruption to the ECM or a loss of battery power. A partial or master controller reset may be necessary to clear the fault.

## Warnings and Cautions

> [!warning] CAUTION · Осторожно
>

**To avoid pin and harness damage, use the following test leads when taking a measurement: Part No. 3822758 - male Deutsch/Cannon/Metri-Pack test lead.**

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the equipment battery system. |  |
|  | **STEP 1A.** Inspect the battery cable connections. | No damaged connections |
|  | **STEP 1B.** Check the battery voltage. | 17.3 to 34.7 VDC (24 Volt System) |
| STEP 2. | Check the engine harness. |  |
|  | **STEP 2A.** Inspect the engine harness adaptor cable and ECM connector pins. | No damaged pins |
|  | **STEP 2A-1.** Inspect the engine harness and engine harness extension cable(s) connector pins. | No damaged pins |
|  | **STEP 2B.** Check for an open circuit in the unswitched battery supply circuit. | Less than 10 Ohms |
|  | **STEP 2B-1.** Check for an open in the engine harness adaptor cable and any extension cable used. | Less than 10 Ohms |
|  | **STEP 2C.** Check for a short circuit from pin to pin in the unswitched battery supply. | More than 100k ohms |
|  | **STEP 2C-1.** Check for a short circuit from pin to pin in the engine harness adaptor cable and any extension cable used. | More than 100k ohms |
|  | **STEP 2D.** Check the engine harness ground connection. | No damaged connections |
|  | **STEP 2E.** Check for an open circuit in the block ground circuit. | Less than 10 ohms |
|  | **STEP 2E-1.** Check for an open circuit in the block ground circuit in the engine harness adaptor cable and any extension cable used. | Less than 10 ohms |
| STEP 3. | Perform a Controller Reset. |  |
|  | **STEP 3A.** Perform a partial reset on the controller. | Fault Code 342 or 346 inactive |
|  | **STEP 3B.** Perform a master reset on the controller. | Fault Code 342 or 346 inactive |
| STEP 4. | Clear the fault code. |  |
|  | **STEP 4A.** Disable the fault code. | Fault Code 342 or 346 inactive |
|  | **STEP 4B.** Clear any inactive fault codes. | All fault codes cleared |

### STEP 1. Check the equipment battery system.

#### STEP 1A. Inspect the battery cable connections.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| corrosion loose connections. | No damaged connections | 1B |
| **Repair damaged connections** Repair or replace the battery connections. Refer to the OEM Troubleshooting and Repair Manual. | 4A |  |

#### STEP 1B. Check the battery voltage.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the battery voltage. | 17.3 to 34.7 Volts DC (24 Volt System) | 2A |
| **Replace the battery** Refer to OEM Procedures. | 4A |  |

### STEP 2. Check the engine harness.

#### STEP 2A. Inspect the engine harness adaptor cable and the ECM connector pins.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2A-1 |
| **Repair the damaged pins** Repair or replace the engine harness adaptor cable or the ECM, whichever has the damaged pins. Repair the engine harness adaptor cable. Refer to Procedure 019-240 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the ECM. Refer to OEM troubleshooting procedures. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 4A |  |

#### STEP 2A-1. Inspect the engine harness and any engine harness extension cable(s).

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| bent or broken pins pushed back or expanded pins corroded pins moisture in or on the connector. | No damaged pins | 2B |
| **Repair the damaged pins** Repair or replace the engine harness or the engine harness extension cable(s), whichever has the damaged pins. Repair the engine harness or the engine harness extension cable(s). Refer to Procedure 019-240 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness or the engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Dry the connector by using electrical contact cleaner, Part No. 3824510. | 4A |  |

#### STEP 2B. Check for an open circuit in the unswitched battery supply circuit.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the battery. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from pin 38 of the engine harness adaptor cable connector to the positive battery connection on the engine harness measure the resistance from pin 16 thru pin 20 of the engine harness adaptor cable connector to the positive battery connection on the engine harness. | Less than 10 Ohms | 2C |
|  | 2B-1 |  |

#### STEP 2B-1. Check for an open in the engine harness adaptor cable and any extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from any engine harness extension cable(s). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the continuity for pin 38 of the engine harness adaptor cable and any engine harness extension cable(s) used. measure the continuity for pins 16 thru 20 of the engine harness adaptor cable and any engine harness extension cable(s) used. | Less than 10 Ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |
| **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |

#### STEP 2C. Check for a short circuit from pin to pin in the unswitched battery supply.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the battery. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from pin 38 of the engine harness adaptor cable connector to all other pins in the connector except pins 16 thru 20 measure the resistance from pins 16 thru 20 of the engine harness adaptor cable connector to all other pins in the connector except pins 38 and 16 thru 20. | More than 100k ohms | 2D |
|  | 2C-1 |  |

#### STEP 2C-1. Check for a short circuit from pin to pin in the engine harness adaptor cable and any extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from pin 38 of the engine harness adaptor cable connector and any engine harness extension cable connectors to all other pins in the connector except pins 16 thru 20 measure the resistance from pins 16 thru 20 of the engine harness adaptor cable connector and any engine harness extension cable connectors to all other pins in the connector except pins 38 and 16 thru 20. | More than 100k ohms Repair or replace the engine harness Repair the engine harness. Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |
| **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |

#### STEP 2D. Check the engine harness ground connection.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from the battery. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| broken connections corroded connections loose connections excessive paint, oil, or dirt. | No damaged connections | 2E |
| **Repair or replace engine harness** Repair the engine harness. Refer to Procedure 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |

#### STEP 2E. Check for an open circuit in the block ground circuit.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness adaptor cable from the ECM. Disconnect the engine harness from engine block ground. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the resistance from pins 26 thru 30 of the engine harness adaptor cable connector to the engine block ground connection on the engine harness. | Less than 10 ohms | 3A |
|  | 2E-1 |  |

#### STEP 2E-1. Check for an open circuit in the block ground circuit in the engine harness adaptor cable and any extension cable used.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller not in the diagnostic mode. Disconnect the engine harness from the engine harness extension cable(s). Disconnect the engine harness adaptor cable from the ECM. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| measure the continuity for pins 26 thru 30 of the engine harness adaptor cable and any engine harness extension cable(s) used. | Less than 10 ohms Repair or replace engine harness Repair the engine harness. Refer to Procedure 019-197 and 019-240 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness. Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |
| **Repair or replace the engine harness adaptor cable or engine harness extension cable(s), whichever is found faulty** Repair the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedures 019-240 and 019-197 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. Replace the engine harness adaptor cable or engine harness extension cable(s). Refer to Procedure 019-043 in the Troubleshooting and Repair Manual, QST Fuel System QST30 G-Drive Engine Series, Bulletin No. [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual\|3666184]]. | 4A |  |

### STEP 3. Perform a controller reset.

#### STEP 3A. Perform a partial controller reset.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Using INSITE™, Part No. 3825145, pull down the “Tools” menu and select “Controller Partial Reset”. | Fault Code 342 or 346 inactive | 3B |
|  | 3B |  |

#### STEP 3B. Perform a master controller reset.

| **Conditions:** Stop/Run switch in the "STOP" position. Controller in the diagnostic mode. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Using INSITE™, Part No. 3825145, pull down the “Tools” menu and select “Controller Master Reset”. **NOTE:** Performing a master reset on the controller will cause all data (fault code data, parameter settings, ECM time and engine run time) in the ECM to be lost. You must configure all adjustable parameters to their original settings after performing the reset. | Fault Code 342 or 346 inactive | 4A |

### STEP 4. Clear the fault code.

#### STEP 4A. Disable the fault code.

| **Conditions:** Connect all of the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| connect all components start engine and idle for one minute | Fault Code 342 or 346 inactive | 4B |
| Return to troubleshooting steps or contact your local Cummins Authorized Repair Location if all steps have been completed and rechecked. | 1A |  |

#### STEP 4B. Clear any inactive fault codes.

| **Conditions:** Connect all of the components. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Erase inactive fault codes using INSITE™, Part No. 3825145. **NOTE:** The datalink connector is located on the right bank of the flywheel housing. | All faults cleared | Repair complete |
| **Troubleshoot any remaining active fault codes.** | Appropriate troubleshooting chart |  |
