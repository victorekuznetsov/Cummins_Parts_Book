---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "100-013-019"
title_en: "Starter Solenoid"
title_ru: "Втягивающее реле стартера"
modified: "2003-09-03"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/100"
---

# Starter Solenoid
**Втягивающее реле стартера**

> [!abstract] Процедура · `100-013-019`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2003-09-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-013-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-013-019.pdf)

### Initial Check

Before troubleshooting the starting motor, make sure the battery terminals are **not** loose or corroded.

![[ea8cosa.png]]

If the starting motor solenoid does **not** make an audible sound, check for loose wiring connections.

![[es900ka.png]]

Use a digital multimeter, Cummins Part Number 3164488, or equivalent, to set the voltage scale.

Check for system voltage at the starting motor solenoid battery terminal.

![[es900wk.png]]

If the multimeter indicates system voltage at the starting motor battery terminal, check the voltage at the starting motor solenoid S terminal, when the starting switch is energized.

If the multimeter indicates system voltage at the S terminal, but the starter does **not** engage, the starting motor solenoid is malfunctioning and the starter **must** be replaced. Refer to Procedure [[100-013-020 — Starting Motor|013-020]].

![[es900wl.png]]

If the multimeter does **not** indicate system voltage at the S terminal, check:

- Fuses
- Voltage to the ignition switch and magnetic switch. Refer to "Starting Motor Switch and Magnetic Switch - Checking" in this section. Refer to Procedures [[100-013-017 — Starter Magnetic Switch|013-017]] and [[100-013-018 — Starter Switch|013-018]]
- Application safety shutoff systems

![[es900wm.png]]

### Voltage Check

Set the digital multimeter, Part Number 3164488, to measure DC voltage.

Connect the multimeter positive (+) lead to the starter solenoid positive cable terminal and the negative (-) lead to a chassis or engine ground location.

The multimeter **must** show a voltage with the starter switch “OFF” to be normal.

![[sb800ki.png]]

If the multimeter does **not** indicate a voltage, check the cable connecting the starter solenoid and battery for breaks.

Also check for loose or corroded connections.

![[sb800kk.png]]

If the multimeter indicates a voltage, but the starter will **not** operate, check the wire connecting the starter solenoid to the starter switch for breaks.

Also check for loose or corroded connections.

Be sure to check for:

- Fuses
- Application engine shutoff systems.

![[sb800kl.png]]

If the wire connecting the starter solenoid and starter switch is **not** loose or damaged, and the starter will **not** operate, remove the cable connecting the starter and starter solenoid from the solenoid terminal.

Connect the multimeter positive (+) lead to the solenoid positive (+) terminal and the negative (-) lead to the chassis or an engine ground location.

![[sb800km.png]]

Turn the starter switch to the “START” position.

If the multimeter indicates a voltage, the starter solenoid is malfunctioning and **must** be replaced.

![[sb800kn.png]]

If the multimeter does **not** indicate a voltage, check the wire connecting the starter solenoid to the magnetic switch for breaks, and for loose or corroded connections.

![[sb800ko.png]]

If the wire connecting the starter solenoid to the magnetic switch is **not** loose or damaged and the starter will **not** operate, check the cable connecting the starter solenoid to the starting motor for breaks, and for loose or corroded connections.

![[es900ka.png]]

Check the cable connecting the starting motor to the battery for breaks, and for loose or corroded connections.

![[sb8cosa.png]]

If the cables are **not** loose or damaged, the starting motor is defective and **must** be replaced. Refer to Procedure [[100-013-020 — Starting Motor|013-020]].

![[13900038.png]]
