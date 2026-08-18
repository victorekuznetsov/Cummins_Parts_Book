---
aliases:
  - "Переключатель блока управления дизелем не переходит в местный режим"
type: "Процедура"
doc: "116-t02-1050"
title_en: "Diesel Control Unit Local/Remote Switch Does Not Switch to Local"
title_ru: "Переключатель блока управления дизелем не переходит в местный режим"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Diesel Control Unit Local/Remote Switch Does Not Switch to Local
**Переключатель блока управления дизелем не переходит в местный режим**

> [!abstract] Процедура · `116-t02-1050`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1050.pdf)

Printable Version

### Symptoms

Engine will **not** crank when the start button is pressed at the remote panel.

- Diesel control unit local/remote switch does **not** to switch to remote

- Diesel control unit indicates incorrect assignment

- Remote panel does **not** switch to local

- Remote panel does **not** switch to remote

- Remote panel indicates incorrect assignment.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

To initiate engine crank from the remote panel, the following panel parameters **must** be met:

- The remote panel power lamp illuminated

- The local start **only** lamp is **not** illuminated

- The engine **must** be stopped.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. |  |
|  | **STEP 1A-1.** Check the DCU410 unit power supply wire for voltage +24-VDC. |  |
|  | **STEP 1B.** Check the function of the start button. |  |
|  | **STEP 1C.** Check the engine stop indication wire for an open. |  |
|  | **STEP 1D.** Check the ignition engine stop supply and engine stop switch wires for an open. |  |
|  | **STEP 1E.** Check the vessel remote data link Ethernet signal wire for an open. |  |
|  | **STEP 1F.** Check the engine stop indication wire for a wire-to-wire short. |  |
|  | **STEP 1G.** Check the ignition engine stop supply and engine stop switch wires for a wire-to-wire short. |  |
|  | **STEP 1H.** Check the vessel remote data link Ethernet signal wire for a wire-to-wire short. |  |
|  | **STEP 1I.** Check the engine stop indication wire for a short to ground. |  |
|  | **STEP 1J.** Check the ignition engine stop supply and engine stop switch wires for a short to ground. |  |
|  | **STEP 1K.** Check the vessel remote data link Ethernet signal wire for a short to ground. |  |

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
| Check the voltage at the battery 1 voltage (switched power) at the DCU410 unit. Place one test on the battery 1 voltage supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | 1B |  |

#### STEP 1B. Check the function of the start button.

| **Conditions:** Open the customer interface box. Disconnect the local mode supply wire at the DCU410 unit, CLU, and X4 connections. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the function of the stop button. Place one test lead on the local mode supply wire at the DCU410 unit. Place the other test lead on the local mode supply wire at the CLU unit. Place one test lead on the local mode supply wire at the DCU410 unit. Place the other test lead on the local mode supply wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1C |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1C. Check the engine stop indication wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the engine stop indication and energize to stop relay wires from the DCU410 unit and CLU unit. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine stop indication wire for an open. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on the engine stop indication supply wire at the CLU unit. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test on the energize to stop relay return wire at the CLU unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1D |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1D. Check the ignition engine stop supply and engine stop switch wires for an open.

| **Conditions:** Open the customer interface box. Disconnect the ignition engine stop supply and engine stop switch wires from the C1 connector and switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition engine stop supply and engine stop switch wires for an open. Place one test lead on the ignition stop supply wire at the C1 connector. Place the other test lead on the ignition stop supply wire at the engine stop switch. Place one test lead on the engine stop switch wire at the DCU410 unit. Place the other test lead on the engine stop switch wire at the engine stop switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1E |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the engine stop switch. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1E. Check the vessel remote data link Ethernet signal wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the vessel remote data link Ethernet signal wire at the DCU410 unit and Ethernet switch. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel remote data link Ethernet signal wire for an open. Place one test lead on the vessel remote data link Ethernet signal wire at the DCU410 unit. Place the other test lead on the vessel remote data link Ethernet signal wire at the Ethernet switch. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1F |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1F. Check the engine stop indication wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine stop indication wire for a wire to wire short. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1G |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1G. Check the ignition engine stop supply and engine stop switch wires for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition engine stop supply and engine stop switch wires for a wire-to-wire short. Place one test lead on the ignition stop supply wire at the C1 connector. Place the other test lead on all other wires at the C1 connector. Place one test lead on the engine stop switch wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1H |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1H. Check the vessel remote data link Ethernet signal wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel remote data link Ethernet signal wire for a wire-to-wire short. Place one test lead on the vessel remote data link Ethernet signal wire at the DCU410 unit. Place the other test lead on all other wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1I |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 1I. Check the engine stop indication wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine stop indication wire for a short to ground. Place one test lead on the engine stop indication supply wire at the DCU410 unit. Place the other test lead on panel ground. Place one test lead on the energize to stop relay return wire at the DCU410 unit. Place the other test on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1J |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1J. Check the ignition engine stop supply and engine stop switch wires for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the ignition engine stop supply and engine stop switch wires for a short to ground. Place one test lead on the ignition stop supply wire at the C1 connector. Place the other test lead on panel ground. Place one test lead on the engine stop switch wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 1K |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 1K. Check the vessel remote data link Ethernet signal wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel remote data link Ethernet signal wire for a short to ground. Place one test lead on the vessel remote data link Ethernet signal wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
