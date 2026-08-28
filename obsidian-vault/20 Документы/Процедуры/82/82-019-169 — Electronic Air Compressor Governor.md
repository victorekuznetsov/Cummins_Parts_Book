---
aliases:
  - "Электронный регулятор воздушного компрессора"
type: "Процедура"
doc: "82-019-169"
title_en: "Electronic Air Compressor Governor"
title_ru: "Электронный регулятор воздушного компрессора"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-169.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-169.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Electronic Air Compressor Governor
**Электронный регулятор воздушного компрессора**

> [!abstract] Процедура · `82-019-169`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-169.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-169.pdf)

### Remove

> [!danger] WARNING · Опасно
> Drain the air compressor tank and all lines before removing or installing the air compressor governor. Failure to drain the air compressor tank and lines of pressure could result in personal injury, mechanical damage, or electrical damage, or all of the above.

Lift up on the tab and disconnect the connector from the governor.

Remove the governor from the air compressor.

Inspect the governor for damage.

![[19200315.png]]

### Install

> [!danger] WARNING · Опасно
> Drain the air compressor tank and all lines before removing or installing the air compressor governor. Failure to drain the air compressor tank and lines of pressure could result in personal injury, mechanical damage, or electrical damage, or all of the above.

Make sure the new governor has an o-ring around the surface where it seals against the air compressor.

Install the governor onto the air compressor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19200316.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly into the connector without expanding the connector pins.

Disconnect the actuator harness connector from the ECM. Disconnect the 6-pin electronic governor connector from the engine harness. Insert a test lead into pin 14 of the actuator harness connector, and connect it to the multimeter probe. Insert the other test lead into pin 5 of the 6-pin electronic governor connector, engine harness side. Connect the lead to the other multimeter probe. Set the multimeter to the resistance setting and measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19c00422.png]]

Insert the test lead into pin 11 of the actuator harness connector. Insert the other test lead into pin 6 of the 6-pin electronic governor connector, engine harness side. Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19c00423.png]]
