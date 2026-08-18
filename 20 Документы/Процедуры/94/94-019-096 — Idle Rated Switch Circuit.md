---
aliases:
  - "Цепь выключателя «холостой ход/номинал»"
type: "Процедура"
doc: "94-019-096"
title_en: "Idle Rated Switch Circuit"
title_ru: "Цепь выключателя «холостой ход/номинал»"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 5
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-096.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-096.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Idle Rated Switch Circuit
**Цепь выключателя «холостой ход/номинал»**

> [!abstract] Процедура · `94-019-096`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-096.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-096.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins in the connector.

Insert the test lead into pin 3 of the OEM harness connector.

Measure the resistance from pin 3 to engine block ground.

![[19a00055.png]]

Move the Idle/Rated switch to the IDLE position. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, check for an open circuit in the Idle/Rated switch wiring.

Move the switch to the “Rated” position. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, repair or replace the OEM harness, provided the switch has previously been checked. Refer to OEM Troubleshooting and Repair Procedures.

![[19a00056.png]]

### Check for Short Circuit to Ground

Place the Idle/Rated switch in the RATED position.

Remove the OEM harness connector from the ECM.

Use test lead, Part No. 3822758, and measure the resistance from pin 3 of the OEM harness connector to ground.

![[19a00057.png]]

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, there is a short circuit in the Idle/Rated switch circuit, provided the diagnostic Idle/Rated switch has been previously checked.

Repair or replace OEM harness, refer to OEM Troubleshooting and Repair Procedures.

![[19a00058.png]]

### Check for Short Circuit from Pin to Pin

Remove the engine harness connector from the ECM.

Move the Idle/Rated switch to the RATED position.

Use test lead, Part No. 3822758, and measure the resistance from pin 3 of the OEM harness connector to every other pin in the connector. The multimeter **must** show an open circuit (100k ohms or more).

If the multimeter does not show an open, a short circuit exists between pin 3 and whichever pin showed less than 100k ohms. Repair or replace the OEM harness, refer to OEM Troubleshooting and Repair Procedures.

![[19a00059.png]]
