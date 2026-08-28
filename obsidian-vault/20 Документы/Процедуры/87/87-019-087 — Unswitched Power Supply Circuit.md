---
aliases:
  - "Цепь постоянного питания"
type: "Процедура"
doc: "87-019-087"
title_en: "Unswitched Power Supply Circuit"
title_ru: "Цепь постоянного питания"
modified: "2018-08-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Unswitched Power Supply Circuit
**Цепь постоянного питания**

> [!abstract] Процедура · `87-019-087`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2018-08-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-087.pdf)

### General Information

The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the (+) positive battery post. There are two in-line 15-amp fuses in the unswitched battery wires to protect the ECM.

![[19a00746.png]]

### Initial Check

Inspect the battery cable connections for loose or corroded connections. Repair or replace the battery connections. Refer to the OEM manual.

![[19400082.png]]

Inspect the OEM interface harness fuse connections for loose or corroded fuses. Replace the fuses.

[[99-019-198 — Fuse, Harness In-Line|Refer to Procedure 019-198]].

Check the fuses for resistance. Touch one multimeter lead to each fuse terminal and measure the resistance. The fuse should measure a closed circuit (10 ohms or less).

![[19400084.png]]

Check the battery voltage. Place the multimeter positive probe on the positive (+) terminal of the battery. Place the multimeter negative probe on the negative (-) terminal of the battery. Measure the battery voltage. The voltage should be 17.3 to 34.7 VDC for a 24-VDC system. If the battery voltage is below 17.3 VDC, replace the battery.

Refer to the OEM manual for battery replacement.

![[19400083.png]]

### Resistance Check

Disconnect the engine harness connector from the ECM. Check for damaged pins in the ECM and the harness.

![[19900781.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Insert the lead into pin 38 of the engine harness connector. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the battery connection on the engine harness. Measure the resistance. The resistance **must** be 10 ohms or less.

![[19a00174.png]]

Remove the lead from pin 38 and insert it into pin 39 of the engine harness connector. Touch the other multimeter probe to the battery connection on the engine harness.

Measure the resistance. The resistance **must** be 10 ohms or less.

Repeat the check from pins 40 and 50 of the engine harness connector to the battery connection on the engine harness.

Measure the resistance. The resistance **must** be 10 ohms or less.

![[19a00175.png]]

If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness.

[[99-019-197 — Ring Terminal|Refer to Procedure 019-197]], [[99-019-199 — Connector, Butt Splice|Refer to Procedure 019-199]], [[87-019-250 — Connector, 50-Pin|Refer to Procedure 019-250]], and [[87-019-043 — Engine Wiring Harness|Refer to Procedure 019-043]].

![[19a00176.png]]
