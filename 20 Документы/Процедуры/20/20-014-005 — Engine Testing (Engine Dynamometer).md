---
aliases:
  - "Испытание двигателя (на моторном стенде)"
type: "Процедура"
doc: "20-014-005"
title_en: "Engine Testing (Engine Dynamometer)"
title_ru: "Испытание двигателя (на моторном стенде)"
modified: "2006-07-10"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 68
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-005.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-014-005.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Engine Testing (Engine Dynamometer)
**Испытание двигателя (на моторном стенде)**

> [!abstract] Процедура · `20-014-005`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-07-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-005.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-014-005.pdf)

### General Information

This document provides procedures for the use of an engine control. The engine control is a portable, handheld electronic control, used to start and control engine speed on Cummins® electronic engines. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a datalink provision to connect to an electronic service tool to monitor engine operation and fault codes. The engine control harnesses required for the engines are purchased separately. The engine control and engine control harnesses are designed to be used with both (+) 12-VDC and (+) 24-VDC battery systems.

> [!note] Note · Примечание
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the electronic control module (ECM). After the testing/repair is complete, reload the correct frequency throttle calibration.

![[ck800wa.png]]

### Setup

Make sure the dynamometer capacity is sufficient to permit testing at 100 percent of the engine's rated horsepower. If the capacity is **not** enough, the testing procedure **must** be modified to the restrictions for the dynamometer.

Use engine lifting fixture, Part Number 3162871, to install the engine to the test stand. Align and connect the dynamometer. See the manufactures instructions for aligning and testing the engine.

Refer to Service Bulletin 3666005, Dynamometer and Road Engine Testing, for detailed instructions on auxiliary aftercooling system attachment.

![[nobox.png]]

Air Compressor

All air compressors manufactured by Cummins® **must** operate loaded during the engine run-in.

During the performance check, all air compressors **must** be in the unloaded or non-operating mode.

To unload the compressor, connect a source of compressed air capable of producing 665 kPa \[95 psi\] to the air compressor unloader. This air line (1) **must** contain a valve between the air source and the unloader.

![[14400052.png]]

To load the compressor use an air tank (2), install an air regulator (3) capable of maintaining 345 to 517 kPa \[50 to 75 psi\] of air pressure at both minimum and maximum engine rpm.

Install a steel tube or high temperature hose (1).

The compressed air load in the accompanying illustration **must** be attached to the air compressor outlet (4).

| celsius |  | fahrenheit |
|---|---|---|
| 235 | MIN | 500 |

![[14400053.png]]

Mechanically Actuated Injector

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.

Connect the engine control harness, Part Number 3163891, 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

Electronically Actuated Injector

Use INSITE™ electronic service tool to monitor engine coolant temperature. Install a coolant pressure sensor, if needed.

![[14c00040.png]]

Coolant Plumbing

Connect the coolant supply to the water inlet connection.

Connect the coolant return to the water outlet connection.

Install the drain plugs and close all of the water drain cocks.

Open the coolant vents.

Low temperature aftercooler engines require connecting the low temperature aftercooler water lines to a remote heat exchanger.

Charge air cooled engines require a remote heat exchanger to cool the intake air.

Marine heat exchanger engines require fresh water supplied to the raw water pump to cool the engine. Marine keel cooled engines require a remote heat exchanger or radiator to cool the engine.

![[08400044.png]]

Intake Air Temperature Control

The use of a remote heat exchanger is mandatory when a Cummins® low temperature aftercooler engine is attached to an engine dynamometer for the purpose of engine run-in, performance testing and engine diagnostics. Do **not** attempt to operate a Cummins® low temperature aftercooler engine without any means of controlling the intake manifold air temperature.

1. Aftercooler water out
2. Aftercooler water in
3. Water out to drain
4. Cool water in

![[10400042.png]]

LTA

Used **only** on engines with mechanically actuated injectors.

> [!note] Note · Примечание
> The heat exchanger **must** be sized to maintain 70°C \[160°F\] maximum intake air temperature at full power.

All QSK19 ratings of 601 horsepower and above require low temperature aftercooling and, therefore, have unique radiator requirements. The ratings of 600 HP and below do **not** require low temperature aftercooler. The low temperature aftercooler is a one-pump, two-loop cooling system.

