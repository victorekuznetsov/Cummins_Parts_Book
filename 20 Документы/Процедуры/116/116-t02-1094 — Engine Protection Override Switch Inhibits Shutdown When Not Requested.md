---
aliases:
  - "Выключатель блокировки защиты отменяет останов без запроса"
type: "Процедура"
doc: "116-t02-1094"
title_en: "Engine Protection Override Switch Inhibits Shutdown When Not Requested"
title_ru: "Выключатель блокировки защиты отменяет останов без запроса"
modified: "2008-04-04"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1094.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1094.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Engine Protection Override Switch Inhibits Shutdown When Not Requested
**Выключатель блокировки защиты отменяет останов без запроса**

> [!abstract] Процедура · `116-t02-1094`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1094.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1094.pdf)

Printable Version

### Symptoms

- Check the SDU410 unit shutdown override LED stays on when the shutdown override switch is deactivated at the SDU410 connector.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 input signals are switches. These switches are normally open and closed to activate a shutdown.

Try removing the shutdown override wires from the SDU410 unit. If the LED stays on (with wires removed), then the SDU410 unit has malfunctioned.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box |  |
|  | **STEP 1A.** Check the customer interface box logic unit LED illumination. | Are any alarms active or LEDs illuminated? |
|  | **STEP 1B.** Check the SDU410 power supply wire for +24-VDC. | Less than +24-VDC? |
| STEP 2. | Check customer interface box wiring |  |
|  | **STEP 2A.** Check the engine override protection signal and return wires for an open. | Less than 10 ohms? |
| STEP 3. | Check voltage at engine protection override relay |  |
|  | **STEP 3A.** Check the engine protection override relay supply and signal wires for voltage. | Less than +24-VDC? |

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

#### STEP 2A. Check the engine protection override relay signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override relay signal and return wires at the SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override relay signal and return wires for an open. Place one test lead on the engine protection override relay signal wire at the SDU410 unit. Place the other test lead on the engine protection override relay signal wire at the relay contact. Place one test lead on the engine protection override relay return wire at the SDU410 unit. Place the other test lead on the engine protection override relay return wire at the relay contact. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than 10 ohms? **YES** | 3A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the relay. Contact an Cummins® Authorized Repair Location for replacement of the relay. | Repair complete |  |

### STEP 3. Check voltage at engine protection override relay

#### STEP 3A. Check the engine protection override relay supply and signal wires for voltage.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override relay supply and signal wires for voltage. Place one test lead on the engine protection override relay signal wire at the SDU410 unit. Place the other test lead on the engine protection override relay signal wire at the relay contact. Place one test lead on the engine protection override relay return wire at the SDU410 unit. Place the other test lead on the engine protection override relay return wire at the relay contact. Refer to the appropriate circuit diagram or wiring diagram for connection pin identification. | Less than +24-VDC? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the relay. Contact an Cummins® Authorized Repair Location for replacement of the relay. | Repair complete |
| Less than +24-VDC? **NO** | Contact a Cummins® Authorized Repair Location |  |
