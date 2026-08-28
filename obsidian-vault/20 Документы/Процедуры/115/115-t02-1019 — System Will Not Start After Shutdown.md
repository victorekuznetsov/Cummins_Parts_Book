---
aliases:
  - "Система не запускается после останова"
type: "Процедура"
doc: "115-t02-1019"
title_en: "System Will Not Start After Shutdown"
title_ru: "Система не запускается после останова"
modified: "2008-04-14"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# System Will Not Start After Shutdown
**Система не запускается после останова**

> [!abstract] Процедура · `115-t02-1019`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1019.pdf)

Printable Version

### Symptoms

- The basic alarm panel system will **not** start up after a complete system shutdown.

### How To Use This Tree

This symptom tree can be used to troubleshoot panel startup symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the Engine Stop button |  |
|  | **STEP 1A.** Check Engine Stop button for engagement. | Engine Stop button engaged? |
| STEP 2. | Check customer interface box battery circuit |  |
|  | **STEP 2A.** Check voltage at customer interface box logic unit | +24-VDC? |
|  | **STEP 2B.** Check the battery supply wire (circuit breaker to customer interface box logic unit) | Less than 10 ohms resistance? |
|  | **STEP 2C.** Check the battery suppy wire (X4 connector to circuit breaker) | Less than 10 ohms resistance? |
|  | **STEP 2D.** Check the battery return wire (circuit breaker to customer interface box logic unit) | Less than 10 ohms resistance? |
|  | **STEP 2E.** Check the battery return wire (X4 connector to circuit breaker) | Less than 10 ohms resistance? |
|  | **STEP 2F.** Check battery supply circuit breaker | Less than 10 ohms resistance? |
|  | **STEP 2G.** Check the power supply wire (customer interface box logic unit to customer interface box logic unit circuit breaker) | Less than 10 ohms resistance? |
|  | **STEP 2H.** Check the customer interface box logic unit supply wire (customer interface box logic unit circuit breaker to customer interface box logic unit) | Less than 10 ohms resistance? |
|  | **STEP 2I.** Check customer interface box logic unit circuit breaker | Less than 10 ohms resistance? |
|  | **STEP 2J.** Check the power supply wire (customer interface box logic unit to engine room panel supply circuit breaker) | Less than 10 ohms resistance? |
|  | **STEP 2K.** Check the engine room panel supply wire (engine room panel supply circuit breaker to connector C7) | Less than 10 ohms resistance? |
|  | **STEP 2L.** Check the engine room panel supply circuit breaker | Less than 10 ohms resistance? |
|  | **STEP 2M.** Check the engine room panel return wire (customer interface box logic unit to connector C7) | Less than 10 ohms resistance? |
| STEP 3. | Check panel system cables |  |
|  | **STEP 3A.** Check engine room panel cable | Less than 10 ohms resistance? |
| STEP 4. | Check panel wiring |  |
|  | **STEP 4A.** Check engine room panel supply wire | Less than 10 ohms resistance? |
|  | **STEP 4B.** Check power switch operation | Less than 10 ohms resistance? |

### STEP 1. Check the Engine Stop button

#### STEP 1A. Check the Engine Stop button for disengagement

| **Conditions:** Customer interface box closed. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Be sure the Engine Stop button is fully disengaged. Turn the Engine Stop button 1/16th of a turn clockwise. The Engine Stop button will make an audible noise as it disengages. NOTE: The Engine Stop button will **not** turn if it is already disengaged. | Engine Stop button engaged? **YES** | Repair complete |
| Engine Stop button engaged? **NO** | 2A |  |

### STEP 2. Check interface box battery circuit

#### STEP 2A. Check voltage at customer interface box logic unit

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check battery supply voltage to the customer interface box logic unit. Place one test lead on the battery supply terminal on the customer interface box logic unit. Place the other test lead on the battery return terminal on the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | +24-VDC? **YES** | 2G |
| +24-VDC? **NO** | 2B |  |

#### STEP 2B. Check the battery supply wire (circuit breaker to customer interface box logic unit)

| **Conditions:** Open the customer interface box Disconnect the battery supply wire from the customer interface box logic unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery supply wire. Place one test lead on the battery supply terminal of the battery supply circuit breaker. Place the other test lead on the battery supply terminal of the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2C |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2C. Check the Battery Suppy Wire (X4 Connector to Circuit Breaker)

| **Conditions:** Open the customer interface box Disconnect the battery supply wire from the circuit breaker. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery supply wire. Place one test lead on the battery supply terminal of X4. Place the other test lead on the battery supply terminal of the battery supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2D |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2D. Check the battery return wire (circuit breaker to customer interface box logic unit)

