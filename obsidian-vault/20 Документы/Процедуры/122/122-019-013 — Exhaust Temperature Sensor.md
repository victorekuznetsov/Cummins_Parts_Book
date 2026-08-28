---
aliases:
  - "Датчик температуры отработавших газов"
type: "Процедура"
doc: "122-019-013"
title_en: "Exhaust Temperature Sensor"
title_ru: "Датчик температуры отработавших газов"
modified: "2021-07-28"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-013.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-013.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Exhaust Temperature Sensor
**Датчик температуры отработавших газов**

> [!abstract] Процедура · `122-019-013`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2021-07-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-013.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-013.pdf)

### General Information

The Exhaust Gas Temperature Sensors (EGTS) are located on the exhaust manifold connection on the QSK38 and QSK50 engines. The Exhaust Gas Temperature Sensors (EGTS) are located on the side of the cylinder head on the QSK60 engines.

This engine can use either a full engine set of thermistor or thermocouple EGTS. Note that thermistor and thermocouple EGTS should **not** be mixed and will **not** work properly on a given engine.

Engines that use thermistor EGTS do **not** require the signal converter boxes as the temperature is measured directly by the Engine Control Module (ECM). For engines with thermocouple EGTS, the temperature is measured by using converter boxes which communicate with the ECMs.

After being received by the ECM, each individual measurement is compared to a global warning, serious and critical threshold to detect over or under temperature conditions.

In addition, an average is taken of all exhaust port temperatures, and the deviation of each cylinder temperature from average is calculated. If the deviation from the average is too great (either too high or too low), then an error is set.

![[00r01593.png]]

QSK38, QSK50 Thermistor EGTS

![[00r01622.png]]

QSK50 Thermocouple EGTS

![[00r01618.png]]

QSK60 Thermistor EGTS

![[00r01619.png]]

QSK60 Thermocouple EGTS

### Remove

Thermistor

**Q38Thermistor**

Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).

![[00r01594.png]]

Remove the two wire clamp capscrews.

Loosen and remove the exhaust temperature sensor.

![[00r01595.png]]

**Q50 Thermistor**

Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).

![[00r01594.png]]

Remove the two wire clamp capscrews.

Loosen and remove the exhaust temperature sensor.

![[00r01595.png]]

**Q60 Thermistor**

Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).

![[00r01620.png]]

Remove the wire clamp capscrews.

Loosen and remove the exhaust temperature sensor.

![[00r01621.png]]

Thermocouple

**Q50 Thermocouple**

There are four different EGTS part numbers with different bend profiles. Each of the four parts are used on specific cylinder locations. Prior to removing an EGTS from a cylinder location, label the cylinder location on the EGTS.

Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).

![[00r01623.png]]

Remove the wire clamp capscrew.

Remove wear sleeve and two-piece bracket.

![[00r01624.png]]

Loosen and remove the exhaust temperature sensor.

![[00r01625.png]]

**Q60 Thermocouple**

Disconnect the connector (1) of the exhaust temperature sensor from the injector and exhaust temperature sensor harness (2).

![[00r01620.png]]

Remove the wire clamp capscrews.

Loosen and remove the exhaust temperature sensor.

![[00r01632.png]]

### Clean and Inspect for Reuse

**Q38**, **Q50, and Q60 Thermistors and Thermocouples**

Clean the exhaust gas temperature sensor. Use a clean, lint-free cloth.

Inspect the sensor.

Replace the sensor if:

- Sensor wire damaged or abraded
- Threads damaged or corroded
- Sensor tip bent or cracked.

Inspect the brackets, washers, and capscrews.

Replace the component if:

- Bent
- Cracked.

![[00r01616.png]]

### Install

Thermistor

**Q38and Q50Thermistors**

Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.

Tighten the nut that secures the exhaust temperature sensor.

> [!tip] Момент затяжки · Torque Value
> 44 n•m [32 ft-lb]

![[00r01617.png]]

Install the two wire clamp capscrews.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

![[00r01595.png]]

Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.

![[00r01628.png]]

**Q60 Thermistor**

Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.

Tighten the nut that secures the exhaust temperature sensor.

> [!tip] Момент затяжки · Torque Value
> 44 n•m [32 ft-lb]

![[00r01629.png]]

Install the wire clamp capscrews.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

![[00r01630.png]]

Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.

![[00r01631.png]]

Thermocouple

**Q50 Thermocouple**

Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.

Tighten the nut that secures the exhaust temperature sensor.

> [!tip] Момент затяжки · Torque Value
> 44 n•m [32 ft-lb]

![[00r01626.png]]

Install wear sleeve and two-piece bracket

Install the wire clamp capscrew.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

![[00r01624.png]]

Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.

![[00r01627.png]]

**Q60 Thermocouple**

Apply non-lead based anti-seize compound, Part Number 3824732, or equivalent, to the exhaust temperature sensor threads and install the exhaust temperature sensor.

Tighten the nut that secures the exhaust temperature sensor.

> [!tip] Момент затяжки · Torque Value
> 44 n•m [32 ft-lb]

![[00r01633.png]]

Install the wire clamp capscrews.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

![[00r01634.png]]

Connect the exhaust temperature sensor connector in the harness, pushing it together until it clicks.

![[00r01635.png]]
