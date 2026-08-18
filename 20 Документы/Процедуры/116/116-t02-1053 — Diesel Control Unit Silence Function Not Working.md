---
aliases:
  - "Не работает функция отключения звука блока управления дизелем"
type: "Процедура"
doc: "116-t02-1053"
title_en: "Diesel Control Unit Silence Function Not Working"
title_ru: "Не работает функция отключения звука блока управления дизелем"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1053.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1053.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Diesel Control Unit Silence Function Not Working
**Не работает функция отключения звука блока управления дизелем**

> [!abstract] Процедура · `116-t02-1053`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1053.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1053.pdf)

Printable Version

### Symptoms

Silence mode set for alarm, but still is giving an LED lamp and audible alarm.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
|  | **STEP 1A-2.** Check the CLU unit power supply wire for voltage +24-VDC. |  |
|  | **STEP 1B.** Check the remote silence alarm supply wire for an open. |  |
|  | **STEP 1C.** Check the battery 1 voltage (switched power) supply wire for an open. |  |
|  | **STEP 1D.** Check the power lamp supply wire for an open. |  |
|  | **STEP 1E.** Check the power switch supply wire for an open. |  |
|  | **STEP 1F.** Check the Ethernet switch supply wire for an open. |  |
|  | **STEP 1G.** Check the remote silence alarm supply wire for a wire-to-wire short. |  |
|  | **STEP 1H.** Check the battery 1 voltage (switched power) supply wire for a wire-to-wire short. |  |
|  | **STEP 1I.** Check the power lamp supply wire for a wire-to-wire short. |  |
|  | **STEP 1J.** Check the power switch supply wire for a wire-to-wire short. |  |
|  | **STEP 1K.** Check the Ethernet switch supply wire for a wire-to-wire short. |  |
|  | **STEP 1L.** Check the remote silence alarm supply wire for a short to ground. |  |
|  | **STEP 1M.** Check the battery 1 voltage (switched power) supply wire for a short to ground. |  |
|  | **STEP 1N.** Check the power lamp supply wire for a short to ground. |  |
|  | **STEP 1O.** Check the power switch supply wire for a short to ground. |  |
|  | **STEP 1P.** Check the Ethernet switch supply wire for a short to ground. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
| DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the DCU410 unit power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage (switched power) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 1A-2 |  |

#### STEP 1A-2. Check the CLU unit power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the CLU unit. Place one test on the battery 1 voltage (switched power) wire at the CLU unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 1B |  |

#### STEP 1B. Check the remote silence alarm supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the remote silence alarm wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote silence alarm supply wire for an open. Place one test lead on the remote silence alarm supply wire at the DCU410 unit. Place the other test lead on the remote silence alarm supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1C. Check the battery 1 voltage (switched power) supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery 1 voltage (switched power) supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the battery 1 voltage (switched power) wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1D. Check the power lamp supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and power lamp connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power lamp supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the power lamp supply wire at the power lamp connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1E. Check the power switch supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and power switch connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power switch supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the power switch supply wire at the power switch connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1F. Check the Ethernet switch supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the battery 1 voltage (switched power) supply wire at the DCU410 unit and the Ethernet switch connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the Ethernet switch supply wire for an open. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on the Ethernet switch supply wire at the Ethernet switch connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1G. Check the remote silence alarm supply wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote silence alarm supply wire for a wire-to-wire short. Place one test lead on the remote silence alarm supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1H |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1H. Check the battery 1 voltage (switched power) supply wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery 1 voltage (switched power) supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1I |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1I. Check the power lamp supply wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power lamp supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1J |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1J. Check the power switch supply wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power switch supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1K |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1K. Check the Ethernet switch supply wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the Ethernet switch supply wire for a wire-to-wire short. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1L |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1L. Check the remote silence alarm supply wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote silence alarm supply wire for a short to ground. Place one test lead on the remote silence alarm supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1M |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1M. Check the battery 1 voltage (switched power) supply wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery 1 voltage (switched power) supply wire for a short to ground. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1N |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1N. Check the power lamp supply wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power lamp supply wire for a short to ground. Place one test lead on the power lamp supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1O |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1O. Check the power switch supply wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the power switch supply wire for a short to ground. Place one test lead on the power switch supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1P |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1P. Check the Ethernet switch supply wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the Ethernet switch supply wire for a short to ground. Place one test lead on the Ethernet switch supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
