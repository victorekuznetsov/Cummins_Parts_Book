---
aliases:
  - "Блок управления дизелем сконфигурирован неверно"
type: "Процедура"
doc: "116-t02-1141"
title_en: "Diesel Control Unit Configured Incorrectly"
title_ru: "Блок управления дизелем сконфигурирован неверно"
modified: "2008-07-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021617"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/116"
---

# Diesel Control Unit Configured Incorrectly
**Блок управления дизелем сконфигурирован неверно**

> [!abstract] Процедура · `116-t02-1141`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021617 — C Command Elite and C Command Elite Plus Panel System Marine Master Repair Manual|4021617]]
> **Секции:** Section TT - Troubleshooting Symptoms (New Format)
> **Даты:** изменён 2008-07-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/116/116-t02-1141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/116-t02-1141.pdf)

Printable Version

### Symptoms

- The DCU410 unit is configured incorrectly for the engine application.

### How To Use This Tree

This symptom tree can be used to troubleshoot a malfunction. Start by performing Step 1 troubleshooting. Step 2 will ask a series of questions and will provide a list of troubleshooting steps to perform, depending on the symptom.

### Shoptalk

This fault code has no external wiring from the DCU410 unit except the +24-VDC DCU410 unit power supply.

## Troubleshooting Summary

| STEPS | SPECIFICATIONS |  |
|---|---|---|
| STEP 1. | Check the customer interface box wiring. |  |
|  | **STEP 1A.** Check the DCU410 unit display for faults. | DCU410 unit indicates fault(s)? |
|  | **STEP 1A-1.** Check the DCU410 power supply for voltage +24-VDC. | Less than +24-VDC? |

### STEP 1. Check the customer interface box wiring.

#### STEP 1A. Check the DCU410 unit display for faults.

| **Conditions:** Locate the DCU410 unit display. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the DCU410 unit display for faults. | DCU410 unit indicates fault(s)? **YESRepair:** Refer to the Electronic Control System Troubleshooting and Repair Manual, QSK19 CM850 Modular Common Rail System Series Engine, Bulletin 4021493 or the Electronic Control System Troubleshooting and Repair Manual, QSK38, QSK50, and QSK60 CM850 Modular Common Rail System Series Engine, Bulletin 4021533. | Repair complete |
| DCU410 unit indicates fault(s)? **NO** | 1A-1 |  |

#### STEP 1A-1. Check the DCU410 power supply wire for voltage +24-VDC.

| **Conditions:** Open the customer interface box. |  |  |
|---|---|---|
| **Action** | **Specification/Repair** | **Next Step** |
| Check the voltage at the battery 1 voltage (switched power) wire at the DCU410 unit. Place one test lead at the battery 1 voltage (switched power) supply wire at the DCU410 unit. Place the other test lead on panel ground. Refer to the appropriate circuit diagram or wiring diagram for pin and wire identification. | Less than +24-VDC? **YESRepair:** Check the batteries. Refer to the OEM service manual. | Repair complete |
| Less than +24-VDC? **NO** | Contact a Cummins® Authorized Repair Location. |  |
