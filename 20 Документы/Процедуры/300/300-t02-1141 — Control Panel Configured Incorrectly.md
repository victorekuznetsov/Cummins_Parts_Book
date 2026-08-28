---
type: "Процедура"
doc: "300-t02-1141"
title_en: "Control Panel Configured Incorrectly"
modified: "2019-05-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "4332828"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/300"
---

# Control Panel Configured Incorrectly

> [!abstract] Процедура · `300-t02-1141`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[4332828 — Marine C Command HD Elite™ Panel System Master Repair Manual|4332828]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-05-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/300/300-t02-1141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/300-t02-1141.pdf)

Printable Version

### Symptoms

- The control panel is configured incorrectly for the engine application.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

This fault code has no external wiring from the control panel except the +24 VDC control panel power supply.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box (C.I.B.) wiring. |  |
|  | **STEP 1A.** Check the control panel display for faults. | Control panel indicates fault(s)? |
|  | **STEP 1A-1.** Check the control panel power SUPPLY wire for voltage +24 VDC. | Less than +24 VDC? |

### STEP 1. Check the customer interface box (C.I.B.) wiring.

#### STEP 1A. Check the control panel display for faults.

| **Conditions:** Locate the control panel display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the control panel display for faults. | Control panel indicates fault(s)? **YESRepair:** Troubleshoot the appropriate fault code. Reference the Marine Auxiliary QSB7-DM CM850 Fault Code Troubleshooting Manual, Bulletin 4325972, Section TF; or ISM and QSM 11 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual\|3666266]], Section TF; or X15 CM2350 X125M Fault Code Troubleshooting Manual, Bulletin 5504346, Section TF. | Repair complete |
| Control panel indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the control panel power SUPPLY wire for voltage +24 VDC.

| **Conditions:** Open the C.I.B. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) wire at the control panel. Place one test lead at the battery 1 voltage (switched power) SUPPLY wire at the control panel. Place the other test lead on the panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24 VDC? **YESRepair:** Check the batteries. See equipment manufacturer service information. | Repair complete |
| Less than +24 VDC? **NO** | Contact a Cummins® Authorized Repair Location. |  |
