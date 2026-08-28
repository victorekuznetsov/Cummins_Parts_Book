---
type: "Процедура"
doc: "300-t02-1129"
title_en: "Redundant Power Selector Malfunction Primary Power Malfunction"
modified: "2019-10-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1129.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1129.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Redundant Power Selector Malfunction Primary Power Malfunction

> [!abstract] Процедура · `300-t02-1129`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1129.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1129.pdf)

Printable Version

### Symptoms

- Primary power supply failure error message.

### How To Use This Tree

This symptom tree can be used to troubleshoot signal from the speed pick-up is signal lost. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Primary power supply error message.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
|  | **STEP 1A.** Check the control panel display for faults. | Control panel indicates fault(s)? |
| STEP 2. | Check redundant power selector wiring. |  |
|  | **STEP 2A.** Check redundant power selector primary power input SUPPLY wire for voltage +18 VDC. | Less than +18±0.2-VDC? |
|  | **STEP 2B.** Check redundant power selector secondary power input SUPPLY wire for voltage +18 VDC. | Greater than +18±0.2-VDC? |
| STEP 3. | Check redundant power selector voltage. |  |
|  | **STEP 3A.** Check redundant power selector power output SUPPLY. | Output within ± 0.5 VDC? |

### STEP 1. Check the customer interface box (C.I.B.) wiring.

#### STEP 1A. Check the control panel display for faults.

| **Conditions:** Locate the control panel display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the control panel display for faults. | Control panel indicates fault(s)? **YESRepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF, or the ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF, X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346. | Go to appropriate fault code troubleshooting tree. |
| Control panel indicates fault(s)? **NO** | 2A |  |

### STEP 2. Check redundant power selector wiring.

#### STEP 2A. Check redundant power selector primary power input SUPPLY wire for voltage +18±0.2 VDC.

| **Conditions:** Open the C.I.B. Test the redundant power selector primary power input SUPPLY wire pin 1. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at pin 1 of the redundant power selector. Place one test lead at the primary power SUPPLY wire at pin 1 of the redundant power selector. Place the other test lead on the panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +18±0.2 VDC? **YESRepair:** Check the batteries. See equipment manufacturer service information. | 2B |
| Less than +18±0.2 VDC? **NO** | 2B |  |

#### STEP 2B. Check the control panel secondary power SUPPLY wire for voltage +18±0.2 VDC.

| **Conditions:** Open the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at pin 6 of the redundant power selector. Place one test lead at the secondary power SUPPLY wire at pin 6 of the redundant power selector. Place the other test lead on the redundant power selector ground pin 7. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Greater than +18±0.2 VDC? **YES** | 3A |
| Greater than +18±0.2 VDC? **NO** | 3A |  |

### STEP 3. Check redundant power selector power output SUPPLY.

#### STEP 3A. Check redundant power selector power output.

| **Conditions:** Open the C.I.B. Test the redundant power selector power output SUPPLY wire pin 17. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the output voltage at pin 17 of the redundant power selector. Place one test lead at the power output wire at pin 17 of the redundant power selector. Place the other test lead on the panel ground pin 16. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Output Voltage ±0.5 VDC of the primary and secondary input voltages? **YES** | Repair complete. |
| Output Voltage ±0.5 VDC of the primary and secondary input voltages? **NORepair:** Replace redundant power selector. | 1A |  |
