---
aliases:
  - "Испытание двигателя (на моторном стенде)"
type: "Процедура"
doc: "101-014-005-tr"
title_en: "Engine Testing (Engine Dynamometer)"
title_ru: "Испытание двигателя (на моторном стенде)"
modified: "2014-07-03"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 25
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-005-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-005-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/101"
---

# Engine Testing (Engine Dynamometer)
**Испытание двигателя (на моторном стенде)**

> [!abstract] Процедура · `101-014-005-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2014-07-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/101/101-014-005-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/101-014-005-tr.pdf)

### Setup

> [!note] Note · Примечание
> Due to the large number of engine models and their applications, this procedure has been written to be generic. Illustrations within this procedure will **not** represent all engines and applications.

> [!note] Note · Примечание
> Make sure the dynamometer capacity is sufficient to permit testing at 100 percent of the engine's rated horsepower. If the capacity is **not** high enough, the testing procedure **must** be modified to the restrictions of the dynamometer.

Use engine lifting fixture, Part Number 3162871, to install the engine test stand. Align and connect the dynamometer. Refer to the manufacturer's instructions for aligning and testing the engine.

![[ck800wa.png]]

Coolant Plumbing

Connect the coolant supply to the water inlet connection.

Connect the coolant return to the water outlet connection.

Install the drain plugs and close all of the water drain cocks.

![[08c00129.png]]

Intake Air Temperature Control

The use of a remote aftercooler is mandatory whenever a Cummins® charge-air cooled engine is attached to an engine dynamometer for the purpose of engine run-in, performance testing, and/or engine diagnostics. Do **not** attempt to run a Cummins® charge-air cooled engine without a means of controlling the intake manifold air temperature. Dynamometer-room charge-air cooler, Part Number 3823978, utilizes twin Big Cam™ III aftercooler assemblies arranged for parallel air and water flow to cool the intake air to acceptable levels.

![[nobox.png]]

The parallel airflow circuit heat exchangers provide optimum performance by delivering air to the mixer at temperatures no higher than 66°C \[151°F\], and with less than the maximum allowable intake air pressure drop. The remote aftercooler removes energy from the intake air that is compressed and heated by the turbocharger to temperatures as high as 210°C \[410°F\] and then cooled to temperatures of 66°C \[151°F\] using city water at 16°C \[61°F\].

1. Water in
2. Aftercooler number 1 (2 pass)
3. Aftercooler number 2 (2 pass)
4. Water out
5. Condensate
6. From turbocharger
7. To intake manifold
8. Thermocouple (Fluke™).

![[at100pb.png]]

Water from a city tap line flows to the aftercooler through a 25.4 mm \[1-inch\] inner diameter neoprene hose. Testing has shown that 45.4 liter \[12 gal\] per minute city water flow is required (22.7 liter \[6 gal\] per minute per aftercooler core) to adequately cool the intake air for the 435 through 500 horsepower-rated engines. A typical garden hose is **not** suitable for this flow, due to the excessive restriction. A low-restriction ball-type or gate valve is suitable for the operation, provided that the required flow rates are achieved.

Water returns to the drain or reservoir from the aftercoolers through a 25.4 mm \[1-inch\] inner diameter hose. A low-restriction gate valve or ball valve **must** be placed on the drain line(s) to regulate water flow through the aftercoolers. This provides the ability to maintain optimum intake air temperature during the test or run-in procedure.

The condensate that will develop as the intake air is cooled in the remote aftercooler is allowed to drain at all times through a hole at the bottom of the tubular steel manifold between the aftercoolers. This fitting **must** remain unobstructed throughout each use of the aftercoolers.

> [!note] Note · Примечание
> Some air will escape through the condensate drain opening, but it is insignificant compared to the total airflow.

1. Air in from turbocharger compressor outlet
2. Lifting eye
3. Air out to engine intake manifold
4. Water in to aftercooler
5. Water out to drain
6. Condensate drain.

![[at1bdpa.png]]

The airflow piping requires a 101.6 mm \[4 in\] inner diameter aluminum steel piping. The flow circuit **must** have as few bends as possible, maximizing the length of straight sections. However, when bends are required, use long elbows. Do **not** use square elbows or anything that changes the airflow direction quickly. To reduce intake air restriction, airflow direction changes **must** occur gradually.

![[14c00054.png]]

Air Compressor

> [!note] Note · Примечание
> All air compressors manufactured by Cummins Inc. **must** operate during the engine run-in. During the performance check, all air compressors **must** be in the unloaded or non-operating mode.

Connect a source of compressed air capable of producing 665 kPa \[96 psi\] to the air compressor unloader (1). This air line **must** contain a valve between the air source and the unloader.

> [!note] Note · Примечание
> The compressed air load in the accompanying illustration **must** be attached to the air compressor outlet (2).

![[14c00013.png]]

Use an air tank (2). Install an air regulator (3) capable of maintaining 345 to 517 kPa \[50 to 75 psi\] of air pressure at both minimum and maximum engine rpm.

Install a steel tube or high temperature hose (1).

| Hose Temperature |  |  |
|---|---|---|
| celsius |  | fahrenheit |
| 235 | MIN | 500 |

Connect the tube or hose (1) to the air compressor outlet.

![[14400053.png]]

Starting Motor

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Inspect the voltage rating on the starting motor before installing the electrical wiring.

Install the electrical wiring to the starting motor and batteries, if used.

If another method of starting the engine is used, follow the manufacturer's instructions to make the necessary connections.

![[sb8coma.png]]

Engine Throttle Control

Engines operating on an engine dynamometer **must** have the engine harness installed and connected to the engine. Additionally, the engine controller harness, Part Number 3164242, and engine controller, Part Number 3163890, **must** be used to properly control the engine during the dynamometer run.

Connect the engine controller harness Deutsch™ connector to the engine control module (ECM) original equipment manufacturer (OEM) port.

![[14c00055.png]]

Return parameters to their original value when the test or run-in is complete.

![[19r00163.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Connect battery power to the starter.

Connect the dynamometer test OEM wiring harness starter solenoid lead (yellow) to the starter solenoid. Connect the ground lead (black) to the starter or battery negative (-) or ground side. Connect the +12-VDC power lead (red) to either the starter or battery positive (+12-VDC) side.

![[sb8coma.png]]

Connect the keyswitch panel data link cable to the Cummins® electronic service tool.

Use INSITE™ electronic service tool to set the engine up for the dynamometer. [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14]] for more information on this feature.

The setup is now complete, and the auto/manual throttle can be used to control engine speed.

![[19r00163.png]]

### Test

To monitor engine performance correctly, record the following parameters. To limit dynamometer operating time, instrument the engine or use INSITE™ electronic service tool to make as many checks as possible.

- Engine speed (rpm)
- Fuel rate
- Intake manifold air temperature
- Engine blowby
- Engine coolant pressure
- Engine coolant temperature
- Rail fuel pressure, if applicable
- Engine fule temperature, if needed to correct fuel rate
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

See the Fuel Flow Measurement on Engine or Chassis Dynamometer in this section.

Adjust the fuel rate reading to compensate for temperature variation if required.

| Fuel Inlet Temperature |  |  |
|---|---|---|
| celsius |  | fahrenheit |
| 7.2 | MIN | 45 |
| 55.5 | MAX | 132 |

![[nobox.png]]

Intake Manifold Air Temperature Control - Chassis Dynamometer test

When operating an engine on a chassis dynamometer, lock the cooling fan in the ON position for best results.

If the unit does **not** have a manual fan switch, use INSITE™ electronic service tool/Set Up for Dynamometer feature to lock the fan in the ON position. [[101-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14.]]

![[19r00163.png]]

Use INSITE™ electronic service tool to monitor the intake manifold air temperature.

Observe and record the intake manifold air temperature.

The intake manifold air temperature **must not** exceed the maximum allowable temperature. See the Specifications - Engine Testing page in this section for the maximum allowable intake manifold air temperature. The engine protection system will disrupt performance if the temperature exceeds this level. Maintain the intake manifold air temperature below the maximum allowable temperature during chassis dynamometer operation.

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

See the Specifications - Engine Testing page in this section for the maximum allowable engine coolant pressure.

![[14c00053.png]]

Engine Coolant Temperature

Use INSITE™ electronic service tool to monitor engine coolant temperature.

Observe and record the engine coolant temperature.

See the Specifications - Engine Testing page in this section for the maximum allowable coolant temperature.

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
