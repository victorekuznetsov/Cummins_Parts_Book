---
type: "TSB"
doc: "tsb170085"
title_en: "Fault Code 5867: PACCAR™ Chassis with Battery Disconnect Switch"
modified: "2026-04-08"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170085.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb170085.pdf"
tags:
  - "документ/tsb"
---

# Fault Code 5867: PACCAR™ Chassis with Battery Disconnect Switch

> [!abstract] TSB · `tsb170085`
> **Даты:** изменён 2026-04-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2017/tsb170085.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb170085.pdf)

## Fault Code 5867: PACCAR™ Chassis with Battery Disconnect Switch

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

Information Only - OEM Related Matter Not Covered By Cummins® - Contact Appropriate OEM Dealer or OEM Representative For Additional Information

### Contents

**Product Affected**

Engines:

- B6.7 CM2350 B121B
- ISB6.7 CM2350 B142
- ISL9 CM2350 L111
- L9 CM2350 L116B
- X12 CM2350 X119B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B
- X15 CM2450 X142B

Original Equipment Manufacturer (OEM):

- PACCAR™ (Peterbilt or Kenworth chassis)
- **Only** units equipped with battery disconnect switch

**Issue**

Symptom:

- Fault Code 5867 (Aftertreatment Diesel Exhaust Fluid Dosing Unit Relay Feedback - Voltage Below Normal or Shorted to Low Source) often leading to unnecessary replacement of OEM diesel exhaust fluid (DEF) pump relay or other components.

Root Cause:

- PACCAR™ chassis do **not** provide a dedicated power source to the aftertreatment DEF dosing unit. Units equipped with battery disconnect switches can interrupt the DEF system power down and purge sequence, logging Fault Code 5867.

**Verification**

- If unit is equipped with a battery disconnect switch; clear fault codes, turn key to OFF position for two minutes, turn key to ON position and see if Fault Code 5867 returns. If Fault Code 5867 does **not** return after being cleared, see Resolution section below.

**Resolution**

- Verify notification sticker directing proper power down procedures is affixed to chassis near battery disconnect switch. Contact local PACCAR™ support location for battery disconnect power notification sticker See Figure 1 below.
- Inform operator of proper power down procedure which requires two minutes before disconnecting power using battery disconnect switch.

![[19r99722.png]]

Figure 1, Battery Disconnect Direction Sticker.

### Document History
