---
aliases:
  - "Испытание двигателя (стенд с беговыми барабанами)"
type: "Процедура"
doc: "20-014-002-tr"
title_en: "Engine Testing (Chassis Dynamometer)"
title_ru: "Испытание двигателя (стенд с беговыми барабанами)"
modified: "2020-07-14"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 43
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-002-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-014-002-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Engine Testing (Chassis Dynamometer)
**Испытание двигателя (стенд с беговыми барабанами)**

> [!abstract] Процедура · `20-014-002-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2020-07-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-002-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-014-002-tr.pdf)

### Setup

The performance of an engine installed in on-highway vehicles can be tested on a chassis dynamometer.

> [!note] Note · Примечание
> Due to live driveline inefficiencies and engine-driven accessories, the rated horsepower can be reduced by approximately:

- 20 percent for single axle vehicles
- 25 percent for tandem axle vehicles
- 30 percent for tri-axles vehicles.

These specifications apply to drive axles **only**, **not** tag axles.

The net horsepower available is called Wheel Horsepower (WHP).

> [!note] Note · Примечание
> Operate the vehicle in a gear that produces a road speed of 90 to 95 Km/H \[55 to 60 MPH\].

![[oi100vi.png]]

> [!warning] CAUTION · Осторожно
> Before installing or operating a vehicle on a chassis dynamometer, follow all the vehicle manufacturer's safety precautions.

![[oi100ba.png]]

> [!warning] CAUTION · Осторожно
> Low profile radial tires are more sensitive to heat than bias ply tires. Excessive operating time at full load can damage tires due to overheating. Check the tire manufacturer's recommendations for the maximum allowable chassis dynamometer operating time.

![[oi100bb.png]]

Adjust the vehicle and dynamometer room exhaust system to be sure that all exhaust gases are removed from the room.

Use the chassis dynamometer and vehicle manufacturer's recommendations and specifications for testing procedures.

![[oi100vn.png]]

Make sure all instrumentation is removed before removing the vehicle from the dynamometer.

![[oi100vl.png]]

> [!note] Note · Примечание
> The lubricating oil system **must** be primed before operating the engine after rebuild to avoid internal component damage. Do **not** prime the system from the bypass filter as the filter will be damaged.

Remove the large plug from the oil cooler housing.

![[14400011.png]]

Use a pump capable of supplying 205 kPa \[30 psi\] continuous pressure. Connect the pump to the front of the engine oil cooler as shown.

Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

![[pl4hoha.png]]

Check the engine lubricating oil level to be sure it is filled to the proper level.

![[oi8dsva.png]]

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.

Check the engine coolant level to be sure it is filled to the proper level. [[20-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

![[ra200sa.png]]

Use a known source of good quality number 2 diesel fuel.

This is very important since number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuel. The lighter the fuel, the lower the energy content (BTU) per gallon (liter, etc.).

![[nobox.png]]

Engine operating specifications can be found in publications available from your local Cummins Authorized Repair Location.

![[lt800ga.png]]

### Test

To properly monitor engine performance, record the following parameters. To limit dynamometer operating time, instrument the engine to perform as many checks as possible.

- Engine speed rpm with a verified tachometer
- Fuel pressure
- Fuel rate (use service tool, Part Number 3376375, or equivalent)
- Fuel temperature (if needed to correct fuel rate)
- Fuel inlet restriction
- Fuel drain line restriction
- Intake manifold pressure.

![[eg200ka.png]]

- Intake air restriction
- Exhaust air restriction
- Coolant temperature
- Engine blowby
- Lubricating oil pressure
- Coolant pressure
- Inlet manifold air temperature
- Turbocharger inlet air temperature.

![[eg100km.png]]

To check and verify engine speed (rpm) with a verified tachometer, use a digital optical tachometer, Part Number 3377462, or equivalent.

![[er2tova.png]]

To measure fuel pump pressure; [[20-005-016-tr — Fuel Pump|Refer to Procedure 005-016 in Section 5.]]

![[05500009.png]]

Use fuel measuring device, Part Number 3376375, or equivalent, to measure the rate of fuel consumption. [[20-005-010 — Fuel Consumption|Refer to Procedure 005-010 in Section 5.]]

![[eg8togf.png]]

> [!note] Note · Примечание
> Do **not** measure fuel inlet restriction with the fuel measuring device installed. This will **not** measure the inlet restriction of the vehicle's supply plumbing.

Measure the fuel inlet restriction. Install a vacuum gauge, Part Number ST-434, or equivalent, between the fuel filter and the gear pump inlet.

Refer to Procedure 006-020 in Section 6.

![[06400054.png]]

> [!note] Note · Примечание
> Do **not** measure fuel drain line restriction with the fuel measuring device installed. This will **not** measure the drain line restriction of the vehicle's return plumbing.

Use Pressure Gauge, Part Number ST-1273, or equivalent, to measure fuel drain line restriction. [[20-006-012 — Fuel Drain Line Restriction|Refer to Procedure 006-012 in Section 6.]]

![[06400051.png]]

Measure the intake manifold or INSITE™ electronic service tool pressure (turbocharger boost). Install pressure gauge, Part Number ST-1273, or equivalent, in the intake manifold as shown.

Refer to Procedure 010-057 in Section 10.

Observe the reading on the pressure gauge.

![[06400102.png]]

When operating an engine on a chassis dynamometer for intake air temperature control, follow these steps for best results and safe operation.

If the engine is equipped with automatic fan, lock the cooling fan in the ON mode. This can be done by installing a jumper across the temperature switch, or by supplying shop air to the control valve. Refer to the fan drive manufacturer for the recommended procedure.

![[fa1chwa.png]]

Monitor the intake manifold air temperature using the INSITE™ electronic service tool in the monitor mode, or install digital thermometer, Part Number 3822666, or equivalent, and thermocouple wire kit, Part Number 3822988, or equivalent, into the intake manifold.

The intake manifold air temperature **must not** exceed 77°C \[170°F\].

Maintain intake manifold air temperature to 66°C \[150°F\] or below during chassis dynamometer operation.

![[10400046.png]]

If the intake manifold temperature exceeds 77°C \[170°F\], shut off the engine. Allow the engine to cool.

Check the fan drive. Be sure the fan is locked in the ON mode.

Remove any obstructions such as a winterfront or debris. Manually lock the shutters in the OPEN position if equipped.

Inspect the dynamometer room for adequate supply of suitably cool or outside air. Make sure that dynamometer room recirculation is **not** an issue.

Resume the test.

![[oi100wk.png]]

Measure the inlet air restriction. Install the vacuum gauge, Part Number ST-434, or equivalent, or a manometer, Part Number ST-1111-3, or equivalent, in the intake air piping.

> [!note] Note · Примечание
> The gauge adapter **must** be installed at a 90 degree angle to the air flow in a straight section of pipe at a minimum of one pipe diameter before the turbocharger.

[[20-010-031 — Air Intake Restriction|Refer to Procedure 010-031 in Section 10.]]

![[10400011.png]]

Measure the exhaust air restriction. Install the pressure gauge, Part Number ST-1273, or equivalent, or a manometer in the exhaust air piping.

The gauge adapter **must** be installed near the turbocharger in a straight section of pipe at the turbine outlet.

[[20-011-009 — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]

![[pe4cokb.png]]

> [!note] Note · Примечание
> Excessive blowby indicates an air compressor, a turbocharger, or an engine malfunction, allowing combustion gases or air to enter the crankcase and build a pressure higher than normal.

This procedure describes how to measure crankcase pressure and how to determine the component that is malfunctioning.

Use one of the three blowby service tools and a water manometer Part Number ST-1111-3, or equivalent. Maximum gauge capacity is 1270 mm-H 2 0 \[50 in-H 2 0\]. The engine blowby tools are similar in design. The difference between the tools is in the size of the orifice.

| Blowby Orifice Size |  |
|---|---|
| Blowby Tool Part Number | Orifice Size mm \[in\] |
| 3822566 | 7.68 mm \[0.302\] |
| 3822567 | 8.99 mm \[0.354\] |
| 3822568 | 10.31 mm \[0.406\] |

![[eg8toga.png]]

Use a length of hose (1) to attach the blowby tool to one of the crankcase breathers.

Plug all of the other breathers.

Attach a manometer to the location shown (2).

![[eg4toha.png]]

Operate the engine at rated rpm and full load (wide open throttle) until a steady reading is obtained.

Compare the blowby readings to previous readings on the engine. If previous readings for the engine are **not** available, compare the blowby reading to new engine specifications.

> [!note] Note · Примечание
> A sudden increase in blowby indicates a problem. A gradual increase over a period of time is normal (due to wear of internal engine components).

![[eg8toja.png]]

| Engine Blowby Specifications |  |  |  |  |
|---|---|---|---|---|
| 7.67 mm \[0.302 in\] Orifice: | New/Rebuilt | Used |  |  |
| RPM | mm H 2 0 | \[in H 2 0\] | mm H 2 0 | \[in H 2 0\] |
| All ratings | 508 | \[20\] | 1270 | \[50\] |
| 2000 and above | 355 | \[14\] | 889 | \[35\] |
| 1500 to 1900 | 305 | \[12\] | 762 | \[30\] |
| **9.0 mm \[0.354 in\] Orifice:** | **New/Rebuilt** | **Used** |  |  |
| **RPM** | **mm H** 2 **0** | **\[in H** 2 **0\]** | **mm H** 2 **0** | **\[in H** 2 **0\]** |
| All ratings | 229 | \[9\] | 584 | \[23\] |
| 2000 and above | 203 | \[8\] | 508 | \[20\] |
| 1500 to 1900 | 178 | \[7\] | 457 | \[18\] |
| **10.3 mm \[0.406 in\] Orifice:** | **New/Rebuilt** | **Used** |  |  |
| **RPM** | **mm H** 2 **0** | **\[in H** 2 **0\]** | **mm H** 2 **0** | **\[in H** 2 **0\]** |
| All ratings | 127 | \[5\] | 330 | \[13\] |

If the blowby is higher than normal, check the crankcase breathers and breather tubes to see if they are plugged.

1. Wing nut
2. Washer
3. Breather cap
4. Screen mesh
5. Breather element
6. Breather base.

![[br8etha.png]]

Check the engine oil level. If the level is too high, it can cause a higher than normal crankcase pressure.

![[oi900sb.png]]

> [!danger] WARNING · Опасно
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.

Isolate the turbocharger to determine if the high crankcase pressure is due to seal leakage in the turbocharger.

Disconnect the turbocharger drain line from the oil pan adaptor.

Install a hose assembly with the two shutoff valves arranged as shown. Place the other hose in an 8 to 19 liter \[2 to 5 gallon\] bucket.

> [!note] Note · Примечание
> The valves **must** have a minimum inside diameter of 19 mm \[0.75 in\].

![[eg4tohe.png]]

Close the valve (A) that allows the oil to drain to the bucket.

![[eg4toka.png]]

Open the valve (B) that allows the oil to drain into the engine.

![[eg4tokb.png]]

> [!warning] CAUTION · Осторожно
> Do not operate the engine with valve A open and valve B closed for more than 1 minute. Operation for more than 1 minute can result in severe engine damage.

Operate the engine at rated speed. Record the blowby value.

Continue operating at rated speed and load. Open valve A and close valve B. Record the blowby reading.

![[tb4tosa.png]]

Compare the value to the original reading. If the blowby is **now** acceptable, replace the turbocharger.

[[20-010-033-tr — Turbocharger|Refer to Procedure 010-033 in Section 10.]]

![[tb400ma.png]]

Isolate the air compressor to determine if it is malfunctioning and causing the high blowby pressure.

Relieve the air pressure on the first air tank in the system after the air compressor (wet tank).

Disconnect the air inlet and outlet connections. Plug the intake manifold or air piping where the inlet connection was removed.

![[cp4tbma.png]]

Operate the engine at rated speed and full load (wide open throttle) until a steady blowby reading is obtained.

Compare the blowby readings to the previous value. If the blowby is **now** acceptable, replace the air compressor.

[[20-012-014-tr — Air Compressor|Refer to Procedure 012-014 in Section 14.]]

![[cp400hi.png]]

A sudden increase in blowby or a high reading that is **not** steady indicates that there is internal damage in the engine. To determine which cylinder is at fault. [[00-014-012 — Engine Compression|Refer to Procedure 014-012 in Section 14.]]

![[ew800sa.png]]

Use Pressure Gauge, Part Number 3375275, or equivalent, to measure lubricating oil pressure.

Install the pressure gauge to the main oil rifle (1) or oil filter head (2).

Low Idle (minimum allowable) 138 kPa \[20 psi\]

At 1200 rpm (minimum allowable) 207 kPa \[30 psi\]

![[ov400ha.png]]

Measure the coolant pressure at the water manifold (1).

| Coolant Pressure with Closed Thermostat and No Pressure Cap |  |  |
|---|---|---|
| kpa |  | psi |
| 241 | MAX | 35 |

![[14400009.png]]

To measure lubricating oil temperature; [[20-007-038 — Lubricating Oil Temperature Gauge|Refer to Procedure 007-038 in Section 7.]]

![[07400021.png]]

All air compressors that are manufactured by Cummins Inc. **must** be operating during the engine run-in. During the performance check, all air compressors **must** be in the unload or non-operating mode.

Connect a source of compressed air capable of producing 665 kPa \[95 psi\] to the air compressor unloader (1). This air line **must** contain a valve between the source and the unloader.

The compressed air load in the accompanying illustration **must** be attached to the air compressor outlet (2).

![[cp8vawa.png]]

Use an air tank (2). Install an air regulator (3) capable of maintaining 345 to 517 kPa \[50 to 75 psi\] air pressure at both minimum and maximum engine rpm.

Install a steel tube or high temperature hose (1).

| Measurements |  |  |
|---|---|---|
|  | celsius | fahrenheit |
| Hose Temperature (Minimum) | 260 | 500 |

Connect the tube or hose (1) to the air compressor outlet.

![[cp8tohc.png]]

> [!note] Note · Примечание
> If another method of starting the engine is used, follow the manufacturer's instructions to make the necessary connections.

Inspect the voltage rating on the starting motor before installing the electrical wiring.

Install the electrical wiring to the starting motor and batteries, if used.

![[sb8coma.png]]
