---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "100-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2003-09-03"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/100"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `100-013-018`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-018.pdf)

### Test

> [!danger] WARNING · Опасно
> Make sure the starting motor switch is in the OFF position to prevent electrical shock and personal injury.

Remove the wire connecting the starting motor switch to the magnetic switch (marked S or START) from the starting motor switch terminal.

Connect the positive (+) lead of digital multimeter, Part Number 3377161, to the starting motor switch terminal and the negative (-) lead to a chassis or engine ground location.

![[es900we.png]]

> [!note] Note · Примечание
> With the starting motor switch in the OFF position, there **must not** be voltage at the starting motor switch terminal. If the multimeter indicates voltage, the starting motor switch is malfunctioning and **must** be replaced.

![[sb800kd.png]]

Turn the starting motor switch to the START position. The multimeter **must** indicate system voltage.

![[sb800ks.png]]

If there is no voltage:

- Turn the starting motor switch to the OFF position.
- Connect the multimeter positive lead to the starting motor switch terminal having a wire connecting the starting motor switch to the starting motor solenoid B terminal.

![[sb800kf.png]]

Turn the starter switch to the START position. If the multimeter indicates system voltage at the starting motor switch input terminal, the starting motor switch is **not** the cause of the complaint.

Inspect the wiring from the starting motor switch to the starting motor solenoid B terminal and from the starting motor solenoid to the battery from damaged or broken wires.

![[es900ki.png]]

If the multimeter indicates no voltage, the switch is defective and **must** be replaced.

![[es900kh.png]]
