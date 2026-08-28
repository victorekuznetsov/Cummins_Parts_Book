---
aliases:
  - "Датчик частоты вращения двигателя (ESS)"
type: "Процедура"
doc: "98-019-042-tr"
title_en: "Engine Speed Sensor (ESS)"
title_ru: "Датчик частоты вращения двигателя (ESS)"
modified: "2009-01-12"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-042-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-042-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Speed Sensor (ESS)
**Датчик частоты вращения двигателя (ESS)**

> [!abstract] Процедура · `98-019-042-tr`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2009-01-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-042-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-042-tr.pdf)

### General Information

The engine speed sensor is located in the flywheel housing.

![[19801626.png]]

If the OEM has a single-output sensor installed and it is 3/4 x 16 thread, remove the single-output sensor from the flywheel housing.

![[19200417.png]]

### Remove

Disconnect the engine speed sensor connectors from the main engine harness.

Loosen the locknut.

Remove the engine speed sensor from the flywheel housing.

![[19801632.png]]

### Inspect for Reuse

Inspect the engine speed sensor for debris, cracked or chipped potting, extruded potting, and damage from contact with the ring gear.

If there is debris on the engine speed sensor, clean the sensor.

If the sensor is chipped, cracked, extruded, or damaged, replace the sensor.

![[19800369.png]]

### Install

Make sure a gear tooth is aligned with the hole in the flywheel housing.

Install the engine speed sensor into the hole until it touches the gear tooth.

> [!note] Note · Примечание
> If the engine speed sensor does **not** turn in with finger-pressure, check the flywheel housing hole threads and sensor threads for damage.

![[19801633.png]]

Turn the engine speed sensor out 1/2 to 3/4 of a turn **counterclockwise**.

![[19801634.png]]

> [!warning] CAUTION · Осторожно
> Overtightening the locknut can damage the sensor.

Tighten the locknut against the flywheel housing.

> [!tip] Момент затяжки · Torque Value
> 31 n•m [23 ft-lb]

Install both of the connectors. Make sure they lock into place.

The connectors can be interchanged with each other without changing the performance of the system.

![[19801635.png]]

### Resistance Check

Separate the two connectors. Lift the tab on the connectors and pull them apart.

> [!note] Note · Примечание
> When measuring the resistance values of the engine speed sensor coils, connect a mating connector with short lead extensions. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.

![[19801627.png]]

Use a multimeter to measure the resistance between the two pins of each connector on the engine speed sensor. The resistance value of one coil **must** be between 750 and 1100 ohms. The resistance value of the other coil **must** be 1100 to 1500 ohms. If the resistance is **not** correct, replace the engine speed sensor.

If the resistance value is correct, the engine speed sensor **must** still be checked for a short circuit to ground and a short circuit between coils.

The coil resistance values are measured at 25°C \[77°F\].

![[19801628.png]]

### Check for Short Circuit to Ground

To measure the resistance between pin B and the engine block ground:

- Attach one multimeter lead to the mating sensor connector lead. Touch the other multimeter lead to the engine block ground.
- Measure the resistance. The multimeter **must** show 100k ohms or greater, which is an open circuit.

If the circuit is **not** open, the engine speed sensor has failed.

Replace the engine speed sensor.

![[19801629.png]]

To measure the resistance between pin B of the other connector and engine block ground.

- Attach one multimeter lead to the other mating sensor connector lead. Touch the other multimeter lead to engine block ground.
- Measure the resistance. The multimeter **must** show 100k ohms or greater.

If the circuit is **not** open in either of these checks, the engine speed sensor has failed.

Replace the engine speed sensor.

![[19801630.png]]

### Check for Short Circuit from Pin to Pin

To check for a short circuit between the sensor coils:

- Attach one multimeter lead to pin B of either mating sensor connector lead.
- Attach the other multimeter lead to pin B of the other mating sensor connector lead.
- Measure the resistance.

The multimeter **must** show 100k ohms or greater.

If the circuit is **not** open, replace the engine speed sensor.

If the values are correct for all engine speed sensor checks, the sensor is good.

![[19801631.png]]
