---
aliases:
  - "Проблемы подключения INLINE™ 6 с Windows® 10 версий 1809 и 1903"
type: "TSB"
doc: "tsb190044"
title_en: "Connectivity Issues with INLINE™ 6 Datalink Adapter and Windows® 10 Version 1809 or Windows® 10 Version 1903"
title_ru: "Проблемы подключения INLINE™ 6 с Windows® 10 версий 1809 и 1903"
released: "2019-08-14"
modified: "2019-08-14"
group: "22 - Service Tools"
engines:
  - "33239746"
  - "33239899"
  - "41349633"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK19"
figures: 2
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190044.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb190044.pdf"
tags:
  - "документ/tsb"
  - "двигатель/K38/K50"
  - "двигатель/QSK19"
  - "год/2019"
  - "тема/service-tools"
---

# Connectivity Issues with INLINE™ 6 Datalink Adapter and Windows® 10 Version 1809 or Windows® 10 Version 1903
**Проблемы подключения INLINE™ 6 с Windows® 10 версий 1809 и 1903**

> [!abstract] TSB · `tsb190044`
> **Раздел Cummins:** 22 - Service Tools
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]], [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK19
> **Даты:** выпущен 2019-08-14 · изменён 2019-08-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2019/tsb190044.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/tsb/tsb190044.pdf)

## Connectivity Issues with INLINE™ 6 Datalink Adapter and Windows® 10 Version 1809 or Windows® 10 Version 1903

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

**Products Affected**

- All electronically controlled engine products

**Issue**

Using a Windows® 10 Version 1809 or Windows 10 Version 1903 (sometimes called 19H1) operating system, when trying to connect INSITE™ electronic service tool using an INLINE™ 6 datalink adapter, intermittent connectivity issues can be observed.

**Verification**

To locate Windows® 10 Operating System build:

1. Press the Windows® Key and R key simultaneously to open Run dialog, then type winver and select OK. See Figure 1 below.

![[22r00302.png]]

Figure 1, Run Dialog.

2. About Windows® dialog box will appear and provide the Windows® version and build details. See Figure 2 below.

![[22r00303.png]]

Figure 2, Windows® Version.

**Resolution**

- New INLINE™ 6 drivers have been developed which will resolve this issue.
- Since the INLINE™ 6 drivers are still in field test, send an email to CumminsFieldTest@cummins.com with contact information (name, phone number, email address) and “INLINE 6 Drivers” in the Subject line, if interested in testing the INLINE 6 drivers.
- Additional Workaround: Use INSITE™ electronic service tool with INLINE™ 6 connecting through 9-pin serial port, or use another datalink adapter, such as an INLINE™ 7.
- To avoid any disruptions or download failures, using a computer with a different operating system and/or different version number and/or different datalink adapter for any ECM calibration code downloads is recommended.

### Document History
