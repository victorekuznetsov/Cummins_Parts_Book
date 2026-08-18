---
aliases:
  - "Двигатель не останавливается при низком давлении масла в верхнем диапазоне частот"
type: "Процедура"
doc: "116-t02-1073"
title_en: "Engine Does Not Shut Down with High Speed Range Low Lubricating Oil Pressure"
title_ru: "Двигатель не останавливается при низком давлении масла в верхнем диапазоне частот"
modified: "2008-03-20"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1073.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1073.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Engine Does Not Shut Down with High Speed Range Low Lubricating Oil Pressure
**Двигатель не останавливается при низком давлении масла в верхнем диапазоне частот**

> [!abstract] Процедура · `116-t02-1073`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-03-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1073.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1073.pdf)

Printable Version

### Symptoms

- The SDU410 will **not** shut down the engine if low lubricating oil pressure exists.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown. The SDU410 unit is designed to **not** listen to this circuit unless the engine speed is above a certain threshold (1400 rpm).

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box |  |
|  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
|  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC | Less than +24-VDC? |
| STEP 2. | Check customer interface box wiring |  |
|  | **STEP 2A.** Check the high speed oil pressure signal and return wires for an open. | Less than 10 ohms? |
| STEP 3. | Check the OEM wiring harness |  |
|  | **STEP 3A.** Check the high speed oil pressure signal and return wires for an open. | Less than 10 ohms? |

### STEP 1. Check customer interface box

#### STEP 1A. Check the customer interface box logic unit LED illumination.

| **Conditions:** Check the DCU410 unit for alarms and LED illumination. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for alarms and LED illumination on the DCU410 unit. | Are any alarms active or LEDs illuminated? **YES** | Contact a Cummins® Authorized Repair Location |
| Are any alarms active or LEDs illuminated? **NO** | 1B |  |

#### STEP 1B. Check the DCU410 power supply wire for +24-VDC.

| **Conditions:** Open the customer interface box |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the shutdown unit supply 24-VDC at the SDU410 unit. Place one test lead on the shutdown unit supply 24-VDC supply wire at the SDU410 unit. Place the other test lead on the shutdown unit return wire at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than +24-VDC? **NO** | 2A |  |

### STEP 2. Check customer interface box wiring

#### STEP 2A. Check the high speed oil pressure signal and return wires for an open.

| **Conditions:** Open the customer interface box Disconnect customer interface box to OEM harness cable connector C4 from the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high speed oil pressure signal and return wires for an open. Place one test lead on the high speed oil pressure signal wire at the SDU410 unit. Place the other test lead on the high speed oil pressure signal pin at the C4 connector. Place one test lead on the high speed oil pressure return wire at the SDU410 unit. Place the other test lead on the high speed oil pressure return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | 3A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

### STEP 3. Check the OEM wiring harness

#### STEP 3A. Check the high speed oil pressure signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect customer interface box to OEM harness cable connector C4 from the customer interface box. Disconnect the OEM disconnect C11 connector at its location. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check high speed oil pressure signal wire for an open. Place one test lead on the high speed oil pressure signal wire at the C4 connector. Place the other test lead on the high speed oil pressure signal wire at the C11 connector. Place one test lead on the high speed oil pressure return wire at the C4 connector. Place the other test lead on the high speed oil pressure return wire at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Contact a Cummins® Authorized Repair Location |  |
