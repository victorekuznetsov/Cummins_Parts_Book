---
type: "TSB"
doc: "tsb220065"
title_en: "SmartAccel™ Stumble, Misfire, or Hesitation During a Snap Throttle with a Stationary Vehicle"
modified: "2022-04-01"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220065.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb220065.pdf"
tags:
  - "документ/tsb"
---

# SmartAccel™ Stumble, Misfire, or Hesitation During a Snap Throttle with a Stationary Vehicle

> [!abstract] TSB · `tsb220065`
> **Даты:** изменён 2022-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220065.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb220065.pdf)

## SmartAccel™ Stumble, Misfire, or Hesitation During a Snap Throttle with a Stationary Vehicle

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- ISX12 CM2350 X102
- ISX15 CM2350 X101
- X12 CM2350 X119B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B

**Issue Summary**

Symptom:

- Unit experiences a stumble, misfire, or hesitation during a snap throttle while stationary.

Root Cause:

- The SmartAccel™ feature can limit torque ramp rate of the engine when the vehicle is **not** moving and is **not** in gear; therefore, the SmartAccel™ feature can limit the torque output of the engine during these events.

**Verification**

- Disable the SmartAccel™ feature using INSITE™ electronic service tool.
- Run the snap throttle to verify stumble, misfire, or hesitation is no longer present.

**Resolution**

Review Technical Service Bulletin, SmartAccel™ Feature Release and Initial Tuning Guide, [[tsb160055 — SmartAccel™ Feature Release and Initial Tuning Guide\|TSB160055]] to verify the SmartAccel™ feature is programmed correctly. If so, review the vehicle specifications with the OEM and/or customer to see if the use of SmartAccel™ is needed or if SmartAccel™ could be disabled.

### Document History
