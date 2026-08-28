---
type: "Процедура"
doc: "513-t02-1026"
title_en: "Generator Data Does Not Appear On Display"
modified: "2019-10-25"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1026.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1026.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Generator Data Does Not Appear On Display

> [!abstract] Процедура · `513-t02-1026`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1026.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1026.pdf)

Printable Version

### Symptoms

- Generator set data shows dashes or **not** present on the ED-4 display.

### How To Use This Tree

This symptom tree can be used to troubleshoot J1939 communication issues with the generator set. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- Incorrect vessel personality file

- Short in the J1939 circuit

- Improper setup in the ED-4 display.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the display. |  |
|  | **STEP 1A.** Check the vessel personality file. | New vessel personality file just been downloaded? |
|  | **STEP 1B.** Check the engine J1939 setup in the ED-4 display. | J1939 engine parameters displayed? |
|  | **STEP 1C.** Check the generator set J1939 setup in the ED-4 display. | Generator set configured properly in ED-4 display? |
| STEP 2. | Check the J1939 harness. |  |
|  | **STEP 2A.** Check for an open in the J1939 circuit. | Less than 10 ohms? |

### STEP 1. Check the display.

#### STEP 1A. Check the vessel personality file.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the vessel personality file. Check the vessel personality file. | New vessel personality file just been downloaded? **YESRepair:** Download correct vessel personality file to the display from QuickServe® Online. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] | Repair complete |
| New vessel personality file just been downloaded? **NO** | 1B |  |

#### STEP 1B. Check the engine J1939 setup in the ED-4 display.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the engine J1939 setup in the ED-4 display. Monitor the engine speed, oil pressure, and coolant temperature parameters in the ED-4 display. | J1939 engine parameters displayed? **YES** | 1C |
| J1939 engine parameters displayed? **NORepair:** Reference the Display Does **Not** Display Data - J1939 Does **Not** Work in the troubleshooting symptom tree in Section TT. | Repair complete |  |

#### STEP 1C. Check the generator set J1939 setup in the ED-4 display.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the generator set J1939 setup in the ED-4 display. Verify the generator set is configured in the ED-4 display. Go to the configuration in the menu in the ED-4 display. Refer to Procedure 015-108 in Section 15. | Generator set configured properly in ED-4 display? **YES** | 2A |
| Generator set configured properly in ED-4 display? **NORepair:** An incorrect setup has been detected in the ED-4 display. Select the proper generator set source ID or address for this display. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete |  |

### STEP 2. Check the J1939 harness.

#### STEP 2A. Check for an open in the J1939 circuit.

| **Conditions:** Turn system enable switch OFF. Disconnect display generator set J1939 wiring harness from the generator set. Disconnect the generator set J1939 from the engine harness or customer interface box (C.I.B.). |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check for an open in the J1939 circuit. Measure the J1939 (+) resistance in the harness. Place one test lead on J1939 (+) terminal of the generator set J1939 wiring harness connector (mating to the engine wiring harness or C.I.B.). Place the other test lead on J1939 (+) terminal of the generator set J1939 wiring harness connector (mating to the generator set). Measure the J1939 (-) resistance in the harness. Place one test lead on J1939 (-) terminal of the generator set J1939 wiring harness connector (mating to the engine wiring harness or C.I.B.). Place the other test lead on J1939 (-) terminal of the generator set J1939 wiring harness connector (mating to the generator set). Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Less than 10 ohms? **YESRepair:** Troubleshoot the generator set J1939 circuit. Reference the generator set service manual. | Repair complete. |
| Less than 10 ohms? **NORepair:** Repair or replace the generator set J1939 harness. Reference the generator set service manual. | Repair complete. |  |
