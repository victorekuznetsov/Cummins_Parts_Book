---
aliases:
  - "Воздушный компрессор"
type: "Процедура"
doc: "35-012-014-tr"
title_en: "Air Compressor"
title_ru: "Воздушный компрессор"
modified: "2022-11-02"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-012-014-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-012-014-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Air Compressor
**Воздушный компрессор**

> [!abstract] Процедура · `35-012-014-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 12 - Compressed Air System - Group 12
> **Даты:** изменён 2022-11-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-012-014-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-012-014-tr.pdf)

### Pressure Test

> [!danger] WARNING · Опасно
> The external pressure tank used must meet SAE J10 and FMVSS121 standards, and have a safety pressure relief valve which opens between 1034 to 1207 kPa \[ 150 to 175 psi \]. Failure to use the proper pressure vessel and plumbing can result in property damage and serious personal injury.

#### Air Compressor Diagnostic Test

1. Park the vehicle on a level surface and in an area where it is safe to idle for an extended period of time. Chock the vehicle wheels or use an appropriate anti-roll device to stabilize the vehicle.
2. Drain the vehicle air system.
3. Remove the air discharge hose and air governor signal hose from the air compressor.
4. Plumb an air discharge hose from the air compressor into an external pressure tank. The external pressure tank **must** be equipped with a 1034 kPa \[ 150 psi \] pressure gauge and 1034 kPa \[ 150 psi \] pressure relief valve. Verify that the fittings are installed with appropriate thread sealant and do **not** leak.

Start the engine and operate at idle engine speed.

> [!note] Note · Примечание
> Once the external pressure tank pressure reaches 862 kPa \[ 125 psi \], shut the engine OFF. Depending on the size of the external tank and the diameter/length of the discharge hose being used, the buildup time will vary.

For example, a single cylinder (318 cc) compressor filled an 11 U.S. gal \[ 41.6 liter \] tank to 862 kPa \[ 125 psi \] using a (number 10 x 6 ft \[ 3.05 x 1.83 meters \] length) discharge hose in 90 seconds. This is considered in spec for this setup.

Verify that the air compressor will build pressure in the external tank. If the air pressure successfully builds to 862 kPa \[ 125 psi \], the air compressor is functioning properly. Remove the external air discharge hose from the air compressor and install the vehicle air discharge hose and air governor signal hose to the compressor. Reference the troubleshooting symptom tree being utilized to inspect the rest of the air system components for leaks and proper operation.

If the air compressor does **not** build to 862 kPa \[ 125 psi \], the air compressor is malfunctioning and the air compressor cylinder head needs to be repaired, based on the marking scribed on the head. [[101-012-003-tr — Air Compressor Carbon Buildup|Refer to Procedure 012-003 in Section 12.]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> When using a steam cleaner, wear safety glasses or a face shield, as well as protective clothing. Hot steam can cause serious personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[ 120°F \] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

- Use steam to clean the air compressor. Dry with compressed air.
- Remove the fuel pump. [[35-005-016-tr — Fuel Pump|Refer to Procedure 005-016 in Section 5.]]
- Drain the engine coolant. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Remove the coolant lines from the air compressor.

![[ck800wa.png]]

### Remove

Remove the air connections from the air compressor.

Remove the air compressor support bracket and capscrews.

Remove the four capscrews, the air compressor, and the splined coupling.

![[cp8comc.png]]

### Inspect for Reuse

Inspect the compressor housing for cracks or damage.

Inspect the splined coupling for cracks or damage.

![[cp8hssa.png]]

Remove the air compressor cylinder head. [[101-012-007-tr — Air Compressor Cylinder Head, Single Cylinder|Refer to Procedure 012-007 in Section 12.]]

Inspect the inside circumference for vertical scratches deep enough to be felt with a fingernail.

If a fingernail catches in the scratch, the air compressor **must** be replaced.

Inspect the inside circumference for scuffing, scoring, or polishing.

![[12900140.png]]

Install the air compressor cylinder head. [[101-012-007-tr — Air Compressor Cylinder Head, Single Cylinder|Refer to Procedure 012-007 in Section 12.]]

### Install

Position the timing mark on the air compressor crankshaft at the 12 o'clock position.

Position the accessory drive shaft dowel pin at the 2 o'clock position as viewed from the front of the engine.

![[cp8shwa.png]]

Install the splined coupling on the accessory drive shaft.

Be sure the gasket surfaces of the accessory drive and air compressor are clean and **not** damaged.

![[cp8cpva.png]]

Use a new gasket to install the air compressor and four capscrews to the accessory drive.

> [!tip] Момент затяжки · Torque Value
> Cummins® Air Compressor 44 n•m [32 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Holset® Air Compressor 68 n•m [50 ft-lb]

Install the air compressor support bracket.

> [!tip] Момент затяжки · Torque Value
> Cummins® Air Compressor Support Bracket 44 n•m [32 ft-lb]

> [!tip] Момент затяжки · Torque Value
> Holset® Air Compressor Support Bracket 47 n•m [35 ft-lb]

![[cp2bdmb.png]]

### Finishing Steps

- Install the fuel pump. [[35-005-016-tr — Fuel Pump|Refer to Procedure 005-016 in Section 5.]]
- Fill the engine cooling system. [[35-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Operate the engine and check for leaks.

![[ck800wa.png]]
