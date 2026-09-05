---
type: "TSB"
doc: "tsb120309"
title_en: "Fault Code 3714, 3712, 6255, or 6254 Active with No Other Active Fault Codes"
released: "2026-06-08"
modified: "2026-06-08"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120309.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120309.pdf"
tags:
  - "документ/tsb"
  - "год/2026"
---

# Fault Code 3714, 3712, 6255, or 6254 Active with No Other Active Fault Codes

> [!abstract] TSB · `tsb120309`
> **Даты:** выпущен 2026-06-08 · изменён 2026-06-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120309.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb120309.pdf)

## Fault Code 3714, 3712, 6255, or 6254 Active with No Other Active Fault Codes

### Core Issue

**Product Affected**

- All electronically controlled engines

Symptom:

- Fault Code 3714, 3712, 6255, or 6254 could become active after adjusting multiplexing parameters or troubleshooting other active selective catalytic reduction (SCR) related fault codes.

Root Cause:

- INSITE™ electronic software tool issue.

### Confirmation

For some units that have a hardwired (analog) diesel exhaust fluid (DEF) tank level and temperature sensor, Fault Codes 285 and 4572 will become active because a software parameter defaulted to multiplexed. Even if recommended Cummins® electronic service tool or equivalent is adjusted correctly to reflect the analog sensors, Fault Code 3714 or 6255 will become active.

Other units may trigger SCR related Fault Code(s) 1682, 1683, 1713, 2976, 3151, 3238, 3241, 3258, 3261, 3423, 3425, 3558, 3559, 3563, 3567, 3568, 3572, 3574, 3575, 3596, 3748, 4152, 4156, 4169, or 4769. These fault codes will lead to Fault Code 3714 or 6255 (inducement) within 1 hour and will eventually lead to Fault Code 3712 or 6254 (severe inducement) if **not** addressed. Even when those active fault(s) are addressed before Fault Code 3714 or 6254 becomes active and are cleared, Fault Codes 3714 or 6255 and 3712 or 6254 will still become active because the diagnostic does **not** verify the fault codes are cleared.

### Resolution

- To correct the issue, troubleshoot all active fault codes. Do **not** use the "Clear All Faults" command to clear fault codes off engine control module (ECM) after troubleshooting is complete.
- Follow the instructions under the “Conditions for Clearing the Fault Code” section in the Fault Code Overview page. Verify all fault codes, including Fault Code 3714, 6255, 6254, or 3712, are inactive.
- If the “Clear All Faults” command was used to clear all faults in the ECM, use recommended Cummins® electronic service tool or equivalent to calibrate the ECM with the latest calibration from QuickServe® Online or the April 2013 INCAL Calibration DVD or newer. Once the ECM has the new software, all fault codes will be cleared.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
