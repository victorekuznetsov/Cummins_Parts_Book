---
type: "TSB"
doc: "tsb250016"
title_en: "Engine Control Module (ECM) Calibration Code Change to Exhaust Gas Temperature (EGT) Sensor Thresholds: White Smoke"
modified: "2025-12-10"
engines:
  - "33239746"
families:
  - "QSK60 CM2150 MCRS"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250016.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250016.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60CM2150MCRS"
---

# Engine Control Module (ECM) Calibration Code Change to Exhaust Gas Temperature (EGT) Sensor Thresholds: White Smoke

> [!abstract] TSB · `tsb250016`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]]
> **Семейство:** QSK60 CM2150 MCRS
> **Даты:** изменён 2025-12-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2025/tsb250016.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb250016.pdf)

## Engine Control Module (ECM) Calibration Code Change to Exhaust Gas Temperature (EGT) Sensor Thresholds: White Smoke

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Product Affected**

- QSK60 CM2350 K116
- QSK60 CM2350 K121
- QSK60 CM2350 K135
- QSK60 CM2350 K136

**Issue**

Exhaust gas temperature (EGT) thresholds for setting fault codes in the engine control module (ECM) are too high to alert operators to early exhaust valve cracking and subsequent malfunction.

Symptom:

- White smoke from the exhaust and an underperforming cylinder at the affected position

Root Cause:

- EGT threshold values in the ECM calibration are set too high and do **not** illuminate warning lamps early enough to alert operators to valve malfunction.

**Resolution**

The ECM calibration codes have been changed to lower the EGT thresholds.

**Description of Change**

ECM calibration codes have been changed to lower the EGT thresholds from existing values. All products affected by this TSB share the same change. See Table 1.

| Table 1, EGT Threshold Changes |  |  |
|---|---|---|
| Fault Code Threshold | Existing EGT Value °C \[ °F \] | New EGT Value °C \[ °F \] |
| Moderately Severe Level (Amber Lamp) | 732°C \[ 1349°F \] | 615 °C \[ 1139°F \] |
| Most Severe Level (Red Lamp) | - | 630 °C \[ 1166°F \] |

**Reason for Change**

High exhaust gas temperature fault codes will alert operators of potential exhaust valve malfunction to mitigate further engine damage.

**Service Instructions**

- For CM2350 engines, the new ECM calibration code is released for child 2 ECM. See Table 2.

New ECM calibration codes are available as below:

| Table 2, QSK60 T4 ECM Calibration Codes |  |  |
|---|---|---|
| QSK60 CM2350 ECM Codes (Child 2) |  |  |
| CX60029.05 | CX60149.05 | CX60062.11 |
| CX60050.13 | CX60170.02 | CX60080.11 |
| CX60053.15 | CX60173.02 | CX60083.11 |
| CX60056.15 | CX60176.02 | CX60095.10 |
| CX60065.11 | CX60179.02 | CX60098.10 |
| CX60071.12 | CX60182.02 | CX60116.11 |
| CX60074.11 | CX60191.02 | CX60140.05 |
| CX60077.11 | CX60193.02 | CX60146.05 |
| CX60137.05 | CX60217.02 | CX60205.02 |
| CX60143.05 | CX60059.11 | CX60208.02 |

**Part Compatibility**

These ECM calibrations are cross compatible with existing parent and child calibrations.

**Production Status**

Originally implemented for production on Tier 2 and 4 products. See Table 3.

Tier 2 products are no longer built with this change; therefore, the last engine build information is displayed in Table 4.

| Table 3, ESN First Information |  |  |  |
|---|---|---|---|
| Engine Service Models | ESN First | Build Date 1 | Plant |
| QSK60 CM2150 MCRS | 33237928 | 6 January 2025 | Daventry Engine Plant |
| 1 Engine build date can be found on the engine dataplate. |  |  |  |

| Table 4, Tier 2 Engines Information |  |
|---|---|
| Engine Service Models | Last Build Date 1 |
| QSK60 CM2150 MCRS QSK60 CM850 MCRS | 3 September 2025 |
| 1 Engine build date can be found on the engine dataplate. |  |

### Document History
