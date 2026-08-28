---
aliases:
  - "Неисправность аналогового сигнала судна 3"
type: "Процедура"
doc: "116-t02-1139"
title_en: "Vessel Analog Signal 3 Malfunction"
title_ru: "Неисправность аналогового сигнала судна 3"
modified: "2008-07-11"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1139.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1139.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Vessel Analog Signal 3 Malfunction
**Неисправность аналогового сигнала судна 3**

> [!abstract] Процедура · `116-t02-1139`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-07-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1139.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1139.pdf)

Printable Version

### Symptoms

- The vessel sensor on the OEM application is **not** communicating with DCU410 unit.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The vessel sensor inputs on the customer interface box (CIB) are used by the OEM. The input to the DCU410 measures these values from the sensors.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box wiring. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1B.** Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for an open. |  |
|  | **STEP 1C.** Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for a wire-to-wire short. |  |
|  | **STEP 1D.** Check the vessel temperature sensor 1 signal wire for a short to ground. |  |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for an open. |  |
|  | **STEP 2B.** Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for a wire-to-wire short. |  |
|  | **STEP 2C.** Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for a short to ground. |  |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for faults. | DCU410 unit indicates fault(s)? **YES** | 1B |
| DCU410 unit indicates fault(s)? **NO** | 2A |  |

#### STEP 1B. Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 3 wires from the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel sensor analog input supply and vessel analog signal 3 wires for an open. Place one test lead on the vessel sensor analog input supply wire at the DCU410 unit. Place the other test lead on the vessel sensor analog input supply wire at the X4 connection. Place one test lead on the vessel sensor analog signal 3 wire at the DCU410 unit. Place the other test lead on the vessel sensor analog signal 3 wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1C. Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel sensor analog input supply and vessel analog signal 3 wires for a wire-to-wire short. Place one test lead on the vessel sensor analog input supply wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Place one test lead on the vessel sensor analog signal 3 wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1D |  |

#### STEP 1D. Check the vessel sensor analog signal 3 wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel sensor analog signal 3 wire for a short to ground. Place one test lead on the vessel sensor analog signal 3 wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 3 wires at the X4 connections. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 3 wires at the vessel sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for an open. Place one test lead on the vessel sensor analog input supply wire at the X4 connection. Place the other test lead on the vessel sensor analog input supply wire at the vessel sensor connector. Place one test lead on the vessel sensor analog signal 3 wire at the X4 connection. Place the other test lead on the vessel sensor analog signal 3 wire at the vessel sensor connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 2B. Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 3 wires at the X4 connection. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 3 wires at the vessel sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel sensor analog input supply and vessel analog signal 3 wires for a wire-to-wire short. Place one test lead on the vessel sensor analog input supply wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Place one test lead on the vessel sensor analog signal 3 wire at the X4 connection. Place the other test lead on all other wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 3 wires at the X4 connection. Disconnect the vessel sensor analog input supply and vessel sensor analog signal 3 wires at the vessel sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel sensor analog input supply and vessel sensor analog signal 3 wires for a short to ground. Place one test lead on the analog input supply wire at the X4 connection. Place the other test lead on engine ground. Place one test lead on the vessel sensor analog signal 3 wire at the X4 connection. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the vessel sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
