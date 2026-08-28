---
aliases:
  - "Останов: выключатель контроля клапана отсечки топлива"
type: "Процедура"
doc: "330-t02-1008"
title_en: "Sd FSOV POC Sw"
title_ru: "Останов: выключатель контроля клапана отсечки топлива"
modified: "2024-08-13"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4358403"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1008.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1008.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/330"
---

# Sd FSOV POC Sw
**Останов: выключатель контроля клапана отсечки топлива**

> [!abstract] Процедура · `330-t02-1008`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4358403 — Dual Fuel Technology DF101 Master Repair Manual|4358403]]
> **Секции:** Section TA - Troubleshooting Alarm Codes
> **Даты:** изменён 2024-08-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/330/330-t02-1008.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/330-t02-1008.pdf)

Printable Version

### Symptoms

Dual fuel operation will be prevented. All gas flow will stop if system is operating in dual fuel mode.

### How To Use This Tree

This tree can be used to troubleshoot a malfunction. Step 1 describes the variant of pump control panel. This step will determine which step to start diagnostics.

**Circuit Description:**

Shutdown condition indicates the commanded position of the dual shutoff solenoid and actual positions of the proof of closure switch are **not** in the required positions.

**Conditions for Running the Diagnostics:**

Anytime the control module is powered ON.

**Conditions for Activating the Fault Message:**

Dual fuel control module is powered on and the proof of closure switch (feedback) signal is **not** in the correct position, the system will indicate this message and protection.

**Conditions for Clearing the Fault Codes Automatically:**

None.

**Conditions for Clearing the Fault Codes Manually:**

Fault reset is operated locally or via software.

For NewCtrl (see below), if the error message is inactive, it does **not** mean problem was solved. System will stop gas and state of BI4 and BOUT14 are in correct order (see table BOUT/BIN combination), but once you will try to run on gas error message will appear again.

### Shoptalk

| **Table of BOUT/BIN combination** |  |  |
|---|---|---|
| **BOUT14** | **BIN4** | **Error message** |
| 0 | 0 | FSOV POC Sw |
| 0 | 1 | No message |
| 1 | 0 | No message |
| 1 | 1 | FSOV POC Sw |

The fault condition indicates the dual shutoff solenoid failed to open or close when commanded by the dual fuel control module.

If the gas train harness connector is unplugged, the control will always be in the fault condition (also if the wire is cut, switch is broken, or the valve is mechanically stuck, frozen, or binding).

Because the timing and response are evaluated when the valve is commanded to open, the fault can be difficult to track without the use of WinScope data-logging software.

If steps are exhausted and failure is **not** identified, it is useful to use the WinScope PC tool to data log the responses during normal operations.

Possible causes:

- Malfunctioning proof of closure switch

- Malfunctioning dual shutoff solenoid

- Unplugged connector, bad wiring, damaged connector pins

- Malfunctioning control relay(s) in the dual fuel control panel

- Loose wires at the control relay housing (CR2 and CR4: that operate valves 1 and 2) or at the binary input 6 on the module

- Damaged contacts on the gas shutdown switch

- Damaged or malfunctioning fuses in the dual fuel control panel.

| Dual Fuel Control Module |  |  |
|---|---|---|
| Codes or Messages | Reason | Effect |
| Sd FSOV POC Sw | Commanded FSOV position and feedback signal disagree. | Dual fuel control module will **not** allow gas operations. Dual fuel control module will stop gas flow. |

![[05m00181.png]]

