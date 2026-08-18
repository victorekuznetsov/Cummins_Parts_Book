---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "60-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `60-019-059`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-059.pdf)

### Remove

Disconnect the engine harness connector from the intake manifold air temperature sensor.

Remove the intake manifold air temperature sensor from the engine.

![[19400434.png]]

### Install

Install a new o-ring on the intake manifold temperature sensor.

Install the sensor in the intake manifold.

Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19400435.png]]

Push the connectors together until they lock.

![[19400436.png]]

### Resistance Check

Disconnect the engine harness connector from the intake manifold air temperature sensor.

![[19400436.png]]

Measure the resistance between the intake manifold 1 temperature signal and intake manifold 1 temperature RETURN pin in the sensor.

![[19800980.png]]

| Temperature | Acceptable Resistance Range |  |
|---|---|---|
| **°C** | **°F** | **(ohms)** |
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

If the intake manifold air temperature sensor resistance is **not** within the range, it **must** be replaced.

![[19800980.png]]

### Check for Short Circuit to Ground

Measure the resistance between the intake manifold 1 temperature SIGNAL pin and engine ground.

Replace the sensor if the resistance is **not** greater than 100k ohms.

> [!missing]- Иллюстрация `19800981.png` не извлечена — смотрите PDF-оригинал документа
