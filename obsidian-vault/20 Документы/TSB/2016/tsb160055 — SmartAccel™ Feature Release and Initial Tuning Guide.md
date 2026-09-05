---
type: "TSB"
doc: "tsb160055"
title_en: "SmartAccel™ Feature Release and Initial Tuning Guide"
modified: "2021-10-07"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160055.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160055.pdf"
tags:
  - "документ/tsb"
---

# SmartAccel™ Feature Release and Initial Tuning Guide

> [!abstract] TSB · `tsb160055`
> **Даты:** изменён 2021-10-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2016/tsb160055.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb160055.pdf)

## SmartAccel™ Feature Release and Initial Tuning Guide

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- ISX12 CM2350 X102
- ISX15 CM2350 X101
- X15 CM2350 X114B
- X15 CM2450 X124B
- X12 CM2350 X119B
- X15 CM2450 X134B
- X12 CM2450 X137B

Manual transmissions **only**.

**Issue**

Customer has concerns with vehicle powertrain robustness or has experienced powertrain component malfunctions when launching the vehicle from a stop.

**Resolution**

The SmartAccel™ feature has been released to increase powertrain robustness during a vehicle launch. This is a user-selectable feature in INSITE™ electronic service tool. When enabled, the SmartAccel™ feature will limit the rate at which torque is applied to the flywheel. This feature is designed to protect powertrain components from impact torque from harsh events such as a clutch dump when the Accelerator Pedal Position is 100%. The SmartAccel™ feature is designed to protect powertrain components on all transmissions.

**Enabling SmartAccel™ Feature**

1. Determine Gear Ratio Threshold

- Connect INSITE™ electronic service tool version 8.1.2 or newer.
- Verify/Install engine control module (ECM) calibration code with SmartAccel™ feature. ECM calibration codes after 30 Mar 2016 have the SmartAccel™ feature.
- Enable SmartAccel™ in Features and Parameters.
- Determine highest gear used by customer at vehicle launch.
- Determine transmission gear ratios of the vehicle. See equipment manufacturer service information. See Table 1 below for example gear ratios.

| Table 1, Example Gear Ratios |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
| Gear Number | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| Gear Ratio | 14.8 | 10.95 | 8.09 | 5.97 | 4.46 | 3.32 | 2.45 | 1.81 | 1.34 | 1.00 |

- Determine average gear ratio between highest launch gear and next highest sequential gear. For Example:

2. Determine Torque Ramp Rate Value

- Connect INSITE™ electronic service tool version 8.1.2 or newer.
- Select Features and Parameters and select Vehicle Speed Source to see Rear Axle Ratio.
- If rear axle ratio \< 2.47, then input 370 lb\*ft/s \[ 500 N•m/s \] for Torque Ramp Rate.
- If rear axle ratio \>= 2.47 and rear axle ratio \< 3.91, then input 553 lb\*ft/s \[ 750 N•m/s \] for Torque Ramp Rate.
- If rear axle ratio \>= 3.91, then input 737 lb\*ft/s \[ 1000 N•m/s \] for Torque Ramp Rate.

**Customer Communication**

Decrease in acceleration in the first few gears from launch may be observed.

**Production Status**

SmartAccel™ feature has been implemented for production. See Table 2.

| Table 2, Production Information |  |  |  |
|---|---|---|---|
| Product | Engine Serial Number (ESN) First | Build Date\* | Engine Plant |
| ISX12 CM2350 X102 | 75050864 | 6 Apr 16 | Jamestown Engine Plant |
| ISX15 CM2350 X101 | 79912573 | 5 Apr 16 | Jamestown Engine Plant |
| \*Engine build date can be found on the engine dataplate. |  |  |  |

### Document History
