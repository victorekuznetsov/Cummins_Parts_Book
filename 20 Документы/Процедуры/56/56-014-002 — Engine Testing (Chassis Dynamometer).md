---
aliases:
  - "Испытание двигателя (стенд с беговыми барабанами)"
type: "Процедура"
doc: "56-014-002"
title_en: "Engine Testing (Chassis Dynamometer)"
title_ru: "Испытание двигателя (стенд с беговыми барабанами)"
modified: "2023-07-17"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 28
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-002.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-002.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Engine Testing (Chassis Dynamometer)
**Испытание двигателя (стенд с беговыми барабанами)**

> [!abstract] Процедура · `56-014-002`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 14 - Engine Testing - Group 14 · Section 14 Engine Testing - Group 14
> **Даты:** изменён 2023-07-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-002.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-002.pdf)

### Setup

The performance of an engine installed in “on-highway” vehicles can be tested on a chassis dynamometer.

> [!note] Note · Примечание
> Due to live driveline inefficiencies and engine-driven accessories, the rated horsepower will be reduced by approximately:

- 20 percent for single-axle vehicles
- 25 percent for tandem-axle vehicles.
- 30 percent for tri-axles vehicles.

These specifications apply to drive axles **only**, **not** tag axles.

The net horsepower available is called wheel horsepower.

> [!note] Note · Примечание
> These percentages are used for engine run-in **only** and are **not** to be used as absolute figures.

![[oi100vi.png]]

> [!danger] WARNING · Опасно
> Follow all the OEM's safety precautions before installing or operating a vehicle on a chassis dynamometer. Failure to do so can cause damage to the vehicle and/or cause personal injury.

![[oi100ba.png]]

> [!warning] CAUTION · Осторожно
> Low-profile radial tires are more sensitive to heat than bias ply tires. Excessive operating time at full load can damage tires due to overheating. See equipment manufacturer service information for the maximum allowable chassis dynamometer operating time.

![[oi100bb.png]]

The following are general safety precautions to be observed while operating the chassis dynamometer.

- Use tires that have more than 160 km \[ 100 mi \] on them. Do **not** use new tires.
- Do **not** use recapped tires or tires of different sizes or designs.

![[oi100vj.png]]

- Make sure the tires are inflated to the manufacturer's specifications.
- Remove all rocks or other material from the treads of all tires that will be rotating on the dynamometer rollers.

![[oi100vk.png]]

- Make sure there is correct overhead clearance for exhaust stacks, air deflectors, or other attachments above the cab.

![[oi100vl.png]]

> [!warning] CAUTION · Осторожно
> The “tie-down” chains must have slack to prevent damage to the chassis dynamometer.

- Carefully position the vehicle on the rollers.
- Attach the “tie-down” chains to the rear of the vehicle, and put wheel chocks in front of the front wheels.

![[oi100v30.png]]

- Adjust the vehicle and dynamometer room exhaust system to make sure all exhaust gases are removed from the room.
- Reference the chassis dynamometer and vehicle manufacturer's recommendations and specifications for testing procedures.

![[oi100vn.png]]

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[ 120°F \] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

Check the engine coolant level to make sure it is filled to the proper level.

![[ra200sa.png]]

Check the engine lubricating oil level to make sure it is filled to the proper level.

![[07t00018.png]]

> [!note] Note · Примечание
> Use a known source of good quality Number 2 diesel fuel. Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher American Petroleum Institute (API) gravity) than Number 2 diesel fuel. The lighter the fuel, the lower the energy content British thermal unit (BTU) per gallon (liter).

### Test

To monitor engine performance properly, record the following parameters. To limit dynamometer operating time, instrument the engine to perform as many checks as possible. INSITE™ electronic service tool will provide most if **not** all of the following:

- Engine speed rpm with a verified tachometer
- Fuel pressure
- Fuel rate
- Fuel temperature, if needed to correct fuel rate
- Fuel inlet restriction
- Fuel drain line restriction
- Intake manifold pressure, per bank.

![[eg200ka.png]]

- Intake air restriction, per bank
- Exhaust air restriction, per bank
- Coolant temperature
- Engine blowby
- Lubricating oil pressure
- Coolant pressure
- Inlet manifold air temperature
- Turbocharger inlet air temperature.

![[eg100km.png]]

Engine Speed

Use digital optical tachometer, Part Number 3377462, to check and verify engine speed.

![[er2tova.png]]

Fuel Pressure

Use INSITE™ electronic service tool to measure the fuel supply pressure. [[56-005-016-tr — Fuel Pump|Refer to Procedure 005-016 in Section 5.]]

![[05500009.png]]

Fuel Rate

Use INSITE™ electronic service tool or a fuel measuring device to measure the rate of fuel consumption.

![[19a00042.png]]

Fuel Inlet Restriction

