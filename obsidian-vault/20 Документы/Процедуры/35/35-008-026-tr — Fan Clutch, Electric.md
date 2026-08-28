---
type: "Процедура"
doc: "35-008-026-tr"
title_en: "Fan Clutch, Electric"
modified: "2009-01-23"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-026-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-026-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Fan Clutch, Electric

> [!abstract] Процедура · `35-008-026-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 8 - Cooling System - Group 08
> **Даты:** изменён 2009-01-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-008-026-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-008-026-tr.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the electrical connections, negative (-) cable first, from the batteries. Refer to the OEM service manual.
- Disconnect the fan clutch connector on the base harness from the fan clutch.
- Remove the fan from the engine. Refer to the OEM service manual.
- Remove the fan drive belt. [[35-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]]

![[ck800wa.png]]

### Remove

Remove the fan hub, clutch and capscrews from the engine.

![[fn200he.png]]

### Inspect for Reuse

This type of fan clutch is activated when 12-VDC from the vehicle electrical system is applied.

The clutch will disengage when 0-VDC is applied.

![[fn2drga.png]]

If the fan does **not** operate within the temperature range on the coolant temperature sensor (1), the fan clutch and the controls **must** be checked.

![[08200052.png]]

Inspect wires and harnesses to make sure none are broken or shorted. Replace harnesses or wires that are broken. [[35-008-069-tr — Wiring Harness, Cummins Electric Fan Clutch|Refer to Procedure 008-069 in Section 8.]]

![[wr2cnkb.png]]

The Cummins® electric fan clutch contains an electromagnetic coil. If the fan is **not** operating and all electrical circuits are OK, the coil possibly has an open circuit.

Measure the continuity across the isolated coil. Connect one multimeter lead to pin A in the fan clutch connector. Connect the other lead to pin B.

The resistance **must** be within 6-10 ohms. If the resistance is **not** within this range, replace the fan clutch.

![[ea200gk.png]]

### Install

Install the fan hub, clutch, and capscrews. Tighten the capscrews alternately and evenly.

> [!tip] Момент затяжки · Torque Value
> 47 n•m [35 ft-lb]

![[fn200he.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install the fan drive belt. [[35-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]]
- Install the fan from the engine. Refer to the OEM service manual.
- Connect the fan clutch connector on the base harness to the fan clutch.
- Connect the batteries, negative (-) cable last. Refer to the OEM service manual.
- Operate the engine and check for proper operation.

![[ck800wa.png]]
