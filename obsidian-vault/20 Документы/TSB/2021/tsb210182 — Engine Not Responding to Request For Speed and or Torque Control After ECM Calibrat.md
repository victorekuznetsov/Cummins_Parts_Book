---
type: "TSB"
doc: "tsb210182"
title_en: "Engine Not Responding to Request For Speed and/or Torque Control After ECM Calibration Code Update"
modified: "2021-08-25"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210182.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210182.pdf"
tags:
  - "документ/tsb"
---

# Engine Not Responding to Request For Speed and/or Torque Control After ECM Calibration Code Update

> [!abstract] TSB · `tsb210182`
> **Даты:** изменён 2021-08-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210182.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210182.pdf)

## Engine Not Responding to Request For Speed and/or Torque Control After ECM Calibration Code Update

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

Information Only - OEM Related Matter Not Covered By Cummins® - Contact Appropriate OEM Dealer or OEM Representative For Additional Information

### Contents

**Product Affected**

- X12 CM2350 X119B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2350 X123B
- X15 CM2350 X129B
- X15 CM2450 X124B
- X15 CM2450 X134B

**Issue Summary**

Symptom:

- Sending device **not** functioning or responding after a new ECM calibration code revision was installed. For example, PTO or adaptive cruise controls **not** responding.

Root Cause:

- OEM, truck equipment manufacturer, or body builder set an unsupported parameter.

**Verification**

- Verify customer complaint.
- Confirm ECM calibration code revision date higher than 1 Feb 2021 for X15 product, and 8 January 2021 for X12 products.

**Resolution**

- Contact the supplier: the OEM, truck equipment manufacturer, body builder, or other third party. The supplier needs to update the software to allow the TSC1 messages to follow appropriate Cummins Engineering Bulletin (CEB) and SAE standards.
- Cummins Inc. is **not** able to correct the value used by the third party.

### Document History
