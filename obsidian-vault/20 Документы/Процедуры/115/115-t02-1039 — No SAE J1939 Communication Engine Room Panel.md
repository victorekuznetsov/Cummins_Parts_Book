---
aliases:
  - "Нет связи по SAE J1939 с пультом машинного отделения"
type: "Процедура"
doc: "115-t02-1039"
title_en: "No SAE J1939 Communication Engine Room Panel"
title_ru: "Нет связи по SAE J1939 с пультом машинного отделения"
modified: "2007-01-08"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021587"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1039.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1039.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/115"
---

# No SAE J1939 Communication Engine Room Panel
**Нет связи по SAE J1939 с пультом машинного отделения**

> [!abstract] Процедура · `115-t02-1039`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021587 — C Command Panel System Marine Master Repair Manual|4021587]]
> **Секции:** Section TT — Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2007-01-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/115/115-t02-1039.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/115-t02-1039.pdf)

Printable Version

### Symptoms

- No SAE J1939 Communication with the engine room panel instrument panel.

- Remote panel has SAE J1939 communication.

### How To Use This Tree

This symptom tree can be used to troubleshoot SAE J1939 communication symptoms. Start by checking the terminating resistors. There are two terminating resistors. The terminating resistors are located at the following points:

One resistor is located on the engine wiring harness.

If remote panel(s) are used, the second resistor is located at the last remote panel at the X4 terminal strip between the SAE J1939 Supply and SAE J1939 Return terminals.

If a remote panel is **not** used, the second resistor is located in the Customer Interface Box at the X4 terminal between SAE J1939 Supply and SAE J1939 Return terminals.

Step 1 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SAE J1939 datalink provides information to the instrument panel in the engine room panel.

The SAE J1939 datalink provides the following parameters:

- Engine fault codes

- Engine parameters monitored by the ECM.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check SAE J1939 Datalink Signal |  |
|  | **STEP 1A.** Check SAE J1939 Datalink Communication on Engine | Communication established? |
|  | **STEP 1B.** Check SAE J1939 Datalink Communication at Engine Room Panel | Communication established? |
| STEP 2. | Check Panel Wiring |  |
|  | **STEP 2A.** Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
|  | **STEP 2B.** Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
|  | **STEP 2C.** Check Engine Room Panel SAE J1939 Datalink Shield Wire (Instrument Panel Connector to Service Port Connector) | Less than 10 ohms resistance? |
|  | **STEP 2D.** Check SAE J1939 Datalink Supply Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
|  | **STEP 2E.** Check SAE J1939 Datalink Return Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
|  | **STEP 2F.** Check SAE J1939 Datalink Shield Wire (C14 Connector to Instrument Panel Connector) | Less than 10 ohms resistance? |
| STEP 3. | Check Panel System Cable |  |
|  | **STEP 3A.** Check Engine Room Panel Cable (SAE J1939 Supply and Return Wires) | Less than 10 ohms resistance? |
|  | **STEP 3B.** Check Engine Room Panel Cable (SAE J1939 Return and Shield Wires) | Less than 10 ohms resistance? |
|  | **STEP 3C.** Check Customer Interface Box Cable (SAE J1939 Supply and Return Wires) | Less than 10 ohms resistance? |
|  | **STEP 3D.** Check Customer Interface Box Cable (SAE J1939 Return and Shield Wires) | Less than 10 ohms resistance? |
| STEP 4. | Check Customer Interface Box Wiring |  |
|  | **STEP 4A.** Check SAE J1939 Datalink Supply Wire | Less than 10 ohms resistance? |
|  | **STEP 4B.** Check SAE J1939 Datalink Return Wire | Less than 10 ohms resistance? |
|  | **STEP 4C.** Check SAE J1939 Datalink Shield Wire | Less than 10 ohms resistance? |
| STEP 5. | Check Display Wiring |  |
|  | **STEP 5A.** Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel X4 to Display) | Less than 10 ohms resistance? |
|  | **STEP 5B.** Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel X4 to Display) | Less than 10 ohms resistance? |

### STEP 1. Check SAE J1939 Datalink Signal

#### STEP 1A. Check SAE J1939 Datalink Communication on Engine

| **Conditions:** Engine room panel power switch turned on and power lamp illuminated Locate engine wiring harness Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check SAE J1939 datalink communications. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 1B |
| Communication established? **NORepair:** Refer to the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850, Modular Common Rail System, Series Engines, Bulletin 4021493. | Repair complete. |  |

#### STEP 1B. Check SAE J1939 Datalink Communication at Engine Room Panel

| **Conditions:** Locate engine room panel Connect INSITE™ electronic service tool. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check SAE J1939 datalink communications. Use INSITE™ electronic service tool to establish communication. | Communication established? **YES** | 5A |
| Communication established? **NO** | 2A. |  |

### STEP 2. Check Panel Wiring

#### STEP 2A. Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel Connector to Service Port Connector)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel SAE J1939 datalink supply pin on the instrument panel connector Place the other test lead on the engine room panel SAE J1939 datalink supply pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2B |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | 1B |  |

#### STEP 2B. Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel Connector to Service Port Connector)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel SAE J1939 datalink return pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink return pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2C |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | 1B |  |

#### STEP 2C. Check Engine Room Panel SAE J1939 Datalink Shield Wire (Instrument Panel Connector to Service Port Connector)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Connect one test lead on the engine room panel SAE J1939 datalink shield pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink shield pin on the service port connector. | Less than 10 ohms resistance? **YES** | 2D |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | 1B |  |

