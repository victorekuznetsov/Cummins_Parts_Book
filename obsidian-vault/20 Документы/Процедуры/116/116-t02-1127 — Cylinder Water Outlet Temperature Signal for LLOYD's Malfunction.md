---
aliases:
  - "Неисправность сигнала температуры воды на выходе цилиндра (для LLOYD's)"
type: "Процедура"
doc: "116-t02-1127"
title_en: "Cylinder Water Outlet Temperature Signal for LLOYD's Malfunction"
title_ru: "Неисправность сигнала температуры воды на выходе цилиндра (для LLOYD's)"
modified: "2008-05-22"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1127.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1127.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Cylinder Water Outlet Temperature Signal for LLOYD's Malfunction
**Неисправность сигнала температуры воды на выходе цилиндра (для LLOYD's)**

> [!abstract] Процедура · `116-t02-1127`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1127.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1127.pdf)

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
|  | **STEP 1A.** Check the cylinder water outlet temperature signal, return, and return 2 wires for an open. |  |
|  | **STEP 1B.** Check the cylinder water outlet temperature signal, return, and return 2 wires for a wire-to-wire short. |  |
|  | **STEP 1C.** Check the cylinder water outlet temperature signal wire for a short to ground. |  |

### STEP 1. Check the OEM wiring harness.

#### STEP 1A. Check the cylinder water outlet temperature signal, return, and return 2 wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the cylinder water outlet temperature signal, return, and return 2 wires at the remote input/output unit X7 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the cylinder water outlet temperature signal, return, and return 2 wires for an open. Place one test lead on the cylinder water outlet temperature signal pin at the X7 connector. Place the other test lead on the cylinder water outlet temperature signal pin at the cylinder water outlet temperature sensor. Place one test lead on the cylinder water outlet temperature return pin at the X7 connector. Place the other test lead on the cylinder water outlet temperature return pin at the cylinder water outlet temperature sensor. Place one test lead on the cylinder water outlet temperature return 2 pin at the X7 connector. Place the other test lead on the cylinder water outlet temperature return 2 pin at the cylinder water outlet temperature sensor. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1B |
| Less than 10 ohms? **NORepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |  |

#### STEP 1B. Check the cylinder water outlet temperature signal, return, and return 2 wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the cylinder water outlet temperature signal, return, and return 2 wires at the remote input/output unit X7 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the cylinder water outlet temperature signal, return, and return 2 wires for a wire-to-wire short. Place one test lead on the cylinder water outlet temperature signal pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the cylinder water outlet temperature return pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Place one test lead on the cylinder water outlet temperature return 2 pin at the X7 connector. Place the other test lead on all other pins at the X7 connector. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the cylinder water outlet temperature signal wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the cylinder water outlet temperature signal wire at the remote input/output unit X7 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the cylinder water outlet temperature signal wire for a short to ground. Place one test lead on the cylinder water outlet temperature signal pin at the X7 connector. Place the other test lead on engine ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NORepair:** Replace the cylinder water outlet temperature sensor. Refer to the OEM service manual or contact a Cummins® Authorized Repair Location. | Repair complete |  |
