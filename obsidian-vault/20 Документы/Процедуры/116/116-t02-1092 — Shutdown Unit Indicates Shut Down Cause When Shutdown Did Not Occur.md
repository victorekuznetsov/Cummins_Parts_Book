---
aliases:
  - "Блок останова указывает причину останова, которого не было"
type: "Процедура"
doc: "116-t02-1092"
title_en: "Shutdown Unit Indicates Shut Down Cause When Shutdown Did Not Occur"
title_ru: "Блок останова указывает причину останова, которого не было"
modified: "2008-04-04"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1092.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1092.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Shutdown Unit Indicates Shut Down Cause When Shutdown Did Not Occur
**Блок останова указывает причину останова, которого не было**

> [!abstract] Процедура · `116-t02-1092`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1092.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1092.pdf)

Printable Version

### Symptoms

The engine does **not** shut down, but the SDU410 unit falsely indicates that a shutdown has occurred.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Check that the Shutdown Override is **not** active. If the Shutdown Override is active and no shutdown occurred but an alarm informs operator shut down would have occurred if it had **not** been overridden. Deactivate the shutdown override alarm. If the alarm can **not** be deactivated, reference the appropriate troubleshooting tree.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box |  |
|  | **STEP 1A.** Check for alarm and LED illumination. | LED flashing? |
|  | **STEP 1A-1.** Check the shutdown unit Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1A-2.** Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1A-3.** Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1A-4.** Check the engine protection override signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1A-5.** Check the engine protection override signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1A-6.** Check the engine protection override signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1A-7.** Check the engine protection override relay supply and signal wires for an open. | Less than 10 ohms? |
|  | **STEP 1A-8.** Check the engine protection override relay signal and return wires for wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1A-9.** Check the engine protection override relay signal wire for a short to ground. | Less than 10 ohms? |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check for alarm and LED illumination.

| **Conditions:** Check for alarm and LED illumination. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the Shutdown Override circuit for activation. | LED flashing? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| LED flashing? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1A-2 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1A-2. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1A-3 |  |

#### STEP 1A-3. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1A-4 |  |

#### STEP 1A-4. Check the engine protection override signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override signal and return wires at the SDU410 unit and engine protection override relay. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override signal and return wires for an open. Place one test lead on the engine protection override signal wire at the SDU410 unit. Place the other test lead on the engine protection override signal wire at the engine protection override relay contact. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override return wire at the engine protection override relay contact. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1A-5 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1A-5. Check the engine protection override signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override signal and return wires at the SDU410 unit and engine protection override relay. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override signal and return wires for a wire-to-wire short. Place one test lead on the engine protection override signal wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on all other contacts on the engine protection override relay. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1A-6 |  |

#### STEP 1A-6. Check the engine protection override signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override signal wire at the DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override signal wire for a short to ground. Place one test lead on the engine protection override signal wire at the SDU410 terminal strip. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1A-7 |  |

#### STEP 1A-7. Check the engine protection override relay supply and signal wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override relay supply and signal wires at the engine protection override relay. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override relay supply and signal wires for an open. Place one test lead on the engine protection override relay signal wire at the engine protection override relay. Place the other test lead on the engine protection override relay signal pin at the C3 connector. Place one test lead on the engine protection override relay signal wire at the engine protection override relay. Place the other test lead on the engine protection override relay signal pin at the X4 connector. Place one test lead on the engine protection override return wire at the SDU410 unit. Place the other test lead on the engine protection override relay return wire at the engine protection override relay contact. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1A-8 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1A-8. Check the engine protection override relay signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override relay signal and return wires at the SDU410 unit and engine protection override relay. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override relay signal and return wires for a wire-to-wire short. Place one test lead on the engine protection override relay signal wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the engine protection override relay return wire at the SDU410 unit. Place the other test lead on all other contacts on the engine protection override relay. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1A-9 |  |

#### STEP 1A-9. Check the engine protection override relay signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the engine protection override relay signal wire at the DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine protection override relay signal wire for a short to ground. Place one test lead on the engine protection override relay signal wire at the SDU410 terminal strip. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location |  |
