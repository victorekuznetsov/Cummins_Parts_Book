---
aliases:
  - "Цепь лампы предупреждения защиты двигателя"
type: "Процедура"
doc: "19-019-041"
title_en: "Engine Protection Warning Lamp Circuit"
title_ru: "Цепь лампы предупреждения защиты двигателя"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-041.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-041.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Protection Warning Lamp Circuit
**Цепь лампы предупреждения защиты двигателя**

> [!abstract] Процедура · `19-019-041`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-041.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-041.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758, on the 40-pin OEM harness connector and Part Number 3823993, on the 31-pin OEM harness connector. The leads must fit tightly in the connector without expanding the pins in the connector.

Turn the vehicle keyswitch to the OFF position. Disconnect the OEM interface harness from the ECM. Disconnect the OEM interface harness from the OEM harness at the 31-pin connector.

Measure the resistance from pin 2 of the OEM interface harness connector to pin 1 of the 31-pin OEM interface connector, OEM interface side. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM interface harness. Refer to Procedure 019-231, 019-240, or [[19-019-072 — OEM Interface Harness|019-072]].

Check the OEM harness resistance. Refer to the manufacturer's instructions.

![[19400233.png]]

### Check for Short Circuit to Ground

Turn the vehicle keyswitch to the OFF position. Disconnect the OEM interface harness from the ECM. Disconnect the OEM interface harness from the OEM harness at the 31-pin connector.

Measure the resistance from pin 2 of the OEM interface harness ECM connector to the engine block.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, repair or replace the OEM interface harness. Refer to Procedure 019-240 or [[19-019-072 — OEM Interface Harness|019-072]].

Check the OEM harness for a short circuit to ground. Refer to the manufacturer's instructions.

![[19400232.png]]

### Voltage Check

Disconnect the OEM interface harness from the ECM.

Insert one lead into pin 2 of the OEM interface harness connector.

![[19400230.png]]

Connect the alligator clip to the positive (+) multimeter probe. Connect the negative (-) multimeter probe to the engine block. Turn the vehicle keyswitch to the ON position. Set the multimeter to measure VDC. The multimeter **must** show battery voltage. If battery voltage is **not** present, wire number 2 **must** be checked for an open circuit or a short circuit to ground.

![[19400231.png]]
