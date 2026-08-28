---
aliases:
  - "Воздушный компрессор"
type: "Процедура"
doc: "10-012-014-tr"
title_en: "Air Compressor"
title_ru: "Воздушный компрессор"
modified: "2013-07-03"
engines:
  - "80141463"
  - "80248213"
families:
  - "QSX15"
manuals:
  - "3666239"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-012-014-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-012-014-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSX15"
  - "группа/10"
---

# Air Compressor
**Воздушный компрессор**

> [!abstract] Процедура · `10-012-014-tr`
> **Двигатели:** [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSX15
> **Входит в руководства:** [[3666239 — Signature™, ISX, and QSX15 Service Manual|3666239]]
> **Секции:** Section 12 - Compressed Air System
> **Даты:** изменён 2013-07-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/10/10-012-014-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/10-012-014-tr.pdf)

### Pressure Test

> [!danger] WARNING · Опасно
> The external pressure tank used must meet SAE J10 and FMVSS121 standards, and have a safety pressure relief valve which opens between \[150 to 175 psi\]. Failure to use the proper pressure vessel and plumbing can result in property damage and serious personal injury.

#### Air Compressor Diagnostic Test

1. Park the vehicle on a level surface and in an area where it is safe to idle for an extended period of time. Chock the vehicle wheels or use an appropriate anti-roll device to stabilize the vehicle.
2. Drain the vehicle air system.
3. Remove the air discharge hose and air governor signal hose from the air compressor.
4. Plumb an air discharge hose from the air compressor into an external pressure tank. The external pressure tank **must** be equipped with a **150 psi** pressure gauge and **150 psi** pressure relief valve. Make sure that the fittings are installed with appropriate thread sealant and do **not** leak.

Start the engine and operate at idle engine speed.

> [!note] Note · Примечание
> Once the external pressure tank pressure reaches 862 kPa \[125 psi\], shut the engine OFF. Depending on the size of the external tank and the diameter/length of the discharge hose being used, the buildup time will vary.

For example, a single cylinder (318 cc) compressor filled an 11 gallon tank to 125 psi using a number10 x 6ft length discharge hose in 90 seconds. This is considered in spec for this setup.

Verify that the air compressor will build pressure in the external tank. If the air pressure successfully builds to 125 psi, the air compressor is functioning properly. Remove the external air discharge hose from the air compressor and install the vehicle air discharge hose and air governor signal hose to the compressor. Reference the symptom tree being utilized to inspect the rest of the air system components for leaks and proper operation.

If the air compressor does **not** build to 125 psi, the air compressor is malfunctioning and the air compressor cylinder head needs to be repaired based on the marking scribed on the head. [[101-012-003-tr — Air Compressor Carbon Buildup|Refer to Procedure 012-003 in Section 12.]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Coolant is toxic. Keep away from children and pets. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> Wear safety glasses or a face shield, as well as protective clothing, to prevent personal injury when using a steam cleaner or high-pressure water.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

- Disconnect the batteries. Refer to the original equpment manufacturer (OEM) service manual.
- Drain the engine coolant. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Use steam to clean the air compressor. Dry with compressed air.
- Remove the coolant lines from the air compressor. Refer to Procedure 012-004 in Section 12.
- Remove the air connections from the air compressor.
- Remove or disconnect the air governor. Refer to the original equipment manufacturer (OEM) service manual.
- Remove any driven equipment from the back of the air compressor, if equipped.
- Remove or disconnect the air governor. Refer to the OEM service manual.

![[12c00021.png]]

### Remove

Pin the engine crankshaft. [[10-001-088-tr — Engine Base Timing|Refer to Procedure 001-088 in Section 1.]]

Remove the air compressor support bracket and capscrews.

Remove the four mounting capscrews and the air compressor.

Discard the gasket.

![[12c00036.png]]

### Clean and Inspect for Reuse

Inspect the compressor housing for cracks or other damage.

Inspect the compressor drive gear for cracks or other damage.

![[12c00082.png]]

Make sure the gasket surfaces of the front gear housing and the air compressor are clean and **not** damaged.

![[12c00037.png]]

Remove the air compressor cylinder head. [[101-012-007-tr — Air Compressor Cylinder Head, Single Cylinder|Refer to Procedure 012-007 in Section 12.]]

Inspect the inside circumference for vertical scratches deep enough to be felt with a fingernail.

If a fingernail catches in the scratch, the air compressor **must** be replaced.

Inspect the inside circumference for scuffing, scoring, or polishing.

![[12900140.png]]

### Install

Rotate the gear on the air compressor until the mark on the gear is in line with the V-notch on the air compressor housing, located at the three o'clock position as viewed from the front.

Loctite™, Part Number 3824040, or equivalent, **must** be used on the capscrews that mount the air compressor to the gear housing. This seals the threads in the housing.

To evenly distribute the sealant as the capscrew is tightened, a line of sealant should be placed along the length of the capscrew.

Install the air compressor and the four capscrews onto the front gear housing.

![[12800060.png]]

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

Tighten the capscrews again.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[12800061.png]]

Install the air compressor mounting brace and four capscrews on the block beneath the air compressor. Start threading all four capscrews.

![[12800062.png]]

Tighten the capscrews on the cylinder block and air compressor.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[12800063.png]]

Install the air discharge line.

> [!tip] Момент затяжки · Torque Value
> 60 n•m [44 ft-lb]

Install the air inlet line.

Tighten the hose clamp.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[12800068.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install the air compressor coolant lines. Refer to Procedure 012-004 in Section 12.
- Install the air intake and discharge lines on the air compressor.
- Install the air governor and the air governor signal line to the air compressor. Refer to the OEM service manual.
- Install any driven components that were removed.
- Fill the engine cooling system. [[10-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]
- Connect the batteries. Refer to the OEM service manual.
- Operate the engine and check for leaks.

![[ck800wa.png]]
