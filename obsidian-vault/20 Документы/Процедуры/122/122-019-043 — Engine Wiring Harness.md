---
aliases:
  - "Жгут проводов двигателя"
type: "Процедура"
doc: "122-019-043"
title_en: "Engine Wiring Harness"
title_ru: "Жгут проводов двигателя"
modified: "2022-07-06"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
  - "QSK60"
manuals:
  - "4021530"
  - "4022102"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-043.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-043.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "двигатель/QSK60"
  - "группа/122"
---

# Engine Wiring Harness
**Жгут проводов двигателя**

> [!abstract] Процедура · `122-019-043`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60, QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]], [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2022-07-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-043.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-043.pdf)

### General Information

The engine uses multiple wiring harnesses to control the engine and some of the vehicle operations. Shown are the engine control module (ECM) ports for the following connectors:

- 4-pin original equipment manufacturer (OEM) power supply harness connector
- Engine port harness connector
- 60-pin harness connector.

![[19803860.png]]

The engine has two main harness branches, a left bank main harness and a right bank main harness.

The left bank main harness also has a front extension harness, engine coolant level sensor wiring harness, water in fuel sensor extension harness and a lubricating oil extension harness. The left bank injector harness and the exhaust gas temperature (EGT) harness also connects to the left bank main harness.

The right bank injector harness and right bank EGT extension harness connects to the right bank main harness.

There is an extension harness that joins the right bank and left bank main harnesses at the rear of the engine.

The harness can be replaced in sections, if necessary.

For the specific QSK60 MCRS Industrial Exhaust Gas Temperature Sensor (EGTS), Injector and Mounting Bracket procedure, see QSK60 Modular Common Rail System (MCRS) Harness Installation Instruction, Bulletin 5414606.

![[19600926.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. Refer to equipment manufacturer service information.

![[ck800wa.png]]

### Remove

Disconnect the engine harness from the sensors and switches.

- Engine crankshaft speed/position sensor.
- Engine camshaft speed/position sensor.
- Intake manifold 1 temperature sensor.
- Intake manifold 1 pressure sensor.
- Intake manifold 2 temperature sensor.
- Intake manifold 2 pressure sensor.
- Intake manifold 3 temperature sensor.
- Intake manifold 3 pressure sensor.
- Intake manifold 4 temperature sensor.
- Intake manifold 4 pressure sensor.
- Engine coolant temperature 1 sensor.
- Engine coolant level sensor wiring harness.
- Coolant pressure sensor.
- Engine oil temperature sensor 1.
- Engine oil rifle pressure 1 sensor.
- Barometric pressure sensor.
- Engine oil burn valve solenoid driver.
- Injector metering rail 1 pressure sensor.
- Fuel delivery pressure sensor.
- Engine fuel temperature sensor 1.
- Fuel pump pressurizing assembly.
- Injector solenoid drive (each cylinder).
- Water in fuel sensor extension wiring harness.
- Crankcase pressure sensor.
- Exhaust gas temperature sensor (each cylinder).
- Pre-oil filter pressure sensor.
- Post-oil filter pressure sensor.
- Turbocharger 1 speed sensor.
- Plunger switch.
- Air shutoff valve solenoid.

![[19400386.png]]

Note the engine harness routing and the location of the wire ties and mounting clips holding the engine harness, before removal.

Disconnect the engine harness connectors from the ECM.

![[19600927.png]]

### Inspect for Reuse

Replace or repair the engine harness if there is an open circuit or a short circuit found under the protective covering of the harness body.

![[19400386.png]]

### Install

> [!warning] CAUTION · Осторожно
> Do not overtighten, as connector damage can occur.

Connect the engine harness to the ECM.

Use an inch-pound torque wrench, Part Number 3376592, with 4 mm \[5/32 in\] hex head adapter to tighten the connector jackscrew.

> [!tip] Момент затяжки · Torque Value
> 2.8 n•m [25 in-lb]

Install the harness clamps that hold the engine harness to the block.

![[19600927.png]]

Connect the sensors and switches to the engine harness.

![[19803861.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. Refer to equipment manufacturer service information.

![[ck800wa.png]]
