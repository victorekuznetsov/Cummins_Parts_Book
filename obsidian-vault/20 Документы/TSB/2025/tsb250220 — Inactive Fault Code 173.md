---
aliases:
  - "Неактивный код неисправности 173"
type: "TSB"
doc: "tsb250220"
title_en: "Inactive Fault Code 173"
title_ru: "Неактивный код неисправности 173"
released: "2025-12-01"
modified: "2025-12-01"
group: "19 - Electronic Engine Controls"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250220.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250220.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2025"
  - "тема/electronic-engine-controls"
---

# Inactive Fault Code 173
**Неактивный код неисправности 173**

> [!abstract] TSB · `tsb250220`
> **Раздел Cummins:** 19 - Electronic Engine Controls
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2025-12-01 · изменён 2025-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250220.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250220.pdf)

## Inactive Fault Code 173

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QST30 CM552

**Issue Summary**

Symptom:

- Multiple counts of Fault Code 173 will show as inactive after attempting to start the engine.

Root Cause:

- Some calibrations will activate and deactivate this fault code while attempting to start the engine.

**Verification**

This issue applies to engines with engine control module (ECM) Codes K50042.XX, K50204.XX or K50220.XX. Connect to the ECM with recommended Cummins® Electronic Service Tool or equivalent and verify the ECM Code.

**Resolution**

- If Fault Code 173 continually reappears as inactive, this is a nuisance fault code and can be ignored. If Fault Code173 is showing as active, follow the standard troubleshooting steps.

### Document History
