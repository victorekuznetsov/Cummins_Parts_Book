---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "19-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
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
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `19-019-059`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-059.pdf)

### Remove

Lift up on the locking tab and pull the electrical connectors apart.

Remove the sensor from the engine.

![[19400434.png]]

### Install

Make sure the new sensor has an o-ring around the surface where it seals against the engine block.

Install the sensor in the engine block.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19400435.png]]

Push connectors together until they lock.

![[19400436.png]]

### Resistance Check

Lift up on the locking tab and pull the electrical connectors apart.

![[19400436.png]]

Use a multimeter to measure the resistance between the two pins of the intake air temperature sensor. The resistance **must** be 600 ohms to 36k ohms\*. If the resistance is **not** correct, replace the sensor. If the resistance is correct, the sensor **must** still be checked for a short circuit to ground.

\* The resistance value is temperature-dependent as follows:

| Temp C° | Temp F° | Acceptable Resistance Range (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

![[19800980.png]]

### Check for Short Circuit to Ground

Measure the resistance from a pin of the intake air temperature sensor to the engine block. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, replace the sensor.

![[19800981.png]]
