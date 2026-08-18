---
aliases:
  - "Топливная система с электронным управлением"
type: "Процедура"
doc: "60-101-007"
title_en: "Electronic Controlled Fuel System"
title_ru: "Топливная система с электронным управлением"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-101-007.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-101-007.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Electronic Controlled Fuel System
**Топливная система с электронным управлением**

> [!abstract] Процедура · `60-101-007`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section F — Familiarization
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-101-007.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-101-007.pdf)

### General Information

The generator-drive control system is an electronic control system that is comprised of three ECMs.

- ECM 1 and ECM 3 are CM552 models. The CM552 monitors and controls fueling.
- ECM 2 is a CM850 model. It monitors and controls all other engine functions.

The ECMs share some monitoring functions that are addressed in Section TF.

![[19a00825.png]]

### Diagnostic Fault Codes

The QST30 electronic control system can record certain fault conditions. These conditions can be displayed by connecting an electronic service tool.

There are two data link ports for communication with the ECMs.

The data link ports are located on the left hand side of the engine. The forward data link port is for communication with the CM552 ECMs.

The rear port is for communication with the CM850 ECM and **must** be connected first.

![[19a00837.png]]

There are two types of fault codes:

- Engine electronic fuel system fault codes
- Engine protection system fault codes

All fault codes recorded will either be active (fault code is active on engine) or inactive (fault code was active at one time, but **not** at this moment).

Active and inactive fault codes can be viewed with INSITE™ electronic service tool.

![[19800902.png]]

The engine protection system records separate fault codes when an out-of-range condition is found for any of the sensors in the engine protection system.

The following are engine protection system out-of-range fault codes:

- Coolant temperature
- Coolant level (optional)
- Oil pressure.

![[19e00093.png]]

### Fault Code Snapshot Data

A diagnostic fault code is recorded in the ECM.

The ECM input and output data is recorded from all sensors and switches.

Snapshot data allow the relationships between ECM inputs and outputs to be viewed during troubleshooting.

![[19e00093.png]]

### Engine Protection System

The engine protection system monitors critical engine temperatures, fluid levels, switch positions and pressures. Diagnostic fault codes will log when an over or under normal operating range occurs.

If an out-of-range condition exists, an engine derate action can be initiated. If an out-of-range condition exists, an active fault code will be generated in the ECM.

Engine protection system monitors:

- Coolant temperature
- Coolant level (optional)
- Intake manifold temperature
- Oil pressure.

Engine protection system monitors for:

- High coolant temperature
- Low coolant level (optional)
- High intake manifold temperature
- Low to very low oil pressure.

The engine protection system can have two selectable features:

- Engine protection enable - Engine power and speed are gradually reduced, depending on level of severity of condition.
- Engine protection shutdown - The engine will shut down, but can be restarted by turning the keyswitch off and then back on.

![[19a00825.png]]
