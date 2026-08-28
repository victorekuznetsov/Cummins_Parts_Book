---
aliases:
  - "Неисправность сигнала впускного коллектора 3"
type: "Процедура"
doc: "116-t02-1120"
title_en: "Intake Manifold 3 Signal Malfunction"
title_ru: "Неисправность сигнала впускного коллектора 3"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1120.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1120.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Intake Manifold 3 Signal Malfunction
**Неисправность сигнала впускного коллектора 3**

> [!abstract] Процедура · `116-t02-1120`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1120.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1120.pdf)

Printable Version

### Symptoms

- The OEM charge air temperature (right bank front) sensor has malfunctioned.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The charge air temperature (right bank front) sensor is connected to the Alarm and Safety C4 connector located on the customer interface box.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box wiring. |  |
|  | **STEP 1A.** Check the charge air temperature (right bank front) signal, return, and return 2 wires for an open. |  |
|  | **STEP 1B.** Check the charge air temperature (right bank front) signal, return, and return 2 wires for a wire to wire short. |  |
|  | **STEP 1C.** Check the charge air temperature (right bank front) signal wire for a short to ground. | Less than 10 ohms? |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the charge air temperature (right bank front) signal, return, and return 2 wires for an open. |  |
|  | **STEP 2B.** Check the charge air temperature (right bank front) signal, return, and return 2 wires for a wire to wire short. |  |
|  | **STEP 2C.** Check the charge air temperature (right bank front) signal wire for a short to ground. | Less than 10 ohms? |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the charge air temperature (right bank front) signal, return, and return 2 wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the charge air temperature (right bank front) signal, return, and return 2 wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the charge air temperature (right bank front) signal, return, and return 2 wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the charge air temperature (right bank front) signal wire at the remote input/output unit. Place the other test lead on the charge air temperature (right bank front) signal pin at the C4 connector. Place one test lead on the charge air temperature (right bank front) return wire at the remote input/output unit. Place the other test lead on the charge air temperature (right bank front) return pin at the C4 connector. Place one test lead on the charge air temperature (right bank front) return 2 wire at the remote input/output unit. Place the other test lead on the charge air temperature (right bank front) return 2 pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2A |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the charge air temperature (right bank front) signal, return, and return 2 wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the charge air temperature (right bank front) signal, return, and return 2 wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the charge air temperature (right bank front) signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the charge air temperature (right bank front) signal wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Place one test lead on the charge air temperature (right bank front) return wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Place one test lead on the charge air temperature (right bank front) return 2 wire at the remote input/output unit. Place the other test lead on all other wires at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the charge air temperature (right bank front) signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the charge air temperature (right bank front) signal wire at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the charge air temperature (right bank front) signal wire for a short to ground. Place one test lead on the charge air temperature (right bank front) signal wire at the remote input/output unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the charge air temperature (right bank front) signal, return, and return 2 wires for an open.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the charge air temperature (right bank front) sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the charge air temperature (right bank front) signal, return, and return 2 wires for an open. NOTE: An open has been detected by the remote input/output unit if a false alarm has occurred. Place one test lead on the charge air temperature (right bank front) signal pin at the C4 connector. Place the other test lead on the charge air temperature (right bank front) signal pin at the C11 connector. Place one test lead on the charge air temperature (right bank front) return pin at the C4 connector. Place the other test lead on the charge air temperature (right bank front) return pin at the C11 connector. Place one test lead on the charge air temperature (right bank front) return 2 pin at the C4 connector. Place the other test lead on the charge air temperature (right bank front) return 2 pin at the C11 connector. Place one test lead on the charge air temperature (right bank front) signal pin at the C11 connector. Place the other test lead on the charge air temperature (right bank front) signal pin at the charge air temperature (right bank front) sensor. Place one test lead on the charge air temperature (right bank front) return pin at the C11 connector. Place the other test lead on the charge air temperature (right bank front) return pin at the charge air temperature (right bank front) sensor. Place one test lead on the charge air temperature (right bank front) return 2 pin at the C11 connector. Place the other test lead on the charge air temperature (right bank front) return 2 pin at the charge air temperature (right bank front) sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the charge air temperature (right bank front) signal, return, and return 2 wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the OEM harness at the C4 and C11 connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the charge air temperature (right bank front) signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the charge air temperature (right bank front) signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the charge air temperature (right bank front) return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the charge air temperature (right bank front) return 2 pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the charge air temperature (right bank front) signal wire for a short to ground.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the charge air temperature (right bank front) for a short to ground. Place one test lead on the charge air temperature (right bank front) signal wire at the C4 connector. Place the other test lead on engine ground. Place one test lead on the charge air temperature (right bank front) signal pin at the C11 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the charge air temperature (right bank front) sensor. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
