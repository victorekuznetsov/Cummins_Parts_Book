---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "40-013-017-tr"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-017-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-017-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `40-013-017-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-017-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-017-tr.pdf)

### Initial Check

> [!danger] WARNING · Опасно
> Be sure the starting motor switch is in the OFF position to prevent electrical shock and personal injury.

Remove the cable connecting the magnetic switch to the starting motor solenoid from the magnetic switch terminal.

Connect the leads of digital multimeter, Part Number 3377161, or equivalent, to the two large switch terminals.

![[ea900wb.png]]

Set the multimeter to measure resistance (OHMS).

With the starting motor switch in the OFF position, the multimeter **must** indicate resistance at infinity.

Turn the starting motor switch to the START position.

The multimeter **must** indicate zero or very little resistance.

![[es900wa.png]]

If the multimeter indicates resistance at infinity with the starting motor switch in the START position:

- Turn the starting motor switch to the OFF position.
- Set the multimeter scale to read DC voltage.

![[es900wb.png]]

- Connect one multimeter lead to the magnetic switch terminal marked "S" and the other lead to the ground.
- Turn the starting motor switch to the START position.
- If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint.
- If the multimeter indicates voltage, the magnetic switch is defective and **must** be replaced.

![[es900wc.png]]

- Turn the starting motor switch to the OFF position.
- Remove the multimeter leads, and connect the magnetic switch to the starting motor solenoid wire.

![[es900wd.png]]

### Resistance Check

> [!danger] WARNING · Опасно
> Be sure the starter motor switch is in the OFF position to reduce the possibility of personal injury from electrical shock.

Remove the cable connecting the magnetic switch to the starter motor solenoid from the magnetic switch terminal.

Connect the leads of the digital multimeter, Part Number 3377161, or equivalent, to the two large switch terminals.

Set the digital multimeter, Part Number 3377161, to measure resistance (ohms).

![[ea900wb.png]]

Connect the leads to the two large switch terminals.

With the starter motor switch in the OFF position, the multimeter **must** indicate resistance greater than 100k ohms.

Turn the starter motor switch to the START position.

The multimeter **must** indicate less than 10 ohms. If **not** within specifications, replace the starter magnetic switch according to the manufacturer's instructions.

![[es900wa.png]]

### Voltage Check

If the multimeter indicates resistance greater than 100k ohms with the starter motor switch in the START position:

- Turn the starter motor switch to the OFF position.
- Set the multimeter scale to read DC voltage.

![[es900wb.png]]

- Connect one multimeter lead to the magnetic switch terminal marked "S" and the other lead to the ground.
- Turn the starter motor switch to the START position.
- If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint. Refer to [[40-013-018 — Starter Switch|Procedure 013-018]]. If the starter magnetic switch is **not** within specification, replace the switch according to the manufacturer's instructions.

![[es900wc.png]]

- Turn the starter motor switch to the OFF position.
- Remove the multimeter leads, and connect the magnetic switch to the starter motor solenoid wire.

![[es900wd.png]]
