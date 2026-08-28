---
aliases:
  - "SDU 410: обрыв цепи датчика-реле температуры ОЖ"
type: "Процедура"
doc: "116-t02-1696"
title_en: "SDU 410: Indicates Open Circuit Fault – Coolant Temperature Switch"
title_ru: "SDU 410: обрыв цепи датчика-реле температуры ОЖ"
modified: "2026-04-27"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1696.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1696.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# SDU 410: Indicates Open Circuit Fault – Coolant Temperature Switch
**SDU 410: обрыв цепи датчика-реле температуры ОЖ**

> [!abstract] Процедура · `116-t02-1696`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2026-04-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1696.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1696.pdf)

Printable Version

### Symptoms

The fault message is displayed on the diesel control unit (DCU) 410E.

### How To Use This Tree

**Circuit Description**

The SDU 410 has eight switch inputs. Each switch input has open circuit fault detection. The SDU 410 is monitoring the resistance of the circuit. The coolant temperature switch monitors coolant temperature. A 10k Ohm resistor is installed in the connector that mates to the switch.

**Component Location**

The SDU 410 is in the customer interface box.

**Conditions for Running the Diagnostics**

Customer interface box power switch ON.

**Conditions for Setting the Code**

The SDU 410 detects an open circuit. The overall resistance of the circuit is greater than 10k ohms.

**Actions Taken when the Fault Code is Active**

The DCU 410E will display one of the following faults:

Coolant Temperature Low

**Conditions for Clearing the Fault Code**

SDU 410 detects adequate resistance on the affected circuit.

Acknowledge the fault on the DCU 410E.

### Shoptalk

Possible causes include:

- Broken or disconnected wiring

Damaged or missing open circuit detection resistor

Malfunctioning switch

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check wiring connections. |  |
|  | **STEP 1A.** Check all wiring harness connection points. | Connections tight and secure? |
| STEP 2. | Check the coolant temperature switch. |  |
|  | **STEP 2A.** Check the coolant temperature switch. | Greater than 100k ohms? |
|  | **STEP 2B.** Check the coolant temperature switch connector resistor. | Greater than 11K ohms? |
| STEP 3. | Check the coolant temperature switch wiring harness. |  |
|  | **STEP 3A.** Check the coolant temperature switch signal and return wires for an open circuit. | Greater than 10 ohms? |
|  | **STEP 3B.** Check the coolant temperature switch signal and return wires for a wire-to-wire short. | Greater than 10 ohms? |
|  | **STEP 3C.** Check the coolant temperature switch signal wire for a short to ground. | Greater than 10 ohms? |

### STEP 1. Check wiring connections.

#### STEP 1A. Check all wiring harness connection points.

| **Conditions:** Engine OFF. Customer interface box power switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the following connection points for secure connection. SDU 410 terminal block connection inside the customer interface box. Optional customer-provided circuit connections. | Connections tight and secure? **YES** | 2A |
| Connections tight and secure? **NORepair:** Connect any disconnected harnesses. Repair or replace damaged connections. Inside customer interface box: Refer to Procedure 015-138 in Section 15. Optional customer-provided circuit connections: See equipment manufacturer service information. | Repair complete. |  |

### STEP 2. Check the coolant temperature switch.

#### STEP 2A. Check the coolant temperature switch.

| **Conditions:** Engine OFF. Customer interface box power switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the coolant temperature switch connector. Measure the resistance at the coolant temperature switch. Place one test lead on the coolant temperature switch SIGNAL pin at the switch. Place the other test lead on the coolant temperature switch RETURN pin at the switch. See the appropriate wiring diagram or pin and wire identification. | Greater than 100k ohms? **YES** | 2B |
| Greater than 100k ohms? **NORepair:** Replace the coolant temperature switch. [[116-015-141 — Alarm System Engine Lubricating Oil Pressure Switch\|Refer to Procedure 015-141 in Section 15.]] | Repair complete. |  |

#### STEP 2B. Check the coolant temperature switch connector resistor.

| **Conditions:** Engine OFF. Customer interface box power switch OFF. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Disconnect the coolant temperature switch connector. Measure the resistance across SUPPLY and the SIGNAL pins on the coolant temperature switch connector. Place one test lead on the coolant temperature switch wiring harness SIGNAL pin. Place the other test lead on the SUPPLY pin. See the appropriate wiring diagram or pin and wire identification. | Greater than 11k ohms? **YESRepair:** Replace the resistor in the connector of the coolant temperature switch wiring harness. | Repair complete. |
| Greater than 11k ohms? **NO** | 3A |  |

### STEP 3. Check the coolant temperature switch wiring harness.

#### STEP 3A. Check the coolant temperature switch signal and return wires for an open circuit.

| **Conditions:** Open the customer interface box. Disconnect the coolant temperature switch SIGNAL and RETURN wires at the SDU 410 unit and connector C4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature switch SIGNAL and RETURN wires for an open circuit. Place one test lead on the coolant temperature switch SIGNAL wire at the SDU 410 unit. Place the other test lead on the coolant temperature switch SIGNAL pin at the C4 connector. Place one test lead on the coolant temperature switch RETURN wire at the SDU 410 unit. Place the other test lead on the coolant temperature switch RETURN pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Greater than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | 3B |
| Greater than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete. |  |

#### STEP 3B. Check the coolant temperature switch signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the coolant temperature switch SIGNAL and RETURN wires at the SDU 410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature switch SIGNAL and RETURN wires for a wire-to-wire short. Place one test lead on the coolant temperature switch SIGNAL wire at the SDU 410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the coolant temperature switch RETURN wire at the SDU 410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Greater than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete. |
| Greater than 10 ohms? **NO** | 3C |  |

#### STEP 3C. Check the coolant temperature switch signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the coolant temperature switch SIGNAL wire at the SDU 410 unit and C4 connector |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature switch SIGNAL wire for a short to ground. Place one test lead on the coolant temperature switch SIGNAL wire at the SDU 410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Greater than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete. |
| Greater than 10 ohms? **NORepair:** Replace the SDU 410. [[116-015-122 — Customer Interface Box Shutdown Unit\|Refer to Procedure 015-122 in Section 15.]] | Repair complete. |  |
