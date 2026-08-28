---
aliases:
  - "Блок останова самопроизвольно перезагружается"
type: "Процедура"
doc: "116-t02-1089"
title_en: "Shutdown Unit Resets Unexpectedly"
title_ru: "Блок останова самопроизвольно перезагружается"
modified: "2008-04-04"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1089.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1089.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Shutdown Unit Resets Unexpectedly
**Блок останова самопроизвольно перезагружается**

> [!abstract] Процедура · `116-t02-1089`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-04-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1089.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1089.pdf)

Printable Version

### Symptoms

- The SDU410 unit acknowledges alarms “on its own” with user interaction.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check customer interface box |  |
|  | **STEP 1A.** Check the DCU410 unit or remote panel for flashing LED. | LED flashing? |
|  | **STEP 1B.** Check the low speed oil pressure signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1B-1.** Check the low speed oil pressure signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1B-2.** Check the low speed oil pressure signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1C.** Check the high speed oil pressure signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1C-1.** Check the high speed oil pressure signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1C-2.** Check the high speed oil pressure signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1D.** Check the coolant pressure signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1D-1.** Check the coolant pressure signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1D-2.** Check the coolant pressure signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1E.** Check the coolant temperature signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1E-1.** Check the coolant temperature signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1E-2.** Check the coolant temperature signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1F.** Check the engine speed 1 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1F-1.** Check the engine speed 1 signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1F-2.** Check the engine speed 1 signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1G.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1G-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1G-2.** Check the engine speed 2 signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1H.** Check the remote engine stop signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1H-1.** Check the remote engine stop signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1H-2.** Check the remote engine stop signal wire for a short to ground. | Less than 10 ohms? |
|  | **STEP 1I.** Check the shutdown unit Modicon™ communication bus supply and return wires for an open. | Less than 10 ohms? |
|  | **STEP 1I-1.** Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 1I-2.** Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. | Less than 10 ohms? |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the low speed oil pressure signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 2A-1.** Check the low speed oil pressure signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 2B.** Check the high speed oil pressure signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 2B-1.** Check the high speed oil pressure signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 2C.** Check the coolant pressure signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 2C-1.** Check the coolant pressure signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 2D.** Check the coolant temperature signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 2D-1.** Check the coolant temperature signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 2E.** Check the engine speed 1 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 2E-1.** Check the engine speed 1 signal and return wires for a wire-to-wire short. | Less than 10 ohms? |
|  | **STEP 2F.** Check the engine speed 2 signal and return wires for an open. | Less than 10 ohms? |
|  | **STEP 2F-1.** Check the engine speed 2 signal and return wires for a wire-to-wire short. | Less than 10 ohms? |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the DCU410 unit for alarms and LED illumination.

| **Conditions:** Check for alarm and LED illumination |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the SDU410 unit Acknowledge button. NOTE: Be sure the Acknowledge button is **not** stuck in the activation mode. Press the Acknowledge button to see if it changes to steady illumination. | Acknowledge button stuck? **YESRepair:** Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Acknowledge button stuck? **NO** | 1B |  |

#### STEP 1B. Check the low speed oil pressure signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the low speed oil pressure signal and return wires at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the signal and return wires for an open. Place one test lead on the low speed oil pressure signal wire at the SDU410 unit. Place the other test lead on the low speed oil pressure signal pin at the C4 connector. Place one test lead on the low speed oil pressure return wire at the SDU410 unit. Place the other test lead on the low speed oil pressure return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1B-1. Check the low speed oil pressure signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the low speed oil pressure signal and return wires at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low speed oil pressure signal and return wires for a wire-to-wire short. Place one test lead on the low speed oil pressure signal wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the low speed oil pressure return wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1B-2 |  |

#### STEP 1B-2. Check the low speed oil pressure signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the low speed oil pressure signal wire at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low speed oil pressure signal wire for a short to ground. Place one test lead on the low speed oil pressure signal wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the high speed oil pressure signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the high speed oil pressure signal and return wires at the SDU410 unit and connector C4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high speed oil pressure signal and return wires for an open. Place one test lead on the high speed oil pressure signal wire at the SDU410 unit. Place the other test lead on the high speed oil pressure signal pin at the C4 connector. Place one test lead on the high speed oil pressure return wire at the SDU410 unit. Place the other test lead on the high speed oil pressure return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1C-1. Check the high speed oil pressure signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the high speed oil pressure signal and return wires at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high speed oil pressure signal and return wires for a wire-to-wire short. Place one test lead on the high speed oil pressure signal wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the high speed oil pressure return wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C-2 |  |

#### STEP 1C-2. Check the low speed oil pressure signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the low speed oil pressure signal wire at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high speed oil pressure signal wire for a short to ground. Place one test lead on the low speed oil pressure signal wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1D |  |

#### STEP 1D. Check the coolant pressure signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the coolant pressure signal and return wires at the SDU410 unit and connector C4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure signal and return wires for an open. Place one test lead on the coolant pressure signal wire at the SDU410 unit. Place the other test lead on the coolant pressure signal pin at the C4 connector. Place one test lead on the coolant pressure return wire at the SDU410 unit. Place the other test lead on the coolant pressure return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1D-1. Check the coolant pressure signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the coolant pressure signal and return wires at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure signal and return wires for a wire-to-wire short. Place one test lead on the coolant pressure signal wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the coolant pressure return wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1D-2 |  |

#### STEP 1D-2. Check the coolant pressure signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the coolant pressure signal wire at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure signal wire for a short to ground. Place one test lead on the coolant pressure signal wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1E |  |

