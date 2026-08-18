---
aliases:
  - "Неверная идентификация двигателя при синхронизации агрегатов"
type: "Процедура"
doc: "116-t02-1055"
title_en: "Multiple Unit Synchronization Engine Identification Not Correct"
title_ru: "Неверная идентификация двигателя при синхронизации агрегатов"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1055.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1055.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Multiple Unit Synchronization Engine Identification Not Correct
**Неверная идентификация двигателя при синхронизации агрегатов**

> [!abstract] Процедура · `116-t02-1055`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1055.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1055.pdf)

Printable Version

### Symptoms

Engine identifier is **not** displaying correctly at the DCU410 unit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
|  | **STEP 1B.** Check the multiple unit synchronization circuits for an open. |  |
|  | **STEP 1C.** Check the multiple unit synchronization circuits for a wire-to-wire short. |  |
|  | **STEP 1D.** Check the multiple unit synchronization circuits for a short to ground. |  |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the multiple unit synchronization circuits for an open. |  |
|  | **STEP 2B.** Check the multiple unit synchronization circuits for a wire-to-wire short. |  |
|  | **STEP 2C.** Check the multiple unit synchronization circuits for a short to ground. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
| DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage (switched power) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 1B |  |

#### STEP 1B. Check the multiple unit synchronization circuits for an open.

| **Conditions:** Open the customer interface box. Disconnect the multiple unit synchronization ID pin 3 switch signal wire from the CLU and C2 connectors. Disconnect the multiple unit synchronization ID pin 2 switch signal wire from the CLU and C2 connectors. Disconnect the multiple unit synchronization ID pin 1 switch signal wire from the CLU and C2 connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the multiple unit synchronization switch signal wires for an open. Place one test lead on the multiple unit synchronization ID pin 3 switch signal wire at the CLU connector. Place the other test lead on the multiple unit synchronization ID pin 3 switch signal wire at the C2 connector. Place one test lead on the multiple unit synchronization ID pin 2 switch signal wire at the CLU connector. Place the other test lead on the multiple unit synchronization ID pin 2 switch signal wire at the C2 connector. Place one test lead on the multiple unit synchronization ID pin 1 switch signal wire at the CLU connector. Place the other test lead on the multiple unit synchronization ID pin 1 switch signal wire at the C2 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1C. Check the multiple unit synchronization circuits for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the CLU connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the multiple unit synchronization switch signal wires for a wire-to-wire short. Place one test lead on the multiple unit synchronization ID pin 3 switch signal wire at the CLU connector. Place the other test lead on all other wires at the CLU connector. Place one test lead on the multiple unit synchronization ID pin 2 switch signal wire at the CLU connector. Place the other test lead on all other wires at the CLU connector. Place one test lead on the multiple unit synchronization ID pin 1 switch signal wire at the CLU connector. Place the other test lead on all other wires at the CLU connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
| Less than 10 ohms? **NORepair:** Replace the CLU unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1D. Check the multiple unit synchronization circuits for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the CLU connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the multiple unit synchronization switch signal wires for a short to ground. Place one test lead on the multiple unit synchronization ID pin 3 switch signal wire at the CLU connector. Place the other test lead on panel ground. Place one test lead on the multiple unit synchronization ID pin 2 switch signal wire at the CLU connector. Place the other test lead on panel ground. Place one test lead on the multiple unit synchronization ID pin 1 switch signal wire at the CLU connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the CLU unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the multiple unit synchronization circuits for an open.

| **Conditions:** Locate the OEM wiring harness. Disconnect the multiple unit synchronization ID pin 3 switch signal wire from the C2 and 50-pin ECM connector. Disconnect the multiple unit synchronization ID pin 2 switch signal wire from the C2 and 50-pin ECM connector. Disconnect the multiple unit synchronization ID pin 1 switch signal wire from the C2 and 50-pin ECM connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the multiple unit synchronization switch signal wires for an open. Place one test lead on the multiple unit synchronization ID pin 3 switch signal wire at the C2 connector on panel. Place the other test lead on the multiple unit synchronization ID pin 3 switch signal wire at the 50-pin ECM connector. Place one test lead on the multiple unit synchronization ID pin 2 switch signal wire at the C2 connector on panel. Place the other test lead on the multiple unit synchronization ID pin 2 switch signal wire at the 50-pin ECM connector. Place one test lead on the multiple unit synchronization ID pin 1 switch signal wire at the C2 connector on panel. Place the other test lead on the multiple unit synchronization ID pin 1 switch signal wire at the 50-pin ECM connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the multiple unit synchronization circuits for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the multiple unit synchronization switch signal wires for a wire-to-wire short. Place one test lead on the multiple unit synchronization ID pin 3 switch signal wire at the C2 connector. Place the other test lead on all other wires at the C2 connector. Place one test lead on the multiple unit synchronization ID pin 2 switch signal wire at the C2 connector. Place the other test lead on all other wires at the C2 connector. Place one test lead on the multiple unit synchronization ID pin 1 switch signal wire at the C2 connector. Place the other test lead on all other wires at the C2 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace connector. [[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|Refer to Procedure 019-208 (Deutsch&trade; HD20 and HD30 Connector Series) in Section 19 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493 or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533.]] | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the multiple unit synchronization circuits for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the multiple unit synchronization switch signal wires for a short to ground. Place one test lead on the multiple unit synchronization ID pin 3 switch signal wire at the C2 connector. Place the other test lead on panel ground. Place one test lead on the multiple unit synchronization ID pin 2 switch signal wire at the C2 connector. Place the other test lead on panel ground. Place one test lead on the multiple unit synchronization ID pin 1 switch signal wire at the C2 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace connector. [[99-019-208 — Deutsch HDP20 and HD30 Connector Series\|Refer to Procedure 019-208 (Deutsch&trade; HD20 and HD30 Connector Series) in Section 19 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System, Bulletin 4021493 or the Troubleshooting and Repair Manual, Electronic Control System, QSK38, QSK50, and QSK60 (CM850 Modular Common Rail System), Bulletin 4021533.]] | Repair complete |
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
