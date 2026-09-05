---
type: "TSB"
doc: "tsb240170"
title_en: "Variable Geometry Turbocharger Actuator Installed Incorrectly"
modified: "2024-09-09"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2024/tsb240170.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb240170.pdf"
tags:
  - "документ/tsb"
---

# Variable Geometry Turbocharger Actuator Installed Incorrectly

> [!abstract] TSB · `tsb240170`
> **Даты:** изменён 2024-09-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2024/tsb240170.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb240170.pdf)

## Variable Geometry Turbocharger Actuator Installed Incorrectly

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- B6.7 CM2350 B121B
- L9 CM2350 L116B
- X15 CM2350 X114B
- X15 CM2350 X116B

**Issue Summary**

Symptom:

- Fault Code 3382
- Fault Code 3361
- Fault Code 3389
- Air Handling Performance Test did **not** pass

Root Cause:

- Variable geometry turbocharger actuator installed incorrectly

**Verification**

Verify one of the fault codes listed are active or inactive with more than one count and the Air Handling Performance Test did **not** pass for one of the messages in Table 1.

| Table 1, Air Handling Performance Test and Log Message Reference |  |
|---|---|
| Insite Message | Repair Decision message in test log |
| The VGT is causing exhaust pressure to dither. | VGT Stuck |
| An exhaust manifold leak has been detected. | Exhaust Leak |
| A position error has been detected with the VGT. | VGT Global Position Error |

- Find the did **not** pass log stored on the computer that ran the test, located at C:\\Intelect\\APT.
- Open the log, as shown in Figure1, and confirm that the ESN (1) is correct and that the Repair Decision (2) matches Table 1.
- If the VGT Minimum Position Parameter (3) shown in Figure 1 is greater than 4 percent, continue to the Resolution section.

![[10r00488.png]]

Figure 1, Air Handling Performance Test Log Screenshot.

**Resolution**

See corresponding Service Manual. Reference Procedure 010-134 in Section 10 and perform the following:

- Remove the actuator and check sector gear travel.
- If sector gear travel is within specification, Perform Actuator Install and Calibrate Steps.
- If Install and Calibrate completes successfully, run the Air Handling Performance test to validate the repair.

### Document History
