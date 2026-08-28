---
aliases:
  - "Неисправность сигнала давления масла на входе фильтра (для LLOYD's)"
type: "Процедура"
doc: "116-t02-1131"
title_en: "Lubricating Oil Filter Inlet Pressure Signal for LLOYD's Malfunction"
title_ru: "Неисправность сигнала давления масла на входе фильтра (для LLOYD's)"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Lubricating Oil Filter Inlet Pressure Signal for LLOYD's Malfunction
**Неисправность сигнала давления масла на входе фильтра (для LLOYD's)**

> [!abstract] Процедура · `116-t02-1131`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1131.pdf)

Printable Version

### Symptoms

- The OEM signal for LLOYD's sensor has malfunctioned.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

This LLOYD's sensor is connected to the OEM side (X7 connector) of the remote input/output unit. The OEM is responsible for this connection.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the OEM wiring harness. |  |
|  | **STEP 1A.** Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for an open. |  |
|  | **STEP 1B.** Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. |  |
|  | **STEP 1C.** Check the lubricating oil filter inlet pressure signal wire for a short to ground. |  |
|  | **STEP 1D.** Check the lubricating oil filter inlet pressure sensor supply +24-VDC for voltage. |  |

### STEP 1. Check the OEM wiring harness.

#### STEP 1A. Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for an open.

| **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for an open. Place one test lead on the lubricating oil filter inlet pressure signal pin at the X7 connector. Place the other test lead on the lubricating oil filter inlet pressure signal pin at the sensor connector. Place one test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the X7 connector. Place the other test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a wire-to-wire short.

| **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a wire-to-wire short. Place one test lead on the lubricating oil filter inlet pressure signal pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a short to ground.

| **Conditions:** Disconnect the OEM harness at the X7 connector. Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lubricating oil filter inlet pressure signal and sensor supply +24-VDC wires for a short to ground. Place one test lead on the lubricating oil filter inlet pressure signal pin at the X7 connector. Place the other test lead on engine ground. Place one test lead on the sensor supply +24-VDC pin at the X7 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2D |  |

#### STEP 2D. Check the lubricating oil filter inlet pressure sensor supply +24-VDC wire for voltage.

| **Conditions:** Disconnect the lubricating oil filter inlet pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the lubricating oil filter inlet pressure sensor supply +24-VDC wire for voltage. Place one test lead on the lubricating oil filter inlet pressure sensor supply +24-VDC pin at the sensor connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | +24-VDC? **YESRepair:** Replace the lubricating oil filter inlet pressure sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |
| +24-VDC? **NORepair:** Check the batteries. Refer to the OEM service manual. Replace the remote input/output unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
