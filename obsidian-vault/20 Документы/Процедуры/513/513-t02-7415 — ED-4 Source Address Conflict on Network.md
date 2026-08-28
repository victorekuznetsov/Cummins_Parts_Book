---
type: "Процедура"
doc: "513-t02-7415"
title_en: "ED-4 Source Address Conflict on Network"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# ED-4 Source Address Conflict on Network

> [!abstract] Процедура · `513-t02-7415`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-7415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-7415.pdf)

Printable Version

### Symptoms

- Alarm Code 7415 is displayed.

### How To Use This Tree

This symptom tree can be used to troubleshoot controller area network (CAN) symptoms. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes include:

- Original equipment manufacturer (OEM) device on network

- ED-4 source address.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the ED-4 display |  |
|  | **STEP 1A.** Check ED-4 software. | Latest vessel personality file (VPF) and software installed? |
|  | **STEP 1B.** Check configuration in ED-4 setup. | ED-4 displays setup correctly? |
|  | **STEP 1C.** Check the OEM device. | Alarm Code 7415 active? |

### STEP 1. Check the ED-4 display.

#### STEP 1A. Check ED-4 software.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify latest VPF is downloaded in the display. Refer to Procedure 015-044 in Section 15. Verify the latest display software is downloaded in the ED-4 display. Refer to Procedure 015-107 in Section 15. | Latest vessel personality file and software installed? **YES** | 1B |
| Latest vessel personality file and software installed? **NORepair:** Download correct VPF to the display from Cummins QuickServe® Online. [[513-015-044 — Managing Vessel Personalities\|Refer to Procedure 015-044 in Section 15.]] Download latest version of the display software from Cummins QuickServe® Online. [[513-015-107 — Display Software\|Refer to Procedure 015-107 in Section 15.]] | Repair complete. |  |

#### STEP 1B. Check configuration in ED-4 setup.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify the source address of all ED-4 displays on the network. Refer to Procedure 015-108 in Section 15. | ED-4 displays setup correctly? **YES** | 1C |
| ED-4 displays setup correctly? **NORepair:** An incorrect setup has been detected in the ED-4 display. Select the source address. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete. |  |

#### STEP 1C. Check the OEM device.

| **Conditions:** Turn system enable switch OFF. Remove the OEM device from the network. Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Wait 30 seconds. Read the ED-4 display. | Alarm Code 7415 active? **YESRepair:** Refer to the OEM Display Does **Not** Display Data - NMEA 2000 and/or J1939 Does **Not** Work troubleshooting tree in Section TT. | Repair complete. |
| Alarm Code 7415 active? **NORepair:** Verify the OEM device source address is setup incorrectly. See equipment manufacturer service information. | Repair complete. |  |
