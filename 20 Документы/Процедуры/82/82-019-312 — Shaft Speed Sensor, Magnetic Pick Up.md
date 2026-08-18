---
aliases:
  - "Индуктивный датчик частоты вращения вала"
type: "Процедура"
doc: "82-019-312"
title_en: "Shaft Speed Sensor, Magnetic Pick Up"
title_ru: "Индуктивный датчик частоты вращения вала"
modified: "2002-06-03"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-312.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-312.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Shaft Speed Sensor, Magnetic Pick Up
**Индуктивный датчик частоты вращения вала**

> [!abstract] Процедура · `82-019-312`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-312.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-312.pdf)

### General Information

The shaft speed sensor senses the speed of the shaft by counting gear teeth. The ECM then calculates the shaft speed based on the number of teeth per revolution. The auxiliary governor can control the engine fueling to maintain a constant shaft speed.

![[19200261.png]]

The shaft speed sensor has two coils. One coil is connected to the ECM and the other coil may be connected to some other vehicle device.

> [!note] Note · Примечание
> Sensor design varies with the application. Refer to the equipment manufacturer's manual to understand which type of shaft speed sensor is being used in a given location.

> [!note] Note · Примечание
> Some applications may use **only** one connector.

![[19200262.png]]

### Remove

Disconnect the engine harness from the shaft speed sensor.

Loosen the locknut. Turn the shaft speed sensor out of the housing.

![[19900797.png]]

### Inspect for Reuse

Inspect the tip of the shaft speed sensor for dirt, debris, or physical damage (cracked potting, and so forth).

Clean the tip if it is dirty, or replace the shaft speed sensor if it is damaged.

![[19900798.png]]

### Install

> [!warning] CAUTION · Осторожно
> Make sure a gear tooth is aligned with the hole in the housing.

Install the shaft speed sensor into the hole until it touches the gear tooth.

> [!note] Note · Примечание
> If the shaft speed sensor does **not** turn in with finger pressure, check the housing hole threads and the sensor threads for dirt or damage.

![[19900799.png]]

Turn the shaft speed sensor out 1/2 to 3/4 of a turn.

![[19900800.png]]

Tighten the locknut against the housing.

> [!tip] Момент затяжки · Torque Value
> 47 n•m [35 ft-lb]

Install both of the connectors together until connectors "snap" into position. The connectors can be interchanged with each other without changing the performance of the system.

> [!note] Note · Примечание
> Some applications may use **only** one connector.

![[19900801.png]]

### Resistance Check

Lift the tab on the connectors and pull them apart.

> [!note] Note · Примечание
> When measuring the resistance value of the shaft speed sensor coils, use two female test leads, Part No. 3822996. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.

![[19900802.png]]

Use a multimeter to measure the resistance between the two pins of each connector on the shaft speed sensor. The resistance value of one coil **must** be 750 to 1100 ohms. The resistance value of the other coil **must** be 1100 to 1500 ohms (although the resistance values are different, the coils are interchangeable).

If the resistance is **not** correct, replace the shaft speed sensor. If the resistance value is correct, the shaft speed sensor **must** still be checked for a short circuit to ground and a short circuit between coils.

![[19900803.png]]

### Check for Short Circuit to Ground

Measure the resistance between pin B of one of the connectors and the engine block. The multimeter **must** show an open circuit (100k ohms or more).

> [!note] Note · Примечание
> The open circuit specification (100k ohms or more) for the shaft speed sensor is higher than the open circuit specification used throughout the manual due to the sensitivity of the shaft speed sensor signal.

![[19200262.png]]

Measure the resistance between pin B of the other connector and the engine block. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open (100k ohms or more) in either of these checks, the shaft speed sensor has failed.

Replace the shaft speed sensor.

![[19200263.png]]

**Check for Short Circuit between Coils**

Use a multimeter to measure the resistance between pin B of one of the connectors and pin B of the other connector. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, replace the shaft speed sensor.

![[19200264.png]]
