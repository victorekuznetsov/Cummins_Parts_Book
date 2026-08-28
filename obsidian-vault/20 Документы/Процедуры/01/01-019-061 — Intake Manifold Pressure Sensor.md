---
aliases:
  - "Датчик давления во впускном коллекторе"
type: "Процедура"
doc: "01-019-061"
title_en: "Intake Manifold Pressure Sensor"
title_ru: "Датчик давления во впускном коллекторе"
modified: "2003-07-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Intake Manifold Pressure Sensor
**Датчик давления во впускном коллекторе**

> [!abstract] Процедура · `01-019-061`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-061.pdf)

### Initial Check

Connect an electronic service tool to the datalink.

![[19800902.png]]

Install a 0 to 2030 mm Hg \[0 to 80 in Hg\] manometer (or gauge) in the \[3/8-inch\] pipe plug hole in the aftercooler housing.

Do **not** drill and tap a hole in the aftercooler cover. A faulty reading can result if the aftercooler core is leaking.

![[10400032.png]]

Operate the engine at rated rpm and full load. Compare the reading from the electronic service tool to the gauge reading. If the electronic service tool reading **must** be within 51 mm Hg \[2 in Hg\] of the gauge reading.

If the intake manifold pressure sensor is **not** within specifications, the intake manifold pressure sensor **must** be replaced.

![[17600025.png]]

### Remove

Disconnect the engine harness from the intake manifold pressure sensor.

Remove the sensor using a deep-well socket, Part Number 3823843.

![[19400439.png]]

### Test

Connect an electronic service tool to the datalink.

![[19800902.png]]

Connect the engine harness to the intake manifold pressure sensor.

Allow the sensor and harness to hang in air.

![[08600402.png]]

Monitor the intake manifold pressure with the electronic service tool.

The intake manifold pressure **must** be within ±63.5 mm Hg \[2.5 In Hg\] of the barometric pressure sensor value.

If the intake manifold pressure sensor is not within specifications, the intake manifold pressure sensor **must** be replaced.

Disconnect the electronic service tool.

Disconnect the intake manifold pressure sensor from the engine harness.

![[19800902.png]]

### Install

If a new intake manifold pressure sensor is used, make sure the sensor has an o-ring.

Install the sensor into the air intake manifold.

Use a deep-well socket, Part Number 3823843, to tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19400440.png]]

Connect the engine harness to the intake manifold pressure sensor.

![[19400452.png]]