Figure 1, Legacy controller (LegCtrl , shown left) and new controller (NewCtrl, shown right)

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Determine ComAp configuration. |  |
|  | **STEP 1A.** Determine configuration. | Unit equipped with LegCtrl? |
| STEP 2. | Validate the fault message. |  |
|  | **STEP 2A.** Fault message is active. | Fault active? |
| STEP 3. | Check the FSOV POC switch and circuit. |  |
|  | **STEP 3A.** Inspect the proof of closure switch and connector pins. | Dirty or damaged pins? |
|  | **STEP 3B.** Check the switch. | Binary Input 6 displays a 1 using InteliMonitor? |
|  | **STEP 3C.** Check the wiring harness. | Binary Input 6 displays a 1 using InteliMonitor? |
|  | **STEP 3D.** Test the binary input response. | Binary Input 6 displays a 1 using InteliMonitor? |
| STEP 4. | Check the fuel shutoff valve 2 operation. |  |
|  | **STEP 4A.** Check the fuel shutoff valve 2 circuit. | System voltage read on both side of fuse F3? |
|  | **STEP 4B.** Check the fuel shutoff valve 2 circuit. | 2.7 amps (±0.2 amps) pull in and 0.9 amps (±0.2 amps) hold in current observed during the leak test? |
|  | **STEP 4C.** Check the fuel shutoff valve 2 circuit. | System voltage read at the harness connector to the fuel shutoff valve? |
|  | **STEP 4D.** Check the fuel shutoff valve 2 circuit. | System voltage rad at the C3 connector? |
|  | **STEP 4E.** Check the fuel shutoff valve 2 circuit. | System voltage read at pin 11 of the fuel shutoff valve 2 relay? |
|  | **STEP 4F.** Check the fuel shutoff valve 2 circuit. | System voltage read at pin 14 of the fuel shutoff valve 2 relay? |
| STEP 5. | Reset the fault. |  |
|  | **STEP 5A.** Reset the fault. | Fault returns? |
| STEP 6. | Check for faults. |  |
|  | **STEP 6A.** Review the fault message(s). | Sd FSOV POC Sw alarm code is present? |
| STEP 7. | Check the FSOV POC switch and circuit. |  |
|  | **STEP 7A.** Inspect the proof of closure switch and connector pins. | Dirty or damaged pins? |
|  | **STEP 7B.** Check the switch. | FSOV POC Sw displays a 1 using InteliMonitor? |
|  | **STEP 7C.** Check the wiring harness. | FSOV POC Sw displays a 1 using InteliMonitor? |
|  | **STEP 7D.** Test the binary input response. | FSOV POC Sw displays a 1 using InteliMonitor? |
| STEP 8. | Verify FSOV POC switch response. |  |
|  | **STEP 8A.** Verify FSOV POC switch response. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? |
| STEP 9. | Check the fuel shutoff valve operation. |  |
|  | **STEP 9A.** Inspect the FSOV connector and pins. | Dirty or damaged pins? |
|  | **STEP 9B.** Check the fuel shutoff valve circuit. | System voltage at FSOV 2 supply pin in FSOV connector? |
|  | **STEP 9C.** Check the fuel shutoff valve circuit. | System voltage at FSOV 2 supply pin in panel C4 connector? |
|  | **STEP 9D.** Check the fuel shutoff valve circuit. | System voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector? |
| STEP 10. | Check the fuel shutoff valve operation. |  |
|  | **STEP 10A.** Verify FSOV POC response. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? |

### STEP 1. Determine ComAp configuration.

#### STEP 1A. Determine ComAp configuration.

| **Conditions:** Verify ComAp control panel configuration. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Determine which ComAp control panel is installed on the unit. Refer to panel identification images in alarm code overview. | Unit equipped with LegCtrl? **YES** | 2A |
| Unit equipped with LegCtrl? **NO** | 6A |  |

### STEP 2. Validate the fault message.

#### STEP 2A. Fault message is active.

| **Conditions:** Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for occurrences of Sd FSOV POC. Use InteliMonitor. | Fault active? **YES** | 5A |
| Fault active? **NO** | 3A |  |

### STEP 3. Check the FSOV POC switch and circuit.

#### STEP 3A. Inspect the proof of closure switch and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the proof of closure switch connector from the dual fuel harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the dual fuel harness and proof of closure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the proof of closure switch or harness connector. Check all harnesses connected in series. Clean the connector and pins. Replace the damaged section of harness of damaged proof of closure switch. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the switch. Refer to Procedure 019-581 in Section 19. | 5A |
| Dirty or damaged pins? **NO** | 3B |  |

#### STEP 3B. Check the switch.

| **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the proof of closure switch connector from the engine harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | Binary Input 6 displays a 1 using InteliMonitor? **YES** | 4A |
| Binary Input 6 displays a 1 using InteliMonitor? **NO** | 3C |  |

#### STEP 3C. Check the wiring harness.

| **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the wiring harness from the C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | Binary Input 6 displays a 1 using InteliMontor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 5A |
| Binary Input 6 displays a 1 using InteliMontor? **NO** | 3D |  |

#### STEP 3D. Test the binary input response.

| **Conditions:** Engine not operating. Power ON the dual fuel control module. Place dual fuel control module |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Make a temporary connection from the panel ground stud to the binary input terminal BI-6. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | Binary Input 6 displays a 1 using InteliMontor? **YESRepair:** Repair or replace the wiring from C3-A to the control module BI-6 (wire 2001). See control panel service manual. | 5A |
| Binary Input 6 displays a 1 using InteliMontor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. See control panel service manual. | 5A |  |

### STEP 4. Check the fuel shutoff valve 2 operation.

#### STEP 4A. Check the fuel shutoff valve 2 circuit.

| **Conditions:** Engine not operating. Power ON the dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage on both side of fuse F3 for fuel shutoff valve 2. | System voltage read on both sides of fuse F3? **YES** | 4B |
| System voltage read on both sides of fuse F3? **NORepair:** Inspect the fuse. Refer to Procedure 019-051 in Section 19. Verify the battery is fully charged and working properly. See equipment manufacturer service information. Inspect the wiring to the battery. Refer to Procedure 019-564 in Section 19. | 5A |  |

