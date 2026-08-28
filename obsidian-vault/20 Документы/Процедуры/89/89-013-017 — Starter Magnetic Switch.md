---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "89-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2003-09-04"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `89-013-017`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-013-017.pdf)

### Voltage Check

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, do not touch any ignition wires or components while the engine is operating, unless using suitably insulated tools.

Make sure the starter switch is in the OFF position.

Remove the cable connecting the magnetic switch to the starter solenoid from the magnetic switch terminal.

Connect the leads of the digital multimeter, Part Number 3377161, or digital multimeter, Part Number 3164488, to the two large switch terminals.

![[sb8toha.png]]

Set the multimeter to measure resistance (ohms).

With the starter switch off, the multimeter **must** indicate resistance at infinity, open circuit.

Turn the starter switch to the START position.

The multimeter **must** indicate near zero resistance, closed circuit.

![[sb800ta.png]]

If the multimeter indicates resistance at infinity with the starter switch in the START position:

- Turn the starter switch off.
- Remove the ground wire that is connected to one of the small magnetic switch terminals.

![[sb800kx.png]]

- Set the multimeter scale to indicate volts, 24-VDC or more.
- Connect the positive (+) lead of the multimeter to the magnetic switch ground terminal and the other lead to the ground wire.
- Turn the starter switch to the START position.
- If the multimeter indicates vehicle electrical system voltage, the magnetic switch is defective and **must** be replaced.

![[13400074.png]]

- If the multimeter does **not** indicate voltage connect the positive (+) lead of the multimeter to the small positive (+) terminal on the magnetic switch and the negative multimeter lead to the ground wire.
- Turn the starter switch to the START position.
- If the multimeter indicates vehicle electrical system voltage, the magnetic switch is defective and **must** be replaced.
- If the multimeter does **not** indicate voltage, refer to Procedure [[89-013-018 — Starter Switch|013-018]].

![[13400075.png]]

- Turn the starter switch to the OFF position.
- Remove the multimeter leads.
- Connect the starter solenoid cable to the magnetic switch terminal, and the ground wire to its corresponding terminal on the magnetic switch.

![[sb8toma.png]]
