---
aliases:
  - "Ложный сигнал останова по разносу на блоке останова"
type: "Процедура"
doc: "116-t02-1102"
title_en: "False Overspeed Shut Down Signal at Shutdown Unit"
title_ru: "Ложный сигнал останова по разносу на блоке останова"
modified: "2008-04-04"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1102.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1102.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# False Overspeed Shut Down Signal at Shutdown Unit
**Ложный сигнал останова по разносу на блоке останова**

> [!abstract] Процедура · `116-t02-1102`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1102.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1102.pdf)

Printable Version

### Symptoms

- The SDU410 shuts down engine due to overspeed even though engine was running at normal speed.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box wiring |  |
|  | **STEP 1A.** Check the SDU410 unit for alarms and LED illumination. | LED flashing rapidly? |
|  | **STEP 1A-1.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1B.** Check the SDU410 unit configuration. | Is threshold value correct? |
|  | **STEP 1C.** Check the engine speed 1 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1C-1.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1D.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
|  | **STEP 1D-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector. | Less than 10 ohms? |
|  | **STEP 1E.** Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
|  | **STEP 1E-1.** Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector. | Less than 10 ohms? |
| STEP 2. | Check the OEM wiring harness |  |
|  | **STEP 2A.** Check the engine speed 1 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2A-1.** Check the engine speed 2 signal and return wires for an open at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2B.** Check the engine speed 1 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2B-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2C.** Check the engine speed 1 signal wire for a short to ground at the C4 and C11 connectors. | Less than 10 ohms? |
|  | **STEP 2C-1.** Check the engine speed 2 signal wire for a short to ground at the C4 and C11 connectors. | Less than 10 ohms? |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the SDU410 unit for alarms and LED illumination.

| **Conditions:** Check for alarm and LED illumination. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SDU410 unit for alarms and flashing LED. Press and hold the overspeed test button to clear overspeed test mode. | LED flashing rapidly? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| LED flashing rapidly? **NO** | 1B |  |

#### STEP 1B. Check the SDU410 unit configuration.

| **Conditions:** Check SDU410 unit configuration parameters. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SDU410 unit configuration. Be sure the engine overspeed threshold is correct. | Is threshold value correct? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | 1C |
| Is threshold value correct? **NORepair:** Set the correct overspeed parameter. Contact a Cummins® Authorized Repair Location. | 1B |  |

#### STEP 1C. Check the engine speed 1 signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the engine speed 1 supply wire at the SDU410 unit. Place the other test lead on the engine speed 1 signal pin at the C4 connector. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on the engine speed 1 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1C-1. Check the engine speed 2 signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on the engine speed 2 signal pin at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on the engine speed 2 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1D. Check the engine speed 1 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on all other wires on the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1D-1 |  |

#### STEP 1D-1. Check the engine speed 2 signal and return wires for a wire-to-wire short at the SDU410 unit and C4 connector.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1E |  |

#### STEP 1E. Check the engine speed 1 signal wire for a short to ground at the SDU410 unit and C4 connector.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal wire from the SDU410 unit and disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal wire for short to ground. Place one test lead on the engine speed 1 signal at the SDU410 unit. Place the other test lead to panel ground. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1E-1 |  |

#### STEP 1E-1. Check the engine speed 2 signal wire for a short to ground at the SDU410 unit and C4 connector.

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
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location |  |
