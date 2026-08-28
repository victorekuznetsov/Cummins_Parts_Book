---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "56-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2003-08-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `56-013-018`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-08-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-013-018.pdf)

### Inspect for Reuse

> [!danger] WARNING · Опасно
> Be sure the starter switch is in the OFF position to reduce the possibility of electrical shock and personal injury.

Remove the wire connecting the starter switch to the magnetic switch from the starter switch terminal.

Connect the positive (+) lead of the digital multimeter, Part Number 3377161, to the starter switch terminal and the negative (-) lead to a chassis or engine ground location.

![[sb8tohb.png]]

With the starter switch in the OFF position, there **must not** be voltage at the starter switch terminal. If the multimeter indicates voltage, the starter switch is malfunctioning and **must** be replaced.

![[sb800kd.png]]

Turn the starter switch to the START position.

The multimeter **must** indicate system voltage.

![[sb800ke.png]]

If there is no voltage:

- Turn the starter switch to the OFF position.
- Connect the multimeter positive (+) lead to the starter switch terminal having a wire that connects the starter switch to the starter solenoid.

![[sb800kf.png]]

If the multimeter indicates system voltage, the starter switch is defective and **must** be replaced.

![[sb800kt.png]]

If the multimeter indicates no voltage, the switch is **not** the cause of the complaint.

![[sb8tosg.png]]

Inspect the wiring from the starter switch to the starter solenoid and from the starter solenoid to the battery.

Replace any broken or damaged wires.

![[sb800ki.png]]