#### STEP 4B. Check the fuel shutoff valve 2 circuit.

| **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Install an ammeter (10 amp range) in place of the fuse. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. | 2.7 amps (±0.2 amps) pull in and 0.9 amps (±0.2 amps) hold in current observed during the leak test? **YESRepair:** A malfunctioning closure validation switch has been found. Calibrate the closure validation switch. Refer to Procedure 019-581 in Section 19. If calibration does **not** bring the system into specification, the closure validation switch **must** be replace. | 5A |
| 2.7 amps (±0.2 amps) pull in and 0.9 amps (±0.2 amps) hold in current observed during the leak test? **NO** | 4C |  |

#### STEP 4C. Check the fuel shutoff valve 2 circuit.

| **Conditions:** Engine not operating. Install fuse F3. Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the connector from the fuel shutoff valve. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. | System voltage read at the harness connector to the fuel shutoff valve? **YESRepair:** A malfunctioning fuel shutoff valve has been found. Refer to Procedure 005-044 in Section 5. | 5A |
| System voltage read at the harness connector to the fuel shutoff valve? **NO** | 4D |  |

#### STEP 4D. Check the fuel shutoff valve 2 circuit.

| **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the wiring harness from the C3 connector. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. Measure the voltage for fuel shutoff valve 2 at the SUPPLY pin of the C3 connector. | System voltage read at the C3 connector? **YESRepair:** A malfunctioning wiring harness has been identified. Repair or replace the wiring harness from the C3 connector to the shutoff valve. Refer to Procedure 019-564 in Section 19. | 5A |
| System voltage read at the C3 connector? **NO** | 4E |  |

#### STEP 4E. Check the fuel shutoff valve 2 circuit.

| **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the voltage for fuel shutoff valve 2 at the SUPPLY pin 11 of the fuel shutoff valve 2 relay. | System voltage read at pin 11 of the fuel shutoff valve 2 relay? **YESRepair:** A malfunction in the wiring in the control panel has been identified. Repair or replace the malfunctioning wiring in the control panel. See control panel service manual. | 5A |
| System voltage read at pin 11 of the fuel shutoff valve 2 relay? **NO** | 4F |  |

#### STEP 4F. Check the fuel shutoff valve 2 circuit.

| **Conditions:** Engine not operating. Power ON dual fuel control module. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the connector to the fuel shutoff valve. Initiate the Fuel Shutoff Valve Internal Valve Leak Test. Refer to Procedure 005-236 in Section 5. Measure the voltage for fuel shutoff valve 2 at the SUPPLY pin (pin 14) of the fuel shutoff valve 2 relay. | System voltage read at pin 14 of the fuel shutoff valve 2 relay? **YESRepair:** A malfunction in the wiring in the control panel has been identified. Repair or replace the malfunctioning wiring in the control panel. See control panel service manual. | 5A |
| System voltage read at pin 14 of the fuel shutoff valve 2 relay? **NORepair:** Verify the relay is functioning properly by observing the LED indicator on the body of the relay. If the LED is not lighting, inspect the relay. Refer to Procedure 019-589 in Section 19. If the relay is operating correctly, a malfunction in the control panel wiring between the relay and fuse has bee detected. See control panel service manual. | 5A |  |

### STEP 5. Reset the fault.

#### STEP 5A. Reset the fault.

| **Conditions:** Engine not operating. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Reset the fault on the control panel or through InteliMonitor. Operate the engine under conditions to allow gas substitution. | Fault returns? **YESRepair:** Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. | 2A |
| Fault returns? **NO** | Repair complete |  |

### STEP 6. Check for faults.

#### STEP 6A. Review the fault message(s).

| **Conditions:** Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check local display panel for fault messages in alarm list and history. | Sd FSOV POC Sw alarm code is present? **YES** | 7A |
| Sd FSOV POC Sw alarm code is present? **NO** | Return the pump to service and monitor. |  |

### STEP 7. Check the FSOV POC switch and circuit.

#### STEP 7A. Inspect the proof of closure switch and connector pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the proof of closure switch connector from the dual fuel harness connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the dual fuel harness and proof of closure switch connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** A damaged connection has been detected in the proof of closure switch or harness connector. Repair or replace the damaged section of harness or damaged proof of closure / closure validation switch. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the closure validation switch. Refer to Procedure 019-581 in Section 19. | 8A |
| Dirty or damaged pins? **NO** | 7B |  |

#### STEP 7B. Check the switch.