1. Water in
2. Thermostat housing
3. low temperature aftercooler out
4. Water out
5. Low temperature aftercooler return

![[10400043.png]]

Electronically Actuated Injector

The use of a remote heat exchanger is mandatory when a Cummins® charge air cooled engine is attached to an engine dynamometer for the purpose of engine run-in, performance testing and engine diagnostics. Do **not** attempt to operate a Cummins® charge air cooled engine without any means of controlling the intake manifold air temperature to approximately 49° C \[120° F\] at rated power.

1. Charge air in
2. Air out
3. Cool fresh water in
4. Warm fresh water to drain.

![[10400042.png]]

> [!warning] CAUTION · Осторожно
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.

Remove the large plug from the oil cooler housing.

![[14400011.png]]

Use a pump capable of supplying 207 kPa \[30 psi\] continuous pressure. Connect the pump to the front of the engine oil cooler as shown.

Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

Turn the pump off when the oil level reaches the low level on the dipstick.

![[pl4hoha.png]]

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.

Make sure the cooling system vents on the engine are open. Fill the engine with coolant.

Check the engine coolant level to be sure it is filled to the proper level.

Refer to Procedure [[20-008-018-tr — Cooling System|008-018]].

![[ra200sa.png]]

Check the engine lubricating oil level to be sure it is filled to the proper level.

> [!note] Note · Примечание
> Use a known source of good quality number 2 diesel fuel.

This is very important since number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuel. The lighter the fuel, the lower the energy content (BTU) per gallon (liter, etc.).

![[oi900sb.png]]

Engine Throttle Control

Mechanically Actuated Injectors

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Disconnect the battery cables before beginning the following procedure.

Disconnect the OEM harness from the electronic control module (ECM) if applicable.

![[22c00141.png]]

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness, if connected.

Connect the engine control harness, Part Number 3163891.

Connect the 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

> [!note] Note · Примечание
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3168895.

Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™ 5 datalink adapter kit, Part Number 4918416, (3) and a personal computer to the datalink connector of the engine control.

![[22c00125.png]]

Engines that are run on an engine dynamometer require the engine harness be installed and connected to the engine. Additionally, the engine control, Part Number 3163890, **must** be used to properly control the engine during the dynamometer run.

