---
type: "Процедура"
doc: "89-010-072-tr"
title_en: "Air Intake Manifold Heater"
modified: "2016-11-04"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-010-072-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-010-072-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
---

# Air Intake Manifold Heater

> [!abstract] Процедура · `89-010-072-tr`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2016-11-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-010-072-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-010-072-tr.pdf)

### General Information

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury and property damage, never use starting fluid if the grid heater option is used. Starting fluid, which contains ether, can cause an explosion.

The intake air grid heaters are controlled by the engine control module (ECM), and are used to warm the intake air during cold starting conditions.

The battery power for the intake air grid heaters is supplied by the original equipment manufacturer (OEM). The system has a total amperage draw capacity of approximately 220 amperes when operational.

> [!note] Note · Примечание
> For engines operating in normal conditions, the grid heater is designed to last the life of the engine. For applications which operate in cold climates and have multiple starts per day, the grid heater should be inspected every 6000 hours.

![[10a00121.png]]

There are two intake air grid heaters (1). They are located at the inlet of each intake manifold. Each grid heater has its own solenoid. Reference the QSK23 Industrial Wiring Diagram, Bulletin 4021394.

The intake air grid heaters function as a resistive heater. On one end a voltage or amperage is applied, and the other end is tied to the block ground.

The intake air grid heaters can stop functioning if they have a faulty ground, loss of battery supply, faulty solenoid, or the solenoid stops receiving the ECM command.

![[10r00004.png]]

The ECM uses intake manifold air temperature as the input to determine if the grid heaters should be activated.

The grid heaters are turned on for 30 seconds after key ON if the intake manifold temperature is below 0° C \[32° F\]. Power is removed if the engine starts cranking and the engine speed exceeds 50 rpm.

![[10a00123.png]]

### Remove

Disconnect air intake heater harness.

Remove the air crossover connections.

![[10h00001.png]]

### Clean and Inspect for Reuse

Inspect the air intake manifold heater for damage. If the heater shows signs of cracks or is broken, it **must** be replaced.

![[10d00624.png]]

### Install

Install the air crossover connections.

> [!tip] Момент затяжки · Torque Value
> Capscrew (1): 30 n•m [22 ft-lb]

> [!tip] Момент затяжки · Torque Value
> All Other Capscrews: 66 n•m [49 ft-lb]

![[10h00002.png]]

Connect the air intake heater harness.

![[10a00121.png]]
