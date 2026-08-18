---
aliases:
  - "Неисправность резервного сигнала температуры"
type: "Процедура"
doc: "116-t02-1121"
title_en: "Spare Temperature Signal Malfunction"
title_ru: "Неисправность резервного сигнала температуры"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Spare Temperature Signal Malfunction
**Неисправность резервного сигнала температуры**

> [!abstract] Процедура · `116-t02-1121`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1121.pdf)

Printable Version

### Symptoms

- The OEM spare temperature sensor has malfunctioned.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The spare temperature sensor is connected to the Alarm and Safety C4 connector located on the customer interface box.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box wiring. |  |
|  | **STEP 1A.** Check the spare temperature signal, return, and return 2 wires for an open. |  |
|  | **STEP 1B.** Check the spare temperature signal, return, and return 2 wires for a wire-to-wire short. |  |
|  | **STEP 1C.** Check the spare temperature signal wire for a short to ground. |  |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the spare temperature signal, return, and return 2 wires for an open. |  |
|  | **STEP 2B.** Check the spare temperature signal, return, and return 2 wires for a wire-to-wire short. |  |
|  | **STEP 2C.** Check the spare temperature signal wire for a short to ground. |  |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the spare temperature signal, return, and return 2 wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the spare temperature signal, return, and return 2 wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the spare temperature signal, return, and return 2 wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the spare temperature signal wire at the remote input/output unit. Place the other test lead on the spare temperature signal pin at the C4 connector. Place one test lead on the spare temperature return wire at the remote input/output unit. Place the other test lead on the spare temperature return pin at the C4 connector. Place one test lead on the spare temperature return 2 wire at the remote input/output unit. Place the other test lead on the spare temperature return 2 pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the spare temperature signal, return, and return 2 wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the spare temperature signal, return, and return 2 wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the spare temperature signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the spare temperature signal wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Place one test lead on the spare temperature return wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Place one test lead on the spare temperature return 2 wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1B. Check the spare temperature signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the spare temperature signal, return, and return 2 wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the spare temperature signal wire for a short to ground. Place one test lead on the spare temperature signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the spare temperature signal, return, and return 2 wires for an open.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the spare temperature sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the spare temperature signal, return, and return 2 wires for an open. NOTE: An open has been detected by the remote input/output unit if a false alarm has occurred. Place one test lead on the spare temperature signal pin at the C4 connector. Place the other test lead on the spare temperature signal pin at the C11 connector. Place one test lead on the spare temperature return pin at the C4 connector. Place the other test lead on the spare temperature return pin at the C11 connector. Place one test lead on the spare temperature return 2 pin at the C4 connector. Place the other test lead on the spare temperature return 2 pin at the C11 connector. Place one test lead on the spare temperature signal pin at the C11 connector. Place the other test lead on the spare temperature signal pin at the spare temperature sensor. Place one test lead on the spare temperature return pin at the C11 connector. Place the other test lead on the spare temperature return pin at the spare temperature sensor. Place one test lead on the spare temperature return 2 pin at the C11 connector. Place the other test lead on the spare temperature return 2 pin at the spare temperature sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the spare temperature signal, return, and return 2 wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the spare temperature sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the spare temperature signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the spare temperature signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the spare temperature return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the spare temperature return 2 pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the spare temperature signal pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Place one test lead on the spare temperature return pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Place one test lead on the spare temperature return 2 pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the spare temperature signal wire for a short to ground.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the spare temperature sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the spare temperature for a short to ground. Place one test lead on the spare temperature signal wire at the C4 connector. Place the other test lead on engine ground. Place one test lead on the spare temperature signal pin at the C11 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the spare temperature sensor. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
