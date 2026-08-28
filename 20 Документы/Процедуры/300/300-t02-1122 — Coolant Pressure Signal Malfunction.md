---
aliases:
  - "Неисправность сигнала давления ОЖ"
type: "Процедура"
doc: "300-t02-1122"
title_en: "Coolant Pressure Signal Malfunction"
title_ru: "Неисправность сигнала давления ОЖ"
modified: "2022-02-04"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Coolant Pressure Signal Malfunction
**Неисправность сигнала давления ОЖ**

> [!abstract] Процедура · `300-t02-1122`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2022-02-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1122.pdf)

Printable Version

### Symptoms

- The original equipment manufacturer (OEM) coolant pressure sensor has malfunctioned.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

The coolant pressure sensor is connected to the alarm and safety C2 connector located on the customer interface box (C.I.B.).

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the C.I.B. wiring. |  |
|  | **STEP 1A.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. | Greater than 100k ohms? |
|  | **STEP 1B.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
|  | **STEP 1C.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
| STEP 2. | Check the OEM wiring harness. |  |
|  | **STEP 2A.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. | Greater than 100k ohms? |
|  | **STEP 2B.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
|  | **STEP 2C.** Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. | Less than 10 ohms? |
|  | **STEP 2D.** Check the coolant pressure sensor SUPPLY +24-VDC wire for voltage. | +24-VDC? |

### STEP 1. Check the C.I.B. wiring.

#### STEP 1A. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit.

| **Conditions:** Open the C.I.B. Disconnect the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. Note: An alarm will sound on the remote input/output unit when an open circuit is detected. Place one test lead on the coolant pressure SIGNAL wire at the control panel. Place the other test lead on the coolant pressure SIGNAL pin at the C2 connector. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on the sensor SUPPLY +24-VDC pin at the C2 connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Greater than 100k ohms? **YES** | 1B |
| Greater than 100k ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

#### STEP 1B. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit.

| **Conditions:** Open the C.I.B. Disconnect the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. Place one test lead on the coolant pressure SIGNAL wire at the control panel. Place the other test lead on all other wires at the control panel. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on all other wires at the control panel. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 1C |  |

#### STEP 1C. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground.

| **Conditions:** Open the C.I.B. Disconnect the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires at the control panel. Disconnect the C2 connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. Place one test lead on the coolant pressure SIGNAL wire at the control panel. Place the other test lead on the panel ground. Place one test lead on the sensor SUPPLY +24-VDC wire at the control panel. Place the other test lead on the panel ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |
| Less than 10 ohms? **NO** | 2A |  |

### STEP 2. Check the OEM wiring harness.

#### STEP 2A. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit.

| **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the coolant pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for an open circuit. Note: An alarm will sound on the remote input/output unit if a false alarm has occurred. Place one test lead on the coolant pressure SIGNAL pin at the C2 connector. Place the other test lead on the coolant pressure SIGNAL pin at the C9 connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C2 connector. Place the other test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place one test lead on the coolant pressure SIGNAL pin at the C9 connector. Place the other test lead on the coolant pressure SIGNAL pin at the sensor connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the sensor connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Greater than 100k ohms? **YES** | 2B |
| Greater than 100k ohms? **NORepair:** Replace the wire. [[300-015-023 — Customer Interface Box\|Refer to Procedure 015-023 in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit.

| **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the coolant pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a wire-to-wire short circuit. Place one test lead on the coolant pressure SIGNAL pin at the C2 connector. Place the other test lead on all other pins at the C2 connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C2 connector. Place the other test lead on all other pins at the C2 connector. Place one test lead on the coolant pressure SIGNAL pin at the C9 connector. Place the other test lead on all other pins at the C9 connector. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on all other pins at the C9 connector. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2C |  |

#### STEP 2C. Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground.

| **Conditions:** Disconnect the OEM harness at the C2 and C9 connectors. Disconnect the coolant pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure SIGNAL and sensor SUPPLY +24-VDC wires for a short circuit to ground. Place one test lead on the coolant pressure SIGNAL pin at the C2 connector. Place the other test lead on the engine ground. Place one test lead on the sensor SUPPLY +24-VDC pin at the C9 connector. Place the other test lead on the engine ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | Less than 10 ohms? **YESRepair:** Replace the wire. Refer to the OEM service manual. | Repair complete |
| Less than 10 ohms? **NO** | 2D |  |

#### STEP 2D. Check the coolant pressure sensor SUPPLY +24-VDC wire for voltage.

| **Conditions:** Disconnect the coolant pressure sensor connector. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the coolant pressure sensor SUPPLY +24-VDC wire for voltage. Place one test lead on the coolant pressure sensor SUPPLY +24-VDC pin at the sensor connector. Place the other test lead on the engine ground. Refer to the circuit diagram or the wiring diagram for connector pin identification. | +24-VDC? **YESRepair:** Replace the coolant pressure sensor. Refer to the OEM service manual. Refer to Procedure 019-016 in Section 19. | Repair complete |
| +24-VDC? **NORepair:** Replace the remote input/output unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
