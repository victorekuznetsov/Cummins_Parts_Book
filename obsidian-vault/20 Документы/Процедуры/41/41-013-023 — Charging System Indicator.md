---
aliases:
  - "Индикатор системы зарядки"
type: "Процедура"
doc: "41-013-023"
title_en: "Charging System Indicator"
title_ru: "Индикатор системы зарядки"
modified: "2004-12-07"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-013-023.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-013-023.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/41"
---

# Charging System Indicator
**Индикатор системы зарядки**

> [!abstract] Процедура · `41-013-023`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2004-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/41/41-013-023.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/41-013-023.pdf)

### Initial Check

Be sure the correct terminals are being used on the alternator. The R terminal (Delco®) or W terminal (Bosch® K1) provide half of the system voltage and is used to operate accessories such as the tachometer on generator sets.

![[es900ks.png]]

Trouble with the starting system can be indicated by the indicator lamp or ampmeter.

![[es900kb.png]]

Check the indicator lamp for normal operation as shown below:

| Engine | Switch | Lamp | Ampmeter |
|---|---|---|---|
| Stopped | OFF | OFF | 0 |
| Stopped | ON | ON | - |
| Running | ON | OFF | + |

![[es900kc.png]]

If the lamp is on when the switch is OFF and the engine is **not** running, disconnect the lamp lead at the ignition switch.

- If the lamp stays on, there is a short to a positive wire.
- If the lamp goes out, there is a short in the switch.

![[13900029.png]]

If the lamp goes off when the switch is ON and the engine is **not** running, there can be an open in the circuit.

Check for a blown fuse, a burned out bulb, defective bulb socket, or an open in the No. 1 or D (+) lead circuit between alternator and ignition switch.

![[es900kf.png]]

If the lamp is on when the switch is ON and the engine is running, disconnect the lead to the alternator.

- If the lamp stays on, there is a short to the ground in the lamp circuit.
- If the lamp goes out, inspect the alternator.

![[ea900wd.png]]
