---
aliases:
  - "QST30 промышленный: пересмотр калибровки, коды 299, 423, 772, 773, 611"
type: "TSB"
doc: "tsb120289"
title_en: "QST30 Industrial Calibration Revision: Fault Codes 299, 423, 772, 773, and 611"
title_ru: "QST30 промышленный: пересмотр калибровки, коды 299, 423, 772, 773, 611"
released: "2012-12-21"
modified: "2012-12-21"
group: "00 - Complete Engine / Troubleshooting"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120289.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120289.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QST30"
  - "год/2012"
  - "тема/complete-engine-troubleshooting"
---

# QST30 Industrial Calibration Revision: Fault Codes 299, 423, 772, 773, and 611
**QST30 промышленный: пересмотр калибровки, коды 299, 423, 772, 773, 611**

> [!abstract] TSB · `tsb120289`
> **Раздел Cummins:** 00 - Complete Engine / Troubleshooting
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2012-12-21 · изменён 2012-12-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2012/tsb120289.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb120289.pdf)

## QST30 Industrial Calibration Revision: Fault Codes 299, 423, 772, 773, and 611

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

This document announces a update in the Calibration Software Phase to 5.1.0.5 for QST30 Industrial engines. The calibration change was made to alter the logic for Fault Codes 423, 772, and 773. The calibration also added Fault Codes 299 and 611.

Fault Codes 772 and 773 are for the needle lift sensor for the left and right bank reading **not** being detected or out of range.

Fault Codes 772 and 773 will no longer display a lamp but will be logged in the engine control module (ECM). The lamp strategy of the revised calibrations meets Cummins® Engineering Standards.

Fault Code 423 is caused by incorrect static pump timing, clogged fuel filters or inlet screen, a stuck timing sleeve, air in the fuel lines, or calibration errors. The logic was revised to make the fault code more robust to signal noise.

Fault Codes 299 and 611 were added to these calibrations. Fault Code 299 is for a non-keyswitch hot shutdown, which occurs when the engine is shutdown without the keyswitch when the engine did **not** have time to cool down properly. Fault Code 611 will trigger when the engine was shut down without allowing the proper cool down.

Engines built on or after 19 November 2012 have the updated 5.1.0.5 Calibration Software Phase.

The new calibrations were installed in production engines built on or after 19 November 2012

| Table 1: Previous and Revised Calibrations |  |
|---|---|
| Previous Calibration | Revised Calibration |
| K50176.03 | K50176.04 |
| K50186.01 | K50186.02 |
| K50187.01 | K50187.02 |
| K50017.22 | K50017.23 |
| K50024.23 | K50024.24 |
| K50043.21 | K50043.22 |
| K50054.20 | K50054.21 |
| K50055.18 | K50055.19 |
| K50057.15 | K50057.16 |
| K50059.13 | K50059.14 |
| K50061.11 | K50061.12 |
| K50061.16 | K50061.17 |
| K50063.14 | K50063.15 |
| K50065.14 | K50065.15 |
| K50066.13 | K50066.14 |
| K50067.12 | K50067.13 |
| K50069.14 | K50069.15 |
| K50070.11 | K50070.12 |
| K50071.11 | K50071.12 |
| K50072.05 | K50072.06 |
| K50072.10 | K50072.11 |
| K50073.05 | K50073.06 |
| K50073.10 | K50073.11 |
| K50076.10 | K50076.11 |
| K50077.05 | K50077.06 |
| K50077.10 | K50077.11 |
| K50082.11 | K50082.12 |
| K50083.10 | K50083.11 |
| K50084.09 | K50084.10 |
| K50085.10 | K50085.11 |
| K50088.08 | K50088.09 |
| K50092.03 | K50092.04 |
| K50092.08 | K50092.08 |
| K50093.03 | K50093.04 |
| K50093.07 | K50093.08 |
| K50094.03 | K50094.04 |
| K50094.08 | K50094.09 |
| K50103.03 | K50103.04 |
| K50123.03 | K50123.04 |
| K50126.02 | K50126.03 |
| K50137.01 | K50137.02 |
| K50180.01 | K50180.02 |
| K50074.11 | K50074.12 |
| K50075.12 | K50075.13 |
| K50078.10 | K50078.11 |
| K50086.08 | K50086.09 |
| K50089.08 | K50089.09 |
| K50090.07 | K50090.08 |
| K50091.08 | K50091.09 |
| K50095.08 | K50095.09 |
| K50096.09 | K50096.10 |
| K50097.10 | K50097.11 |
| K50098.04 | K50098.05 |
| K50099.04 | K50099.05 |
| K50101.04 | K50101.05 |
| K50105.03 | K50105.04 |
| K50106.05 | K50106.06 |
| K50110.03 | K50110.03 |
| K50118.02 | K50118.03 |
| K50131.02 | K50131.03 |
| K50133.02 | K50133.03 |
| K50136.02 | K50136.03 |
| K50164.01 | K50164.02 |
| K50183.02 | K50183.03 |
| K50028.20 | K50028.21 |
| K50062.11 | K50062.12 |
| K50064.10 | K50064.11 |
| K50068.07 | K50068.08 |
| K50080.06 | K50080.07 |
| K50081.07 | K50081.08 |
| K50087.05 | K50087.06 |
| K50100.04 | K50100.05 |
| K50102.04 | K50102.05 |
| K50104.02 | K50104.03 |
| K50113.01 | K50113.02 |
| K50130.02 | K50130.03 |
| K50167.03 | K50167.04 |
| K50024.31 | K50024.32 |
| K50045.23 | K50045.24 |
| K50141.01 | K50141.02 |
| K50142.01 | K50142.02 |
| K50143.02 | K50143.03 |
| K50144.01 | K50144.02 |
| K50145.01 | K50145.02 |
| K50146.01 | K50146.02 |
| K50147.02 | K50147.03 |
| K50148.01 | K50148.02 |
| K50149.01 | K50149.02 |
| K50150.03 | K50150.04 |
| K50151.01 | K50151.02 |
| K50152.01 | K50152.02 |
| K50153.01 | K50153.02 |
| K50154.01 | K50154.02 |
| K50155.02 | K50155.03 |
| K50156.02 | K50156.03 |
| K50157.01 | K50157.02 |
| K50158.01 | K50158.02 |
| K50159.01 | K50159.02 |
| K50162.01 | K50162.02 |
| K50163.01 | K50163.02 |
| K50166.01 | K50166.02 |
| K50171.01 | K50171.02 |
| K50172.01 | K50172.02 |
| K50173.02 | K50173.03 |
| K50174.02 | K50174.03 |
| K50175.01 | K50175.02 |
| K50177.02 | K50177.03 |
| K50178.01 | K50178.02 |
| K50179.01 | K50179.02 |
| K50181.01 | K50181.02 |
| K50182.01 | K50182.02 |
| K50161.03 | K50161.04 |
| K50014.21 | K50014.22 |
| K50132.02 | K50132.03 |
| K50160.01 | K50160.02 |
| K50139.02 | K50139.03 |
| K50140.02 | K50140.03 |
| K50165.01 | K50165.02 |
| K50169.01 | K50169.02 |
| K50170.01 | K50170.02 |
| K50188.01 | K50188.02 |
| K50189.01 | K50189.02 |

### Document History
