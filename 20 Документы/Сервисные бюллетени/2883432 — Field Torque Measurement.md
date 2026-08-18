---
aliases:
  - "Измерение момента затяжки в полевых условиях"
type: "Сервисный бюллетень"
doc: "2883432"
title_en: "Field Torque Measurement"
title_ru: "Измерение момента затяжки в полевых условиях"
released: "2013-11-12"
modified: "2014-03-21"
group: "00 - Complete Engine / Troubleshooting"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
figures: 9
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883432.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/2883432.pdf"
tags:
  - "документ/бюллетень"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "тема/complete-engine-troubleshooting"
---

# Field Torque Measurement
**Измерение момента затяжки в полевых условиях**

> [!abstract] Сервисный бюллетень · `2883432`
> **Раздел Cummins:** 00 - Complete Engine / Troubleshooting
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2013-11-12 · изменён 2014-03-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/bulletin/2883432.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/bulletin/2883432.pdf)

## Field Torque Measurement

## Introduction

This document outlines the proper steps to take when a field torque measurement is requested.

Cummins Inc. may request the field personal to take torque measurements on specific capscrew joints to help in field investigations. Due to numerous joint designs, Cummins Inc. will specify the field torque measurement procedure and capscrew numbering pattern to use for each request of field torque measurement. This procedure will describe the tools, methods, determination factors, and limitations involved in making these measurements in the field.

## Limitations of Field Torque Measurement Methods:

Field torque measurement methods are used to estimate torque on the capscrew, **not** clamp load on the joint. Environmental influences such as heat, moisture, and chemicals can cause oxidation at the contact surfaces between the mounting component and the capscrew. This oxidation increases friction at the capscrew, resulting in increased torque required to move the capscrew. In this case, the higher torque measurement due to friction does **not** mean that the actual clamp load on the joint is increased.

Field torque measurement methods incorporate uncertainty due to oxidation, friction, fretting, calibration accuracy of the torque wrench, use of extensions on the wrench, interpretation of onset of motion, and the accuracy of aligning marks. Due to these limitations, the accuracy of the torque reading is **not** guaranteed. These values, therefore, should be considered to be estimates.

## Correct Tools for the Job:

All three measurement methods require a torque wrench calibrated to acceptable accuracy in the torque range to be measured. For tool calibration, contact a local tool manufacturer. Direct indicating wrenches (digital or dial readout) are the easiest to use and are recommended. A click-style wrench can be used for loosening direction breakaway torque method, but manually adjusting the torque on the wrench can be time consuming. The maximum torque recall feature on electronic wrenches is useful for the Breakaway Torque and Return to Line Methods.

![[17800197.png]]

Dial Wrench

## 1) Return to Line Method:

![[17800199.png]]

Before the capscrews are disturbed, mark a line using a paint pen or permanent marker on both the capscrew and the mounting surface (1).

The capscrew is turned 90 degrees in the loosen direction (2).

Then, while monitoring the torque value on the wrench, tighten the capscrew until the scribed lines are aligned (3).

> [!note] Note · Примечание
> If more than one capscrew is checked, use the numbering pattern required by Cummins Inc. Return capscrew to where scribed lines are aligned before moving to next capscrew.

![[17800200.png]]

Record the value the torque wrench reads.

## 2) Breakaway Torque Methods:

![[17800201.png]]

Figure 1

#### Loosening - Direction Breakaway Torque:

- Slowly increasing torque is applied to the fastener in the loosening direction until the nut rotates noticeably or the capscrew head rotates 90 degrees (Figure 1).
- The peak torque value observed is the breakaway torque value.

> [!note] Note · Примечание
> If more than one capscrew is checked, use the numbering pattern required by Cummins Inc. Return capscrew to where scribed lines are aligned before moving to next capscrew.

![[17800202.png]]

Figure 2

#### Tightening - Direction Breakaway Torque:

- Slowly increasing torque is applied to the fastener in the tightening direction until the nut rotates noticeably or the capscrew head rotates noticeably (Figure 2).
- The torque at the onset of motion is the breakaway torque value (Figure 2).

## Determining Torque Measurement Method:

Use the following chart to determine which torque measurement method to use, based on joint condition and the capscrew's grip length/diameter ratio.

| Joint Condition | Torque Measurement Method | Grip Length/Diameter Ratio |
|---|---|---|
| Joints where oxidation is likely | Return to Line Method | **Not** Applicable |
| Joints where oxidation is unlikely and grip length/diameter ratio is 2:1 or less. | Loosening - direction breakaway method. | Figure 1 |
| Joints where oxidation is unlikely and grip length/diameter ratio is greater than 2. | Return to Line Method | Figure 2 |

![[17800203.png]]

Figure 1

Grip length/diameter ratio is 2:1 or less.

![[17800204.png]]

Figure 2

Grip length/diameter ratio is greater than 2.

## 3) Torque - Turn and Measurement Method:

![[17800205.png]]

Before the capscrews are disturbed, mark a line using a paint pen or permanent marker on both the capscrew and the mounting surface (1).

The capscrew is turned 180 degrees in the loosen direction (2).

Tighten the capscrew to the primary torque value. Do **not** turn to the angle prescribed in the Service Manual. (3).

![[17800206.png]]

Measure and report the number degree +/- between the marked lines (4).

> [!note] Note · Примечание
> If more than one capscrew is checked, use the numbering pattern required by Cummins Inc. Return capscrew to where scribed lines are aligned before moving to next capscrew.

### Document History
