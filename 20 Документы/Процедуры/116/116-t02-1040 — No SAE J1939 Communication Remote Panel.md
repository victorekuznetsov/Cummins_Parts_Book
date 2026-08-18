---
aliases:
  - "Нет связи по SAE J1939 с дистанционным пультом"
type: "Процедура"
doc: "116-t02-1040"
title_en: "No SAE J1939 Communication Remote Panel"
title_ru: "Нет связи по SAE J1939 с дистанционным пультом"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1040.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1040.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# No SAE J1939 Communication Remote Panel
**Нет связи по SAE J1939 с дистанционным пультом**

> [!abstract] Процедура · `116-t02-1040`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1040.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1040.pdf)

Printable Version

### Symptoms

- No SAE J1939 Communication to DCU410 unit.

- No SAE J1939 communication with the remote panel display panel.

- Engine room panel has SAE J1939 communication.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Start by checking the terminating resistor. The terminating resistor is located on the QSK19, QSK38, QSK50, and QSK60 CM850 wiring diagrams on the engine wiring harness.

The SAE J1939 data link provides information to the display in the remote panel.

The SAE J1939 data link provides the following parameters:

- Engine fault codes

- Engine parameters monitored by the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box wiring. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
| STEP 2. | Check the SAE J1939 data link signal. |  |
|  | **STEP 2A.** Check SAE J1939 data link communication on engine. |  |
|  | **STEP 2B.** Check the SAE J1939 data link communication at remote panel. |  |
| STEP 3. | Check the remote panel wiring. |  |
|  | **STEP 3A.** Check SAE J1939 supply wire for an open. |  |
|  | **STEP 3B.** Check SAE J1939 return wire for an open. |  |
|  | **STEP 3C.** Check the SAE J1939 data link shield wire for an open. |  |
| STEP 4. | Check the remote panel wiring. |  |
|  | **STEP 4A.** Check the SAE J1939 data link supply, return, and shield wires for a wire-to-wire short. |  |
|  | **STEP 4B.** Check the SAE J1939 data link supply, return, and shield wires for a short to ground. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 2A |
| DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 2A |  |

### STEP 2. Check the SAE J1939 data link signal.

#### STEP 2A. Check SAE J1939 data link communication on engine.

| **Conditions:** Locate the engine wiring harness from the ECM. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check SAE J1939 data link communication on engine. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 2B |
| Communication established? **NORepair:** For QSK19 engines, refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493. For QSK38, QSK50, and QSK60 engines, refer to Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533. | Repair complete |  |

#### STEP 2B. Check the SAE J1939 data link communication at the remote panel.

| **Conditions:** Open the customer interface box. Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SAE J1939 data link communication at the remote panel. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | Repair complete |
| Communication established? **NO** | 3A |  |

### STEP 3. Check the remote panel wiring.

#### STEP 3A. Check SAE J1939 supply wire for an open.

| **Conditions:** Open the customer interface box. Locate the remote panel display. Disconnect the SAE J1939 supply wire at the DCU410 unit and service port connector. Disconnect the C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check SAE J1939 supply wire for an open. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on the supply wire at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link supply wire at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 3B. Check SAE J1939 return wire for an open.

| **Conditions:** Open the customer interface box. Locate the remote panel display. Disconnect the SAE J1939 return wire at the DCU410 unit and service port connector. Disconnect the C3 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check SAE J1939 return wire for an open. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on the return wire at the SAE J1939 data link service port connector. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on the SAE J1939 data link return wire at the C3 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 3C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 3C. Check SAE J1939 data link shield wire for an open.

| **Conditions:** Open the customer interface box. Locate the remote panel display. Disconnect the SAE J1939 data link shield wire at the DCU410 unit and service port connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check SAE J1939 data link shield wire for an open. Place one test lead on the SAE J1939 data link shield wire at the DCU410 unit. Place the other test lead on the return wire at the SAE J1939 data link service port connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 4A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

### STEP 4. Check the remote panel wiring.

#### STEP 4A. Check the SAE J1939 data link supply, return, and shield wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Locate the remote panel display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SAE J1939 data link supply wire for wire-to-wire short. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the SAE J1939 data link shield wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 4B |  |

#### STEP 4B. Check the SAE J1939 data link supply, return, and shield wires for a short to ground.

| **Conditions:** Open the customer interface box. Locate the remote panel display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SAE J1939 data link supply, return, and shield wires for a short to ground. Place one test lead on the SAE J1939 data link supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link return wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the SAE J1939 data link shield wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
