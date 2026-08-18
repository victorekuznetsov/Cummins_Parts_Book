---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "01-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
modified: "2002-12-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `01-019-059`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-059.pdf)

### Remove

Lift up on the locking tab and pull the electrical connectors apart.

Remove the intake manifold air temperature sensor from the engine.

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

Use a multimeter to measure the resistance between the two pins of the intake air temperature sensor. The resistance **must** be 600 ohms to 36K ohms\*. If the resistance is **not** correct, replace the sensor. If the resistance is correct, the sensor **must** still be checked for a short to ground.

![[19800980.png]]

\* The resistance value is temperature-dependent as follows:

| Temperature | Acceptable ResistanceRange |  |
|---|---|---|
| **°C** | **°F** | **(ohms)** |
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

![[19800980.png]]

### Check for Short Circuit to Ground

Measure the resistance from a pin of the intake air temperature sensor to the engine block. The multimeter **must** show an open circuit (more than 100K ohms). If the circuit is **not** open, replace the sensor.

> [!missing]- Иллюстрация `19800981.png` не извлечена — смотрите PDF-оригинал документа
