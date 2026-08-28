---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "19-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `19-019-019`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-019.pdf)

### Initial Check

**Cold Engine**

Connect an electronic service tool to the vehicle datalink.

Turn the keyswitch to the ON position.

Start the engine and let it idle.

![[19400357.png]]

Monitor the coolant temperature with the electronic service tool.

Compare the cool temperature value with the water temperature gauge in the vehicle dash, or connect a temperature probe to the engine near the coolant temperature sensor and compare the reading on the service tool with the temperature probe reading.

If the coolant temperature on the electronic service tool is excessively higher than the water temperature, replace the coolant temperature sensor.

If the coolant temperature on the electronic service tool does **not** increase with the water temperature, replace the coolant temperature sensor.

![[19400068.png]]

**Warm Engine**

Remove the coolant temperature sensor.

Connect the coolant temperature sensor to the engine harness.

![[19400380.png]]

Connect an electronic service tool to the vehicle datalink.

Turn the keyswitch to the ON position.

Monitor the coolant temperature with the electronic service tool.

If the coolant temperature does **not** decrease to the current ambient air temperature, replace the coolant temperature sensor.

![[19400357.png]]

### Remove

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the coolant system pressure cap. Heated coolant spray or steam can cause personal injury.

Drain the cooling system. Refer to the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098, the Troubleshooting and Repair Manual, QSK45 and QSK60 Series Engines, Bulletin 3666261, or the Troubleshooting and Repair Manual, QSK78 Series Engines, Bulletin 3666727.

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

![[19400382.png]]
