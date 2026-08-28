---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "87-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
modified: "2004-02-06"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `87-019-059`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-02-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-059.pdf)

### Remove

Lift up on the locking tab and pull the electrical connectors apart.

![[19a00247.png]]

Remove the sensor from the engine.

![[19a00248.png]]

### Install

Make sure the new sensor has an o-ring around the surface where it seals against the engine block.

Lubricate the o-ring with clean engine oil.

![[19a00250.png]]

Install the sensor in the engine block.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19a00248.png]]

> [!warning] CAUTION · Осторожно
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.

Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire connector cavity lubricant.

![[cel29.png]]

Push connectors together until they lock.

![[19a00247.png]]

### Resistance Check

Lift up on the locking tab and pull the electrical connectors apart.

![[19a00247.png]]

Use a multimeter to measure the resistance between the two pins of the intake air temperature sensor. The resistance **must** be 600 ohms to 36k ohms\*. If the resistance is **not** correct, replace the sensor. If the resistance is correct, the sensor **must** still be checked for a short circuit to ground.

\* The resistance value is temperature-dependent as follows:

| Temp C° | Temp F° | Acceptable Resistance Range (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

![[19a00251.png]]

### Check for Short Circuit to Ground

Measure the resistance from one of the pins of the intake air temperature sensor to the engine block.

The multimeter **must** show an open circuit (more than 100k ohms).

If the circuit is **not** open, replace the sensor.

![[19a00252.png]]