#### STEP 1E. Check the coolant temperature signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the coolant temperature signal and return wires at the SDU410 unit and connector C4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature signal and return wires for an open. Place one test lead on the coolant temperature signal wire at the SDU410 unit. Place the other test lead on the coolant temperature signal pin at the C4 connector. Place one test lead on the coolant temperature return wire at the SDU410 unit. Place the other test lead on the coolant temperature return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1E-1. Check the coolant temperature signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the coolant temperature signal and return wires at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature signal and return wires for a wire-to-wire short. Place one test lead on the coolant temperature signal wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the coolant temperature return wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1E-2 |  |

#### STEP 1E-2. Check the coolant temperature signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the coolant temperature signal wire at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature signal wire for a short to ground. Place one test lead on the coolant temperature signal wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1F |  |

#### STEP 1F. Check the engine speed 1 signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires at the SDU410 unit and connector C4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 signal and return wires for an open. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead on the engine speed 1 signal pin at the C4 connector. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on the engine speed 1 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1F-1. Check the engine speed 1 signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal and return wires at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1F-2 |  |

#### STEP 1F-2. Check the engine speed 1 signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 signal wire at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 signal wire for a short to ground. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1G |  |

#### STEP 1G. Check the engine speed 2 signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires at the SDU410 unit and connector C4. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 2 signal and return wires for an open. Place one test lead on the engine speed 2 signal wire at the SDU410 unit. Place the other test lead on the engine speed 2 signal pin at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on the engine speed 2 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1G-1. Check the engine speed 2 signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal and return wires at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 2 signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 signal wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1G-2 |  |

#### STEP 1G-2. Check the engine speed 2 signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 2 signal wire at the SDU410 unit and C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 2 signal wire for a short to ground. Place one test lead on the engine speed 2 signal wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1H |  |

#### STEP 1H. Check the remote engine stop signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the remote engine stop signal and return wires at the SDU410 unit and X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote engine stop signal and return wires for an open. Place one test lead on the remote engine stop signal wire at the SDU410 unit. Place the other test lead on the remote engine stop signal pin at the X4 connector. Place one test lead on the remote engine stop return wire at the SDU410 unit. Place the other test lead on the remote engine stop return pin at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1H-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1H-1. Check the remote engine stop signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the remote engine stop signal and return wires at the SDU410 unit and X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote engine stop signal and return wires for a wire-to-wire short. Place one test lead on the remote engine stop signal wire at the SDU410 unit. Place the other test lead on all other pins at the X4 connector. Place one test lead on the remote engine stop return wire at the SDU410 unit. Place the other test lead on all other pins at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1H-2 |  |

#### STEP 1H-2. Check the remote engine stop signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the remote engine stop signal wire at the SDU410 unit and X4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote engine stop signal wire for a short to ground. Place one test lead on the remote engine stop signal wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1I |  |

#### STEP 1I. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1I-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1I-1. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1I-2 |  |

#### STEP 1I-2. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit and DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the low speed oil pressure signal and return wires for an open.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low speed oil pressure signal and return wires for an open. Place one test lead on the low speed oil pressure signal pin at the C4 connector. Place the other test lead on the low speed oil pressure signal pin at the C11 connector. Place one test lead on the low speed oil pressure return pin at the C4 connector. Place the other test lead on the low speed oil pressure return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2A-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2A-1. Check the low speed oil pressure signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the low speed oil pressure signal and return wires for a wire-to-wire short. Place one test lead on the low speed oil pressure signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the low speed oil pressure return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2B |  |

#### STEP 2B. Check the high speed oil pressure signal and return wires for an open.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high speed oil pressure signal and return wires for an open. Place one test lead on the high speed oil pressure signal pin at the C4 connector. Place the other test lead on the high speed oil pressure signal pin at the C11 connector. Place one test lead on the high speed oil pressure return pin at the C4 connector. Place the other test lead on the high speed oil pressure return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2B-1. Check the high speed oil pressure signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the high speed oil pressure signal and return wires for a wire-to-wire short. Place one test lead on the high speed oil pressure signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the high speed oil pressure return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the coolant pressure signal and return wires for an open.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure signal and return wires for an open. Place one test lead on the coolant pressure signal pin at the C4 connector. Place the other test lead on the coolant pressure signal pin at the C11 connector. Place one test lead on the coolant pressure return pin at the C4 connector. Place the other test lead on the coolant pressure return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2C-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2C-1. Check the coolant pressure signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure signal and return wires for a wire-to-wire short. Place one test lead on the coolant pressure signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the coolant pressure return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2D |  |

#### STEP 2D. Check the coolant temperature signal and return wires for an open.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature signal and return wires for an open. Place one test lead on the coolant temperature signal pin at the C4 connector. Place the other test lead on the coolant temperature signal pin at the C11 connector. Place one test lead on the coolant temperature return pin at the C4 connector. Place the other test lead on the coolant temperature return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2D-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2D-1. Check the coolant temperature signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant temperature signal and return wires for a wire-to-wire short. Place one test lead on the coolant temperature signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the coolant temperature return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2E |  |

#### STEP 2E. Check the engine speed 1 signal and return wires for an open.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 signal and return wires for an open. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on the engine speed 1 signal pin at the C11 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on the engine speed 1 return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2E-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2E-1. Check the engine speed 1 signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 1 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 1 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2F |  |

#### STEP 2F. Check the engine speed 2 signal and return wires for an open.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 2 signal and return wires for an open. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead on the engine speed 2 signal pin at the C11 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on the engine speed 2 return pin at the C11 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2F-1 |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2F-1. Check the engine speed 2 signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM wiring harness from the customer interface box at the C4 connector. Disconnect the OEM wiring harness at the C11 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 2 signal and return wires for a wire-to-wire short. Place one test lead on the engine speed 2 signal pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Place one test lead on the engine speed 2 return pin at the C4 connector. Place the other test lead on all other pins at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location |  |
