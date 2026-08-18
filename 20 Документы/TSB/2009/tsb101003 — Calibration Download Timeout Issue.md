---
aliases:
  - "Таймаут при загрузке калибровки"
type: "TSB"
doc: "tsb101003"
title_en: "Calibration Download Timeout Issue"
title_ru: "Таймаут при загрузке калибровки"
released: "2009-10-24"
modified: "2009-10-24"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101003.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb101003.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "год/2009"
  - "тема/service-tools"
---

# Calibration Download Timeout Issue
**Таймаут при загрузке калибровки**

> [!abstract] TSB · `tsb101003`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Даты:** выпущен 2009-10-24 · изменён 2009-10-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb101003.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb101003.pdf)

## Calibration Download Timeout Issue

### Core Issue

This Early Field Notification describes an issue that occurs with some Electronic Control Modules (ECMs) during a calibration attempt. Due to a possible timeout issue during calibration download, the initial calibration transfer can fail and cause the ECM to be ROM booted. All other calibration attempts will fail.

### Confirmation

- ISB CM2150
- ISC CM2150
- ISL CM2150
- ISLe CM2150
- ISX CM871
- ISM CM876
- ISZ CM2150
- QSB CM850
- QSC CM850
- QSL CM850
- QSK19 MCRS
- QSK38 MCRS
- QSK50/60 MCRS
- QSK19 MCRS Power Generation
- QSK38 MCRS Power Generation
- QSK50/60 MCRS Power Generation

When attempting to calibrate an ECM that has failed calibration download, the next attempts can fail at 70 percent of “Preparing ECM to receive calibration.”, or early during the “Transferring ECM calibration.” process.

None

A timeout occurs, during the calibration download process in INSITE™ electronic service tool, that causes the calibration process to fail and the ECM to become ROM booted.

None

### Resolution

This issue has been resolved with INSITE™ 7.3 electronic service tool, Feature Pack 2. Use INSITE™ electronic service tool that has been updated with INSITE™ 7.3 Feature Pack 2, to calibrate ECMs that have experienced this issue.

- Download and install INSITE™ 7.3 electronic service tool Feature Pack 2 using the Cummins® INSITE™ electronic service tool Update Manager, by either the Internet or the CD Option.
- The INSITE™ 7.3 electronic service tool Feature Pack 2, is a free download through the Internet. CDs will be available for purchase from your local distributor.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.
