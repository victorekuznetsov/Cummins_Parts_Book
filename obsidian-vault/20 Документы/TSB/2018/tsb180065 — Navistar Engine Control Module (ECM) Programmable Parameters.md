---
type: "TSB"
doc: "tsb180065"
title_en: "Navistar Engine Control Module (ECM) Programmable Parameters"
modified: "2018-06-26"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2018/tsb180065.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb180065.pdf"
tags:
  - "документ/tsb"
---

# Navistar Engine Control Module (ECM) Programmable Parameters

> [!abstract] TSB · `tsb180065`
> **Даты:** изменён 2018-06-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2018/tsb180065.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb180065.pdf)

## Navistar Engine Control Module (ECM) Programmable Parameters

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

Information Only - OEM Related Matter Not Covered By Cummins® - Contact Appropriate OEM Dealer or OEM Representative For Additional Information

### Contents

**Product Affected**

Engines:

- X15 CM2350 X101
- L9 CM2350
- B6.7 CM2350

Original Equipment Mmanufacturer (OEM):

- Navistar

Chassis:

- LT
- HV
- MV

**Issue**

Symptom:

- Fault Codes 2222 and 6261
- Features and parameters are erased when performing an engine control module (ECM) calibration download via 9 pin connector.

Root Cause:

- Door controllers or “door pods” will interfere with data transfer required when calibrating the ECM, which prevents features and parameters from installing.

**Resolution**

- Perform ECM calibrations using 3 pin connector.
- Create an ECM calibration code template in case ECM calibration code download malfunctions.
- Remove door controller fuses before performing an ECM calibration code download using 9 pin connector.
- Reference iKNow article IK2600236 for further instructions.

### Document History
