---
aliases:
  - "Двигатель не проворачивается ни от блока управления, ни с дистанционного пульта"
type: "Процедура"
doc: "116-t02-1047"
title_en: "Engine Will Not Crank From Diesel Control Unit or Remote Panel"
title_ru: "Двигатель не проворачивается ни от блока управления, ни с дистанционного пульта"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1047.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1047.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Engine Will Not Crank From Diesel Control Unit or Remote Panel
**Двигатель не проворачивается ни от блока управления, ни с дистанционного пульта**

> [!abstract] Процедура · `116-t02-1047`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1047.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1047.pdf)

Printable Version

### Symptoms

- The SDU410 unit is preventing the engine from starting after engine shutdown.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

NOTE: A jumper **must** be in place at the prelubrication sensor, if prelubrication is **not** used.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the engine stop button for engagement. |  |
|  | **STEP 1B.** Check the customer interface box logic unit LED illumination. |  |
|  | **STEP 1C.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
|  | **STEP 1D.** Check the remote start supply wire for an open. |  |
|  | **STEP 1E.** Check the starter relay switch signal wire for an open. |  |
|  | **STEP 1F.** Check the prelubrication activation signal wire for an open. |  |
|  | **STEP 1G.** Check the prelubrication complete signal wire for an open. |  |
|  | **STEP 1H.** Check the remote start supply wire for a wire-to-wire short. |  |
|  | **STEP 1I.** Check the starter relay switch signal wire for a wire-to-wire short. |  |
|  | **STEP 1J.** Check the prelubrication activation signal wire for a wire-to-wire short. |  |
|  | **STEP 1K.** Check the prelubrication complete signal wire for a wire-to-wire short. |  |
|  | **STEP 1L.** Check the remote start supply wire for a short to ground. |  |
|  | **STEP 1M.** Check the prelubrication activation signal wire for a short to ground. |  |
|  | **STEP 1N.** Check the prelubrication complete signal wire for a short to ground. |  |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the starter relay switch signal and return wires for an open. |  |
|  | **STEP 2B.** Check the starter relay switch signal and return wires for a wire-to-wire short. |  |
|  | **STEP 2C.** Check the starter relay switch signal wire for a short to ground. |  |
|  | **STEP 2D.** Check the prelubrication supply and return wires for an open. |  |
|  | **STEP 2E.** Check the prelubrication supply and return wires for a wire-to-wire short. |  |
|  | **STEP 2F.** Check the prelubrication supply wire for a short to ground. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the engine stop button for engagement.

| **Conditions:** Check the engine stop button on the front of the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check to be sure the engine stop button is fully disengaged. Turn engine stop button 1/16th turn clockwise. The engine stop button will make an audible noise as it disengages. The engine stop button will not turn if it is disengaged. | Engine stop button engaged? **YESRepair:** Turn engine stop button 1/16th turn **clockwise** to disengage. | Repair complete |
| Engine stop button engaged? **NO** | 1B |  |

#### STEP 1B. Check the customer interface box logic unit LED illumination.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the crank lamp LED on the DCU 410 unit or remote panel for illumination. | Crank lamp illuminated? **YES** | 1C |
| Crank lamp illuminated? **NO** | Contact a Cummins® Authorized Repair Location |  |

#### STEP 1C. Check the DCU410 power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 1D |  |

#### STEP 1D. Check the remote start supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the remote start supply wire from the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote start supply wire at the DCU410 unit and X4 connection for an open. Place one test lead on the remote start supply wire at the DCU410 unit. Place the other test lead on the remote start supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1E. Check the starter relay switch signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the starter relay switch signal wire at the DCU410 unit. Place the other test lead on the starter relay switch signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1F. Check the prelubrication activation signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication activation signal wire from the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead prelubrication activation signal pin at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1G. Check the prelubrication complete signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit and CLU unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication complete signal wire at the DCU410 unit, CLU unit, and C1 connector for an open. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on the prelubrication complete signal wire at the CLU unit. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on the prelubrication complete signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1H |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1H. Check the remote start supply wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the remote start supply wire at the DCU410 unit and the X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote start supply at the DCU410 unit for a wire-to-wire short. Place one test lead on the remote start supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the remote start supply wire at the X4 connector. Place the other test lead on all other wires at the X4 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1I |  |

#### STEP 1I. Check the starter relay switch signal wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the starter relay switch signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal wire at the DCU410 unit and C1 connector for a wire-to-wire short. Place one test lead on the starter relay switch signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1J |  |

#### STEP 1J. Check the prelubrication activation signal wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication activation signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for a wire-to-wire short. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the prelubrication activation signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1K |  |

#### STEP 1K. Check the prelubrication complete signal wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication complete signal wire at the DCU410 unit and C1 connector for a wire-to-wire short. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the prelubrication complete signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1L |  |

#### STEP 1L. Check the remote start supply wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the remote start supply wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote start supply wire at the DCU410 unit and X4 connection for a short to ground. Place one test lead on the remote start supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the remote start supply wire at the X4 connection. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1M |  |

#### STEP 1M. Check the prelubrication activation signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication activation and complete signal wires at the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for a short to ground. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the prelubrication activation signal pin at the C1 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1N |  |

#### STEP 1N. Check the prelubrication complete signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication complete signal wire at the DCU410 unit and C1 connector for a short to ground. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the prelubrication complete signal pin at the C1 connector. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. Replace the SDU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the starter relay switch signal and return wires for an open.

| **Conditions:** Disconnect the starter relay switch signal and return wires at the starting motor ring terminals. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal and return wires at the C1 connector for an open. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on the starter relay switch signal wire at the starting motor ring terminal. Place one test lead on the starter relay switch return pin at the C1 connector. Place the other test lead on the starter relay switch return wire at the starting motor ring terminal. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the starter relay switch signal and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal and return wires at the C1 connector for a wire-to-wire short. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Place one test lead on the starter relay switch return pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the starter relay switch signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the starter relay switch signal wire at the C1 connector for a short to ground. Place one test lead on the starter relay switch signal pin at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |
| Less than 10 ohms? **NO** | 2D |  |

#### STEP 2D. Check the prelubrication supply and return wires for an open.

| **Conditions:** Disconnect the C1 connector. Disconnect the prelubrication sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication supply and return wires for an open. Place one test lead on the prelubrication supply pin at the C1 connector. Place the other test lead on the prelubrication supply pin at the prelubrication sensor connector. Place one test lead on the prelubrication return pin at the C1 connector. Place the other test lead on the prelubrication return pin at the prelubrication sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2E |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2E. Check the prelubrication supply and return wires for a wire-to-wire short.

| **Conditions:** Disconnect the C1 connector. Disconnect the prelubrication sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication supply and return wires for a wire-to-wire short. Place one test lead on the prelubrication supply pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Place one test lead on the prelubrication return pin at the C1 connector. Place the other test lead on all other pins at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2F |  |

#### STEP 2F. Check the prelubrication supply wire for a short to ground.

| **Conditions:** Disconnect the C1 connector. Disconnect the prelubrication sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication supply wire for a short to ground. Place one test lead on the prelubrication supply pin at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the prelubrication sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
