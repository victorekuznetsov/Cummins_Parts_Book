---
aliases:
  - "Блок останова показывает неверную неисправность датчика частоты"
type: "Процедура"
doc: "116-t02-1100"
title_en: "Shutdown Unit Indicates Incorrect Speed Pickup Fault"
title_ru: "Блок останова показывает неверную неисправность датчика частоты"
modified: "2008-04-04"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1100.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1100.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Shutdown Unit Indicates Incorrect Speed Pickup Fault
**Блок останова показывает неверную неисправность датчика частоты**

> [!abstract] Процедура · `116-t02-1100`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1100.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1100.pdf)

Printable Version

### Symptoms

- The SDU410 unit engine speed value reading is correct, but the SDU410 unit has an alarm for malfunctioned engine speed sensor.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The SDU410 unit has two engine speed input signals. If the signals differ, the SDU410 unit uses the higher of the two readings as the signal.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box wiring |  |
|  | **STEP 1A.** Check the engine speed 1 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1A-1.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1B.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
|  | **STEP 1B-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
|  | **STEP 1C.** Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
|  | **STEP 1C-1.** Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
| STEP 2. | Check the OEM wiring harness |  |
|  | **STEP 2A.** Check the engine speed 1 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2A-1.** Check the engine speed 2 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2B.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2B-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2C.** Check the engine speed 1 signal wire for a short to ground at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2C-1.** Check the engine speed 2 signal wire for a short to ground at the C4 and C11 connectors. | Less than 10 ohms? |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the engine speed 1 signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires from the SDU410 unit and the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the engine speed 1 supply wire at the SDU410 unit. Place the other test lead on the engine speed 1 signal pin at the C4 connector. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on the engine speed 1 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1A-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1A-1. Check the engine speed 2 signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires from the SDU410 unit and the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on the engine speed 2 signal pin at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on the engine speed 2 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1B-1 |  |

#### STEP 1B-1. Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal wire from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal wire for short to ground. Place one test lead on the engine speed 1 signal at the SDU410 unit. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C-1 |  |

#### STEP 1C-1. Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal wire from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal wire for short to ground. Place one test lead on the engine speed 2 signal at the SDU410 unit. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the engine speed 1 signal and return wires for an open at the C4 and C11 connectors.

| **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 1 sensor connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on the engine speed 1 signal pin at the C11 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on the engine speed 1 return pin at the C11 connector. Place one test lead on the engine speed 1 signal pin at the sensor connector. Place the other test lead on the engine speed 1 signal pin at the C11 connector. Place one test lead on the engine speed 1 return pin at the sensor connector. Place the other test lead on the engine speed 1 return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2A-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2A-1. Check the engine speed 2 signal and return wires for an open at the C4 and C11 connectors.

| **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 2 sensor connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the engine speed 2 signal pin at C4 connector. Place the other test lead on the engine speed 2 signal pin at the C11 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on the engine speed 2 return pin at the C11 connector. Place one test lead on the engine speed 2 signal pin at the sensor connector. Place the other test lead on the engine speed 2 signal pin at the C11 connector. Place one test lead on the engine speed 2 return pin at the sensor connector. Place the other test lead on the engine speed 2 return pin at the C11 connector. Refer to the circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the engine speed 1 signal and return wires for a wire-to-wire short at the C4 and C11 connectors.

| **Conditions:** Open the customer interface box. Disconnect the C4 and C11 connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2B-1 |  |

#### STEP 2B-1. Check the engine speed 2 wire signal and return for a wire-to-wire short at the C4 and C11 connectors.

| **Conditions:** Open the customer interface box. Disconnect the C4 and C11 connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the engine speed 1 signal wire for a short to ground at the C4 and C11 connectors.

| **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 1 sensor connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal wire for short to ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C11 connector. Place the other test lead on panel ground. Place one test lead on the engine speed 1 signal pin at the engine speed 1 sensor connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2C-1 |  |

#### STEP 2C-1. Check the engine speed 2 signal wire for a short to ground at the C4 and C11 connectors.

| **Conditions:** Open the customer interface box. Disconnect the C4, C11, and engine speed 2 sensor connectors. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal wire for short to ground. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead to panel ground. Place one test lead on the engine speed 2 signal pin at the C11 connector. Place the other test lead on panel ground. Place one test lead on the engine speed 2 signal pin at the engine speed 2 sensor connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NORepair:** The troubleshooting steps **must** be checked again from the beginning. A fault mode should have been detected. | 1A |  |
