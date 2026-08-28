---
aliases:
  - "Воздушный компрессор"
type: "Процедура"
doc: "269-012-014-tr"
title_en: "Air Compressor"
title_ru: "Воздушный компрессор"
modified: "2022-11-02"
engines:
  - "93948840"
families:
  - "QSZ13"
manuals:
  - "4358369"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-012-014-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-012-014-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSZ13"
  - "группа/269"
---

# Air Compressor
**Воздушный компрессор**

> [!abstract] Процедура · `269-012-014-tr`
> **Двигатели:** [[93948840 — QSZ13 CM2150 Z102 CPL 4858|93948840]]
> **Семейство:** QSZ13
> **Входит в руководства:** [[4358369 — QSZ13 CM2150 Z102 Service Manual|4358369]]
> **Секции:** Section 12 - Compressed Air System - Group 12
> **Даты:** изменён 2022-11-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/269/269-012-014-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/269-012-014-tr.pdf)

### Pressure Test

> [!danger] WARNING · Опасно
> The external pressure tank used must meet Society of Automotive Engineers (SAE) J10 and FMVSS121 standards, and have a safety pressure relief valve which opens between 1034 to 1207 kPa \[ 150 to 175 psi \]. Failure to use the proper pressure vessel and plumbing can result in property damage and serious personal injury.

Purpose of the test is to check the pump up time to verify proper pressure is built up within the maximum time frame outlined below in the Maximum Pump-up Time Chart in Seconds table.

- Park unit on a level surface and in an area that is safe for extended time. Chock the unit wheels or use an appropriate anti-roll device to stabilize the unit.
- Drain the unit air system.
- Remove the air discharge hose and air governor signal hose from the air compressor.
- Plumb an air discharge line (steel braided Teflon® line) from the air compressor into an external pressure tank. The external pressure tank **must** be equipped with a 1379 kPa \[ 200 psi \] pressure gauge and 1206 kPa \[ 175 psi \] pressure relief valve. Verify the fittings are installed with appropriate thread sealant and do **not** leak.

Start the engine and operate at idle engine speed.

> [!note] Note · Примечание
> Once the external pressure tank pressure reaches 862 kPa \[ 125 psi \], shut the engine OFF. Depending on the size of the external pressure tank and the diameter/length of the discharge hose being used, the air pressure buildup time will vary.

Verify that the air compressor will build air pressure in the external tank. If air pressure successfully builds to 862 kPa \[ 125 psi \], the air compressor functions properly. Remove the external air discharge hose from the air compressor and install the vehicle air discharge hose and air governor signal hose to the compressor. Reference the symptom tree being utilized to inspect the rest of the air system components for leaks and proper operation.

| **Maximum Pump-up Time Chart in Seconds** |  |  |  |
|---|---|---|---|
| **Air Compressor Size (cubic centimeters)** | **Fill Rate \[Seconds / U.S. Gallon \]** | **Tank Volume (1000 cubic inches = 16 liters \[4.2 U.S. gallons\]** | **Tank Volume (2000 cubic inches = 32 liters \[8.4 U.S. gallons\])** |
| 250 cc | 15.5 | 65 sec | 130 sec |
| 318 cc | 13 | 55 sec | 110 sec |
| 500 cc | 9.5 | 40 sec | 80 sec |
| 636 cc | 8.5 | 35 sec | 70 sec |

If the air compressor does **not** build to 862 kPa \[ 125 psi \], the air compressor is malfunctioning and the air compressor cylinder head **must** be repaired, based on the marking scribed on the air compressor cylinder head. Refer to Procedure 012-003 in Section 12.

### Preparatory Steps

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°f\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

- Use steam to clean the air compressor. Dry with compressed air.
- Drain the engine coolant. [[269-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Remove the air compressor coolant lines. Refer to Procedure 012-004 in Section 12.
- Disconnect the air governor pressure signal line. Remove the air governor, if equipped.
- Remove the air discharge line. Refer to Procedure 012-015 in Section 12.

![[ck800wa.png]]

### Remove

Remove the air compressor support bracket and capscrews.

Remove the two mounting nuts and the air compressor.

Discard the gasket.

![[12c00237.png]]

### Clean and Inspect for Reuse

Inspect the compressor housing for cracks or other damage.

If cracks or other damage is found, replace the compressor housing.

Inspect the compressor drive gear for cracks or other damage.

If cracks or other damage is found, replace the drive gear.

![[12c00185.png]]

Verify the gasket surfaces of the front gear housing and the air compressor are clean and **not** damaged.

If damage is found on the gasket surface that will result in a leak path, the damaged component **must** be replaced.

![[12c00186.png]]

Remove the air compressor cylinder head if **not** already removed. Refer to Procedure 012-007 in Section 12.

Inspect the inside circumference for vertical scratches deep enough to be felt with a fingernail.

If a fingernail catches in the scratch, the air compressor **must** be replaced.

Inspect the inside circumference for scuffing, scoring, or polishing.

![[12900140.png]]

Install the air compressor cylinder head. Refer to Procedure 012-007 in Section 12.

### Install

Install the air compressor and the two nuts onto the front gear housing.

![[12c00237.png]]

Tighten the nuts.

> [!tip] Момент затяжки · Torque Value
> 75 n•m [55 ft-lb]

Tighten the nuts again.

> [!tip] Момент затяжки · Torque Value
> 75 n•m [55 ft-lb]

![[12c00215.png]]

Install the air compressor mounting brace and four capscrews on the cylinder block beneath the air compressor.

Start installing all four capscrews.

![[12c00210.png]]

Tighten the capscrews on the cylinder block and air compressor.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[12c00211.png]]

### Finishing Steps

- Install the coolant lines and fittings. Refer to Procedure 012-004 in Section 12.
- Install the air governor, if removed. Connect the air governor pressure signal line.
- Install the air discharge line. Refer to Procedure 012-015 in Section 5.
- Fill the engine cooling system. [[269-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Operate the engine to normal operating temperature and check for leaks.

![[ck800wa.png]]
