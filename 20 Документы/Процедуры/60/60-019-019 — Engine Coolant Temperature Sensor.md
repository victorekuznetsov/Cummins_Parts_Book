---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "60-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `60-019-019`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-019.pdf)

### Test

Connect an INSITE™ electronic service tool to the data link connector.

Place the RUN/STOP switch in the RUN position.

Controller **not** in the diagnostic mode.

Start the engine and let it idle.

![[19800902.png]]

Place a temperature probe in close proximity of the coolant temperature sensor.

Record the coolant temperature from the INSITE™ electronic service tool.

Compare the temperature of the probe and the INSITE™ electronic service tool.

If the coolant temperature on the electronic service tool is excessively higher than the water temperature, replace the coolant temperature sensor.

Refer to the Remove step in this procedure.

If the coolant temperature on the electronic service tool does **not** increase with the water temperature, replace the coolant temperature sensor.

Refer to the Remove step in this procedure.

![[19400068.png]]

Place the RUN/STOP switch in the STOP position.

Monitor the coolant temperature with the electronic service tool.

If the coolant temperature does not decrease to the ambient air temperature, replace the coolant temperature sensor.

Refer to the Remove step in this procedure.

![[19800902.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap or the coolant temperature sensor. Heated coolant spray or steam can cause personal injury.

- Drain the cooling system. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 in the QST30 Service Manual, Bulletin 4021539.]]

![[ck800wa.png]]

### Remove

Lift up on the locking tab and pull the electrical connectors apart.

Remove the sensor.

![[19c00247.png]]

### Install

Make sure the new sensor has an o-ring installed.

Lubricate the o-ring with clean vegetable oil.

Install the new sensor into the engine. Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19c00247.png]]

Push the connectors together until they lock.

![[19c00248.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap or the coolant temperature sensor. Heated coolant spray or steam can cause personal injury.

- Fill the cooling system and check for coolant leaks. [[57-008-018 — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8 in the QST30 Service Manual, Bulletin 4021539.]]

![[ck800wa.png]]
