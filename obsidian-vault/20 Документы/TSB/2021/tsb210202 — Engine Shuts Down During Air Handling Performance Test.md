---
type: "TSB"
doc: "tsb210202"
title_en: "Engine Shuts Down During Air Handling Performance Test"
modified: "2023-11-16"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210202.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210202.pdf"
tags:
  - "документ/tsb"
---

# Engine Shuts Down During Air Handling Performance Test

> [!abstract] TSB · `tsb210202`
> **Даты:** изменён 2023-11-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2021/tsb210202.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb210202.pdf)

## Engine Shuts Down During Air Handling Performance Test

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- B6.7 CM2350 B121B
- L9 CM2350 L116B
- X15 CM2350 X114B
- X15 CM2350 X116B

**Issue**

Symptom:

- Engine Shuts Down During Air Handling Performance Test
- Air Handling Performance Test did **not** complete

Root Cause:

- Idle Shutdown time less than test time

**Verification**

- The Engine Shuts Down During the Air Handling Performance Test. The following message is displayed in INSITE™ electronic service tool, “The test has stopped or could not start because the keyswitch was turned off or an engine shutdown request was active. Correct the issue and restart the test.”
- Check the Time Before Shutdown Parameter in the Idle Shutdown Feature located in INSITE™ electronic service tool Features and Parameters. If the Time Before Shutdown Parameter is less than 10 minutes, proceed to the Resolution section below.

**Resolution**

- The following products have ECM calibration code revisions released to fix the issue:
- Compare the ECM code and revision number in the ECM to the ECM calibration revision listed in the ECM Calibration Revision History Database on QuickServe® Online (QSOL) for applicable changes.
- If an ECM calibration code update for this fault code is available, the ECM calibration code revision **must** be that revision or higher. For ECM calibration code calibration process, see corresponding Service Manual. Reference Procedure 019-032 in Section 19.

For X15 CM2350 X114B and X15 CM2350 X116B:

- Temporarily disable Idle Shutdown or temporarily extend the Idle Shutdown to greater than 10 minutes.
- Once repair is complete, restore the customers Idle Shutdown Parameters to original setting.
- If Idle Shutdown Parameters are protected with greenhouse gas emissions password, then the test is **not** able to be performed.

### Document History
