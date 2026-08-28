---
type: "Процедура"
doc: "513-t02-1028"
title_en: "Display Software Will Not Install and/or Update"
modified: "2019-10-22"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1028.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1028.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Display Software Will Not Install and/or Update

> [!abstract] Процедура · `513-t02-1028`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1028.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1028.pdf)

Printable Version

### Symptoms

- Display software will **not** download into the display.

- Display shows a red screen while downloading.

### How To Use This Tree

This symptom tree can be used to troubleshoot display software download issues. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes include:

- Incompatible USB stick

- USB stick **not** plugged in properly

- Software corrupted.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check USB stick and port. |  |
|  | **STEP 1A.** Software file download. | Software file download? |
|  | **STEP 1B.** Check the USB stick installation. | USB stick installed properly? |
|  | **STEP 1C.** Check USB stick compatibility. | USB stick compatible? |
| STEP 2. | Check the display software. |  |
|  | **STEP 2A.** Check the display software. | Display software compatible? |
|  | **STEP 2B.** Download display software into another ED-4 display. | Display software downloaded properly? |
|  | **STEP 2C.** Download display software into another USB stick. | Display software downloaded properly? |

### STEP 1. Check USB stick and port.

#### STEP 1A. Software file download.

| **Conditions:** Turn enable switch OFF. Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check USB stick and port. Attempt to download the software file to the ED-4 display. Refer to Procedure 015-107 in Section 15. | Software file download? **YESRepair:** The download of the software file has corrected the issue. | Repair complete. |
| Software file download? **NO** | 1B |  |

#### STEP 1B. Check the USB stick installation.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the USB stick installation. Verify the USB stick is installed in the display USB port properly. Refer to Procedure 015-107 in Section 15. If a Cummins® USB extension harness is **not** being used, verify USB connection. Some USB connectors are reversible. | USB stick installed properly? **YES** | 1C |
| USB stick installed properly? **NORepair:** Install USB stick properly. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |

#### STEP 1C. Check USB stick compatibility.

| **Conditions:** None. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check USB stick compatibility. Verify the USB stick is compatible with the display. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | USB stick compatible? **YES** | 2A |
| USB stick compatible? **NORepair:** Download the display software to a compatible USB stick. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |

### STEP 2. Check the display software.

#### STEP 2A. Check the display software.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check display software. Verify the display software on USB stick meets download requirements. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Display software compatible? **YES** | 2B |
| Display software compatible? **NORepair:** Re-download the latest version of the display software from Cummins® QuickServe® On-line webpage to the USB stick. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |

#### STEP 2B. Download the display software into another ED-4 display.

| **Conditions:** Turn enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Download the display software. Download the latest display software to another ED-4 display. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Display software download properly? **YESRepair:** The download of the display software has corrected the issue. | Repair complete. |
| Display software download properly? **NO** | 2C |  |

#### STEP 2C. Download the display software into another USB stick.

| **Conditions:** Turn enable ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Download the display software. Download the display software into another USB stick. Re-attempt to download software to malfunctioning ED-4 display. | Display software downloaded properly? **YESRepair:** The download of the display software has corrected the issue. | Repair complete. |
| Display software downloaded properly? **NORepair:** Replace the ED-4 display. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] | Repair complete. |  |
