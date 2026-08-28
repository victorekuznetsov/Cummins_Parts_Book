---
type: "Процедура"
doc: "300-t02-1061"
title_en: "Low Oil Pressure Shutdown Lamp Driver Malfunction"
modified: "2019-05-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Low Oil Pressure Shutdown Lamp Driver Malfunction

> [!abstract] Процедура · `300-t02-1061`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1061.pdf)

Printable Version

### Symptoms

- The low pressure shutdown lamp is illuminated when a low pressure shutdown condition does **not** exist.

- The low pressure shutdown lamp is **not** illuminated when a low pressure shutdown condition exists.

### How To Use This Tree

This symptom tree can be used to troubleshoot a low oil pressure shutdown lamp driver malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

None.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
|  | **STEP 1A.** Check the low pressure shutdown SIGNAL wire for an open circuit. | Less than 10 ohms? |
|  | **STEP 1B.** Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. | Greater than 100k ohms? |
|  | **STEP 1C.** Check the low pressure shutdown SIGNAL wire for a short circuit to ground. | Greater than 100k ohms? |
| STEP 2. | Check the engine harness to the C.I.B. |  |
|  | **STEP 2A.** Check the low pressure shutdown SIGNAL wire for an open circuit. | Less than 10 ohms? |
|  | **STEP 2B.** Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. | Greater than 100k ohms? |

### STEP 1. Check the customer interface box (C.I.B.) wiring.

#### STEP 1A. Check the low pressure shutdown SIGNAL wire for an open circuit.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low oil pressure shutdown SIGNAL wire for an open circuit. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on the low oil pressure shutdown SIGNAL terminal on the X1 connector. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on each of the remaining terminals in the X1 connector. | Greater than 100k ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
| Greater than 100k ohms? **NO** | 1C |  |

#### STEP 1C. Check the low pressure shutdown SIGNAL wire for a short circuit to ground.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low pressure shutdown SIGNAL wire for a short circuit to ground. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on the panel ground. | Greater than 100k ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
| Greater than 100k ohms? **NO** | 2A |  |

### STEP 2. Check the engine harness to the C.I.B. cable.

#### STEP 2A. Check the low oil pressure shutdown SIGNAL wire for an open circuit.

| **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C4 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low oil pressure shutdown SIGNAL wire for an open circuit. Place a jumper between the low oil pressure shutdown SIGNAL pin and the common shutdown SIGNAL pin in the C4 connector. Place one test lead in the low oil pressure shutdown SIGNAL pin of the C1 connector. Place the other test lead in the common shutdown SIGNAL pin of the C1 connector. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit.

| **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C4 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low pressure shutdown SIGNAL wire for a wire-to-wire short circuit. Place one test lead on the low oil pressure shutdown SIGNAL pin in connector C1. Place the other test lead on each of the remaining pins in the C1 connector. | Greater than 100k ohms? **YESRepair:** Replace the cable. | Repair complete |
| Greater than 100k ohms? **NORepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |  |
