---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "60-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2009-06-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `60-019-042`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2009-06-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-042.pdf)

### Remove

Disconnect the engine speed sensor connectors from the engine harness.

![[19a00245.png]]

Loosen the capscrew.

Remove the engine speed sensor from the flywheel housing.

![[19a00246.png]]

### Clean and Inspect for Reuse

Clean any debris on the engine speed sensor.

Inspect the engine speed sensor for debris, cracks, or chipped potting, extruded potting, and damage from contact with the flywheel.

If the engine speed sensor is chipped, cracked, extruded, or otherwise damaged, the sensor **must** be replaced.

![[19800369.png]]

### Install

Check that the engine speed sensor is directly above a flywheel ring gear tooth.

Install the engine speed sensor by turning it **clockwise** until it contacts the flywheel.

Back out the sensor by turning it **counterclockwise** 180 degrees.

Continue turning the engine speed sensor **counterclockwise** until the lock hole is aligned.

Install the lock capscrew and tighten.

> [!tip] Момент затяжки · Torque Value
> 7 n•m [62 in-lb]

![[00a00106.png]]

> [!warning] CAUTION · Осторожно
> Only use lubricant Lubriplate™ DS-ES, Part Number 3822934, recommended by Cummins Inc. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.

Apply a small amount of lubricant to the connector terminals. Before installing, fill the entire connector cavity with lubricant.

![[cel29.png]]

Connect the sensor to the sensor harness. Push the connectors together until they lock.

![[19a00245.png]]

### Resistance Check

Separate the three-way connector. Lift the tab and pull the connector apart. Install a mating connector with short test leads on the sensor connector.

> [!note] Note · Примечание
> The purpose of installing a mating connector is to allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.

![[19a00245.png]]

Use a multimeter to measure the resistance from pin C to pin B.

The multimeter **must** show between 1000 and 2000 ohms.

![[19a00268.png]]

Use a multimeter to measure the resistance from pin A to pin B.

The multimeter **must** show between 1000 and 2000 ohms. If both resistance values are within the specifications, the sensor **must** still be checked for short circuit to ground.

If any of the resistance checks are **not** within specifications, replace the engine speed sensor.

![[19a00269.png]]

### Check for Short Circuit to Ground

Measure the resistance from pin A to the engine block ground. The multimeter **must** show an open circuit (10M ohms or more).

> [!note] Note · Примечание
> The open circuit specification (10M ohms) for the engine speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the engine speed sensor.

![[19a00270.png]]

Measure the resistance from pin C to the engine block ground. The multimeter **must** show an open circuit (100k ohms or more).

If any of the resistance checks are **not** within specifications, replace the engine speed sensor.

![[19a00271.png]]

### Check for Short Circuit from Pin to Pin

Measure the resistance from pin A to pin C. The multimeter **must** show an open circuit (100k ohms or more). If any of the resistance checks are **not** within specifications, the sensor is damaged.

Replace the engine speed sensor.

![[19a00272.png]]
