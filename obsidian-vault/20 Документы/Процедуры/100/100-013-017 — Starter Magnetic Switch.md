---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "100-013-017"
title_en: "Starter Magnetic Switch"
title_ru: "Втягивающее реле стартера"
modified: "2003-09-03"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-017.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-017.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/100"
---

# Starter Magnetic Switch
**Втягивающее реле стартера**

> [!abstract] Процедура · `100-013-017`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-017.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-017.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> Make sure the starting motor switch is in the OFF position to prevent electrical shock and personal injury.

Remove the cable connecting the magnetic switch to the starting motor solenoid from the magnetic switch terminal.

Connect the leads of digital multimeter, Part No. 3377161, to the two large switch terminals.

![[es900kg.png]]

Set the multimeter to measure resistance (ohms).

With the starting motor switch in the OFF position, the multimeter **must** indicate infinity.

Turn the starting motor switch to the START position.

The multimeter **must** indicate zero or very little resistance.

![[es900wa.png]]

### Voltage Check

If the multimeter indicates resistance at infinity with the starting motor switch in the START position:

- Turn the starting motor switch to the OFF position.
- Set the multimeter scale to read DC voltage.

![[es900wb.png]]

- Connect one multimeter lead to the magnetic switch terminal marked S and the other lead to a good ground.
- Turn the starting motor switch to the START position.
- If the multimeter indicates no voltage, the magnetic switch is **not** the cause of the complaint. Refer to Starter Motor Switch - Test in this section.
- If the multimeter indicates voltage, the magnetic switch is defective and **must** be replaced.

![[es900wc.png]]

- Turn the starting motor switch to the OFF position.
- Remove the multimeter leads and connect the magnetic switch to the starting motor solenoid wire.

![[es900wd.png]]
