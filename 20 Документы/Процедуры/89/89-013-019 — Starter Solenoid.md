---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "89-013-019"
title_en: "Starter Solenoid"
title_ru: "Втягивающее реле стартера"
modified: "2003-07-28"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
---

# Starter Solenoid
**Втягивающее реле стартера**

> [!abstract] Процедура · `89-013-019`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-07-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-019.pdf)

### Voltage Check

Use the multimeter, Part No. 3164488, and set it to measure DC voltage.

Connect the multimeter positive lead to the starter solenoid positive cable terminal and the negative lead to the battery cable connection at the starting motor. The multimeter **must** show system voltage.

![[sb800ki.png]]

If the multimeter does **not** indicate system voltage, check the battery to starting motor cable for broken, loose, or corroded connections.

![[sb800kk.png]]

If the multimeter indicates system voltage, but the starting motor will **not** operate, check the wire connecting the starter solenoid to the starter switch for broken, loose, or corroded connections.

![[sb800kl.png]]

If the wire connecting the starter solenoid and starter switch is **not** loose or damaged and the starter will **not** operate:

- Remove the cable connecting the starting motor and starter solenoid from the solenoid terminal.
- Connect the multimeter positive lead to the solenoid **positive** terminal and the negative lead to a chassis or engine ground.

![[sb800km.png]]

Turn the starter switch to the START position.

If the multimeter indicates system voltage, the starter solenoid is malfunctioning and **must** be replaced.

![[sb800kn.png]]

If the multimeter does **not** indicate system voltage, check the wire connecting the starter solenoid to the magnetic switch for broken, loose, or corroded connections.

![[sb800ko.png]]

If the wire connecting the starter solenoid to the magnetic switch is **not** loose or damaged and the starting motor will **not** operate:

- Check the cable connecting the starter solenoid to the starting motor for broken, loose, or corroded connections.

![[sb800kp.png]]

Check the cable connecting the starter to the battery for broken, loose, or corroded connections.

![[sb8cosa.png]]

If the cables are **not** loose or damaged, the starting motor is defective and **must** be replaced. Refer to Procedure [[89-013-020 — Starting Motor|013-020]].

![[sb2cosa.png]]
