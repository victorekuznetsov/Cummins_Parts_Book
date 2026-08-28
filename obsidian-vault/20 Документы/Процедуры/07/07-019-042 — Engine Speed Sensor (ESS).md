---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "07-019-042"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2003-12-09"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-042.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-042.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `07-019-042`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-042.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-019-042.pdf)

### Remove

Disconnect the engine speed sensor connectors from the engine harness.

![[19a00245.png]]

Loosen the capscrew.

Remove the engine speed sensor from the flywheel housing.

![[19a00246.png]]

### Inspect for Reuse

Inspect the engine speed sensor for debris, cracked or chipped potting, extruded potting, and damage from contact with the flywheel.

If there is debris on the engine speed sensor, clean the sensor.

If the sensor is chipped, cracked, extruded, or damaged, replace it with a new one.

![[19800369.png]]

### Install

Check that the engine speed sensor is directly above a flywheel ring gear tooth.

Install the engine speed sensor until it contacts the flywheel.

Back the sensor off until the lock hole is aligned.

Install the lock capscrew and tighten.

> [!tip] Момент затяжки · Torque Value
> 7 n•m [62 in-lb]

![[00a00106.png]]

Connect the sensor to the sensor harness.

Push the connectors together until they lock.

![[19a00245.png]]

### Resistance Check

Disconnect the sensor connector from the engine harness.

Lift the tab and pull the connector apart.

Install a mating connector with short test leads on the sensor connector.

> [!note] Note · Примечание
> The purpose of installing a mating connector is to allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.

![[19a00245.png]]

Use a multimeter to measure the resistance from the engine speed signal primary pin to the engine speed return primary pin.

Measure the resistance from the engine speed +5-VDC primary pin to the engine speed return pin.

The multimeter **must** measure between 1000 and 2000 ohms.

If both resistance values are within specifications, the sensor **must** still be checked for short circuit to ground.

If any of the preceding checks fail, replace the engine speed sensor.

![[19901401.png]]

### Check for Short Circuit to Ground

Measure the resistance from the engine speed +5-VDC primary pin to the engine block.

The multimeter **must** show an open circuit (10M ohms or more).

> [!note] Note · Примечание
> The open circuit specification (10M ohms) for the engine speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the engine speed sensor.

![[19901403.png]]

Measure the resistance from the engine speed signal primary pin to the engine block.

The multimeter **must** show an open circuit (100k ohms or more).

If either of the preceding checks fail, replace the engine speed sensor.

![[19901404.png]]

### Check for Short Circuit from Pin to Pin

Measure the resistance from the engine speed +5-VDC primary pin to the engine speed return pin.

The multimeter **must** show an open circuit (100k ohms or more).

If any of the previous resistance checks are **not** within specifications, the sensor has failed.

Replace the sensor.

![[19901405.png]]
