---
aliases:
  - "Нет индикации тревоги от логического блока интерфейсной коробки"
type: "Процедура"
doc: "116-t02-1049"
title_en: "Customer Interface Box Logic Unit Alarm Indication Not Received When Alarm Activated"
title_ru: "Нет индикации тревоги от логического блока интерфейсной коробки"
modified: "2008-05-29"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Customer Interface Box Logic Unit Alarm Indication Not Received When Alarm Activated
**Нет индикации тревоги от логического блока интерфейсной коробки**

> [!abstract] Процедура · `116-t02-1049`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1049.pdf)

Printable Version

### Symptoms

- No communication between the DCU410 unit and CLU unit when alarm is activated.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1A-1.** Check the CLU power supply wire for voltage +24-VDC. |  |
|  | **STEP 1B.** Check the customer interface box logic unit alarm signal wire for an open. |  |
|  | **STEP 1C.** Check the customer interface box logic unit alarm signal wire for a wire to wire short. |  |
|  | **STEP 1D.** Check the customer interface box logic unit alarm signal wire for short to ground. |  |

### STEP 1. Check the customer interface box.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for indication of faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
| DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the CLU power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test lead on the battery 1 voltage supply wire at the CLU. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC. **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
| Less than +24-VDC. **NO** | 1B |  |

#### STEP 1B. Check the customer interface box logic unit alarm signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the customer interface box logic unit alarm signal wire at the DCU410 unit and CLU. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface box logic unit alarm signal wire for an open. Place one test lead on the customer interface box logic unit signal wire at the DCU410 unit. Place the other test lead on the customer interface box logic unit signal wire at the CLU X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1C. Check the customer interface box logic unit alarm signal wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface box logic unit alarm signal wire for a wire-to-wire short. Place one test lead on the customer interface box logic unit alarm signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the CLU. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 1D |  |

#### STEP 1D. Check the customer interface box logic unit alarm signal wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the customer interface box logic unit alarm signal wire for a short to ground. Place one test lead on the customer interface box logic unit alarm signal wire at the DCU410 unit. Place the other test on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the CLU. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | Contact a Cummins® Authorized Repair Location. |  |
