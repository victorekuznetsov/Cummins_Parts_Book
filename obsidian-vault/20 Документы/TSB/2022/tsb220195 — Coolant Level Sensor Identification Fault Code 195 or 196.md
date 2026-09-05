---
type: "TSB"
doc: "tsb220195"
title_en: "Coolant Level Sensor Identification: Fault Code 195 or 196"
modified: "2022-10-13"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220195.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb220195.pdf"
tags:
  - "документ/tsb"
---

# Coolant Level Sensor Identification: Fault Code 195 or 196

> [!abstract] TSB · `tsb220195`
> **Даты:** изменён 2022-10-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2022/tsb220195.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb220195.pdf)

## Coolant Level Sensor Identification: Fault Code 195 or 196

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- B6.7 CM2350 B121B
- B6.7 CM2450 B155B
- ISX12 CM2350 X102
- L9 CM2350 L116B
- L9 CM2350 L123B
- L9 CM2450 L126B
- L9N CM2380 L142B
- X12 CM2350 X119B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B

**Issue Summary**

Symptom:

- Fault Code 195 or 196
- There can be two coolant level sensors (typically on the Bus Applications) that are related to the coolant level sensor. One coolant level sensor is connected to the ECM and the fault code, the other coolant level sensor is connected to the OEM as the dashboard light.

**Verification**

The fault code can **only** be cleared and issue corrected by troubleshooting the correct coolant level sensor. Before beginning the troubleshooting process, the correct sensor that connects back to the ECM **must** be identified. When the ECM is powered down the OEM sensor will still have voltage

![[19r99881.png]]

Figure 1, Example of Two Coolant Level Sensors.

**Resolution**

If there are two coolant level sensors, identify the correct ECM connected coolant level sensor and continue with the normal troubleshooting steps.

### Document History
