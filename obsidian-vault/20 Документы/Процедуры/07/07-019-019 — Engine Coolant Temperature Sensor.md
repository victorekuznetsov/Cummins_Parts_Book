---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "07-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2004-03-15"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `07-019-019`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-03-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-019.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

- Drain the cooling system. Refer to Procedure 008-018 in the Troubleshooting and Repair Manual, C Series Engines, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]].

![[ck800wa.png]]

### Initial Check

Cold Engine

Connect an electronic service tool to the vessel datalink.

Turn the keyswitch to the ON position.

Start the engine and let it idle.

![[19900524.png]]

Monitor the coolant temperature with the electronic service tool.

Compare the coolant temperature value with the water temperature gauge in the helm, or connect a temperature probe to the engine near the coolant temperature sensor and compare the reading on the service tool with the temperature probe reading.

If the coolant temperature on the electronic service tool is excessively higher than the water temperature, replace the coolant temperature sensor.

If the coolant temperature on the electronic service tool does **not** increase with the water temperature, replace the coolant temperature sensor.

![[19400068.png]]

Warm Engine

Remove the coolant temperature sensor as described in this procedure.

Connect the coolant temperature sensor to the engine harness.

![[19901360.png]]

Connect an electronic service tool to the vessel datalink.

Turn the keyswitch to the ON position.

Monitor the coolant temperature with the electronic service tool.

If the coolant temperature does **not** decrease to the current ambient air temperature, replace the coolant temperature sensor.

![[19900524.png]]

### Remove

Lift the locking tab and pull the electrical connectors apart.

Remove the sensor.

![[19901388.png]]

### Install

Make sure the new sensor has an o-ring installed.

Lubricate the o-ring with clean engine oil.

Install the new sensor into the engine.

Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19901389.png]]

Push the connectors together until they lock.

![[19901390.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

- Fill the cooling system. Refer to Procedure 008-018 in the Troubleshooting and Repair Manual, C Series Engines, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]].
- Operate the engine and check for leaks.

![[ck800wa.png]]
