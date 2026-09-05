---
type: "TSB"
doc: "tsb250211"
title_en: "J1939 Data Link Diagnostic Tool Not Available in INSITE™ Electronic Service Tool Version 9.1.1.92"
modified: "2025-11-26"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250211.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250211.pdf"
tags:
  - "документ/tsb"
---

# J1939 Data Link Diagnostic Tool Not Available in INSITE™ Electronic Service Tool Version 9.1.1.92

> [!abstract] TSB · `tsb250211`
> **Даты:** изменён 2025-11-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250211.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250211.pdf)

## J1939 Data Link Diagnostic Tool Not Available in INSITE™ Electronic Service Tool Version 9.1.1.92

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

- The J1939 Data Link Diagnostic Tool is not available.

Root Cause:

- Latest revision of the J1939 Data Link Diagnostic Tool is not recognized in INSITE™ electronic service tool version 9.1.1.92.

**Verification**

The J1939 Data Link Diagnostic Tool under the Tools tab in INSITE is greyed out.

**Resolution**

Download and install the Inline 7 + USB Link 3 drivers version 3.3.0.2 or newer. Reference the link below:

https://www.cummins.com/support/digital-products-and-services-support/inline-support

Manually open the application by using the following directory in File Explorer.

C:\\Program Files (x86)\\Cummins\\J1939DataLinkDiagnosticTool\\J1939DatalinkDiagnosticTool.exe

### Document History