| **Conditions:** Engine not operating. Power ON dual fuel control panel. Disconnect the proof of closure switch connector from the dual fuel harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the wiring harness connector. | FSOV POC Sw displays a 1 using InteliMonitor? **YESRepair:** Readjust or replace the closure validation switch. Refer to Procedure 019-581 in Section 19. | 8A |
| FSOV POC Sw displays a 1 using InteliMonitor? **NO** | 7C |  |

#### STEP 7C. Check the wiring harness.

| **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. Disconnect the dual fuel wiring harness from the C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Place a jumper wire between the SIGNAL and RETURN wire on the C3 wiring harness connector. | FSOV POC Sw displays a 1 using InteliMonitor? **YESRepair:** The wiring harness has malfunctioned. Repair or replace the wiring harness. Refer to Procedure 019-564 in Section 19. | 8A |
| FSOV POC Sw displays a 1 using InteliMonitor? **NO** | 7D |  |

#### STEP 7D. Test the binary input response.

| **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Make a temporary connection from the panel ground to the POC Signal pin on IBF Module connector. Use an approved jumper wire. Observe when the connection is made, the input status becomes 1. | FSOV POC Sw displays a 1 using InteliMonitor? **YESRepair:** Repair or replace the panel internal wiring harness. | 8A |
| FSOV POC Sw displays a 1 using InteliMonitor? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. See control panel service manual. | 9A |  |

### STEP 8. Verify FSOV POC switch response.

#### STEP 8A. Verify FSOV POC switch response.

| **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Verify POC Switch status matches valve command with InteliMonitor. While manually operating the FSOV using InteliMonitor and with the engine off you should be able to hear and feel the valve move. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **YES** | Return the pump to service and monitor. |
| FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **NO** | 9A |  |

### STEP 9. Check the fuel shutoff valve operation.

#### STEP 9A. Inspect the FSOV connector and pins.

| **Conditions:** Turn keyswitch OFF. Disconnect the dual fuel harness from the FSOV. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Inspect the dual fuel harness and FSOV connector pins for the following: Loose connector Corroded pins Bent or broken pins Pushed back or expanded pins Moisture in or on the connector Missing or damaged connector seals Dirt or debris in or on the connector pins Connector shell broken Wire insulation damage Damaged connector locking tab. Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection\|Refer to Procedure 019-361 in Section 19.]] | Dirty or damaged pins? **YESRepair:** Repair or replace the dual fuel harness or damaged FSOV. Repair the harness. Refer to Procedure 019-564 in Section 19. Replace the FSOV. Refer to Procedure 005-044 in Section 5. | 10A |
| Dirty or damaged pins? **NO** | 9B |  |

#### STEP 9B. Check the fuel shutoff valve circuit.

| **Conditions:** Engine not operating. Disconnect the dual fuel harness from the FSOV. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Measure for battery voltage FSOV 2 supply pins. | System voltage at FSOV 2 supply pin in FSOV connector? **YES** | 10A |
| System voltage at FSOV 2 supply pin in FSOV connector? **NO** | 9C |  |

#### STEP 9C. Check the fuel shutoff valve circuit.

| **Conditions:** Engine not operating. Disconnect the dual fuel harness C4 connector from panel. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Measure for battery voltage FSOV 2 supply pin in Dual Fuel Control Panel C4 Connector. | System voltage at FSOV 2 supply pin in panel C4 connector? **YESRepair:** Repair or replace damaged dual fuel wiring harness. Refer to Procedure 019-564 in Section 19. | 10A |
| System voltage at FSOV 2 supply pin in panel C4 connector? **NO** | 9D |  |

#### STEP 9D. Check the fuel shutoff valve circuit.

| **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Measure for battery voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector. Refer to wiring diagram for connector pin identification. | System voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector? **YESRepair:** Repair or replace damaged dual fuel control panel internal wiring harness. | 10A |
| System voltage at FSOV 2 supply pin Inteli Bi-Fuel module connector? **NORepair:** A malfunctioning Inteli Bi-Fuel module has been detected. Replace IBF module. Refer to Procedure 019-568 in Section 19. | 10A |  |

### STEP 10. Verify FSOV and POC switch response.

#### STEP 10A. Verify FSOV POC response.

| **Conditions:** Engine not operating. Power ON dual fuel control module. Connect InteliMonitor to the dual fuel control panel |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Manually Operate FSOV 2 in manual mode: IMON - Remote switches – “FSOV 2 ON” (Level 2 password required). Verify POC Switch status matches valve command with InteliMonitor. While manually operating the FSOV using InteliMonitor and with the engine off you should be able to hear and feel the valve move. If not proceed directly to Step 9A. | FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **YES** | Return the pump to service and monitor. |
| FSOV POC Sw status matches FSOV 2 command in InteliMonitor? **NO** | Return to the troubleshooting steps or contact a Cummins® Authorized Repair Location if all steps have been completed and checked again. |  |
