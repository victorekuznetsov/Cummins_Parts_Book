---
type: "Процедура"
doc: "40-005-069"
title_en: "Cold Start Timing Advance System Temperature Switch"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-069.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-069.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Cold Start Timing Advance System Temperature Switch

> [!abstract] Процедура · `40-005-069`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-069.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-069.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries.

![[13900050.png]]

### Remove

Wax-Motor Style

Remove the temperature switch.

![[cs9swma.png]]

> [!warning] CAUTION · Осторожно
> The switches are not interchangeable. White smoke will be present if the wrong temperature switch is used.

Notes:

1. The wax motor KSB (used on pre-1991 engines) uses a 71°C \[160°F\] normally open coolant temperature switch, Cummins Part Number 3915945.
2. The electrical solenoid-style KSB (used on '91 models and newer) uses a 32°C \[90°F\] normally closed intake manifold temperature switch, Cummins Part Number 3921642.

![[cs900gv.png]]

Electrical Solenoid Style

Remove the temperature switch from the intake manifold.

![[cs9swmc.png]]

> [!warning] CAUTION · Осторожно
> The switches are not interchangeable. White smoke will be present if the wrong temperature switch is used.

Check the part number to be sure the correct temperature switch is used.

> [!note] Note · Примечание
> The electrical solenoid-style KSB (used on 1991 models and newer) uses a 32°C \[90°F\] normally closed intake manifold temperature switch, Part Number 3921642.

![[cs900gv.png]]

### Test

Wax-Motor Style

The operation of the temperature switch for the wax motor style KSB can be checked by connecting a multimeter to the switch, placing the switch in water, and then heating the water to 71°C \[160°F\].

Connect the multimeter to the two pins on the left when viewed with the plastic tang on top.

![[cs9swvb.png]]

Check the water temperature with a thermometer.

The multimeter **must** indicate an open circuit below 71°C \[160°F\] and a closed circuit above 71°C \[160°F\].

Replace the switch, if necessary.

![[cs9swvc.png]]

Electrical Solenoid Style

Although the electrical solenoid-style KSB uses an intake manifold temperature switch, the operation of the switch can be checked by connecting a multimeter to the switch, placing the switch in ice water, and then heating the water to 32°C \[90°F\].

Connect the multimeter to the two outside pins of the temperature switch.

![[19901094.png]]

Check the water temperature with a thermometer.

The multimeter should indicate a closed circuit below 32°C \[90°F\] and an open circuit above 32°C \[90°F\].

Replace the switch, if necessary.

![[cs9swvc.png]]

### Install

Electrical Solenoid Style

Install the original pressure relief valve or a replacement into the KSB housing.

> [!tip] Момент затяжки · Torque Value
> 13 n•m [115 in-lb]

![[05900101.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries
- Operate the engine and check for leaks.

![[13900050.png]]
