---
aliases:
  - "Регистратор данных CENSE™"
type: "Процедура"
doc: "81-019-431"
title_en: "CENSE™ Datalogger"
title_ru: "Регистратор данных CENSE™"
modified: "2013-01-18"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "37292556"
  - "37295879"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
  - "QST30"
manuals:
  - "3666134"
  - "3666260"
  - "3666410"
  - "4021374"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "двигатель/QST30"
  - "группа/81"
---

# CENSE™ Datalogger
**Регистратор данных CENSE™**

> [!abstract] Процедура · `81-019-431`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60, QST30
> **Входит в руководства:** [[3666134 — QST30 Operation and Maintenance Manual|3666134]], [[3666260 — QSK45 and QSK60 Operation and Maintenance Manual|3666260]], [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]], [[4021374 — QSK23 Operation and Maintenance Manual|4021374]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19 · Section 4 - Maintenance Procedures at 250 Hours or 6 Months
> **Даты:** изменён 2013-01-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-019-431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-019-431.pdf)

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
