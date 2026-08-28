---
type: "TSB"
doc: "tsb100262"
title_en: "Engine Hours Broadcast"
modified: "2004-03-22"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100262.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100262.pdf"
tags:
  - "документ/tsb"
  - "двигатель/QSK60"
---

# Engine Hours Broadcast

> [!abstract] TSB · `tsb100262`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Даты:** изменён 2004-03-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/tsb/2010/tsb100262.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/tsb/tsb100262.pdf)

## Engine Hours Broadcast

### Warranty Statement

The information in this document has no effect on present warranty coverage or repair practices, nor does it authorize TRP or Campaign actions.

### Contents

This Technical Service Bulletin informs field service of software phase compatibilities with engine hour monitoring devices using a datalink broadcast to J1939 and J1587/1708.

This Technical Service Bulletin also informs field service of engine hour offset monitoring capabilities via datalink.

Engine hours broadcast via J1587/J1708 is **only** available with calibrations of software Phase 5.9.5.4 or higher.

Engine hours broadcast via J1939 is **only** available with calibrations of software Phase 5.9.7.1 or higher.

Calibration software phases can be monitored and identified via Insite™ 6.2.

Phase 5.9.7.1 software will be available middle-2004. Calibrations will be upgraded accordingly.

After replacing an ECM, the engine hours+offset are read as total engine hours when using Insite™.

> [!note] Note · Примечание
> When reading engine hours via the datalink, the offset will **not** be added to the engine hours.

> [!note] Note · Примечание
> Insite™ can monitor engine hours on **all** QSK19 calibrations.

| Software Broadcast Limitation Matrix |  |  |  |  |
|---|---|---|---|---|
| Broadcast Link | Software Phase 2.7 | Software Phase 5.9.5.4 | Software Phase 5.9.6.11 | Software Phase 5.9.7.1 (Release Middle-2004) |
| **J1587 / J1708** | No | Yes | Yes | Yes / or higher |
| **J1939** | No | No | No | Yes / or higher |
