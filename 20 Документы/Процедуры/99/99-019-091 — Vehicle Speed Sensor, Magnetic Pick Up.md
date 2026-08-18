---
aliases:
  - "Индуктивный датчик скорости машины"
type: "Процедура"
doc: "99-019-091"
title_en: "Vehicle Speed Sensor, Magnetic Pick Up"
title_ru: "Индуктивный датчик скорости машины"
modified: "2008-05-30"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-091.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-091.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Vehicle Speed Sensor, Magnetic Pick Up
**Индуктивный датчик скорости машины**

> [!abstract] Процедура · `99-019-091`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2008-05-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-091.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-091.pdf)

### General Information

The vehicle speed sensor (VSS) senses the speed of the output shaft of the transmission. The vehicle's road speed is computed from this data by the electronic control module (ECM). The ECM uses programmed gearing and tire size data to compute the road speed.

![[19c01291.png]]

The vehicle speed sensor is located in the rear of the transmission housing.

The vehicle speed sensor has two coils. One coil is connected to the ECM and the other coil is connected to the vehicle speedometer, or some other vehicle device.

> [!note] Note · Примечание
> Vehicle speed sensor design varies with the application. Refer to the original equipment manufacturer (OEM) troubleshooting and repair manual to understand which type of vehicle speed sensor is being used in a given location.

![[19200262.png]]

### Remove

Disconnect the engine harness from the vehicle speed sensor.

Loosen the locknut. Turn the vehicle speed sensor out of the transmission housing.

![[19900797.png]]

### Inspect for Reuse

Inspect the tip of the vehicle speed sensor for dirt, debris, or physical damage (cracked potting, and so forth).

Clean the tip if dirty, or replace the vehicle speed sensor if damaged.

![[19900798.png]]

### Install

> [!warning] CAUTION · Осторожно
> Make sure a gear tooth is aligned with the hole in the housing. Install the vehicle speed sensor into the hole until it touches the gear tooth.

> [!note] Note · Примечание
> If the vehicle speed sensor does **not** turn in with finger pressure, check the transmission hole threads and the sensor threads for dirt or damage.

![[19900799.png]]

Turn the vehicle speed sensor out 1/2 to 3/4 of a turn.

![[19900800.png]]

Tighten the locknut against the transmission housing.

Torque the sensor according to the OEM or transmission specifications. Refer to the OEM troubleshooting and repair manual for detailed procedures.

Install both of the connectors together until connectors "snap" into position. The connectors can be interchanged with each other without changing the performance of the system.

![[19900801.png]]

### Resistance Check

Lift the tab on the connectors and pull them apart.

> [!note] Note · Примечание
> When measuring the resistance value of the vehicle speed sensor coils, use two female test leads. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.

![[19900802.png]]

Use a multimeter to measure the resistance between the two pins of each connector on the vehicle speed sensor. Refer to the OEM troubleshooting and repair manual for detailed procedures. If the resistance is **not** correct, replace the vehicle speed sensor. If the resistance value is correct, the vehicle speed sensor **must** still be checked for a short circuit to ground and a short circuit between coils.

![[19900803.png]]

### Check for Short Circuit to Ground

Measure the resistance between the magnetic vehicle speed sensor signal negative (-) pin of one of the connectors and the engine block. Refer to the OEM troubleshooting and repair manual for detailed procedures.

![[19200262.png]]

Measure the resistance between the magnetic vehicle speed sensor signal negative (-) pin of the other connector and the engine block. Refer to the OEM troubleshooting and repair manual for detailed procedures.

![[19200263.png]]

Check for a short circuit between coils

Use a multimeter to measure the resistance between the magnetic vehicle speed sensor signal negative (-) pin of one of the connectors and the magnetic vehicle speed sensor signal (-) pin of the other connector. Refer to the OEM troubleshooting and repair manual for detailed procedures.

![[19200264.png]]
