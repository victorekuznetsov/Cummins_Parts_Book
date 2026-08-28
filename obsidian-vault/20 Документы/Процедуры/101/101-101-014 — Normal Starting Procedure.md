---
aliases:
  - "Порядок обычного пуска"
type: "Процедура"
doc: "101-101-014"
title_en: "Normal Starting Procedure"
title_ru: "Порядок обычного пуска"
modified: "2023-09-11"
engines:
  - "41343322"
  - "41370103"
  - "80141463"
  - "80248213"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QSX15"
manuals:
  - "3666251"
  - "3666423"
  - "4021631"
  - "4915540"
  - "4960314"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-014.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-014.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QSX15"
  - "группа/101"
---

# Normal Starting Procedure
**Порядок обычного пуска**

> [!abstract] Процедура · `101-101-014`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QSX15
> **Входит в руководства:** [[3666251 — Signature and ISX Operation and Maintenance Manual|3666251]], [[3666423 — QSX15 Operation and Maintenance Manual|3666423]], [[4021631 — NT NTA855 Big Cam III Construction, Industrial, and Generator Drive|4021631]], [[4915540 — QSX15 Owners Manual|4915540]], [[4960314 — ISX Owners Manual|4960314]]
> **Секции:** Section 1 - Operating Instructions
> **Даты:** изменён 2023-09-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-101-014.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-101-014.pdf)

### General Information

The STOP or STOP ENGINE lamp is red and indicates the need to stop the engine as soon as safely done. The engine **must** then remain shut down until repaired.

The WARNING or CHECK ENGINE lamp is yellow. When the check engine lamp illuminates, the engine is in need of repair at the first available opportunity.

The yellow lamp will flash for 30 seconds at keyswitch ON when one of the following occurs:

- Maintenance required (if Maintenance Monitor is enabled)
- Water-in-fuel is detected
- Low coolant level.

If the warning light flashes for 30 seconds at keyswitch ON and water is drained from the suction side water-separating fuel filter, the pressure side fuel filter **must** be replaced.

![[19900833.png]]

> [!warning] CAUTION · Осторожно
> Do not depress the accelerator pedal or move the accelerator lever from the idle position while cranking the engine. This movement can result in engine overspeed and severe damage to the engine.

> [!warning] CAUTION · Осторожно
> To prevent damage to the starting motor, do not engage the starting motor for more than 30 seconds. Wait 2 minutes between each attempt to start (electrical starting motors only).

> [!note] Note · Примечание
> Engines equipped with air starting motors require a minimum of 480 kPa \[ 70 psi \] air pressure.

- Disengage the driven unit, or if equipped, put the transmission in neutral.
- With the accelerator pedal or lever in the idle position, turn the keyswitch to the ON position, then turn the keyswitch to the START position.
- If the engine does **not** start after three attempts, check the fuel supply system. Absence of blue or white exhaust smoke during cranking indicates no fuel is being delivered.

![[oi800v01.png]]

> [!warning] CAUTION · Осторожно
> The engine must have adequate oil pressure within 15 seconds after starting. If the warning lamp indicating low oil pressure has not gone out or no oil pressure is indicated on a gauge within 15 seconds, shut OFF the engine immediately to reduce the possibility of engine damage. The low oil pressure troubleshooting procedure is located in Troubleshooting Symptoms (Section TS).

![[eg8gask.png]]

Idle the engine 3 to 5 minutes before operating with a load.

![[oi800v02.png]]

After starting a cold engine, increase the engine speed (rpm) slowly to provide adequate lubrication to the bearings and to allow the oil pressure to stabilize.

![[07900017.png]]

> [!warning] CAUTION · Осторожно
> Do not operate engine at low idle for long periods with engine coolant temperature below the minimum specification in Coolant Recommendations and Specifications (Section V). Low coolant temperature can result in:

- Fuel dilution of the lubricating oil
- Carbon buildup in the cylinder
- Cylinder head valve sticking
- Reduced performance.

![[oi800be.png]]

### Jump Starting

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> When using jumper cables to start the engine, connect the cables in parallel: Positive (+) to positive (+) and negative (-) to negative (-). When using an external electrical source to start the engine, turn the disconnect switch to the OFF position. Remove the key before attaching the jumper cables.

> [!warning] CAUTION · Осторожно
> To reduce the possibility of damage to engine parts, do not connect jumper starting or battery charging cable to any fuel system or electronic component.

The accompanying illustration shows a typical parallel battery connection. This arrangement doubles the cranking amperage.

![[sb8coga.png]]

This illustration shows a typical series battery connection. This arrangement, positive (+) to negative (-), doubles the voltage.

![[sb8cogb.png]]
