---
aliases:
  - "Реле блока останова не индицирует активную неисправность"
type: "Процедура"
doc: "116-t02-1097"
title_en: "Shutdown Unit Relay Does Not Indicate Fault When Fault is Active"
title_ru: "Реле блока останова не индицирует активную неисправность"
modified: "2008-04-04"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1097.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1097.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Shutdown Unit Relay Does Not Indicate Fault When Fault is Active
**Реле блока останова не индицирует активную неисправность**

> [!abstract] Процедура · `116-t02-1097`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1097.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1097.pdf)

Printable Version

### Symptoms

- Data link circuit is malfunctioning between the SDU410 and DCU410 exists.

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
|  | **STEP 2A.** Check the shutdown unit Modicon™ communication buss circuit for an open. | Less than 10 ohms? |
|  | **STEP 2B.** Check the shutdown unit Modicon™ communication buss circuit for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 2C.** Check the shutdown unit Modicon™ communication buss circuit for a short to ground. | Less than 10 ohms? |
|  | **STEP 2D.** Check to make sure the DCU410 unit is communicating with the SDU410 unit. |  |

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

#### STEP 2A. Check the shutdown unit Modicon™ communication buss circuit for an open.

| **Conditions:** Open the customer interface box Disconnect the signal and return wires at the shutdown unit Modicon™ communication buss circuit at the SDU410 and DCU410 terminal strips. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication buss circuit for an open. Place one test lead on the shutdown unit Modicon™ communication buss supply wire at the SDU410 terminal strip. Place the other test lead on the shutdown unit Modicon™ communication buss supply at the DCU410 terminal strip. Place one test lead on the shutdown unit Modicon™ communication buss return wire at the SDU410 terminal strip. Place the other test lead on the shutdown unit Modicon™ communication buss return at the DCU410 terminal strip. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the shutdown unit Modicon™ communication buss circuit for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the signal and return wires at the shutdown unit Modicon™ communication buss circuit at the SDU410 and DCU410 terminal strips. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communicaton buss circuit for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication buss supply wire on the SDU410 terminal strip. Place the other test lead on all other pins on the terminal strip at the SDU410. Place one test lead on the shutdown unit Modicon™ communication buss return wire on the SDU410 terminal strip. Place the other test lead on all other pins on the terminal strip at the SDU410. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the shutdown unit Modicon™ communication buss circuit for short to ground.

| **Conditions:** Open the customer interface box. Disconnect the signal and return wire at the shutdown unit Modicon™ communication buss circuit at the SDU410 and DCU410 terminal strips. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication buss circuit for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2D |  |

#### STEP 2D. Check the DCU410 troubleshooting display.

| **Conditions:** |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check to make sure the DCU410 unit is communicating with the SDU410 unit. Check the DCU410 for correct configuration. | Is the DCU410 communicating with SDU410 unit? **YES** | Repair complete |
| Is the DCU410 communicating with SDU410 unit? **NORepair:** Check the configuration. Contact a Cummins® Authorized Repair Location. | Contact a Cummins® Authorized Repair Location |  |
