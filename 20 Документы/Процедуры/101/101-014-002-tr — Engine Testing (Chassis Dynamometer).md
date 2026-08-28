---
aliases:
  - "Испытание двигателя (стенд с беговыми барабанами)"
type: "Процедура"
doc: "101-014-002-tr"
title_en: "Engine Testing (Chassis Dynamometer)"
title_ru: "Испытание двигателя (стенд с беговыми барабанами)"
modified: "2020-07-14"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 22
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-002-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-002-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
---

# Engine Testing (Chassis Dynamometer)
**Испытание двигателя (стенд с беговыми барабанами)**

> [!abstract] Процедура · `101-014-002-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2020-07-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-002-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-002-tr.pdf)

### Setup

The performance of an engine installed in “on-highway” vehicles can be tested on a chassis dynamometer.

> [!note] Note · Примечание
> Due to live driveline inefficiencies and engine-driven accessories, the rated horsepower will be reduced by approximately:

- 20 percent for single-axle vehicles
- 25 percent for tandem-axle vehicles
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
> Low-profile radial tires are more sensitive to heat than bias ply tires. Excessive operating time at full load can damage tires due to overheating. Check the tire manufacturers's recommendations for the maximum allowable chassis dynamometer operating time.

![[oi100bb.png]]

The following are general safety precautions to be observed while operating the chassis dynamometer.

- Use tires that have more than 160 km \[100 mi\] on them. Do **not** use new tires.
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
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

Check the engine coolant level to make sure it is filled to the proper level.

![[ra200sa.png]]

Check the engine lubricating oil level to make sure it is filled to the proper level.

![[oi8dsva.png]]

> [!note] Note · Примечание
> Use a known source of good quality Number 2 diesel fuel. Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher American Petroleum Institute (API) gravity) than Number 2 diesel fuel. The lighter the fuel, the lower the energy content British thermal unit (BTU) per gallon (liter).

### Test

To monitor engine performance correctly, record the following parameters. To limit dynamometer operating time, instrument the engine or use INSITE™ electronic service tool to make as many checks as possible.

- Engine speed (rpm)
- Fuel rate
- Intake manifold air temperature
- Engine blowby
- Engine coolant pressure
- Engine coolant temperature
- Rail fuel pressure (if applicable)
- Engine fule temperature (if needed to correct fuel rate)
- Fuel inlet restriction
- Fuel drain line restriction
- Intake manifold pressure
- Intake air restriction
- Exhaust restriction
- Engine oil pressure.

![[19r00163.png]]

Engine Speed

Use INSITE™ electronic service tool to monitor engine speed.

Observe and record the engine speed.

![[19r00163.png]]

Fuel Rate

Reference the Fuel Flow Measurement on Engine or Chassis Dynamometer in this section.

> [!note] Note · Примечание
> Adjust the fuel rate reading to compensate for temperature variation, if required.

| Fuel Inlet Temperature |  |  |
|---|---|---|
| celsius |  | fahrenheit |
| 7.2 | MIN | 45 |
| 55.5 | MAX | 132 |

![[nobox.png]]

Intake Manifold Air Temperature Control - Chassis Dynamometer test

When operating an engine on a chassis dynamometer, lock the cooling fan in the ON position for best results.

If the unit does **not** have a manual fan switch, use INSITE™ electronic service tool Set Up for Dynamometer feature to lock the fan in the ON position. [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14.]]

![[19r00163.png]]

Use INSITE™ electronic service tool to monitor the intake manifold air temperature.

Observe and record the intake manifold air temperature.

The intake manifold air temperature **must not** exceed the maximum allowable temperature. Reference the Specifications - Engine Testing page in this section for the maximum allowable intake manifold air temperature. The engine protection system will disrupt performance if the temperature exceeds this level. Maintain the intake manifold air temperature below the maximum allowable temperature during chassis dynamometer operation.

![[19r00163.png]]

If the intake manifold air temperature exceeds the maximum allowable temperature during the test, unload the dynamometer and allow the engine to cool.

Shut the engine off and inspect the charge-air cooler fins for obstructions to the airflow.

Check the fan drive. Make sure the fan is locked in the ON position.

Remove any obstructions, such as a winterfront or debris. Manually lock the shutters in the OPEN position, if equipped.

Inspect the dynamometer room for an adequate supply of suitably cool or outside air. Make sure that dynamometer room air recirculation is **not** an issue.

![[oi100wk.png]]

Engine Blowby

Use blowby checking tool, Part Number 3822566 (ISM) or Part Number 3822567 (ISX), and water manometer, Part Number ST-1111-3, to measure the engine crankcase pressure.

![[14c00071.png]]

Install the blowby checking tool to the end of the blowby tube. Install the water manometer to the blowby checking tool. Operate the engine at advertised horsepower rpm at full load. Observe and record the blowby.

Engine blowby **must not** exceed the maximum allowable specifications. [[101-014-010-tr — Crankcase Blowby, Measure|Refer to Procedure 014-010 in Section 14.]]

![[14c00061.png]]

Engine Coolant Pressure

Use pressure gauge, Part Number 3822995, to measure engine coolant pressure.

Observe and record engine coolant pressure.

Reference the Specifications - Engine Testing page in this section for the maximum allowable coolant temperature.

![[14c00053.png]]

Engine Coolant Temperature

Use INSITE™ electronic service tool to monitor engine coolant temperature.

Observe and record the engine coolant temperature.

Reference the Specifications - Engine Testing page in this section for the maximum allowable coolant temperature.

![[19r00163.png]]

If the coolant temperature exceeds the maximum allowable coolant temperature, unload the dynamometer and allow the engine to cool.

Shut the engine off and inspect the radiator fins for obstructions to the airflow.

Check the fan drive. Make sure the fan is locked in the ON position.

Remove any obstructions, such as a winterfront or debris. Manually lock the shutters in the OPEN position, if equipped.

Inspect the dynamometer room for an adequate supply of suitable cool or outside air. Make sure that dynamometer room air recirculation is **not** an issue.

![[oi100wk.png]]

Engine Fuel Temperature

Use immersion probe, Part Number 3164492, with a digital multimeter, Part Number 3164488, and a thermocouple module, Part Number 3164499, to monitor fuel temperature.

Observe and record the engine fuel temperature.

![[14c00077.png]]
