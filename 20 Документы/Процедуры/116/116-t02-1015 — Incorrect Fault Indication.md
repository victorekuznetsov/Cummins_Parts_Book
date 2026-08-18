---
aliases:
  - "Неверная индикация неисправности"
type: "Процедура"
doc: "116-t02-1015"
title_en: "Incorrect Fault Indication"
title_ru: "Неверная индикация неисправности"
modified: "2008-05-22"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021617"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Incorrect Fault Indication
**Неверная индикация неисправности**

> [!abstract] Процедура · `116-t02-1015`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/116-t02-1015.pdf)

Printable Version

### Symptoms

Alarm lamp is **not** illuminated at the DCU410 unit or the remote panel when alarm condition is active.

- ECM Fault Acknowledgement **Not** Operational

- False Indication of Engine Shutdown.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the Panel Alarm Lamp Indication |  |
|  | **STEP 1A.** Check the DCU410 unit panel alarm lamp indication. |  |
|  | **STEP 1B.** Check the remote panel alarm lamp indication. |  |
| STEP 2. | Check the Customer Interface Box |  |
|  | **STEP 2A.** Check the battery voltage 1 (primary power supply) wire for an open. |  |
|  | **STEP 2B.** Check the battery voltage 1 (secondary power supply) wire for an open. |  |
|  | **STEP 2C.** Check the remote panel supply wire for an open. |  |
|  | **STEP 2D.** Check the battery voltage 1 (primary power supply) wire for a wire-to-wire short. |  |
|  | **STEP 2E.** Check the battery voltage 1 (secondary power supply) wire for a wire-to-wire short. |  |
|  | **STEP 2F.** Check the remote panel supply wire for a wire-to-wire short. |  |
|  | **STEP 2G.** Check the battery voltage 1 (primary power supply) wire for a short to ground. |  |
|  | **STEP 2H.** Check the battery voltage 1 (secondary power supply) wire for a short to ground. |  |
|  | **STEP 2I.** Check the remote panel supply wire for a short to ground. |  |

### STEP 1. Check the panel alarm lamp indication.

#### STEP 1A. Check the DCU410 unit panel alarm lamp indication.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the DCU410 unit panel lamp is illuminated. | Alarm lamp illuminated? **YES** | 1B |
| Alarm lamp illuminated? **NO** | 2A |  |

#### STEP 1B. Check the remote panel alarm lamp indication.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the remote panel lamp is illuminated. | Alarm lamp illuminated? **YES** | Repair complete |
| Alarm lamp illuminated? **NO** | Repair complete |  |

### STEP 2. Check the customer interface box.

#### STEP 2A. Check the battery voltage 1 (primary power supply) wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (primary power supply) wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 (primary power supply) wire for an open. Place one test lead on the battery voltage 1 (primary power supply) wire at the DCU410 unit. Place the other test lead on the battery voltage 1 (primary power supply) wire at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2B |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2B. Check the battery voltage 1 (secondary power supply) wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (secondary power supply) wire at the DCU410 unit and circuit breaker. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 (secondary power supply) wire for an open. Place one test lead on the battery voltage 1 (secondary power supply) wire at the DCU410 unit. Place the other test lead on the battery voltage 1 (secondary power supply) wire at the circuit breaker. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2C |
| Less than 10 ohms? **NORepair:** Replace the wire. [[116-015-023 — Customer Interface Box\|Refer to Procedure 015-023 (Customer Interface Box) in Section 15.]] | Repair complete |  |

#### STEP 2C. Check the remote panel supply wire for an open.

| **Conditions:** Open the customer interface box. Disconnect the remote panel supply wire at the X4 connection and remote panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel supply wire for an open. Place one test lead on the remote panel supply wire at the X4 connection. Place the other test lead on the remote panel supply wire at the remote panel. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2D |
| Less than 10 ohms? **NORepair:** Replace the wire or connector. Refer to Procedure 015-023 (Customer Interface Box) in Section 15 to replace the wire. Contact a Cummins® Authorized Repair Location to replace the connector. | Repair complete |  |

#### STEP 2D. Check the battery voltage 1 (primary power supply) wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (primary power supply) wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the wire for a wire-to-wire short. Place one test lead on the battery voltage 1 (primary power supply) wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2E |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair location. | Repair complete |  |

#### STEP 2E. Check the battery voltage 1 (secondary power supply) wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (secondary power supply) wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 (secondary power supply) wire for a wire-to-wire short. Place one test lead on the battery voltage 1 (secondary power supply) wire at the DCU410 unit. Place the other test lead on all wires at the DCU410 unit. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2F |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair location. | Repair complete |  |

#### STEP 2F. Check the remote panel supply wire for a wire-to-wire short.

| **Conditions:** Open the customer interface box. Disconnect the remote panel supply wire at the X4 connection and remote panel. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel supply wire for a wire-to-wire short. Place one test lead on the remote panel supply wire at the X4 connection. Place the other test lead on all wires at the X4 connection. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2G |
| Less than 10 ohms? **NORepair:** Replace the remote panel. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 2G. Check the battery voltage 1 (primary power supply) wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (primary power supply) wire at the DCU410 unit and X4 connection. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 (primary power supply) wire for a short to ground. Place one test lead on the battery voltage 1 (primary power supply) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2H |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair location. | Repair complete |  |

#### STEP 2H. Check the battery voltage 1 (secondary power supply) wire for a short to ground.

| **Conditions:** Open the customer interface box. Disconnect the battery voltage 1 (secondary power supply) wire at the DCU410 and circuit breaker. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the battery voltage 1 (secondary power supply) wire for a short to ground. Place one test lead on the battery voltage 1 (secondary power supply) wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | 2I |
| Less than 10 ohms? **NORepair:** Replace the DCU410 unit. Contact a Cummins® Authorized Repair Location. | Repair complete |  |

#### STEP 2I. Check the remote panel supply wire for a short to ground.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the remote panel supply wire for a short to ground. Place one test lead on the remote panel supply wire at the X4 connection. Place the other test lead on remote panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than 10 ohms? **YES** | Contact a Cummins® Authorized Repair Location. |
| Less than 10 ohms? **NORepair:** Replace the remote panel. Contact a Cummins® Authorized Repair Location. | Repair complete |  |
