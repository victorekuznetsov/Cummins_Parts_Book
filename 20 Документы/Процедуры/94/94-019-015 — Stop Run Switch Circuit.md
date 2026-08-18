---
aliases:
  - "Цепь выключателя «Стоп/Работа»"
type: "Процедура"
doc: "94-019-015"
title_en: "Stop/Run Switch Circuit"
title_ru: "Цепь выключателя «Стоп/Работа»"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 4
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-015.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-015.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Stop/Run Switch Circuit
**Цепь выключателя «Стоп/Работа»**

> [!abstract] Процедура · `94-019-015`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-015.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-015.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins in the connector.

Disconnect the connector from the positive battery terminal.

Disconnect the OEM connector from the ECM.

![[19a00055.png]]

Insert a test lead into pin 63 of the OEM harness connector.

Measure the resistance from pin 63 to the positive battery connector.

Place the Stop/Run switch in the RUN position. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, check for an open circuit in the Stop/Run switch wiring, considering the switch has already been checked.

Repair or replace the OEM harness. Refer to OEM Troubleshooting and Repair Procedures.

![[19a00051.png]]

Move the Stop/Run switch to STOP. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, a short circuit exists in the Stop/Run switch wiring, providing the switch has already been checked.

Repair or replace the OEM harness. Refer to OEM Troubleshooting and Repair Procedures.

![[19a00051.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the OEM harness from the ECM.

Disconnect the connector from the positive battery lead.

Measure the resistance from pin 63 of the OEM harness connector to all other pins in the connector. The multimeter **must** show an open circuit (100k ohms or less).

If any check shows less than 100k ohms, repair or replace the OEM harness. Refer to OEM Troubleshooting and Repair Procedures.

> [!missing]- Иллюстрация `19a00052.png` не извлечена — смотрите PDF-оригинал документа
