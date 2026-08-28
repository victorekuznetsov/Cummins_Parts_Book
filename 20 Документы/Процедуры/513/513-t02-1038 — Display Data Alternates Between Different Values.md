---
type: "Процедура"
doc: "513-t02-1038"
title_en: "Display Data Alternates Between Different Values"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1038.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1038.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Display Data Alternates Between Different Values

> [!abstract] Процедура · `513-t02-1038`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2019-10-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-t02-1038.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-t02-1038.pdf)

Printable Version

### Symptoms

- Data parameters repeatedly switch between different values on the display.

### How To Use This Tree

This symptom tree can be used to troubleshoot accessory relay control devices. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

Possible causes are:

- Incorrect vessel personality file

- ED-4 display setup improperly.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the ED-4 display. |  |
|  | **STEP 1A.** Check ED-4 display configuration. | J1939 source 1 and 2 set properly? |
|  | **STEP 1B.** Check vessel personality file. | Vessel personality file correct? |

### STEP 1. Check the ED-4 display.

#### STEP 1A. Check ED-4 display configuration.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Verify engine J1939 source. Go to the configuration in the menu in the ED-4 display. Verify engine J1939 source 1 and 2 settings. Refer to Procedure 015-108 in Section 15. | J1939 source 1 and 2 set properly? **YES** | 1B |
| J1939 source 1 and 2 set properly? **NORepair:** Configure the ED-4 display properly. [[513-015-108 — Display Configuration\|Refer to Procedure 015-108 in Section 15.]] | Repair complete. |  |

#### STEP 1B. Check the vessel personality file.

| **Conditions:** Turn system enable switch ON. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Measure the resistance. Verify correct vessel personality file is downloaded in the display. Refer to Procedure 015-044 in Section 15. Refer to the circuit diagram or wiring diagram for connector pin identification. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter\|Refer to Procedure 019-360 in Section 19.]] | Vessel personality file correct? **YESRepair:** Request a Cummins® Marine application engineer on site. | Repair complete. |
| Vessel personality file correct? **NORepair:** Download correct vessel personality file to the display for Cummins QuickServe® Online. [[513-015-035 — Display(s) and Instrumentation\|Refer to Procedure 015-035 in Section 15.]] | Repair complete. |  |
