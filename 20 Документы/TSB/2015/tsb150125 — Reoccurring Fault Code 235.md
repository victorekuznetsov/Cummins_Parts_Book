---
aliases:
  - "Повторяющийся код неисправности 235"
type: "TSB"
doc: "tsb150125"
title_en: "Reoccurring Fault Code 235"
title_ru: "Повторяющийся код неисправности 235"
released: "2015-08-03"
modified: "2015-08-03"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150125.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb150125.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2015"
  - "тема/electronic-engine-controls"
---

# Reoccurring Fault Code 235
**Повторяющийся код неисправности 235**

> [!abstract] TSB · `tsb150125`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2015-08-03 · изменён 2015-08-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150125.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb150125.pdf)

## Reoccurring Fault Code 235

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Issue**

Reoccurring fault code 235 on the right bank CM552 engine control module (ECM).

Fault code 235: Coolant Level - Data Valid But Below Normal Operating Range - Most Severe Level

**Product Affected**

- QST30 CM552

**Verification**

Fault Code 235 on the right bank is **only** seen with calibration software phase 4. Using INSITE™ electronic service tool, under the Calibration Information heading, verify the calibration software phase. Verify the fault code is **only** seen on the right bank ECM.

**Resolution**

If the following are confirmed.

- Fault code 235 active on the right bank ECM.
- Engine has a calibration software phase 4.

A wiring change can be made to prevent the reoccurring fault code. Perform the following on the engine harness connector for the right bank ECM.

- Jump pin 27 to pin 10 (5 VDC).
- Jump pin 37 to pin 30 (ground).

This will create a shorting plug and disable the fault code on the right bank.

For pin replacement instructions, use the following procedure in the QST30 Industrial Electronic Control System Troubleshooting and Repair Manual, Bulletin 3666214. [[99-019-217 — Bosch™ ECM OEM Connector Series|Refer to Procedure 019-217 in Section 19.]]

Calibration software phase 5 is **not** affected by the reoccurring right bank fault code 235.

### Document History
