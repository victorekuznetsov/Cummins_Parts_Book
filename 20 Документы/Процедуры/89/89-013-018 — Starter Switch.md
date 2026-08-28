---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "89-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2003-09-04"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `89-013-018`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-018.pdf)

### Voltage Check

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, do not touch any ignition wires or components while the engine is operating, unless using suitably insulated tools.

Make sure the starter switch is in the OFF position.

Remove the wire connecting the starter switch to the magnetic switch from the starter switch terminal.

Connect the positive (+) lead of the digital multimeter, Part Number 3377161, or digital multimeter, Part Number 3164488, to the starter switch terminal and the negative (-) lead to a chassis or engine ground location.

![[sb8tohb.png]]

With the starter switch in the OFF position, there **must** be no voltage at the starter switch terminal. If the multimeter indicates voltage, the starter switch is malfunctioning and **must** be replaced.

![[sb800kd.png]]

Turn the starter switch to the START position.

The multimeter **must** indicate system voltage.

![[sb800ke.png]]

If there is no voltage:

- Turn the starter switch to the OFF position.
- Connect the multimeter positive (+) lead to the starter switch terminal having a wire connecting the starter switch to the starter solenoid.
- Turn the starter switch to the START position.

![[sb800kf.png]]

If the multimeter indicates system voltage, the starter switch is defective and **must** be replaced.

![[13400073.png]]

If the multimeter indicates no voltage, the switch is **not** the cause of the problem.

![[sb8tosg.png]]

Inspect the wiring from the starter switch to the starter solenoid and from the starter solenoid to the battery.

Replace any broken or damaged wires.

![[sb800ki.png]]
