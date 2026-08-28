---
aliases:
  - "Выключатель подтверждения промежуточной частоты вращения"
type: "Процедура"
doc: "19-019-108"
title_en: "Intermediate Speed Control Validation Switch"
title_ru: "Выключатель подтверждения промежуточной частоты вращения"
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
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-108.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-108.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Intermediate Speed Control Validation Switch
**Выключатель подтверждения промежуточной частоты вращения**

> [!abstract] Процедура · `19-019-108`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-108.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-108.pdf)

### Initial Check

Connect the electronic service tool to the vehicle datalink. Turn the keyswitch to the ON position.

Operate the intermediate speed control validation switch while monitoring INSITE™. INSITE™ reading should change with the switch position.

![[19900524.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use the probes or leads other than Part Number 3822758 on the ECM connectors and Part Number 3829993 on the 31-pin OEM interface harness connector. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the OEM interface harness from the ECM.

Disconnect the 31-pin OEM interface harness from the OEM harness at the 31-pin.

Measure the resistance from pin 35 of the OEM interface harness connector to pin 21 of the engine side of the 31-pin connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM interface wiring harness. Refer to Procedure 019-231, 019-240, or [[19-019-072 — OEM Interface Harness|019-072]].

![[19400288.png]]

Measure the resistance from pin 38 of the OEM interface harness connector to pin 20 of the engine side of the 31-pin connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM wiring harness. Refer to Procedure 019-231, 019-240, or [[19-019-072 — OEM Interface Harness|019-072]].

![[19400289.png]]

Measure the resistance from pin 37 of the OEM interface harness connector to pin 19 of the engine side of the 31-pin connector. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the OEM wiring harness. Refer to Procedure 019-231, 019-240, or [[19-019-072 — OEM Interface Harness|019-072]].

If the OEM harness on the engine side of the 31-pin OEM interface connector passes the above resistance checks then check the resistance of the vehicle side of the 31-pin OEM interface connector. Refer to the vehicle manufacturer's instructions.

![[19400290.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use the probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the OEM interface harness from the ECM.

Move the ISC switch to the center OFF position.

Measure the resistance from pins 35, 38, and 37 of the OEM interface harness connector to the engine block. The multimeter **must** show 100k ohms or more.

If the circuit is **not** open, check for short circuit to ground in the OEM wiring harness, provided the switch has been checked previously.

![[19400291.png]]

Disconnect the OEM interface harness from the OEM harness at the 31-pin connector.

Measure the resistance from pins 35, 38, and 37 of the OEM interface harness connector to the engine block. The multimeter **must** show 100k ohms or more.

If the circuit is **not** open, check for a short circuit to ground on the vehicle side of the 31-pin OEM interface harness connector. Refer to the vehicle manufacturer's instructions.

![[19400291.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the OEM interface harness from the ECM.

Measure the resistance from pin 35 to all other pins in the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 37 to all other pins in the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 38 to all other pins in the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, check for short circuit from pin to pin on the engine side of the 31-pin connector, provided the switch has been checked earlier.

![[19400292.png]]

Disconnect the 31-pin pass-through connector.

Measure the resistance from pin 35 to all other pins in the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 37 to all other pins in the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

Measure the resistance from pin 38 to all other pins in the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, check for short circuit from pin to pin on the vehicle side of the 31-pin connector. Refer to the vehicle manufacturer's instructions.

![[19400292.png]]
