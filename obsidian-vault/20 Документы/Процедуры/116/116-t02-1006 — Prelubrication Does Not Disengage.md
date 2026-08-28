---
aliases:
  - "Предпусковая прокачка не отключается"
type: "Процедура"
doc: "116-t02-1006"
title_en: "Prelubrication Does Not Disengage"
title_ru: "Предпусковая прокачка не отключается"
modified: "2008-05-29"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1006.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1006.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Prelubrication Does Not Disengage
**Предпусковая прокачка не отключается**

> [!abstract] Процедура · `116-t02-1006`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1006.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1006.pdf)

Printable Version

### Symptoms

- Engine prelubrication will **not** disengage.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

NOTE: A jumper wire **must** be removed at the prelubrication connector, if prelubrication is to be used.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the customer interface box logic unit LED illumination. |  |
|  | **STEP 1B.** Check the DCU410 power supply wire for voltage +24-VDC. |  |
|  | **STEP 1C.** Check the prelubrication activation supply wire for an open. |  |
|  | **STEP 1D.** Check the prelubrication complete signal wire for an open. |  |
|  | **STEP 1E.** Check the prelubrication activation and complete signal wires for an open. |  |
|  | **STEP 1F.** Check the prelubrication activation and complete signal wires for a short to ground. |  |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the prelubrication supply and return wires for an open. |  |
|  | **STEP 2B.** Check the prelubrication supply and return wires for a wire-to-wire short. |  |
|  | **STEP 2C.** Check the prelubrication supply wire for a short to ground. |  |

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

#### STEP 1C. Check the prelubrication activation signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication activation signal wire from the DCU410 unit. Disconnect the C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication activation signal wire at the DCU410 unit and C1 connector for an open. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead prelubrication activation signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1D. Check the prelubrication complete signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication complete signal wire at the DCU410 unit, CLU unit, and C1 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication complete signal wire at the DCU410 unit, CLU unit, and C1 connector for an open. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on the prelubrication complete signal wire at the CLU unit. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on the prelubrication complete signal wire at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1E. Check the prelubrication activation and complete signal wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication activation and complete signal wire at the DCU410 unit for a wire-to-wire short. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1F |  |

#### STEP 1F. Check the prelubrication activation and complete signal wires for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication activation and complete signal wires at the DCU410 unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication activation and complete signal wires at the DCU410 unit for a short to ground. Place one test lead on the prelubrication activation signal wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the prelubrication complete signal wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the prelubrication supply and return wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the prelubrication supply and return wires at the C1 connector and prelubrication sensor. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication supply and return wires at the C1 connector and prelubrication sensor for an open. Place one test lead on the prelubrication supply wire at the C1 connector. Place the other test lead on the prelubrication supply wire at the prelubrication sensor. Place one test lead on the prelubrication return wire at the C1 connector. Place the other test lead on the prelubrication return wire at the prelubrication return wire at prelubrication sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the prelubrication supply and return wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication supply and return wires at the C1 connector for a wire-to-wire short. Place one test lead on the prelubrication supply wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Place one test lead on the prelubrication return wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the prelubrication supply wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the prelubrication supply wire at the C1 connector for a short to ground. Place one test lead on the prelubrication supply wire at the C1 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the prelubrication sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
