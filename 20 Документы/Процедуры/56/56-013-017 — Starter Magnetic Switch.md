---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "56-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2003-08-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `56-013-017`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-08-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-013-017.pdf)

### Inspect for Reuse

Before inspecting specific starting system components with the multimeter:

- Inspect terminals for loose, broken, or corroded connections.
- Replace or repair wiring and components as necessary.

![[sb8coca.png]]

> [!danger] WARNING · Опасно
> Be sure the starter switch is in the OFF position to reduce the possibility of electrical shock and personal injury.

Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.

Connect the leads of digital multimeter, Part Number 3377161, to the two large switch terminals.

![[sb8toha.png]]

Set the multimeter to measure resistance.

With the starter switch in the OFF position, the multimeter **must** indicate resistance at infinity.

- If the multimeter indicates zero or very little resistance, replace the magnetic switch.
- If the multimeter indicates resistance at infinity, proceed with the following instructions.

![[sb8toha.png]]

Turn the starter switch to the START position.

The multimeter **must** indicate zero or very little resistance. A click will be heard when the starting switch is turned to the START position.

![[sb800ta.png]]

If the multimeter indicates resistance at infinity with the starter switch in the START position and a click is **not** heard:

- Turn the starter switch to the OFF position.
- Set the multimeter scale to indicate DC voltage.

![[sb800kx.png]]

Connect the positive (+) lead of the multimeter to the magnetic switch ground wire terminal and the other lead to the small magnetic switch terminal.

Turn the starter switch to the START position.

The multimeter will indicate some voltage across the magnetic switch terminals. If the multimeter indicates FULL SYSTEM VOLTAGE, the magnetic switch is malfunctioning and **must** be replaced.

![[sb800ky.png]]

If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint. Refer to Procedure [[56-013-018 — Starter Switch|013-018]].

![[sb200ka.png]]

Turn the starter switch to the OFF position.

Remove the multimeter leads and connect the magnetic switch to the starter solenoid wire.

![[sb8toma.png]]
