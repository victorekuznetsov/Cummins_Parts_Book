---
aliases:
  - "Двигатель работает только в номинальном режиме"
type: "Процедура"
doc: "300-t02-1027"
title_en: "Engine Only Operates in Rated Mode"
title_ru: "Двигатель работает только в номинальном режиме"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1027.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1027.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Engine Only Operates in Rated Mode
**Двигатель работает только в номинальном режиме**

> [!abstract] Процедура · `300-t02-1027`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1027.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1027.pdf)

Printable Version

### Symptoms

- The engine will **only** operate in rated mode.

### How To Use This Tree

This symptom tree can be used to troubleshoot engine symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

None.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
|  | **STEP 1A.** Check the idle/rated switch SIGNAL wire with the engine harness disconnected. | Less than 10 ohms? |
|  | **STEP 1B.** Check the idle/rated switch RETURN wire with the engine harness disconnected. | Less than 10 ohms? |
| STEP 2. | Check the engine harness to the C.I.B. |  |
|  | **STEP 2A.** Check the idle/rated switch SIGNAL wire. | Less than 10 ohms? |

### STEP 1. Check the customer interface box (C.I.B.) wiring.

#### STEP 1A. Check the idle/rated switch SIGNAL wire with the engine harness disconnected.

| **Conditions:** Open the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the idle/rated switch SIGNAL wire. Disconnect the idle/rated switch SIGNAL wire from the X1 connector. Place one test lead on the idle/rated switch SIGNAL pin in connector C1. Place the other test lead on idle rated switch SIGNAL pin on the X1 connector. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the idle/rated switch RETURN wire with the engine harness disconnected.

| **Conditions:** Open the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the idle/rated switch RETURN wire. Disconnect the idle/rated switch RETURN wire from the X1 connector. Place one test lead on the idle/rated switch return terminal. Place the other test lead on the idle rated switch RETURN pin on the X1 connector. | Less than 10 ohms? **YES** | 2A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

### STEP 2. Check the engine harness to the C.I.B.

#### STEP 2A. Check the idle/rated switch SIGNAL wire.

| **Conditions:** Disconnect the C.I.B. to the engine harness cable connector C1 from the C.I.B. Disconnect the C.I.B. to the engine harness cable connector C10 from the engine harness. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the idle/rated switch SIGNAL wire. Place one test lead in the idle/rated switch SIGNAL pin of the C1 connector. Place the other test lead in the idle/rated switch SIGNAL pin of the C10 connector. | Less than 10 ohms? **YESRepair:** Use the following for idle switch repair instructions. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or the ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or the X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF; or the equipment manufacturer service information. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the cable. | Repair complete |  |
