---
aliases:
  - "Блок останова самопроизвольно останавливает двигатель"
type: "Процедура"
doc: "116-t02-1080"
title_en: "Shutdown Unit Shuts Engine Down Un-Requested"
title_ru: "Блок останова самопроизвольно останавливает двигатель"
modified: "2009-07-15"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1080.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1080.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Shutdown Unit Shuts Engine Down Un-Requested
**Блок останова самопроизвольно останавливает двигатель**

> [!abstract] Процедура · `116-t02-1080`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2009-07-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1080.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1080.pdf)

Printable Version

### Symptoms

- The SDU410 will shut down the engine with ignition keyswitch in the ON position. An open exists in the power on supply and signal circuit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box |  |
|  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
|  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
| STEP 2. | Check customer interface box wiring |  |
|  | **STEP 2A.** Check the power on supply and signal wires for an open. | Less than 10 ohms? |
|  | **STEP 2B.** Check the power on supply and signal wires for voltage. | Less than +24-VDC? |
| STEP 3. | Check the OEM harness to customer interface box cable |  |
|  | **STEP 3A.** Check the ignition (engine stop) supply wire for an open. | Less than 10 ohms? |

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

#### STEP 2A. Check the power on supply and signal wires for an open.

| **Conditions:** Open the customer interface box Disconnect the wire at the power on supply and power on signal wires at the SDU410 unit and the power on supply and signal wires at the customer logic unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power on supply and signal wires for an open. Place one test lead on the power on supply wire at the SDU410 unit. Place the other test lead on the power on supply wire at the customer interface box logic unit. Place one test lead on the power on signal wire at the SDU410 unit. Place the other test lead on the power on signal wire at the customer interface box logic unit. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the power on supply and signal wires for voltage.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power on supply and signal wires for voltage. Place one test lead on the power on supply wire at the SDU410 unit. Place the other test lead on the panel ground. Place one test lead on the power on signal wire at the customer interface box logic unit. Place the other test lead on the panel ground. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than +24-VDC? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | 3A |
| Less than +24-VDC? **NO** | Repair complete |  |

### STEP 3. Check OEM harness to customer interface box cable

#### STEP 3A. Check the ignition (engine stop) supply wire for an open.

| **Conditions:** Disconnect customer interface box to OEM harness cable connector C1 from the customer interface box. Disconnect the OEM harness from the C1 connector on the engine. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition (engine stop) supply wire for an open. Place a jumper between the ignition (engine stop) pin in the C1 connector. Place one test lead on the ignition (engine stop) pin in the OEM connector on the engine. Place the other test lead on the ignition (engine stop) pin at the C8 connector. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the OEM wiring harness. Refer to the OEM installation instructions. | Contact a Cummins® Authorized Repair Location |  |
