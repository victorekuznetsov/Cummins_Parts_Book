---
aliases:
  - "Порядок обычного пуска"
type: "Процедура"
doc: "00-101-014-om-ind"
title_en: "Normal Starting Procedure"
title_ru: "Порядок обычного пуска"
modified: "2012-11-20"
engines:
  - "41349633"
  - "41353297"
  - "85017333"
  - "93047320"
families:
  - "6B5.9"
  - "QSK19"
  - "QSK23"
manuals:
  - "3666120"
  - "4021374"
  - "4021389"
  - "4021391"
  - "4915552"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-101-014-om-ind.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-101-014-om-ind.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/QSK19"
  - "двигатель/QSK23"
  - "группа/00"
---

# Normal Starting Procedure
**Порядок обычного пуска**

> [!abstract] Процедура · `00-101-014-om-ind`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]], [[85017333 — QSK23 CM500 CPL 2858|85017333]], [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9, QSK19, QSK23
> **Входит в руководства:** [[3666120 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Operation and Maintenance Manual|3666120]], [[4021374 — QSK23 Operation and Maintenance Manual|4021374]], [[4021389 — B3.9, B4.5, B5.9 Industrial Operation and Maintenance Manual|4021389]], [[4021391 — B3.9, B4.5, and B5.9 Industrial Owners Manual|4021391]], [[4915552 — QSK23 Owners Manual|4915552]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2012-11-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/00/00-101-014-om-ind.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/00-101-014-om-ind.pdf)

### General Information

> [!danger] WARNING · Опасно
> Do not depress the accelerator pedal or move the accelerator lever from the idle position while cranking the engine. This can result in engine overspeed and severe damage to the engine.

> [!warning] CAUTION · Осторожно
> To prevent damage to the starting motor, do not engage the starting motor for more than 30 seconds. Wait 2 minutes between each attempt to start (electrical starting motors only).

> [!note] Note · Примечание
> Engines equipped with air starting motors require a minimum of 480 kPa \[70 psi\].

- Disengage the driven unit, or if equipped, put the transmission in neutral.
- With the accelerator pedal or lever in the idle position, turn the key switch to the ON position, and wait for the WAIT-TO-START lamp to go out; then, turn the key to the START position.
- If the engine does **not** start after three attempts, check the fuel supply system. Absence of blue or white exhaust smoke during cranking indicates no fuel is being delivered.

![[oi800v01.png]]

> [!warning] CAUTION · Осторожно
> The engine must have adequate oil pressure within 15 seconds after starting. If the WARNING lamp indicating low oil pressure has not gone out or there is no oil pressure indicated on a gauge within 15 seconds, shut off the engine immediately to avoid engine damage. The low oil pressure troubleshooting procedure is located in Troubleshooting Symptoms(Section TS).

![[eg8gask.png]]

Idle the engine 3 to 5 minutes before operating with a load.

![[oi800v02.png]]

After starting a cold engine, increase the engine speed (rpm) slowly to provide adequate lubrication to the bearings and to allow the oil pressure to stabilize.

![[07900017.png]]

> [!warning] CAUTION · Осторожно
> Do not operate engine at low idle for long periods with engine coolant temperature below the minimum specification in Maintenance Specifications (Section V). This can result in the following:

- Fuel Dilution of the lubricating oil
- Carbon build up in the cylinder
- Cylinder head valve sticking
- Reduced performance.

![[oi800be.png]]

### Jump Starting

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative(-) battery cable last.

> [!warning] CAUTION · Осторожно
> When using jumper cables to start the engine, make sure to connect the cables in parallel: Positive (+) to positive (+) and negative(-) to negative (-). When using an external electrical source to start the engine, turn the disconnect switch to the OFF position. Remove the key before attaching the jumper cables.

> [!warning] CAUTION · Осторожно
> To avoid damage to engine parts, do not connect jumper starting or battery charging cable to any fuel system or electronic component.

This illustration shows a typical parallel battery connection. This arrangement doubles the cranking amperage.

> [!note] Note · Примечание
> **Always** reference the relevant OEM literature for jump starting procedures. Failure to follow correct procedures can result in damage to the ECM and other electrical equipment.

![[sb8coga.png]]

This illustration shows a typical series battery connection. This arrangement, positive (+) to negative (-), doubles the voltage.

> [!note] Note · Примечание
> **Always** reference the relevant OEM literature for jump starting procedures. Failure to follow correct procedures can result in damage to the ECM and other electrical equipment.

![[sb8cogb.png]]
