---
aliases:
  - "Датчик давления во впускном коллекторе"
type: "Процедура"
doc: "87-019-061"
title_en: "Intake Manifold Pressure Sensor"
title_ru: "Датчик давления во впускном коллекторе"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-061.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-061.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Intake Manifold Pressure Sensor
**Датчик давления во впускном коллекторе**

> [!abstract] Процедура · `87-019-061`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-061.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-061.pdf)

### Initial Check

Connect an electronic service tool to the vehicle datalink.

![[19900524.png]]

Install a 0- to 2030-mm Hg \[0- to 80-in Hg\] manometer (or gauge) in the 3/8-inch pipe plug hole in the aftercooler housing.

Do **not** drill and tap a hole in the aftercooler cover. A faulty reading can result if the aftercooler core is leaking.

![[19a00340.png]]

Operate the engine at rated rpm and full load. Compare the reading from the electronic service tool to the gauge reading. If the electronic service tool reading differs by more than 50 mm Hg \[2 in Hg\] from the gauge reading, then replace the intake manifold pressure sensor.

![[10400033.png]]

### Remove

Lift up on the tab and disconnect the connector from the sensor.

![[19a00243.png]]

Remove the sensor from the air intake manifold with deep flank drive socket, Part Number 3823843.

![[19a00244.png]]

### Install

Make sure the new sensor has an o-ring around the surface where it seals against the air intake manifold.

Lubricate the o-ring with clean engine oil.

![[19a00253.png]]

Install the sensor into the air intake manifold by turning it **clockwise**.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19a00244.png]]

> [!warning] CAUTION · Осторожно
> Use only Cummins-recommended lubricant DS-ES, Part Number, 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.

Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire cavity with lubricant.

![[cel29.png]]

Push the harness connector into the sensor until it locks.

![[19a00243.png]]
