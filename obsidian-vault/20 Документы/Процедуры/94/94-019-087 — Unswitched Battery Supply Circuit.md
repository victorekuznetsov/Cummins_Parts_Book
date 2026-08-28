---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "94-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `94-019-087`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-087.pdf)

### General Information

The ECM receives constant voltage from the battery through the unswitched battery wires that are connected directly to the (+) positive battery post.

![[19a00039.png]]

### Initial Check

Inspect the battery cable connections for loose or corroded connections. Repair or replace the battery connections. Refer to the OEM manual.

![[19400082.png]]

Check the battery voltage. Place the multimeter's positive probe on the positive (+) terminal of the battery. Place the multimeter's negative probe on the negative (-) terminal of the battery. Measure the battery voltage. The voltage should be 17.3 to 34.7 volts DC for a 24 volt system. If the battery voltage is below 17.3 volts replace the battery. Refer to the Base Engine Troubleshooting and Repair Manual for battery replacement.

![[19400083.png]]

### Resistance Check

Disconnect the engine harness from the ECM. Check the ECM and engine harness for damaged pins.

![[19400242.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins in the connector.

Insert the test lead into pin 38 of the engine harness. Connect the alligator clip to the multimeter probe. Touch the other probe to the battery connection on the engine harness. Measure the resistance. The resistance **must** be 10 ohms or less.

Repeat this step for pins 16 thru 20.

![[19a00033.png]]

If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness. Refer to Procedures 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00035.png]]
