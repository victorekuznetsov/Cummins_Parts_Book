---
aliases:
  - "Цепь лампы предупреждения защиты двигателя"
type: "Процедура"
doc: "87-019-041"
title_en: "Engine Protection Warning Lamp Circuit"
title_ru: "Цепь лампы предупреждения защиты двигателя"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-041.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-041.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Protection Warning Lamp Circuit
**Цепь лампы предупреждения защиты двигателя**

> [!abstract] Процедура · `87-019-041`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-041.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-041.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3823993, on the 31-pin connector, and test lead, Part Number 3822758, on the 50-pin connector, when taking a measurement.

Turn the vehicle keyswitch to the OFF position. Disconnect the OEM interface harness and the engine harness from the ECM. Disconnect the OEM harness from the OEM interface harness at the 31-pin connector.

![[19a00331.png]]

Measure the resistance from pin 4 of the 50-pin OEM interface harness connector to pin 14 of the 31-pin OEM interface harness connector, interface harness side. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness.

Refer to Procedure 019-231 or [[87-019-250 — Connector, 50-Pin|019-250]] to repair the harness. Refer to Procedure [[87-019-043 — Engine Wiring Harness|019-043]] to replace the harness.

![[19a00331.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Turn the vehicle keyswitch to the OFF position. Disconnect the OEM and engine harnesses from the ECM. Disconnect the OEM harness from the OEM interface harness at the 31-pin connector.

![[19a00712.png]]

Insert the test lead into pin 4 of the 50-pin OEM interface harness connector, and attach it to the multimeter probe. Touch the other multimeter probe to the engine block.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, repair or replace the engine harness.

Refer to Procedure [[87-019-250 — Connector, 50-Pin|019-250]] or [[87-019-043 — Engine Wiring Harness|019-043]].

![[19a00712.png]]

### Voltage Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the OEM and engine harnesses from the ECM. Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC.

Insert a test lead into pin 4 of the OEM harness connector.

![[19a00332.png]]

Connect the alligator clip to the positive (+) multimeter probe. Touch the negative (-) multimeter probe to the engine block. Measure the voltage. The multimeter **must** show battery voltage.

If battery voltage is **not** present, wire 4 **must** be checked for an open circuit or a short circuit to ground.

![[19a00332.png]]
