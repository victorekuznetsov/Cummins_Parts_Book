---
aliases:
  - "Датчик давления охлаждающей жидкости"
type: "Процедура"
doc: "60-019-016"
title_en: "Coolant Pressure Sensor"
title_ru: "Датчик давления охлаждающей жидкости"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-016.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-016.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Coolant Pressure Sensor
**Датчик давления охлаждающей жидкости**

> [!abstract] Процедура · `60-019-016`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-016.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-016.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or stream can cause personal injury.

- Drain the cooling system. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 of the QST30 Service Manual, Bulletin 4021539.]]

![[ck800wa.png]]

### Remove

> [!note] Note · Примечание
> The QSK19 engine is used in the following illustrations. The remove and install steps are the same.

Disconnect the engine harness from the coolant pressure sensor.

![[19400387.png]]

Remove the coolant pressure sensor.

Use the Deep Well Socket, Part Number 3823843, to remove the coolant pressure sensor.

![[19801029.png]]

### Test

Connect the INSITE™ electronic service tool to the data link.

![[19800902.png]]

Connect the engine harness to the coolant pressure sensor.

Allow the sensor and harness to hang in the air.

![[08600402.png]]

Monitor the coolant pressure sensor with the electronic service tool.

The coolant pressure **must** be within 17.2 kPa \[2.5 psi\] of the barometric pressure sensor value.

If the coolant pressure is **not** within specifications, the coolant pressure sensor **must** be replaced.

Disconnect INSITE™ electronic service tool.

Disconnect the coolant pressure sensor from the engine harness.

![[19800902.png]]

### Install

Install the coolant pressure sensor into the thermostat housing.

Tighten the coolant pressure sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19801029.png]]

Connect the engine harness to the coolant pressure sensor.

![[19801028.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

- Fill the cooling system. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 of the QST30 Service Manual, Bulletin 4021539.]]

![[ck800wa.png]]
