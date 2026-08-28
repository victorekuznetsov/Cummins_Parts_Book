---
aliases:
  - "Датчик давления во впускном коллекторе"
type: "Процедура"
doc: "60-019-061"
title_en: "Intake Manifold Pressure Sensor"
title_ru: "Датчик давления во впускном коллекторе"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Intake Manifold Pressure Sensor
**Датчик давления во впускном коллекторе**

> [!abstract] Процедура · `60-019-061`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-061.pdf)

### Remove

[[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E for sensor location.]]

Disconnect the engine harness connector from the intake manifold pressure sensor.

Remove the sensor using a deep-well socket, Part Number 3823843, or equivalent.

![[19400439.png]]

### Install

If a new intake manifold pressure sensor is used, make sure the sensor has an o-ring.

Install the sensor into the air intake manifold.

Use a deep-well socket, Part Number 3823843, to tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19400440.png]]

Connect the engine harness to the intake manifold pressure sensor.

![[19400452.png]]

### Test

Connect an electronic service tool to the data link.

Remove the intake manifold pressure sensor.

![[19800902.png]]

Connect the engine harness to the intake manifold pressure sensor.

Allow the sensor and harness to hang in the air.

![[08600402.png]]

Monitor the intake manifold pressure with the electronic service tool.

The intake manifold pressure **must** be within ±63.5 mm Hg \[2.5 In Hg\] of the barometric pressure sensor value.

If the intake manifold pressure sensor is not within specifications, the intake manifold pressure sensor **must** be replaced.

Disconnect the electronic service tool.

Disconnect the intake manifold pressure sensor from the engine harness.

Install the intake manifold pressure sensor.

![[19800902.png]]

### Pressure Test

> [!warning] CAUTION · Осторожно
> Do not drill and tap a hole into the aftercooler cover. A faulty reading can result if the aftercooler core is leaking.

Connect an electronic service tool to the data link.

![[19800902.png]]

Install a 0 to 2030 mm Hg \[0 to 80 in Hg\] manometer (or gauge) in the \[3/8-inch\] pipe plug hole in the aftercooler housing.

![[10400032.png]]

Operate the engine at rated rpm and full load. Compare the reading from the electronic service tool to the gauge reading. The electronic service tool reading **must** be within 51 mm Hg \[2 in Hg\] of the gauge reading.

If the intake manifold pressure sensor is **not** within specifications, the intake manifold pressure sensor **must** be replaced.

![[17600025.png]]
