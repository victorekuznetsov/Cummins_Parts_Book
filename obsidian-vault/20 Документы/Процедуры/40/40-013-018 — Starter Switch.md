---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "40-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `40-013-018`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-018.pdf)

### Initial Check

> [!danger] WARNING · Опасно
> Be sure the starting motor switch is in the OFF position to reduce the possibility of personal injury from electrical shock.

Remove the wire connecting the starting motor switch to the magnetic switch (marked "S" or START) from the starting motor switch terminal.

Connect the positive lead of digital multimeter, Part Number 3377161, or equivalent, to the starting motor switch terminal and the negative lead to a chassis or engine ground location.

![[es900we.png]]

> [!note] Note · Примечание
> With the starting motor switch in the OFF position, there **must not** be voltage at the starting motor switch terminal. If the meter indicates voltage, the starting motor switch is malfunctioning and **must** be replaced.

![[sb800kd.png]]

Turn the starting motor switch to the START position.

The multimeter **must** indicate system voltage.

![[sb800ks.png]]

If there is no voltage:

- Turn the starting motor switch to the OFF position.
- Connect the multimeter positive lead to the starting motor switch terminal having a wire connecting the starting motor switch to the starting motor solenoid “B” terminal.

![[sb800kf.png]]

Turn the starter switch to the START position.

If the meter indicates system voltage at the starting motor switch input terminal, the starting motor switch is **not** the cause of the complaint.

Check the wiring from the starting switch to the starting motor solenoid “B” terminal, and from the starting motor solenoid to the battery for broken or damaged wires.

![[es900wi.png]]

If the meter indicates no voltage, the switch is defective and **must** be replaced.

Check the wiring from the starting switch to the starting motor solenoid "B" terminal and from the starting motor solenoid to the battery for broken or damaged wires.

![[es900wj.png]]
