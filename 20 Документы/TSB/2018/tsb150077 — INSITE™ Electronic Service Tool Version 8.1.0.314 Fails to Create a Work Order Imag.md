---
aliases:
  - "INSITE™ 8.1.0.314 не создаёт наряд-заказ/образ"
type: "TSB"
doc: "tsb150077"
title_en: "INSITE™ Electronic Service Tool Version 8.1.0.314 Fails to Create a Work Order/Image"
title_ru: "INSITE™ 8.1.0.314 не создаёт наряд-заказ/образ"
released: "2018-10-04"
modified: "2018-10-04"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "37292556"
  - "37295879"
  - "41349633"
  - "93058669"
families:
  - "C8.3 · 6C8.3"
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
  - "QST30"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150077.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb150077.pdf"
tags:
  - "документ/tsb"
  - "двигатель/C8.3"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "двигатель/QST30"
  - "год/2018"
  - "тема/service-tools"
---

# INSITE™ Electronic Service Tool Version 8.1.0.314 Fails to Create a Work Order/Image
**INSITE™ 8.1.0.314 не создаёт наряд-заказ/образ**

> [!abstract] TSB · `tsb150077`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3, K38/K50 · QSK38, QSK50, QSK60, QSK19, QST30
> **Даты:** выпущен 2018-10-04 · изменён 2018-10-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2015/tsb150077.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb150077.pdf)

## INSITE™ Electronic Service Tool Version 8.1.0.314 Fails to Create a Work Order/Image

### Core Issue

At the end of the calibration download process, when INSITE™ electronic service tool reconnects, the new Work Order window pops up to create a new work order.

After a few seconds, INSITE™ electronic service tool may display:

- “Microsoft Visual C++ Runtime Library \> Runtime Error" and no Work Order is created.

This issue may also be encountered after manually creating Work Orders. INSITE™ electronic service tool may:

- Display, "Microsoft Visual C++ Runtime Library \> Runtime Error"
- Display, "Error 5201"
- Stop at 25% during a Work Order creation.

This issue happens randomly and may be seen after:

- Multiple successive calibration downloads
- Multiple Work Orders are created

### Confirmation

None

### Resolution

1. Repeat the process until a Work Order is created successfully.

OR

2. Uninstall INSITE™ electronic service tool version 8.1.0.314, download the INSITE™ electronic service tool version 8.1.0 ISO, and install INSITE™ electronic service tool version 8.0.3 from the downloaded ISO file.

INSITE 8.1.0 ISO can be downloaded using the link below:

> [!note] Note · Примечание
> [https://www.cummins.com/support/electronic-service-tools-support/insite-support](https://www.cummins.com/support/electronic-service-tools-support/insite-support)

A permanent solution will be provided with the release of INSITE™ electronic service tool version 8.1.1 in the third quarter of 2015.

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Document History
