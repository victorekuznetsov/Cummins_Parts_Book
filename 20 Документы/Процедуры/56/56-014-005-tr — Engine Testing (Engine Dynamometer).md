---
aliases:
  - "Испытание двигателя (на моторном стенде)"
type: "Процедура"
doc: "56-014-005-tr"
title_en: "Engine Testing (Engine Dynamometer)"
title_ru: "Испытание двигателя (на моторном стенде)"
modified: "2023-07-12"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 41
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-005-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-005-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Engine Testing (Engine Dynamometer)
**Испытание двигателя (на моторном стенде)**

> [!abstract] Процедура · `56-014-005-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 14 - Engine Testing - Group 14 · Section 14 Engine Testing - Group 14
> **Даты:** изменён 2023-07-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-005-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-005-tr.pdf)

### General Information

This document provides procedures for the use of an engine control, Part Number 3163890. The engine control is a portable, handheld electronic control, used to start and control engine speed on the Cummins® electronic engines. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a datalink provision to connect to an electronic service tool to monitor engine operation and fault codes. The engine control harnesses required for the engines are purchased separately. The engine control and engine control harnesses are designed to be used with both (+) 12-VDC and (+) 24-VDC battery systems.

> [!note] Note · Примечание
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the electronic control module (ECM). After the testing/repair is complete, reload the correct frequency throttle calibration.

### Install

> [!note] Note · Примечание
> : Make sure the dynamometer capacity is sufficient to permit testing at 100 percent of the engine's rated horsepower. If the capacity is not enough, the testing procedure **must** be modified to the restrictions of the dynamometer.

Use engine lifting fixture, Part Number 3163264, to install the engine to the test stand. Align and connect the dynamometer. See the manufacturer's instructions for aligning and testing the engine.

![[00600042.png]]

Coolant Plumbing

Connect the coolant supply to the water inlet connection.

Connect the coolant return to the water outlet connection.

Install the drain plugs, and close all of the water draincocks.

> [!note] Note · Примечание
> : LTA engines require connecting the LTA water lines to a remote heat exchanger.

![[08400044.png]]

Intake Air Temperature Control

The use of a remote heat exchanger is mandatory whenever a Cummins LTA engine is attached to an engine dynamometer for the purpose of engine run-in, performance testing, and/or engine diagnostics. Do **not** attempt to run a Cummins® LTA engine with out any means of controlling the intake manifold air temperature.

1. Aftercooler water out
2. Aftercooler water in
3. Cooling water out to drain
4. Cooling water in.

![[10400042.png]]

LTA

All QSK45 and QSK60 industrial engines require LTA and, therefore, have unique radiator requirements.

The heat exchanger **must** be sized to maintain 70°C \[158°F\] maximum intake air temperature at full power.

1. Cooling water in
2. Thermostat housing
3. LTA out
4. Cooling water out
5. LTA return.

![[10400043.png]]

Engine Throttle Control

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Mechanically Actuated Injectors

Disconnect the battery cables before beginning the following procedure.

Disconnect the OEM harness from the electronic control module (ECM), if applicable.

![[22c00141.png]]

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.

Connect the engine control harness, Part Number 4918643.

Connect the engine control harness 21-pin and 31 pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

> [!note] Note · Примечание
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.

Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™5 datalink adapter kit (3), Part Number 4918416,, and a personal computer to the datalink connector of the engine control.

![[22c00125.png]]

Engines that are run on an engine dynamometer require the engine harness be installed and connected to the engine. Additionally, the engine control, Part Number 3163890, **must** be used to properly control the engine during the dynamometer run.

![[wr8coac.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Connect battery power to the starter.

Connect the dynamometer test OEM wiring harness starter solenoid lead (yellow) to the starter solenoid. Connect the ground lead (black) to the starter solenoid. Connect the ground lead black) to the starter or battery negative (-) or ground side. Connect the (+) 12 VDC power lead red) to either the starter or battery positive (+) 12 VDC side.

![[sb8coma.png]]

Rotate the throttle knob fully **counterclockwise**.

Push down on the throttle knob to return the throttle to the idle position.

Repeat this step three times.

Turn the keyswitch to the OFF position for 30 seconds.

![[22c00155.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

with Electronically Actuated Injector

Disconnect the OEM harness 16-pin and 23-pin Deutsch connectors from the engine harness, if connected.

Remove the 3-pin Deutsch terminal resistor cap (cap will have a blue insert) from the wiring harness.

Connect the engine control harness 3-pin Deutsch connector to the SAE J1939 Datalink connector of the engine wiring harness.

The 3-pin Deutsch terminal resistor cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.

![[22400280.png]]

Ground Connection

Connect the black-wire alligator clip of the engine control harness to the engine block to achieve electrical ground.

![[19c01031.png]]

> [!warning] CAUTION · Осторожно
> Do not connect the alligator clip to the starter motor solenoid “S” terminal. Doing so can cause equipment damage.

Starter Connection

If **not** already equipped, install and wire a magnetic starter switch.

Clip the alligator connector to the positive (+) coil terminal of the magnetic starter switch.

![[22400055.png]]

Air Starter

If an air starter is being used, coil the red wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.

![[19c01032.png]]

Engine Operation

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Attach the control harness using the ring terminal of the red wire to the positive (+) terminal of the battery.

Attach the control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.

Attach the control harness using the ring terminal of the red wire to the positive (+) terminal of the battery. Attach the control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.

![[sb8coma.png]]

> [!warning] CAUTION · Осторожно
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Equipment or engine damage can result if not connected properly.

The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.

If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.

Turn the keyswitch to the ON position.

![[22c00127.png]]

Light indicators on the engine control, STOP,

WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.

If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the OEM service literature to diagnose the engine fault code.

![[22c00128.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00127.png]]

> [!note] Note · Примечание
> The engine can be returned to idle at any time by pushing in on the throttle knob.

Slowly rotate the throttle knob **counterclockwise** to increase the engine rpm.

Slowly rotate the throttle knob **clockwise** to decrease the engine rpm.

![[22c00130.png]]

Turn the keyswitch to the OFF position to stop the engine.

![[22c00131.png]]

Return parameters to their original values when the test or run-in is complete.

Connect the keyswitch panel datalink cable to the Cummins® electronic service tool.

Use INSITE™ electronic service tool to set the engine up for the dynamometer. [[56-014-008-tr — Engine Testing (In Chassis)|Refer to Procedure 014-008 in Section 14 for more information on this feature.]]

The setup is now complete, and the auto/manual throttle can be used to control engine speed.

![[14c00040.png]]

Engine operating specifications are available from Cummins® authorized repair locations.

![[lt800ga.png]]

### Test

> [!warning] CAUTION · Осторожно
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.

Industrial QSK45 and QSK60 engines are equipped with an automatic prelube system from the factory. If the engine is **not** equipped with an automatic prelube system, follow the instructions to prelube the engine manually.

![[14400011.png]]

For engines without an automatic prelube device, use a pump capable of supplying 205 kPa \[30 psi\] continuous pressure.

Remove the pipe plug at the front rear underside of the one-piece lubricating oil filter head.

Install an extended elbow (1) into the rear port the pipe plug was removed from. The final position of this elbow is facing the rear of the engine and slightly inboard to make sure the check valve clears the front filter on the one-piece lubricating filter head.

Tighten the elbow.

> [!tip] Момент затяжки · Torque Value
> 60 n•m [44 ft-lb]

Apply a small amount of Loctite® 641 to the tapered threads of the male adapter (3) and install it into the flow end of the check valve (2).

Apply a small amount of Loctite® 641 to the tapered threads of the extended elbow (1) and install the check valve with the arrow pointing at the elbow in the lubricating oil filter head.

Tighten the check valve.

> [!tip] Момент затяжки · Torque Value
> 48 n•m [35 ft-lb]

Connect the pump to the male adapter.

Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

![[07600483.png]]

Check the engine lubricating oil level to make sure it is filled to the proper level.

![[oi900sb.png]]

Remove the pump.

Remove the elbow (1), check valve (2), and adapter (3) from the lubricating oil filter head.

Install the pipe plug.

![[07600483.png]]

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.

Check the engine coolant level. [[56-008-018-tr — Cooling System|Refer to Procedure 008-018 in Section 8.]]

Use a known source of good-quality number 2 diesel fuel. Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuel. The lighter the fuel, the lower the energy content per gallon (liter).

![[ra200sa.png]]

To properly monitor engine performance, record the following parameters. To limit dynamometer operating time, instrument the engine to make as many checks as possible. The INSITE™ electronic service tool will provide most, if **not** all of the following:

- Engine speed rpm with a verified tachometer
- Fuel pressure
- Fuel rate
- Fuel temperature (if needed to correct fuel rate)
- Fuel inlet restriction
- Fuel drain line restriction
- Intake manifold pressure (per bank).

![[eg200ka.png]]

- Intake air restriction (per bank)
- Exhaust air restriction (per bank)
- Coolant temperature
- Engine blowby
- Lubricating oil pressure
- Coolant pressure
- Inlet manifold air temperature
- Turbocharger inlet air temperature.

![[eg100km.png]]

Engine Speed

Use digital optical tachometer, Part Number 3377462, along with reflective tape, Part Number 3377464, to check the engine speed.

![[er2tova.png]]

> [!note] Note · Примечание
> Do **not** measure fuel drain line restriction with the fuel measuring device installed. This will **not** measure the drain line restriction of the vehicle's return plumbing.

Use pressure gauge, Part Number ST-1273, to measure fuel drain line restriction. [[56-006-012 — Fuel Drain Line Restriction|Refer to Procedure 006-012 in Section 6.]]

![[06400051.png]]

Intake Air Restriction

Install the gauge adapter at a 90-degree angle to the airflow in a straight section of pipe at a minimum of one pipe diameter before the turbocharger.

Install the vacuum gauge, Part Number ST-434, or a manometer, Part Number ST-1111-3, in the intake air piping.

Measure the inlet air restriction.

[[56-010-031 — Air Intake Restriction|Refer to Procedure 010-031 in Section 10.]]

![[10400011.png]]

Exhaust Air Restriction

Install the gauge adapter near the turbocharger in a straight section of pipe at the turbine outlet.

Install the pressure gauge, Part Number ST-1273, or a manometer in the exhaust air piping.

Measure the exhaust air restriction.

[[56-011-009 — Exhaust Restriction|Refer to Procedure 011-009 in Section 11.]]

![[pe4cokb.png]]

Engine Blowby

Measure the crankcase pressure. [[56-014-010-tr — Crankcase Blowby, Measure|Refer to Procedure 014-010 in Section 14.]]

![[eg8toga.png]]

Check the engine oil level. If the level is too high, it can cause a higher than normal crankcase pressure.

![[oi900sb.png]]

Lubricating Oil Pressure

Use pressure gauge, Part Number 3375275, to measure lubricating oil pressure.

Install the pressure gauge to the main oil rifle (1) or air filter head (2).

| Lubricating Oil Pressure |  |  |  |
|---|---|---|---|
|  | kpa |  | psi |
| Low Idle | 138 | MIN | 20 |
| Rated rpm | 413 | MIN | 60 |

![[ov400ha.png]]

Engine Coolant Pressure

Use pressure gauge, Part Number 3375275, to measure lubricating oil pressure.

Install the pressure gauge to the main oil rifle (1) or air filter head (2).

| Lubricating Oil Pressure |  |  |  |
|---|---|---|---|
|  | kpa |  | psi |
| Low Idle | 138 | MIN | 20 |
| Rated rpm | 413 | MIN | 60 |

![[14400009.png]]

Air Compressor

All air compressors manufactured by Cummins Inc. **must** be operating during the engine run-in. During the performance check, all air compressors **must** be in the unloaded or non-operating mode.

Connect a source of compressed air capable of producing 665 kPa \[95 psi\] to the air compressor unloader (1). This air line **must** contain a valve between the source and the unloader.

Attach compressed air load to the air compressor outlet (2).

![[cp8vawa.png]]

Use an air tank (2). Install an air regulator (3) capable of maintaining 345- to 517-kPa \[50- to 75-psi\] air pressure at both **minimum and maximum** engine rpm at 260°C \[500°F\].

Install a steel tube or high-temperature hose (1).

Connect the tube or hose (1) to the air compressor outlet.

![[cp8tohc.png]]

Starting Motor

Inspect the voltage rating on the starting motor before installing the electrical wiring.

Install the electrical wiring to the starting motor and batteries, if used.

> [!note] Note · Примечание
> If another method of starting the engine is used, follow the manufacturer's instructions to make the necessary connections.

![[sb8coma.png]]
