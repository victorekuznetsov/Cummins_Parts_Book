---
aliases:
  - "Порядок обычного пуска"
type: "Процедура"
doc: "40-101-014-om"
title_en: "Normal Starting Procedure"
title_ru: "Порядок обычного пуска"
modified: "2009-06-17"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3810205"
  - "4960250"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-101-014-om.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-101-014-om.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Normal Starting Procedure
**Порядок обычного пуска**

> [!abstract] Процедура · `40-101-014-om`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3810205 — B Automotive, Recreational Vehicle, and Bus Operation and Maintenance Manual|3810205]], [[4960250 — B Automotive, Recreational Vehicle, and Bus Owners Manual|4960250]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2009-06-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-101-014-om.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-101-014-om.pdf)

### General Information

> [!danger] WARNING · Опасно
> Do not depress the accelerator pedal or move the accelerator lever from the idle position while cranking the engine. This can result in engine overspeed and severe damage to the engine.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damage to the starting motor, do not engage the starting motor for more than 30 seconds. Wait 2 minutes between each attempt to start (electrical starting motors only).

> [!note] Note · Примечание
> Engines equipped with air starting motors require a minimum of 480 kPa \[70 psi\].

1. Disengage the driven unit, or if equipped, put the transmission in neutral.
2. With the accelerator pedal or lever in the idle position, turn the keyswitch to the ON position, and wait for the WAIT-TO-START lamp to go out; then, turn the key to the START position.
3. If the engine does **not** start after three attempts, check the fuel supply system. Absence of blue or white exhaust smoke during cranking indicates no fuel is being delivered.

![[oi800v01.png]]

> [!warning] CAUTION · Осторожно
> The engine must have adequate oil pressure within 15 seconds after starting. If the WARNING lamp indicating low oil pressure has not gone out or there is no oil pressure indicated on a gauge within 15 seconds, shut off the engine immediately to reduce the possibility of engine damage.

Refer to Lubricating Oil Pressure Low symptom tree in Section TS if no oil pressure is indicated.

![[eg8gask.png]]

Idle the engine 3 to 5 minutes before operating with a load.

![[oi800v02.png]]

After starting a cold engine, increase the engine speed (rpm) slowly to provide adequate lubrication to the bearings and to allow the oil pressure to stabilize.

![[07900017.png]]

Do **not** operate the engine at low idle for long periods with the engine coolant temperature below the minimum specification. Refererence Engine Specifications in Section V.

This can result in the following:

- Fuel dilution of the lubricating oil
- Carbon build up in the cylinder
- Cylinder head valve sticking
- Reduced performance.

![[oi800be.png]]

### Jump Starting

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> When using jumper cables to start the engine, make sure to connect the cables in parallel: Positive (+) to positive (+) and negative (-) to negative (-). When using an external electrical source to start the engine, turn the disconnect switch to the OFF position. Remove the key before attaching the jumper cables.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damage to engine parts, do not connect jumper starting or battery charging cable to any fuel system or electronic component.

This illustration shows a typical parallel battery connection. This arrangement doubles the cranking amperage.

> [!note] Note · Примечание
> **Always** reference the relevant OEM literature for jump starting procedures. Failure to follow correct procedures can result in damage to the ECM and other electrical equipment.

![[sb8coga.png]]

This illustration shows a typical series battery connection. This arrangement, positive (+) to negative (-), doubles the voltage.

> [!note] Note · Примечание
> **Always** reference the relevant OEM literature for jump starting procedures. Failure to follow correct procedures can result in damage to the ECM and other electrical equipment.

![[sb8cogb.png]]

| Starting Procedure Matrix |  |
|---|---|
| Automotive and industrial | Idle throttle |
| All pumps above 16°C \[60°F\] | X (after 5 seconds, see note) |
| Automotive and industrial | Full throttle |
| All pumps below 16°C \[60°F\] | X (see note) |
| (1) Full throttle on the VE pump makes sure there is sufficient start-fuel delivery and helps keep the engine operating once started. The in-line pumps with RQV and RQV-K governors require full throttle to position and hold the rack in the start-fuel position. |  |

> [!note] Note · Примечание
> Full throttle is applied after engaging the starter.

1. Disengage the driven unit, or if equipped, put the transmission in neutral.
2. Position the fuel shutoff, electrical switch, or mechanism control to the RUN position.

> [!note] Note · Примечание
> Full throttle procedure **not** required on Tier II B3.9, B4.5, and B5.9 engines.
