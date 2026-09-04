---
type: "TSB"
doc: "tsb240169"
title_en: "Air Handling Performance Test Freezes after Engine Start: Fault Code 1117"
modified: "2024-10-03"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2024/tsb240169.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb240169.pdf"
tags:
  - "документ/tsb"
---

# Air Handling Performance Test Freezes after Engine Start: Fault Code 1117

> [!abstract] TSB · `tsb240169`
> **Даты:** изменён 2024-10-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2024/tsb240169.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb240169.pdf)

## Air Handling Performance Test Freezes after Engine Start: Fault Code 1117

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- B6.7 CM2350 B121B
- B6.7 CM2450 B155B
- L9 CM2350 L116B
- L9 CM2450 L126B
- X15 CM2350 X114B
- X15 CM2350 X116B
- X15 CM2450 X124B
- X15 CM2450 X134B
- X15 CM2450 X142B
- X12 CM2450 X137B

**Issue Summary**

Symptom:

- Air Handling Performance Test does **not** continue after engine start and does **not** display an abort message in the test screen status box.
- Fault Code 1117
- Air Handling Performance Test did not complete

Root Cause:

- Battery voltage dropped out during engine cranking, causing the ECM to reset

**Verification**

- Air Handling Performance Test does **not** continue 20 seconds after engine start and does **not** display an abort message
- Fault Code 1117 is active

**Resolution**

- Check the ECM and block ground straps for loose or corroded connections. Reference [[tsb220192 — Premature Battery Power loss Fault Code 1117\|TSB220192]].
- Load test the batteries. See equipment manufacturer service information.

### Document History
