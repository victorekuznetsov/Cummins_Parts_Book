---
aliases:
  - "Выключатель «холостой ход/номинал»"
type: "Процедура"
doc: "94-019-095"
title_en: "Idle Rated Switch"
title_ru: "Выключатель «холостой ход/номинал»"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 4
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-095.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-095.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Idle Rated Switch
**Выключатель «холостой ход/номинал»**

> [!abstract] Процедура · `94-019-095`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-095.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-095.pdf)

### General Information

The Idle/Rated switch is used to switch between Idle speed and Rated speed.

![[19a00061.png]]

### Resistance Check

Using INSITE™, Part No. 3825145, in the monitor mode, toggle the Idle/Rated switch between IDLE and RATED checking for proper operation.

If the switch does **not** operate properly or INSITE™ is **not** available, follow the troubleshooting procedures in this section.

Remove and tag the connectors from the terminals on the switch. Place the multimeter leads on each terminal.

![[19800348.png]]

Place the Idle/Rated switch in the RATED position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed and **must** be replaced. Refer to OEM Troubleshooting and Repair Procedures.

![[19a00053.png]]

Move the switch to the IDLE position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed and **must** be replaced. Refer to OEM Troubleshooting and Repair Procedures.

![[19a00054.png]]
