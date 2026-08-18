---
aliases:
  - "Выключатель стартера"
type: "Процедура"
doc: "20-013-018"
title_en: "Starter Switch"
title_ru: "Выключатель стартера"
modified: "2006-06-30"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-018.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-013-018.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Starter Switch
**Выключатель стартера**

> [!abstract] Процедура · `20-013-018`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-018.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-013-018.pdf)

### Inspect for Reuse

> [!danger] WARNING · Опасно
> The engine must not be running and the ignition or keyswitch must be in the OFF position when installing or removing the ignition generator. To reduce the possibility of personal injury or equipment damage, do not touch the pins on the ignition generator when the engine is operating. Always use suitably insulated tools.

Remove the wire connecting the starter switch to the magnetic switch from the starter switch terminal.

Connect the positive lead of the digital multimeter, Part Number 3164488 or 3164489, to the starter switch terminal and the negative lead to a chassis or engine ground location.

![[sb8tohb.png]]

With the starter switch in the OFF position, there **must** be **no** voltage at the starter switch terminal. If the multimeter indicates voltage, the starter switch is malfunctioning and **must** be replaced.

![[sb800kd.png]]

Turn the starter switch to the START position.

The multimeter **must** indicate system voltage.

![[sb800ke.png]]

If there is **no** voltage:

- Turn the starter switch to the OFF position.
- Connect the multimeter positive lead to the starter switch terminal having a wire connecting the starter switch to the starter solenoid.

![[sb800kf.png]]

If the multimeter indicates system voltage, the starter switch is defective and **must** be replaced.

![[sb800kt.png]]

If the multimeter indicates **no** voltage, the switch is **not** the cause of the complaint.

![[sb8tosg.png]]

Inspect the wiring from the starter switch to the starter solenoid and from the starter solenoid to the battery. Replace any broken or otherwise damaged wires.

![[sb800ki.png]]
