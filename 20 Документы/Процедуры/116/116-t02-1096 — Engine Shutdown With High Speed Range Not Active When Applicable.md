---
aliases:
  - "Останов двигателя без активного верхнего диапазона частот, когда он применим"
type: "Процедура"
doc: "116-t02-1096"
title_en: "Engine Shutdown With High Speed Range Not Active When Applicable"
title_ru: "Останов двигателя без активного верхнего диапазона частот, когда он применим"
modified: "2009-07-17"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1096.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1096.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Engine Shutdown With High Speed Range Not Active When Applicable
**Останов двигателя без активного верхнего диапазона частот, когда он применим**

> [!abstract] Процедура · `116-t02-1096`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2009-07-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1096.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1096.pdf)

Printable Version

### Symptoms

- The SDU410 unit is **not** reacting to the high speed range sensor when activated and does **not** shut down the engine.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.

The SDU410 unit has two lube oil pressure sensors. One for the low engine speed range (LSR) and one for the high engine speed range (HSR). The LSR sensor is **always** active, but the HSR sensor is **only** active when the engine speed is above 1400 rpm.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box |  |
|  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
|  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
| STEP 2. | Check engine speed |  |
|  | **STEP 2A.** Check the engine speed on the SDU410 unit display. | Engine speed above 1400 rpm? |
| STEP 3. | Check OEM harness to customer interface box cable |  |
|  | **STEP 3A.** Check the engine speed 1 and engine speed 2 signal and return wires for an open. | Less than 10 ohms? |

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

### STEP 2. Check engine speed

#### STEP 2A. Check the engine speed reading on the SDU410 unit.

| **Conditions:** Engine running. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed. Verify the engine speed on the SDU410 unit display. | Engine speed above 1400 rpm? **YESRepair:** Check the SDU410 configuration. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Engine speed above 1400 rpm? **NORepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | 3A |  |

### STEP 3. Check OEM Harness to customer interface box cable

#### STEP 3A. Check the engine speed 1 and engine speed 2 signal and return wires for an open.

| **Conditions:** Disconnect customer interface box to OEM harness cable connector. Disconnect the OEM disconnect C11 connector on engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 and engine speed 2 signal and return wires for an open. Place one test lead on the engine speed 1 signal at the C4 connector. Place the other test lead on the engine speed 1 signal wire at the OEM C11 connector. Place one test lead on the engine speed 1 return at the C4 connector. Place the other test lead on the engine speed 1 return wire at the OEM C11 connector. Place one test lead on the engine speed 2 signal at the C4 connector. Place the other test lead on the engine speed 2 signal wire at the OEM C11 connector. Place one test lead on the engine speed 2 return at the C4 connector. Place the other test lead on the engine speed 2 return wire at the OEM C11 connector. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the OEM wiring harness. Refer to the OEM installation instructions. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Contact a Cummins® Authorized Repair Location |  |
