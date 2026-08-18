---
aliases:
  - "Нагнетательный узел топливного насоса"
type: "Процедура"
doc: "102-005-232"
title_en: "Fuel Pump Pressurizing Assembly"
title_ru: "Нагнетательный узел топливного насоса"
modified: "2020-05-12"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4021528"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/102/102-005-232.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/102-005-232.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/102"
---

# Fuel Pump Pressurizing Assembly
**Нагнетательный узел топливного насоса**

> [!abstract] Процедура · `102-005-232`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4021528 — K38, K50, QSK38, and QSK50 Service Manual|4021528]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2020-05-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/102/102-005-232.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/102-005-232.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Depending on the circumstance, diesel fuel is flammable. When inspecting or performing service or repairs on the fuel system, to reduce the possibility of fire and resulting severe personal injury, death or property damage, never smoke or allow sparks or flames (such as pilot lights, arcing equipment, or welding equipment) in the work area.

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacture's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause bodily injury.

> [!warning] CAUTION · Осторожно
> A very small amount of dirt and debris can be very harmful to the fuel pump. Extra care is required to keep the fuel connections clean during removal and installation. Connections must be covered immediately to keep them clean when components are removed from the fuel pump.

- Disconnect the battery cables. See the equipment manufacturer service information.
- Clean the fuel pump and the surrounding area. Dry with compressed air.
- Dry with compressed air.

![[ck800wa.png]]

### Remove

Disconnect the wiring harness connector (1) from the fuel pump pressurizing assembly.

Remove the three inner capscrews (2) and the fuel pump pressurizing assembly.

Discard the o-rings.

![[05600383.png]]

> [!note] Note · Примечание
> Remove **only** the adapter plate, if necessary. If removing, mark the orientation of the plate so that it can be installed in the same orientation. This will make sure that the wiring harness connector will be positioned in the correct location when the fuel pump pressurizing assembly is installed.

To remove the adapter plate, remove the four outer capscrews (1) and pull out the adapter plate.

Discard the o-rings.

![[05600384.png]]

### Inspect for Reuse

Inspect the fuel pump pressurizing assembly for damage.

Replace, the assembly if damage is found.

Check the resistance of the fuel pump pressuring assembly. Use the following procedure in the Troubleshooting and Repair Manual Electronic Control System, QSK50 and QSK60 Modular Common Rail System Series Engines, Bulletin 4021533. [[99-019-360 — Resistance Measurement Using a Multimeter|Refer to Procedure 019-360 in Section 19.]]

![[05600222.png]]

### Resistance Check

Disconnect the engine wiring harness from the fuel pump pressurizing assembly.

Measure the resistance from the SIGNAL pin and all other pins in the connector. The multimeter **must** measure between 1 and 10 ohms or above 100k ohms. If the resistance values are within specifications, the connector **must** still be checked for a short to ground.

Measure the resistance from the SIGNAL pin and ground. The multimeter **must** measure between 1 and 10 ohms.

If any of the preceding checks fail, check each harness connected in series to determine which one contains the open circuit. Repair or replace the damaged section of the engine harness. If no harness issues are found, replace the fuel pump pressurizing assembly.

![[05400247.png]]

### Install

> [!note] Note · Примечание
> This step block **only** applies if the adapter plate has been removed. The adapter plate should **only** be removed if necessary.

Install the adapter plate onto the fuel pump and the four outer capscrews (1), using new o-rings. Make sure that the adapter plate is oriented so that when the fuel pump pressurizing assembly is installed, the wiring harness connector will be in the correct location.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[05600384.png]]

Install the fuel pump pressurizing assembly with new o-rings and the three inner capscrews (2).

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> Fuel pump pressurizing capscrews 6.5 n•m [58 in-lb]

Connect the wiring harness to the fuel pump pressurizing assembly (1).

![[05600383.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See the equipment manufacturer service information.
- Operate the engine and check for leaks.

![[ck800wa.png]]
