---
aliases:
  - "Выключатель «Стоп/Работа»"
type: "Процедура"
doc: "94-019-014"
title_en: "Stop/Run Switch"
title_ru: "Выключатель «Стоп/Работа»"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-014.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-014.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Stop/Run Switch
**Выключатель «Стоп/Работа»**

> [!abstract] Процедура · `94-019-014`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-014.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-014.pdf)

### General Information

The Stop/Run switch supplies an input signal to the ECM which “Starts” or “Stops” the ECM.

The switch must be in the STOP position for the controller to be in the diagnostic mode.

![[19a00038.png]]

### Resistance Check

Using INSITE™, Part No. 3825145, in the monitor mode, toggle the Stop/Run switch between STOP and RUN checking for proper operation.

If the switch does **not** operate properly, follow the troubleshooting procedures in this section.

Remove and tag the connectors from the terminals on the switch. Place the multimeter leads on each terminal.

![[19800348.png]]

Place the Stop/Run switch in the STOP position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM Troubleshooting and Repair manual for replacement instructions.

![[19a00048.png]]

Move the switch to the RUN position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed. Refer to the OEM Troubleshooting and Repair manual for replacement instructions.

![[19a00049.png]]
