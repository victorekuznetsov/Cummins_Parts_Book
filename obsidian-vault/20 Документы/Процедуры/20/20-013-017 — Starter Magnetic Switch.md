---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "20-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2006-06-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `20-013-017`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-013-017.pdf)

### Inspect for Reuse

Before inspecting specific starting system components with the multimeter:

- Inspect terminals for loose, broken, or corroded connections.
- Replace or repair wiring and components as necessary.

![[sb8coca.png]]

> [!danger] WARNING · Опасно
> The engine must not be running and the ignition or keyswitch must be in the OFF position when installing or removing the ignition generator. To reduce the possibility of personal injury or equipment damage, do not touch the pins on the ignition generator when the engine is operating. Always use suitably insulated tools.

Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.

Connect the leads of the Digital Multimeter, Part Number 3164488 or 3164489, to the two large switch terminals.

![[sb8toha.png]]

Set the multimeter to measure resistance (OHMS).

With the starter switch in the OFF position, the multimeter **must** indicate resistance at infinity.

- If the multimeter indicates ZERO ("0") or very little resistance, replace the magnetic switch.
- If the multimeter indicates resistance at infinity, proceed with the following instructions.

![[sb8toha.png]]

Turn the starter switch to the START position.

The multimeter **must** indicate ZERO ("0") or very little resistance. An audible click will be heard when the starting switch is turned to the START position.

![[sb800ta.png]]

If the multimeter indicates resistance at infinity with the starter switch in the START position and an audible click is **not** heard:

- Turn the starter switch to the OFF position.
- Set the multimeter scale to indicate DC voltage.

![[sb800kx.png]]

Connect the positive lead of the one multimeter to the magnetic switch ground wire terminal and the other lead to the small magnetic switch terminal.

Turn the starter switch to the START position.

The multimeter will indicate some voltage across the magnetic switch terminals. If the multimeter indicates FULL SYSTEM VOLTAGE, the magnetic switch is malfunctioning and **must** be replaced.

![[sb800ky.png]]

If the multimeter indicates **no** voltage, the magnetic switch is **not** the cause of the complaint. Refer to Procedure [[20-013-018 — Starter Switch|013-018]].

![[sb200ka.png]]

Turn the starter switch to the OFF position.

Remove the multimeter leads and connect the magnetic switch to starter solenoid wire.

![[sb8toma.png]]
