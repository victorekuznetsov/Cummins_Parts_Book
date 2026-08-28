---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "87-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2010-08-02"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `87-019-019`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2010-08-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-019.pdf)

### Initial Check

Connect an electronic service tool to the vehicle datalink.

Turn the keyswitch to the ON position.

Start the engine and let it idle.

![[19900524.png]]

Monitor the coolant temperature with the electronic service tool.

Compare the cool temperature value with the water temperature gauge in the vehicle dash, or connect a temperature probe to the engine near the coolant temperature sensor and compare the reading on the service tool with the temperature probe reading.

If the coolant temperature on the electronic service tool is excessively higher than the water temperature, replace the coolant temperature sensor.

If the coolant temperature on the electronic service tool does **not** increase with the water temperature, replace the coolant temperature sensor.

![[19400068.png]]

Remove the coolant temperature sensor. [[87-019-019 — Engine Coolant Temperature Sensor|Refer to Procedure 019-019]].

Connect the coolant temperature sensor to the engine harness.

![[19400380.png]]

Connect an electronic service tool to the vehicle datalink.

Turn the keyswitch to the ON position.

Monitor the coolant temperature with the electronic service tool.

If the coolant temperature does **not** decrease to the present ambient air temperature, replace the coolant temperature sensor.

![[19900524.png]]

### Remove

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

Drain the cooling system.

Use the following procedure in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. [[57-008-018 — Cooling System|Refer to Procedure 008-018 in Section 8.]]

![[ra800qa.png]]

Lift up on the locking tab and pull the electrical connectors apart.

Remove the sensor.

![[19400380.png]]

### Install

Make sure the new sensor has an o-ring installed.

Lubricate the o-ring with clean engine oil.

Install the new sensor into the engine. Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19400381.png]]

Push the connectors together until they lock.

Fill the cooling system and operate the engine to check for leaks.

Use the following procedure in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]]. [[57-008-018 — Cooling System|Refer to Procedure 008-018 in Section 8.]]

![[19400382.png]]
