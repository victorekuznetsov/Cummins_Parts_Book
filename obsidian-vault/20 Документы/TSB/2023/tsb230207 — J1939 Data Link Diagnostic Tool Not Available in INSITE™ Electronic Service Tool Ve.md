---
type: "TSB"
doc: "tsb230207"
title_en: "J1939 Data Link Diagnostic Tool Not Available in INSITE™ Electronic Service Tool Version 8.8.0 or Newer When Using Nexiq NEXIQ USB- Link™ II Data Link Adapter Version 2.7.0.3 or Newer."
modified: "2024-12-12"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230207.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb230207.pdf"
tags:
  - "документ/tsb"
---

# J1939 Data Link Diagnostic Tool Not Available in INSITE™ Electronic Service Tool Version 8.8.0 or Newer When Using Nexiq NEXIQ USB- Link™ II Data Link Adapter Version 2.7.0.3 or Newer.

> [!abstract] TSB · `tsb230207`
> **Даты:** изменён 2024-12-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2023/tsb230207.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb230207.pdf)

## J1939 Data Link Diagnostic Tool Not Available in INSITE™ Electronic Service Tool Version 8.8.0 or Newer When Using Nexiq NEXIQ USB- Link™ II Data Link Adapter Version 2.7.0.3 or Newer.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- B6.7 CM2350 B121B
- B6.7 CM2450 B155B
- L9 CM2350 L116B
- L9 CM2350 L123B
- L9 CM2450 L126B
- X12 CM2350 X119B
- X12 CM2450 X137B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B
- X15 CM2450 X142B

**Issue Summary**

Symptom:

- The J1939 Data Link Diagnostic Tool is **not** available.

Root Cause:

- INLINE™ 7 drivers are required to use the J1939 Data Link Diagnostic tool with the NEXIQ USB-Link™ II Data Link Adapter.

**Verification**

The J1939 Data Link Diagnostic Tool, (previously known as CAN Bus Diagnostics Tool) under the Tools tab in INSITE™ Electronic Service Tool is greyed out.

**Resolution**

- Download and install the INLINE™ 7 drivers version 2.8.0.7 or newer. Reference the link below: **Note:** [https://www.cummins.com/support/digital-products-and-services-support/inline-support](https://www.cummins.com/support/digital-products-and-services-support/inline-support)

- If the J1939 Data Link Diagnostics Tool is still greyed out, manually install the application by using the following directory.
- C:\\Program Files (x86)\\Cummins\\INLINE 7\\ Setup\_Cummins\_CAN\_Bus\_Diagnostics.exe

### Document History
