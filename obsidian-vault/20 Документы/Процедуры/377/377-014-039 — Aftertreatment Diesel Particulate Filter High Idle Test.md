---
type: "Процедура"
doc: "377-014-039"
title_en: "Aftertreatment Diesel Particulate Filter High Idle Test"
modified: "2026-03-24"
manuals:
  - "5411181"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-039.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-039.pdf"
tags:
  - "документ/процедура"
  - "группа/377"
---

# Aftertreatment Diesel Particulate Filter High Idle Test

> [!abstract] Процедура · `377-014-039`
> **Входит в руководства:** [[5411181 — X15 CM2350 X114B - Efficiency Series Service Manual|5411181]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2026-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/377/377-014-039.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/377-014-039.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool or equivalent.

#### Additional Service Items

- No additional service items required.

### General Information

The following procedure contains information on how to perform an update to the aftertreatment diesel particulate filter (DPF) soot load.

The final aftertreatment DPF soot load is based on a combination two inputs:

- Aftertreatment DPF differential pressure
- A soot load estimate (used in conditions where the DPF differential pressure is **not** trusted).

The procedure can be used to:

- Validate a repair when aftertreatment DPF soot load was high because of an issue with the aftertreatment DPF differential pressure sensor or tubes.
- Bring final aftertreatment DPF soot load down when incorrectly reading high due to too much time spent on the estimate (excessive low exhaust flow operation or fault codes active that limit aftertreatment DPF differential pressure input into the soot load value.
- Reduce the aftertreatment DPF soot load to prevent false Fault Code 1922 occurrences during road tests or other electronic service tests, thereby avoiding unnecessary stationary regenerations.

### Setup

Retrieve an ECM image using the Cummins® electronic service tool or equivalent and clear fault codes if Fault Code 3382, 3383, 124, 125, 3389, or 3361 are active.

### Test

- Monitor Exhaust Volumetric Flowrate in Cummins® electronic service tool or equivalent.
- Operate the engine with Exhaust Volumetric Flowrate greater than 0.278 m3/s \[ 9.82 ft3/s \] for 10 minutes.
- After 10 minutes, return engine speed to idle.

> [!note] Note · Примечание
> If the engine is having trouble reaching the desired exhaust volumetric flowrate, temporarily disconnect the EGR valve from the engine wiring harness and retry the test.

Aftertreatment DPF soot load can rise briefly and drop again as the aftertreatment DPF differential pressure-based soot load converges on the new lower value after a stationary regeneration.

If Fault Code 1921, 1922 or 2639 went inactive, check the Aftertreatment DPF soot load in Cummins® electronic service tool or equivalent.

- If the soot load is less than or equal to 22 grams \[ 0.78 oz \] and Fault Codes 1921, 2639, and 1922 are **not** active:

- · If soot load is greater than 22 grams \[ 0.78 oz \] but less than 127 grams \[ 4.47 oz \],

- If soot load is greater than or equal to 127 grams \[ 4.47 oz \] or Fault Code 1922 is still active:

If using this procedure to update the differential pressure based aftertreatment DPF soot load estimate in preparation to run another electronic service test, no further action is required. Return to published troubleshooting.

### Finishing Steps

Reconnect the EGR valve (if applicable).

Return to published troubleshooting.
