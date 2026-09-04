---
type: "TSB"
doc: "tsb200210"
title_en: "Fault Code 6637 on PACCAR™ Chassis with Horton® Fan Controller"
modified: "2020-10-21"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200210.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb200210.pdf"
tags:
  - "документ/tsb"
---

# Fault Code 6637 on PACCAR™ Chassis with Horton® Fan Controller

> [!abstract] TSB · `tsb200210`
> **Даты:** изменён 2020-10-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2020/tsb200210.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb200210.pdf)

## Fault Code 6637 on PACCAR™ Chassis with Horton® Fan Controller

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

Information Only - OEM Related Matter Not Covered By Cummins® - Contact Appropriate OEM Dealer or OEM Representative For Additional Information

### Contents

**Product Affected**

This issue is unique to Kenworth™ and Peterbilt™ units equipped with Horton® fan controller.

- X15 CM2350 X114B
- X15 CM2450 X124B

**Issue**

Symptom:

- Fault Code 6637 is active or has inactive counts.
- Amber service lamp intermittently illuminates.

Root Cause:

- Horton® fan controller (OEM part with firmware part number 230023) sends “Fan speed signal \>100%” to engine control module (ECM) causing FC6637 to become active.

**Verification**

- The firmware version of the fan controller can be found on the back label of the fan controller.
- Confirm unit has fan controller with old firmware, part number 230023.

![[08r00548.png]]

Figure 1, Horton® Fan Controller

**Resolution**

- This issue is unique to PACCAR™ chassis. All claims and parts should be sourced appropriately through PACCAR™.
- Contact the OEM for the appropriate part number, reference Horton® Product Technical Bulletin PTB 2020.
- Horton® has released an updated fan controller under the existing assembly part number.
- The firmware part number located on the back of the fan controller has been updated.

### Document History