Use INSITE™ electronic service tool or pressure gauge, Part Number ST-434, to measure the fuel restriction between the fuel filter and the gear pump inlet. [[56-006-020 — Fuel Inlet Restriction|Refer to Procedure 006-020 in Section 6.]]

![[06400054.png]]

Fuel Drain Line Restriction

Use pressure gauge, Part Number ST-1273, to measure fuel drain line restriction. [[56-006-012 — Fuel Drain Line Restriction|Refer to Procedure 006-012 in Section 6.]]

![[06400051.png]]

Intake Manifold Pressure

Use INSITE™ electronic service tool or manually measure the intake manifold pressure (turbocharger boost). Reference the QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]], or the appropriate electronic service tool manual.

![[06400102.png]]

Intake Manifold Air Temperature Control - Chassis Dynamometer test

When operating an engine on a dynamometer, follow these steps for best results and safe operation.

If the engine is equipped with an automatic fan, lock the cooling fan in the ON mode. This can be done by installing a jumper across the temperature switch, or by supplying shop air to the control valve. See equipment manufacturer service information for the recommended procedure.

![[fa1chwa.png]]

Monitor the intake manifold air temperature using INSITE™ electronic service tool in the Monitor Mode, or install Fluke™ digital thermometer, Part Number 3822666, and thermocouple wire kit, Part Number 3822988, into the intake manifold.

The intake manifold air temperature **must not** exceed 77°C \[ 171°F \].

Maintain intake manifold air temperature to 66°C \[ 110°F \] or below during chassis dynamometer operation.

![[10400046.png]]

If the intake manifold temperature exceeds 77°C \[ 171°F \], shut off the engine. Allow the engine to cool.

Check the fan drive. Be sure the fan is locked in the ON mode.

Remove any obstructions such as a winterfront or debris. Manually lock the shutters in the OPEN position if equipped.

Inspect the dynamometer room for adequate supply of suitably cool or outside air. Make sure that dynamometer room recirculation is **not** an issue.

Resume the test.

![[oi100wk.png]]

Intake Air Restriction

Measure the inlet air restriction. Install a manometer, Part Number ST-1111-3, in the intake air piping.

The gauge adapter **must** be installed at a 90-degree angle to the airflow in a straight section of pipe at a minimum of one pipe diameter before the turbocharger.

[[56-010-031 — Air Intake Restriction|Refer to Procedure 010-031 in Section 10.]]

![[10400011.png]]

Exhaust Air Restriction

Measure the exhaust air restriction. Install the pressure gauge, Part Number ST-1273, or a manometer Part Number ST-1111-3, in the exhaust air piping.

The gauge adapter **must** be installed near the turbocharger in a straight section of pipe at the turbine outlet.

[[56-011-009 — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]

![[pe4cokb.png]]

Engine Blowby

Excessive blowby indicates an air compressor, a turbocharger, or an engine malfunction, allowing combustion gases or air to enter the crankcase and build a pressure higher than normal.

[[56-014-010-tr — Crankcase Blowby, Measure|Refer to Procedure 014-010 in Section 14.]]

![[ck800wa.png]]

Lubricating Oil Pressure

Use pressure gauge, Part Number. 3375275, or INSITE™ electronic service tool to measure lubricating oil pressure. Reference the QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and Repair Manual, Bulletin [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R\|3666113]].

Install the pressure gauge to the main oil rifle (1) or oil filter head (2).

| Lubricating Oil Pressure |  |  |  |  |
|---|---|---|---|---|
|  | kpa |  | psi |  |
| Low Idle (Minimum Allowable) |  | 138 | MAX | 20 |
| At 1200 rpm (Minimum Allowable) |  | 207 | MAX | 30 |

![[ov400ha.png]]

Air Compressor

All air compressors manufactured by Cummins Inc. **must** be operating during the engine run-in. During the performance check, all air compressors **must** be in the unload or nonoperating mode.

Connect a source of compressed air capable of providing 665 kPa \[ 97 psi \] to the air compressor unloader (1). This air line **must** contain a valve between the source and the unloader.

The compressed air load in the accompanying illustration **must** be attached to the air compressor outlet (2).

![[cp8vawa.png]]

Use an air tank (2). Install an air regulator (3) capable of maintaining 345- to 517-kPa \[ 50- to 75-psi \] air pressure at both minimum and maximum engine rpm.

Install a steel tube or high-temperature hose (1).

| Measurements |  |  |
|---|---|---|
|  | celsius | fahrenheit |
| Hose Temperature (Minimum): | 260 | 500 |

Connect the tube or hose (1) to the air compressor outlet.

![[cp8tohc.png]]

Starting Motor

Inspect the voltage rating on the starting motor before installing the electrical wiring.

Install the electrical wiring to the starting motor and batteries, if used.

If another method of starting the engine is used, see equipment manufacturer service information to make the necessary connections.

![[sb8coma.png]]
