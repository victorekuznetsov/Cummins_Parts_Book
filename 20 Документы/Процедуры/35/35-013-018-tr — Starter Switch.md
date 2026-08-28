---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "35-013-018-tr"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-018-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-018-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `35-013-018-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-018-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-018-tr.pdf)

### Voltage Check

> [!danger] WARNING · Опасно
> Be sure the starter switch is in the OFF position to prevent electrical shock.

Remove the wire connecting the starter switch to the magnetic switch from the starter switch terminal.

Connect the positive (+) lead of digital multimeter, Part Number 3377161, to the starter switch terminal and the negative (-) lead to the chassis or an engine ground location.

![[sb8tohb.png]]

Set the multimeter to the VDC position.

With the starter switch in the OFF position, there **must not** be a voltage reading. If the meter indicates a voltage, the starter switch is malfunctioning and **must** be replaced.

![[sb800kd.png]]

Turn the starter switch to the START position.

The multimeter **must** indicate a voltage in order for this check to be normal.

![[sb800ke.png]]

If there is **not** a voltage:

- Turn the starter switch to the OFF position
- Check the cable from the positive (+) voltage terminal of the starter solenoid to the starter switch for breaks. Also, check for loose or corroded connections.

![[sb800kf.png]]

If the cable is good and the connections are clean and tight, the starter switch is malfunctioning and **must** be replaced.

![[sb800kt.png]]
