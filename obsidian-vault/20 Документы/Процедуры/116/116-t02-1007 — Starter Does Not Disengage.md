---
aliases:
  - "Стартер не отключается"
type: "Процедура"
doc: "116-t02-1007"
title_en: "Starter Does Not Disengage"
title_ru: "Стартер не отключается"
modified: "2008-06-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Starter Does Not Disengage
**Стартер не отключается**

> [!abstract] Процедура · `116-t02-1007`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-06-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1007.pdf)

Printable Version

### Symptoms

- Starter does **not** disengage after engine cranking and the keyswitch is in the ON position.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the customer interface box logic unit LED illumination. |  |
|  | **STEP 1B.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
|  | **STEP 1C.** Check the engine speed 1 and engine speed 2 signal wires for an open. |  |
|  | **STEP 1D.** Check the engine speed 1 and engine speed 2 return wires for an open. |  |
|  | **STEP 1E.** Check the starter relay switch signal wire for an open. |  |
|  | **STEP 1F.** Check the shutdown unit Modicon™ communication bus supply and return wires for an open. |  |
|  | **STEP 1G.** Check the engine speed 1 and engine speed 2 signal and return wires for a wire-to-wire short. |  |
|  | **STEP 1H.** Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short. |  |
|  | **STEP 1I.** Check the engine speed 1 and engine speed 2 signal wires for a short to ground. |  |
|  | **STEP 1J.** Check the shutdown unit Modicon™ communication bus supply wire for a short to ground. |  |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the starter relay switch signal and return wires for an open. |  |
|  | **STEP 2B.** Check the starter relay switch signal and return wires for a wire-to-wire short. |  |
|  | **STEP 2C.** Check the starter relay switch signal wire for a short to ground. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the customer interface box logic unit LED illumination.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the crank lamp LED on the DCU 410 unit or remote panel for illumination. | Crank lamp illuminated? **YES** | 1B |
| Crank lamp illuminated? **NO** | Contact a Cummins® Authorized Repair Location |  |

#### STEP 1B. Check the DCU410 power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 1C |  |

#### STEP 1C. Check the engine speed 1 and engine speed 2 signal wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 signal wires at the SDU410 unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 and engine 2 signal wires at the SDU410 unit and C4 connector for an open. Place one test lead on the engine speed 1 signal wire at the SDU410 unit. Place the other test lead engine speed 1 signal pin at the C4 connector. Place one test lead on the engine speed 2 signal wire at the SDU410 unit. Place the other test lead engine speed 2 signal pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1D. Check the engine speed 1 and engine speed 2 return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 return wires at the SDU410 unit. Disconnect the C4 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 and engine speed 2 return wires at the SDU410 unit and C4 connector for an open. Place one test lead on the engine speed 1 return wire at the SDU410 unit. Place the other test lead on the engine speed 1 return pin at the C4 connector. Place one test lead on the engine speed 2 return wire at the SDU410 unit. Place the other test lead on the engine speed 2 return pin at the C4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1E. Check the starter relay switch signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the starter relay switch signal wire at the DCU410 unit. Place the other test lead on the starter relay switch signal pin at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1F. Check the shutdown unit Modicon™ communication bus supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit and SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit and the SDU410 unit for an open. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1G. Check the engine speed 1 and engine speed 2 signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 signal and return wires at the DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 and engine speed 2 signal and return lines at the DCU410 unit for a wire-to-wire short. Place one test lead on the engine speed 1 signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the engine speed 2 signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the engine speed 1 return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the engine speed 2 return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1H |  |

#### STEP 1H. Check the shutdown unit Modicon™ communication bus supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit. Disconnect the shutdown unit Modicon™ communication bus supply and return wires at the SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply and return wires at the DCU410 unit and SDU410 unit for a wire-to-wire short. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Place one test lead on the shutdown unit Modicon™ communication bus return wire at the SDU410 unit. Place the other test lead on all other wires at the SDU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1I |  |

#### STEP 1I. Check the engine speed 1 and engine speed 2 signal wires for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the engine speed 1 and engine speed 2 signal wires from the DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine speed 1 and engine speed 2 signal wires at the DCU410 unit for a short to ground. Place one test lead on the engine speed 1 signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the engine speed 2 signal wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1J |  |

#### STEP 1J. Check the shutdown unit Modicon™ communication bus supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the shutdown unit Modicon™ communication bus supply wire from the DCU410 unit. Disconnect the shutdown unit Modicon™ communication bus supply wire from the SDU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit and SDU410 unit for a short to ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the shutdown unit Modicon™ communication bus supply wire at the SDU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the starter relay switch signal and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the C1 connector. Disconnect the starter relay switch signal and return wires at the starter motor ring terminal. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal and return wires at the C1 connector for an open. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on the starter relay switch signal wire at the starting motor ring terminal. Place one test lead on the starter relay switch return pin at the C1 connector. Place the other test lead on the starter relay switch return wire at the starting motor ring terminal. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the starter relay switch signal and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal and return wires at the C1 connector for a wire-to-wire short. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Place one test lead on the starter relay switch return pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the starter relay switch signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal wire at the C1 connector for a short to ground. Place one test lead on the starter relay switch signal wire at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |  |
