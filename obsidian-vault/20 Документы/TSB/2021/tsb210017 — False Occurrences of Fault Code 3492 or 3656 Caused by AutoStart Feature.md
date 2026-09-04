---
type: "TSB"
doc: "tsb210017"
title_en: "False Occurrences of Fault Code 3492 or 3656 Caused by AutoStart Feature"
modified: "2021-01-29"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210017.pdf"
tags:
  - "документ/tsb"
---

# False Occurrences of Fault Code 3492 or 3656 Caused by AutoStart Feature

> [!abstract] TSB · `tsb210017`
> **Даты:** изменён 2021-01-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210017.pdf)

## False Occurrences of Fault Code 3492 or 3656 Caused by AutoStart Feature

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B

**Issue**

Symptom:

- Engine with AutoStart feature has active Fault Codes 3492, 3656, or has more than one inactive count within the last 25 engine operating hours.

Root Cause:

- The interaction between the AutoStart system and an engine diagnostic to detect errors in the engine off timer has caused a false occurrence of this fault code.

**Verification**

- Verify unit is equipped with AutoStart system and system was in use recently.

**Resolution**

- Troubleshoot active or inactive fault codes with more than one count in the last 25 engine hours.
- Engine control module (ECM) calibration code to address this issue will be available in second quarter of 2021.
- Do **not** replace the ECM for this issue.

### Document History
