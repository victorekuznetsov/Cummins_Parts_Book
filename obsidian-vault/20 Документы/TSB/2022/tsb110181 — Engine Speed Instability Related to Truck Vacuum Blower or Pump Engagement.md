---
type: "TSB"
doc: "tsb110181"
title_en: "Engine Speed Instability Related to Truck Vacuum Blower or Pump Engagement"
released: "2022-05-26"
modified: "2022-05-26"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110181.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110181.pdf"
tags:
  - "документ/tsb"
  - "год/2022"
---

# Engine Speed Instability Related to Truck Vacuum Blower or Pump Engagement

> [!abstract] TSB · `tsb110181`
> **Даты:** выпущен 2022-05-26 · изменён 2022-05-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2011/tsb110181.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb110181.pdf)

## Engine Speed Instability Related to Truck Vacuum Blower or Pump Engagement

### Core Issue

Some units, with transfer cases, have exhibited low power and/or engine speed instability when the transfer case or pump system is engaged. This instability typically causes the operator to shut down the system. New engine control module (ECM) software has added new engine speed governor tuning that can address most of these issues. Other possible causes include incorrect setting of ECM Features and Parameters.

### Confirmation

**Product Affected:**

- ISL9 CM2350 L101
- ISX12 CM2350 X102
- ISX12/ISX11.9 CM2250
- ISX12N CM2380 X120B
- ISX15 CM2250
- ISX15 CM2250 SN
- ISX15 CM2350 X101
- L9 CM2350 L116B
- L9 CM2450 L126B
- L9N CM2380 L124B
- X12 CM2350 X119B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B

In order to properly test for low power or instability; the unit **must** be operated with the transmission in gear, the transfer case engaged, and a load placed on the engine.

1. If the unit displays vehicle speed on the dash during operation, most likely the Transmission Driven PTO feature is **not** properly set up. Reference “Resolution” section for proper feature settings.
2. Incorrect Transmission Driven PTO Type may have been selected. Reference “Resolution” below for proper feature settings.
3. The truck body builder may have disabled the vehicle speed sensor (VSS) signal to the ECM.
4. The truck original equipment manufacturer (OEM) may have installed an additional PTO switch that may be labeled “PTO Control”. This switch will disable the VSS signal to the ECM.
5. Check for engine control module (ECM) updates for this issue on QuickServe™ Online or using latest INCAL™ DVD.
6. Check for fault codes, including intermittent ones.
7. If the vehicle has a Parking Brake Switch input that is either wired directly to the ECM or is multiplexed within, INSITE™ electronic service tool Parking Brake Switch **must** be ENABLED.

> [!note] Note · Примечание
> If the vehicle does not have a parking brake switch input, then the OEM or body builder must install the governor type switch to indicate to the ECM when the transfer case is engaged.

### Resolution

1. Proper settings for Transmission Driven PTO:
2. Proper settings for PTO:
3. Restore the VSS signal back to original factory condition. Ensure the VSS circuit is **not** interrupted. The ECM **must** read vehicle speed for the feature to work.
4. Check for engine control module (ECM) updates for this issue on QuickServe™ Online or using latest INCAL™ DVD. Update the ECM calibration. Reference Procedure 019-032. See Service Manual.
5. Repair all fault codes.

If none of the above resolves the issue, contact your authorized Cummins® repair location. For authorized Cummins® repair locations, follow your technical support escalation process.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
