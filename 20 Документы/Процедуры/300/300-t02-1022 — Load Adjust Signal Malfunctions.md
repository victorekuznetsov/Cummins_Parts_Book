---
aliases:
  - "Неисправности сигнала регулировки нагрузки"
type: "Процедура"
doc: "300-t02-1022"
title_en: "Load Adjust Signal Malfunctions"
title_ru: "Неисправности сигнала регулировки нагрузки"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1022.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1022.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Load Adjust Signal Malfunctions
**Неисправности сигнала регулировки нагрузки**

> [!abstract] Процедура · `300-t02-1022`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1022.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1022.pdf)

Printable Version

### Symptoms

- Engine does **not** respond to load adjust request.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

None.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
|  | **STEP 1A.** Check the droop adjust potentiometer SUPPLY wire. | Less than 10 ohms? |
|  | **STEP 1B.** Check the droop adjust potentiometer RETURN wire. | Less than 10 ohms? |
|  | **STEP 1C.** Check the frequency adjust SIGNAL wire. | Less than 10 ohms? |
| STEP 2. | Check the engine harness to the C.I.B. |  |
|  | **STEP 2A.** Check the frequency adjust SUPPLY and SIGNAL wires. | Less than 10 ohms? |
|  | **STEP 2B.** Check the frequency adjust RETURN and SIGNAL wires. | Less than 10 ohms? |

### STEP 1. Check the C.I.B. wiring.

#### STEP 1A. Check the droop adjust potentiometer SUPPLY wire.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer SUPPLY wire. Place one test lead on the droop adjust potentiometer 5 volt SUPPLY pin in connector C1. Place the other test lead on the droop adjust potentiometer 5 volt supply terminal on the X1 connector. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the droop adjust potentiometer RETURN wire.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the droop adjust potentiometer RETURN wire. Place one test lead on the droop adjust potentiometer RETURN pin in connector C1. Place the other test on droop adjust potentiometer return terminal on the X1 connector. | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

#### STEP 1C. Check the frequency adjust SIGNAL wire.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the frequency adjust SIGNAL wire. Place one test lead on the generator output frequency adjust potentiometer SIGNAL pin in connector C1. Place the other test lead on the generator output frequency adjust potentiometer signal terminal on the X1 connector. | Less than 10 ohms? **YES** | 2A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

### STEP 2. Check the engine harness to the C.I.B.

#### STEP 2A. Check the frequency adjust SUPPLY and SIGNAL wires.

| **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable from the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check frequency adjust SUPPLY and SIGNAL wires. Place a jumper between the droop adjust potentiometer 5 volt SUPPLY pin and the generator output frequency adjust potentiometer SIGNAL pin in the engine-side connection. Place one test lead in the droop adjust potentiometer 5 volt SUPPLY pin of the C1 connector. Place the other test lead in the generator output frequency adjust potentiometer SIGNAL pin of the C1 connector. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |

#### STEP 2B. Check the frequency adjust RETURN and SIGNAL wires.

| **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B to engine harness cable from the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check frequency adjust RETURN and SIGNAL wires. Place a jumper between the generator output frequency adjust potentiometer SIGNAL pin and the droop adjust potentiometer RETURN pin in the engine-side connection. Place one test lead in the droop adjust potentiometer RETURN pin of the C1 connector. Place the other test lead in the generator output frequency adjust potentiometer SIGNAL pin of the C1 connector. | Less than 10 ohms? **YESRepair:** Use the following for potentiometer repair instructions. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF, or the ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF, X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF or refer to the equipment manufacturer service information. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
