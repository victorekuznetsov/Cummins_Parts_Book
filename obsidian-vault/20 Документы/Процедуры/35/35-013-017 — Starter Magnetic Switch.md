---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "35-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `35-013-017`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-017.pdf)

### Current Check

> [!danger] WARNING · Опасно
> Be sure the starter switch is in the OFF position to prevent electrical shock.

Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.

Connect the leads of the digital multimeter, Part Number 3377161, to the two large-switch terminals.

![[sb8toha.png]]

Set the multimeter to measure resistance (ohms).

With the starter switch off, the multimeter **must** indicate resistance at infinity, open circuit.

Turn the starter switch to the START position.

The multimeter **must** indicate zero resistance, closed circuit.

![[sb800ta.png]]

If the multimeter indicates resistance at infinity with the starter switch in the START position:

- Turn the starter switch off.
- Remove the ground wire that is connected to one of the small magnetic switch terminals.

![[sb800kx.png]]

- Set the multimeter scale to indicate volts, 24 VDC or more.
- Connect the positive (+) lead of the multimeter to the magnetic switch ground terminal and the other lead to the ground wire.
- Turn the starter switch to the START position.
- The multimeter **must** indicate vehicle electrical system voltage.

![[sb800ky.png]]

- If the multimeter does **not** indicate voltage, refer to Starter Switch - Check in this section.

![[sb200ka.png]]

- Turn the starter switch to the OFF position.
- Remove the multimeter leads.
- Connect the starter solenoid cable to the magnetic switch terminal and the ground wire to its corresponding terminal on the magnetic switch.

![[sb8toma.png]]
