---
aliases:
  - "Неисправность сигнала датчика утечки топлива"
type: "Процедура"
doc: "116-t02-1117"
title_en: "Fuel Leakage Switch Signal Malfunction"
title_ru: "Неисправность сигнала датчика утечки топлива"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1117.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1117.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Fuel Leakage Switch Signal Malfunction
**Неисправность сигнала датчика утечки топлива**

> [!abstract] Процедура · `116-t02-1117`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1117.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1117.pdf)

Printable Version

### Symptoms

- OEM fuel leakage switch has malfunctioned.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The fuel leakage switch is a normally closed switch. The alarm sounds when there is an open in the circuit.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box wiring. |  |
|  | **STEP 1A.** Check the fuel leakage signal and return wires for an open. |  |
|  | **STEP 1B.** Check the fuel leakage signal and return wires for a wire-to-wire short. |  |
|  | **STEP 1C.** Check the fuel leakage signal wire for a short to ground. |  |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the fuel leakage signal and return wires for an open. |  |
|  | **STEP 2B.** Check the fuel leakage signal and return wires for a wire-to-wire short. |  |
|  | **STEP 2C.** Check the fuel leakage signal wire for a short to ground. |  |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the fuel leakage signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the fuel leakage signal and return wires at remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel leakage signal and return wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the fuel leakage signal wire at the remote input/output unit. Place the other test lead on the fuel leakage signal pin at the C4 connector. Place one test lead on the fuel leakage return wire at the remote input/output unit. Place the other test lead on the fuel leakage return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the fuel leakage signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the fuel leakage signal and return wires at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel leakage signal and return wires for a wire-to-wire short. Place one test lead on the fuel leakage signal pin at the remote input/output unit. Place the other test lead on all other pins at the remote input/output unit. Place one test lead on the fuel leakage return pin at the remote input/output unit. Place the other test lead on all other pins at the remote input/output unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the fuel leakage signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the fuel leakage signal wire at the remote input/output unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel leakage signal wire for a short to ground. Place one test lead on the fuel leakage signal wire at the remote input/output unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the fuel leakage signal and return wires for an open.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the fuel leakage sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel leakage signal and return wires for an open. NOTE: An alarm will sound on the remote input/output unit when an open is detected. Place one test lead on the fuel leakage signal pin at the C4 connector. Place the other test lead on the fuel leakage signal pin at the C11 connector. Place one test lead on the fuel leakage return pin at the C4 connector. Place the other test lead on the fuel leakage return pin at the C11 connector. Place one test lead on the fuel leakage signal pin at the C11 connector. Place the other test lead on the fuel leakage signal pin at the sensor connector. Place one test lead on the fuel leakage return pin at the C11 connector. Place the other test lead on the fuel leakage return pin at the sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the fuel leakage signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the fuel leakage sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel leakage signal and return wires for a wire-to-wire short. Place one test lead on the fuel leakage signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the fuel leakage signal pin at the C11 connector. Place the other test lead on all other pins at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the fuel leakage signal wire for a short to ground.

| **Conditions:** Disconnect the OEM harness at the C4 and C11 connectors. Disconnect the fuel leakage sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the fuel leakage signal wire for a short to ground. Place one test lead on the fuel leakage signal pin at the C4 connector. Place the other test lead on engine ground. Place one test lead on the fuel leakage signal pin at the C11 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the fuel leakage switch. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