| **Conditions:** Open the customer interface box Disconnect the battery return wire from the customer interface box logic unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery return wire. Place one test lead on the battery return terminal of the battery supply circuit breaker. Place the other test lead on the battery return terminal of the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2E |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2E. Check the battery return wire (X4 connector to circuit breaker)

| **Conditions:** Open the customer interface box Disconnect the battery return wire from the circuit breaker. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery return wire. Place one test lead on the battery return terminal of X4. Place the other test lead on the battery return terminal of the battery supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2F |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2F. Check battery supply circuit breaker

| **Conditions:** Open the customer interface box Disconnect all wires from the circuit breaker Close the circuit breaker. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery supply circuit breaker. Place one test lead on a terminal on one side of the circuit breaker. Place the other test lead on the corresponding terminal on the other side of the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2G |
| Less than 10 ohms resistance? **NORepair:** Replace the circuit breaker. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2G. Check the power supply wire (customer interface box logic unit to customer interface box logic unit circuit breaker)

| **Conditions:** Open the customer interface box Disconnect the power supply wire from the customer interface box logic unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power supply wire. Place one test lead on the power supply terminal of the customer interface box logic unit. Place the other test lead on the power supply terminal of the customer interface box logic unit circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2H |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2H. Check the customer interface box logic unit supply wire (customer interface box logic unit circuit breaker to customer interface box logic unit)

| **Conditions:** Open the customer interface box Disconnect the customer interface box logic unit supply wire from the customer interface box logic unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface logic unit supply wire. Place one test lead on the customer interface box logic unit supply terminal of the customer interface box logic unit. Place the other test lead on the customer interface box logic unit supply terminal of the customer interface box logic unit circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2I |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2I. Check customer interface box logic unit circuit breaker

| **Conditions:** Open the customer interface box Disconnect all wires from the circuit breaker Close the circuit breaker. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface logic unit circuit breaker. Place one test lead on the terminal on one side of the circuit breaker. Place the other test lead on the terminal on the other side of the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2J |
| Less than 10 ohms resistance? **NORepair:** Replace the circuit breaker. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2J. Check the power supply wire (customer interface box logic unit to engine room panel supply circuit breaker)

| **Conditions:** Open the customer interface box Disconnect the power supply wire from the customer interface box logic unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power supply wire. Place one test lead on the power supply terminal of the customer interface box logic unit. Place the other test lead on the power supply terminal of the engine room panel supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2K |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2K. Check the engine room panel supply wire (engine room panel supply circuit breaker to connector C7)

| **Conditions:** Open the customer interface box Disconnect the engine room panel cable at connector C7 of the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel supply wire. Place one test lead on the engine room panel supply pin of connector C7. Place the other test lead on the engine room panel supply terminal of the engine room panel supply circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2L |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2L. Check the engine room panel supply circuit breaker

| **Conditions:** Open the customer interface box Disconnect all wires from the circuit breaker Close the circuit breaker. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel supply circuit breaker. Place one test lead on the terminal on one side of the circuit breaker. Place the other test lead on the terminal on the other side of the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 2M |
| Less than 10 ohms resistance? **NORepair:** Replace the circuit breaker. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 2M. Check the engine room panel return wire (customer interface box logic unit to connector C7)

| **Conditions:** Open the customer interface box Disconnect the engine room panel cable at connector C7 of the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel return wire. Place one test lead on the engine room panel return pin of connector C7. Place the other test lead on the engine room panel return terminal of the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

### STEP 3. Check panel system cables

#### STEP 3A. Check engine room panel cable

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Install a jumper between engine room panel supply pin and the engine room panel return pin in connector C14. Place one test lead in the engine room panel supply pin in connector C7. Place the other test lead in the engine room panel return pin in connector C7. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

### STEP 4. Check panel wiring

#### STEP 4A. Check engine room panel supply wire

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and control panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel supply pin on connector C14. Place the other test lead in the engine room panel supply pin on the control panel connector. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YES** | 4B |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |

#### STEP 4B. Check power switch operation

| **Conditions:** Open engine room panel Disconnect engine room panel connector control panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power switch operation. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel power switch supply terminal of the control panel connector. Place the other test lead on the engine room panel power supply terminal on the control panel connector. Move the power switch to the on position. Refer to the appropriate circuit diagram or wiring diagram for correct pin and wire identification. | Less than 10 ohms resistance? **YESRepair:** Replace the customer interface box logic unit. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the control panel. [[115-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete. |  |
