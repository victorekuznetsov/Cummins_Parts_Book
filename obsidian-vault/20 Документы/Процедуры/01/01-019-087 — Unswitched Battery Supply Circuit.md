---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "01-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2003-12-04"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `01-019-087`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-087.pdf)

### General Information

The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There is one inline 20 AMP fuse in the unswitched battery wire to protect the ECM.

![[19802554.png]]

### Initial Check

Inspect the battery cable connections for loose or corroded connections. Repair or replace the battery connections. Refer to the OEM manual.

![[19400082.png]]

Inspect the harness fuse connections for loose or corroded fuses. Replace the fuses. Refer to Procedure [[99-019-198 — Fuse, Harness In-Line|019-198]].

![[19400084.png]]

Check the battery voltage. Place the multimeter positive probe on the positive (+) terminal of the battery. Place the multimeter negative probe on the negative (-) terminal of the battery. Measure the battery voltage. The voltage should be 17.3 to 34.7 VDC for a 24 VDC system. If the battery voltage is below 17.3 VDC, replace the battery. Refer to the OEM manual for battery replacement.

![[19400083.png]]

### Resistance Check

Disconnect the extension harness connectors from the ECM. Check for damaged pins in the ECM and the harness.

![[19802555.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822917. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Insert the lead into one of the B+ pins of the engine harness. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the battery connector on the harness. Measure the resistance. The resistance **must** be 10 ohms or less.

![[19802550.png]]

Repeat this test for all the B+ pins in the harness. Measure the resistance. The resistance **must** be 10 ohms or less.

If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]] or the OEM manual.

![[19802550.png]]

Repeat this test for all the B - pins in the harness. Measure the resistance. The resistance **must** be 10 ohms or less.

If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]] or the OEM manual.

![[19802550.png]]
