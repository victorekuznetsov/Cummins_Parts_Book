---
aliases:
  - "Регистратор данных CENSE™"
type: "Процедура"
doc: "81-019-431"
title_en: "CENSE™ Datalogger"
title_ru: "Регистратор данных CENSE™"
modified: "2013-01-18"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666134"
figures: 2
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/81-019-431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/81"
---

# CENSE™ Datalogger
**Регистратор данных CENSE™**

> [!abstract] Процедура · `81-019-431`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666134 — QST30 Operation and Maintenance Manual|3666134]]
> **Секции:** Section 4 - Maintenance Procedures at 250 Hours or 6 Months
> **Даты:** изменён 2013-01-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/81-019-431.pdf)

### Reset

with Mechanically Actuated Injector

CENSE™ data **must** be reset every 250 hours in order to maintain maximum memory capacity.

For CENSE™ CM530 modules **only**, the data **must** be reset every 250 hours in order to maintain maximum memory capacity.

1. First retrieve the CENSE™ data that has been saved.
2. Select the fault codes and trend data options for resetting.

Contact a Cummins ® Authorized Repair Location for detailed instructions.

![[19800902.png]]

with Electronically Actuated Injector

These engines do **not** use CENSE™. Instead, they have advanced engine monitoring built into the ECMs. This data does **not** need to be reset because it will automatically write over the oldest data if the memory capacity becomes full. However, this memory can be cleared manually using INSITE™ electronic service tool. Fault logs **must** be viewed every 250 hours even if they are **not** going to be reset.

> [!note] Note · Примечание
> CENSE™ CM2330 modules do **not** need to be reset.

![[19800902.png]]