![[wr8coac.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Connect battery power to the starter.

Connect the dynamometer test OEM wiring harness starter solenoid lead (yellow) to the starter solenoid. Connect the ground lead (black) to the starter solenoid. Connect the ground lead (black) to the starter or battery negative (-) or ground side. Connect the (+) 12 VDC power lead (red) to either the starter or battery positive (+) 12 VDC side.

![[sb8coma.png]]

Rotate the throttle knob fully **counterclockwise**. Push down on the throttle knob to return the throttle to the idle position.

Repeat this step three times.

Turn the keyswitch to the OFF position for 30 seconds.

![[22c00156.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

Electrically Actuated Injectors

Disconnect the OEM harness 16-pin and 23-pin Deutsch connectors from the engine harness if connected.

Connect the engine control harness Part Number 4918643.

Remove the 3-pin Deutsch terminating resistor cap (cap will have a blue insert) from the wiring harness.

Connect the engine control harness 3-pin Deutsch connector to the SAE J1939 Datalink connector of the engine wiring harness.

The 3-pin Deutsch terminating resisting cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.

![[22400280.png]]

Ground Connection

Connect the black-wire alligator clip of the engine control harness to the engine block to achieve electrical ground.

![[19c01031.png]]

> [!warning] CAUTION · Осторожно
> Do not connect the alligator clip to the starter motor solenoid “S” terminal. Doing so can cause equipment damage.

Starter Connection

If **not** already equipped, install and wire a starter magnetic switch.

Clip the alligator connector to the positive (+) coil terminal of the starter magnetic switch.

![[22400055.png]]

Air Starter

If an air starter is being used, coil the red wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.

![[19c01032.png]]

Engine Operation

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Attach the engine control harness using the ring terminal of the red wire to the positive (+) terminal of the battery.

Attach the engine control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.

![[22c00141.png]]

> [!warning] CAUTION · Осторожно
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Equipment or engine damage can result if not connected properly.

The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.

If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.

Turn the keyswitch to the ON position.

![[22c00127.png]]

Light indicators on the engine control, STOP, WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.

If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the OEM service literature to diagnose the engine fault code.

![[22c00128.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

> [!note] Note · Примечание
> The engine can be returned to idle at any time by pushing in on the throttle knob.

Slowly rotate the throttle knob **counterclockwise** to increase the engine rpm.

Slowly rotate the throttle knob **clockwise** to decrease the engine rpm.

![[22c00130.png]]

Turn the keyswitch to the OFF position to stop the engine.

![[22c00131.png]]

Mechanically Actuated Injector

> [!note] Note · Примечание
> Some engines are equipped with fittings used for Compuchek™ testing sensors. The sensor probes used for Compuchek™ and dynamometer testing are **not** compatible. If the same location is used, remove the Compuchek™ fitting and install adapters for the dynamometer sensor.

Install the coolant pressure sensor (1).

Install the coolant temperature sensor (2).

![[19400310.png]]

Return parameters to their original value when the test or run-in is complete.

Connect the keyswitch panel datalink cable to the Cummins® electronic service tool.

Use INSITE™ electronic service tool to set the engine up for the dynamometer. Refer to Procedure [[20-014-008 — Engine Testing (In Chassis)|014-008]] for more information on this feature.

The setup is now complete, and the auto/manual throttle can be used to control engine speed.

![[14c00040.png]]

Engine operating specifications are available from your Cummins® Authorized Repair Location.

![[lt800ga.png]]

### Test

The INSITE™ electronic service tool will provide most, if **not** all, of the parameters.

To properly monitor engine performance, record the following parameters. To limit dynamometer operating time, instrument the engine to make as many checks as possible.

- Engine speed rpm with a verified tachometer
- Fuel pressure
- Fuel rate (use service tool, Part Number 3376375, or equivalent)
- Fuel temperature (if needed to correct fuel rate)
- Fuel inlet restriction
- Fuel drain line restriction
- Intake manifold pressure.
- Intake air restriction
- Exhaust restriction
- Coolant temperature
- Engine blowby
- Lubricating oil pressure
- Coolant pressure
- Intake manifold air temperature
- Turbocharger inlet air temperature.

![[nobox.png]]

Engine Speed (rpm)

Use INSITE™ electronic service tool to monitor engine speed. Observe and record the engine speed.

Or use digital optical tachometer, Part Number 3377462, or equivalent, to check and verify engine speed.

![[er2tova.png]]

Fuel Pressure

Mechanically Actuated Injectors

Check fuel supply pressure. Refer to Procedure [[20-005-016-tr — Fuel Pump|005-016]].

![[05500009.png]]

Fuel Rate

Mechanically Actuated Injector

Use fuel measuring device, Part Number 3376375, or equivalent, to measure the rate of fuel consumption.

![[eg8togf.png]]

Fuel Inlet Restriction

Mechanically Actuated Injectors

Measure the fuel inlet restriction. Install a vacuum gauge, Part Number ST-434, or equivalent, between the fuel filter and the gear pump inlet.

> [!note] Note · Примечание
> Do **not** measure fuel inlet restriction with the fuel measuring device installed. This will **not** measure the inlet restriction of the vehicle's supply plumbing.

Electronically actuated injector refer to Procedure 006-020.

![[06400054.png]]

Fuel Drain Line Restriction

Mechanically Actuated Injectors

Use Pressure Gauge, Part Number ST-1273, or equivalent, to measure fuel drain line restriction.

> [!note] Note · Примечание
> Do **not** measure fuel drain line restriction with the fuel measuring device installed. This will **not** measure the drain line restriction of the vehicle's return plumbing.

Refer to Procedure [[20-006-012 — Fuel Drain Line Restriction|006-012]].

![[06400051.png]]

Intake Manifold Pressure

Measure the intake manifold pressure (turbocharger boost). Install pressure gauge, Part Number ST-1273, or equivalent, in the intake manifold as shown.

Refer to Procedure 010-057.

Observe the reading on the pressure gauge. Or use INSITE™ electronic service tool.

![[06400102.png]]

Intake Air Restriction

Measure the inlet air restriction. Install the vacuum gauge, Part Number ST-434, or equivalent, or a manometer in the intake air piping.

> [!note] Note · Примечание
> The gauge adapter **must** be installed at a 90 degree angle to the air flow in a straight section of pipe at a minimum of one pipe diameter before the turbocharger.

Or use INSITE™ electronic service tool.

Refer to Procedure [[20-010-031 — Air Intake Restriction|010-031]].

![[10400011.png]]

Exhaust Air Restriction

Measure the exhaust air restriction. Install the pressure gauge, Part Number ST-1273, or equivalent, or a manometer in the exhaust air piping.

The gauge adapter **must** be installed near the turbocharger in a straight section of pipe at the turbine outlet.

Refer to Procedure [[20-011-009 — Exhaust Restriction|011-009]].

![[pe4cokb.png]]

Engine Blowby

Excessive blowby indicates an air compressor, a turbocharger, or an engine malfunction, allowing combustion gases or air to enter the crankcase and build a pressure higher than normal.

This procedure describes how to measure crankcase pressure and how to determine the component that is malfunctioning, or use INSITE™ electronic service tool.

Use one of the three blowby service tools and a water manometer, Part Number ST-1111-3, or equivalent. Maximum gauge capacity is 1270 mm-H 2 0 \[50 in-H 2 0\]. The engine blowby tools are similar in design. The difference between the tools is in the size of the orifice.

| Blowby Tool Part Number | Orifice Size \[inch\] |
|---|---|
| 3822566 | \[0.302\] |
| 3823567 | \[0.354\] |
| 3822568 | \[0.406\] |

![[eg8toga.png]]

Use a length of hose (1) to attach the blowby tool to one of the crankcase breathers.

Plug all of the other breathers.

Attach a manometer to the location shown (2).

![[14400010.png]]

A sudden increase in blowby indicates a problem. A gradual increase over a period of time is normal (due to wear of internal engine components).

Operate the engine at rated rpm and full load (wide open throttle) until a steady reading is obtained.

Compare the blowby readings to previous readings on the engine. If previous readings for the engine are **not** available, compare the blowby reading to new engine specifications.

![[eg8toja.png]]

| QSK19 Blowby Limits (using 0.302 inch diameter orifice at rated load and speed) |  |  |
|---|---|---|
| Engine HP (RPM Rating) | New/Rebuilt | Used Engine Limit |
| 699 HP and Below (1500 - 1900) | 305 mm H 2 O \[12 in H 2 O\] | 762 mm H 2 O \[30 in H 2 O\] |
| 699 HP and Below (2000 and above) | 355 mm H 2 O \[14 in H 2 O\] | 889 mm H 2 O \[35 in H 2 O\] |
| 700 HP and Above | 508 mm H 2 O \[20 in H 2 O\] | 1270 mm H 2 O \[50 in H 2 O\] |

| QSK19 Blowby Limits (using 0.354 inch diameter orifice at rated load and speed) |  |  |
|---|---|---|
| Engine HP (RPM Rating) | New/Rebuilt | Used Engine Limit |
| 699 HP and Below (1500 - 1900) | 178 mm H 2 O \[7 in H 2 O\] | 457 mm H 2 O \[18 in H 2 O\] |
| 699 HP and Below (2000 and above) | 203 mm H 2 O \[8 in H 2 O\] | 508 mm H 2 O \[20 in H 2 O\] |
| 700 HP and Above | 229 mm H 2 O \[9 in H 2 O\] | 584 mm H 2 O \[23 in H 2 O\] |

| QSK19 Blowby Limits (using 0.406 inch diameter orifice at rated load and speed) |  |  |
|---|---|---|
| Engine HP (RPM Rating) | New/Rebuilt | Used Engine Limit |
| All Ratings | 127 mm H 2 O \[5 in H 2 O\] | 330 mm H 2 O \[13 in H 2 O\] |

If the blowby is higher than normal, check the crankcase breathers and breather tubes to see if they are plugged.

1. Wing Nut
2. Washer
3. Breather
4. Screen mesh
5. Breather element
6. Breather base

The breather is located inside the housing on electronically actuated injector.

![[br8etha.png]]

Check the engine oil level. If the level is too high it can cause a higher than normal crankcase pressure.

![[oi900sb.png]]

Isolate the turbocharger to determine if the high crankcase pressure is due to seal leakage in the turbocharger.

Disconnect the turbocharger drain line from the oil pan adaptor.

Install a hose assembly with the two shutoff valves arranged as shown. Place the other hose in an 8 to 19 liter \[2 to 5 gallon\] bucket.

> [!note] Note · Примечание
> The valves **must** have a minimum inside diameter of 19 mm \[0.75 inch\].

![[eg4tohe.png]]

Close the valve (A) that allows the oil to drain to the bucket.

![[eg4toka.png]]

Open the valve (B) that allows the oil to drain into the engine.

![[eg4tokb.png]]

> [!warning] CAUTION · Осторожно
> When testing the turbocharger for any contribution to blowby, do not operate the engine with valve A open and valve B closed for more than 1 minute. Operation for more than 1 minute can result in severe engine damage.

Operate the engine at rated speed.

Continue operating at rated speed and load. Open valve A and close valve B. Record the blowby reading.

![[tb4tosa.png]]

Compare the value to the original reading. If the blowby is now acceptable, replace the turbocharger.

Refer to Procedure [[20-010-033-tr — Turbocharger|010-033]].

![[tb400ma.png]]

Isolate the air compressor to determine if it is malfunctioning and causing the high blowby pressure.

Relieve the air pressure on the first air tank in the system after the air compressor (wet tank).

Disconnect the air inlet and outlet connections. Plug the intake manifold or air piping where the inlet connection was removed.

![[cp4tbma.png]]

Operate the engine at rated speed and full load (wide open throttle) until a steady blowby reading is obtained.

![[cp400hi.png]]

Compare the blowby readings to the previous value. If the blowby is now acceptable, replace the air compressor.

Refer to Procedure [[20-012-014-tr — Air Compressor|012-014]].

![[nobox.png]]

A sudden increase in blowby or a high reading that is **not** steady indicates that there is internal damage in the engine.

![[ew800sa.png]]

Lubricating Oil Pressure

> [!warning] CAUTION · Осторожно
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.

Use pressure gauge, Part Number 3375275, or equivalent, to measure lubricating oil pressure, or use INSITE™ electronic service tool.

Install the pressure gauge to the main oil rifle (1) or oil filter head (2).

| kpa |  | psi |
|---|---|---|
| 138 | MIN | 20 |
| 207 | NOM | 30 |

![[ov400ha.png]]

Engine Coolant Pressure

Measure the coolant pressure at the water manifold (1), or the thermostat housing l.

| kpa |  | psi |
|---|---|---|
| 241 | NOM | 35 |

![[14400009.png]]

High Engine Oil Temperature

Measure the lubricating oil temperature. Install a reference gauge to verify the reading of the suspect gauge. Refer to Procedure [[20-007-038 — Lubricating Oil Temperature Gauge|007-038]]. Or use INSITE™ electronic service tool to measure the oil temperature.

![[07400021.png]]

All air compressors manufactured by Cummins Inc. **must** operate loaded during the engine run-in.

During the performance check, all air compressors **must** be in the unloaded or non-operating mode.

To unload the compressor, connect a source of compressed air capable of producing 665 kPa \[95 psi\] to the air compressor unloader. This air line (1) **must** contain a valve between the air source and the unloader.

![[14400052.png]]

Use an air tank (2). Install an air regulator (3) capable of maintaining 345 to 517 kPa \[50 to 75 psi\] air pressure at both minimum and maximum engine rpm at 260°C \[500° F\].

Install a steel tube or high temperature hose (1).

Connect the tube or hose (1) to the air compressor outlet.

![[cp8tohc.png]]

Starting Motor

> [!note] Note · Примечание
> If another method of starting the engine is used, follow the manufacturer's instructions to make the necessary connections.

Inspect the voltage rating on the starting motor before installing the electrical wiring.

Install the electrical wiring to the starting motor and batteries, if used.

![[sb8coma.png]]

> [!warning] CAUTION · Осторожно
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Equipment or engine damage can result if not connected properly.

The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.

If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.

Turn the keyswitch to the ON position.

![[22c00127.png]]

Light indicators on the engine control, STOP, WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.

If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the OEM service literature to diagnose the engine fault code.

![[22c00128.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

> [!note] Note · Примечание
> The engine can be returned to idle at any time by pushing in on the throttle knob.

Slowly rotate the throttle knob **counterclockwise** to increase the engine rpm.

Slowly rotate the throttle knob **clockwise** to decrease the engine rpm.

![[22c00130.png]]

Turn the keyswitch to the OFF position to stop the engine.

![[22c00131.png]]