#### STEP 2D. Check SAE J1939 Datalink Supply Wire (C14 Connector to Instrument Panel Connector)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink supply pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink supply pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 2E |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 2E. Check SAE J1939 Datalink Return Wire (C14 Connector to Instrument Panel Connector)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink return pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink return pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 2F |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 2F. Check SAE J1939 Datalink Shield Wire (C14 Connector to Instrument Panel Connector)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check wires between harness connector and instrument panel connector. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink shield pin on connector C14. Place the other test lead on the engine room panel SAE J1939 datalink shield pin on the instrument panel connector. | Less than 10 ohms resistance? **YES** | 3A |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

### STEP 3. Check Panel System Cables

#### STEP 3A. Check Engine Room Panel Cable (SAE J1939 Supply and Return Wires)

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Install a jumper between engine room panel SAE J1939 datalink supply pin and the engine room panel SAE J1939 datalink return pin in connector C14. Place one test lead in the engine room panel SAE J1939 datalink supply pin in connector C7. Place the other test lead in the engine room panel SAE J1939 datalink return pin in connector C7. | Less than 10 ohms resistance? **YES** | 3B |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 3B. Check Engine Room Panel Cable (SAE J1939 Return and Shield Wires)

| **Conditions:** Disconnect cable connector C14 from the engine room panel Disconnect cable connector C7 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine room panel cable. Install a jumper between engine room panel SAE J1939 datalink return pin and the engine room panel SAE J1939 datalink shield pin in connector C14. Place one test lead in the engine room panel SAE J1939 datalink return pin in connector C7. Place the other test lead in the engine room panel SAE J1939 datalink shield pin in connector C7. | Less than 10 ohms resistance? **YES** | 3C |
| Less than 10 ohms resistance? **NORepair:** Replace the cable. | Repair complete. |  |

#### STEP 3C. Check Customer Interface Box Cable (SAE J1939 Supply and Return Wires)

| **Conditions:** Disconnect SAE J1939 datalink cable connector from the engine wiring harness Disconnect cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface box cable. Install a jumper between SAE J1939 datalink supply pin and the SAE J1939 datalink return pin in SAE J1939 datalink cable connector. Place one test lead in the SAE J1939 datalink supply pin in connector C3. Place the other test lead in the SAE J1939 datalink return pin in connector C3. | Less than 10 ohms resistance? **YES** | 3D |
| Less than 10 ohms resistance? **NORepair:** Replace the cable? | Repair complete. |  |

#### STEP 3D. Check Customer Interface Box Cable (SAE J1939 Return and Shield Wires)

| **Conditions:** Disconnect SAE J1939 datalink cable connector from the engine wiring harness Disconnect cable connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface box cable. Install a jumper between SAE J1939 datalink return pin and the SAE J1939 datalink shield pin in SAE J1939 datalink cable connector. Place one test lead in the SAE J1939 datalink return pin in connector C3. Place the other test lead in the SAE J1939 datalink shield pin in connector C3. | Less than 10 ohms resistance? **YES** | 4A |
| Less than 10 ohms resistance? **NORepair:** Replace the cable? | Repair complete. |  |

### STEP 4. Check Customer Interface Box Wiring

#### STEP 4A. Check SAE J1939 Datalink Supply Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box cable at connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SAE J1939 datalink supply wire. Place one test lead on the SAE J1939 datalink supply (C3) pin in connector C7. Place the other test lead on the engine SAE J1939 datalink supply pin on in the C3 connector. | Less than 10 ohms resistance? **YES** | 4B |
| Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 4B. Check SAE J1939 Datalink Return Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box cable at connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SAE J1939 datalink return wire. Place one test lead on the SAE J1939 datalink return (C3) pin in connector C7. Place the other test lead on the engine room SAE J1939 datalink return pin on the C3 connector. | Less than 10 ohms resistance? **YES** | 4C |
| Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

#### STEP 4C. Check SAE J1939 Datalink Shield Wire

| **Conditions:** Open the customer interface box Disconnect engine room cable at connector C7 from the customer interface box Disconnect customer interface box cable at connector C3 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SAE J1939 datalink shield wire. Place one test lead on the SAE J1939 datalink shield (C3) pin in connector C7. Place the other test lead on the SAE J1939 datalink shield pin on the C3 connector. | Less than 10 ohms resistance? **YESRepair:** Refer to Section TF in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021493. | 5A |
| Less than 10 ohms resistance? **NORepair:** Replace the wire. Refer to Procedure [[115-015-023 — Customer Interface Box\|015-023]]. | Repair complete. |  |

### STEP 5. Check Display Wiring

#### STEP 5A. Check Engine Room Panel SAE J1939 Datalink Supply Wire (Instrument Panel X4 to Display)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink supply pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink supply wire at the display. | Less than 10 ohms resistance? **YES** | 5B |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |

#### STEP 5B. Check Engine Room Panel SAE J1939 Datalink Return Wire (Instrument Panel X4 to Display)

| **Conditions:** Locate engine room panel Open engine room panel door. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check engine room panel wiring. Disconnect cable C14 from the engine room panel. Place one test lead on the engine room panel SAE J1939 datalink return pin on the instrument panel connector. Place the other test lead on the engine room panel SAE J1939 datalink return wire at the display. | Less than 10 ohms resistance? **YESRepair:** Replace the display. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |
| Less than 10 ohms resistance? **NORepair:** Replace the faulty wire. Refer to Procedure [[115-015-024 — Engine Room Panel\|015-024]]. | Repair complete. |  |
