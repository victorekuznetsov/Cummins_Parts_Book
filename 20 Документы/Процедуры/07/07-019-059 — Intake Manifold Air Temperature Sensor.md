---
aliases:
  - "Датчик температуры воздуха во впускном коллекторе"
type: "Процедура"
doc: "07-019-059"
title_en: "Intake Manifold Air Temperature Sensor"
title_ru: "Датчик температуры воздуха во впускном коллекторе"
modified: "2003-12-01"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 9
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-059.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-059.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Intake Manifold Air Temperature Sensor
**Датчик температуры воздуха во впускном коллекторе**

> [!abstract] Процедура · `07-019-059`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-059.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-059.pdf)

### Remove

Lift the locking tab and pull the electrical connectors apart.

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

Apply a small amount of lubricant to the connector terminals.

Before installing, fill the entire connector cavity with lubricant.

![[cdl29.png]]

Push the connectors together until they lock.

![[19a00247.png]]

### Resistance Check

Lift the locking tab and pull the electrical connectors apart.

![[19a00247.png]]

Use a multimeter to measure the resistance between the two pins of the intake air temperature sensor.

The resistance **must** be 600 ohms to 36k ohms\*.

If the resistance is **not** within specifications, replace the sensor.

If the resistance is within specifications, the sensor **must** still be checked for a short to ground.

\* The resistance value is temperature-dependent as follows:

| Temperature | Acceptable Resistance Range |  |
|---|---|---|
| °C | °F | (ohms) |
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

> [!missing]- Иллюстрация `19901411.png` не извлечена — смотрите PDF-оригинал документа

### Check for Short Circuit to Ground

Measure the resistance from one of the pins of the intake air temperature sensor to the engine block.

The multimeter **must** show an open circuit (more than 100k ohms).

If the circuit is **not** open, replace the sensor.

> [!missing]- Иллюстрация `19901412.png` не извлечена — смотрите PDF-оригинал документа
