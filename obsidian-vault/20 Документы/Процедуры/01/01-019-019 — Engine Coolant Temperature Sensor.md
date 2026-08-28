---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "01-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2002-12-05"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `01-019-019`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-12-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-019-019.pdf)

### Initial Check

Connect an electronic Service Tool to the data link connector.

Place the Run/Stop Switch in the Run position.

Controller **not** in the diagnostic mode.

Start the engine and let it idle.

![[19800902.png]]

Monitor the coolant temperature with the electronic Service Tool.

Compare the cool temperature value with the water temperature gauge, or connect a temperature probe to the engine near the coolant temperature sensor and compare the reading on the service tool with the temperature probe reading.

If the coolant temperature on the electronic Service Tool is excessively higher than the water temperature, replace the coolant temperature sensor.

If the coolant temperature on the electronic Service Tool does **not** increase with the water temperature, replace the coolant temperature sensor.

![[19400068.png]]

Remove the coolant temperature sensor. Refer to Procedure [[01-019-019 — Engine Coolant Temperature Sensor|019-019]].

Connect the coolant temperature sensor to the engine harness.

![[19400380.png]]

Connect an electronic Service Tool to the data link.

Place the Run/Stop switch in the Stop position.

Monitor the coolant temperature with the electronic Service Tool.

If the coolant temperature does not decrease to the current ambient air temperature, replace the coolant temperature sensor.

![[19800902.png]]

### Remove

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap or the coolant temperature sensor. Heated coolant spray or steam can cause personal injury.

Drain the cooling system. Refer to the specific engine platform troubleshooting and repair manual.

![[ra800qa.png]]

Lift up on the locking tab and pull the electrical connectors apart.

Remove the sensor.

![[19c00247.png]]

### Install

Make sure the new sensor has an o-ring installed.

Lubricate the o-ring with clean engine oil.

Install the new sensor into the engine. Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19c00247.png]]

Push the connectors together until they lock.

Fill the cooling system and operate the engine to check for leaks.

![[19c00248.png]]
