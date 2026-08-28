---
aliases:
  - "Датчик температуры подогревателя впускного воздуха"
type: "Процедура"
doc: "100-010-123"
title_en: "Intake Manifold Air Heater Temperature Sensor"
title_ru: "Датчик температуры подогревателя впускного воздуха"
modified: "2003-08-26"
engines:
  - "93047320"
  - "93058669"
  - "93087701"
families:
  - "6B5.9"
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
  - "3666087"
figures: 3
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/C8.3"
  - "группа/100"
---

# Intake Manifold Air Heater Temperature Sensor
**Датчик температуры подогревателя впускного воздуха**

> [!abstract] Процедура · `100-010-123`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** 6B5.9, C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]], [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-123.pdf)

### Initial Check

The intake air temperature sensor is located in the intake manifold.

Disconnect the harness connector from the temperature sensor.

![[10900298.png]]

### Resistance Check

Use an ohmmeter to measure the resistance between the two pins of the intake air temperature sensor.

If the resistance is **not** correct, replace the sensor.

If the resistance is correct, the sensor **must** be checked for a short to ground.

The resistance value is temperature-dependent.

| Temperature (°C) | Temperature (°F) | Acceptable Resistance Range (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

![[ee1coke.png]]

Measure the resistance from each pin of the intake air temperature sensor to the engine block.

The ohmmeter **must** show an open circuit (more than 100k ohms).

If the circuit is **not** open, replace the sensor.

![[ee1cokf.png]]
