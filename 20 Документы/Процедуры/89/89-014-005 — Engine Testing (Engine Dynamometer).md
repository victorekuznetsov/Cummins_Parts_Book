---
aliases:
  - "Испытание двигателя (на моторном стенде)"
type: "Процедура"
doc: "89-014-005"
title_en: "Engine Testing (Engine Dynamometer)"
title_ru: "Испытание двигателя (на моторном стенде)"
modified: "2023-07-11"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 41
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-014-005.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-014-005.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
---

# Engine Testing (Engine Dynamometer)
**Испытание двигателя (на моторном стенде)**

> [!abstract] Процедура · `89-014-005`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2023-07-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-014-005.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-014-005.pdf)

### General Information

This document provides procedures for the use of an engine control, Cummins® Part Number 3163890. The engine control is a portable, handheld electronic control, used to start and control engine speed on the Cummins® electronic engines. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a data link provision to connect to an electronic service tool to monitor engine operation and fault codes. The engine control harnesses required for the engines are purchased separately. The engine control and engine control harnesses are designed to be used with both (+) 12-VDC and (+) 24-VDC battery systems.

> [!note] Note · Примечание
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the engine control module. After the testing/repair is complete, reload the correct frequency throttle calibration.

![[ck800wa.png]]

### Install

Be certain that the dynamometer capacity is sufficient to permit testing at 100 percent of the engine rated horsepower. If the capacity is **not** enough, the testing procedure **must** be modified to the restrictions of the dynamometer.

Use engine lifting fixture, Cummins® Part Number 3163264, or equivalent, to install the engine to the test stand. Align and connect the dynamometer. See the manufacturers instructions for aligning and testing the engine.

> [!note] Note · Примечание
> Some engines are equipped with fittings used for Compuchek® testing sensors. The sensor probes used for Compuchek® and dynamometer testing are **not** compatible. If the same location is used, remove the Compuchek® fitting and install adapters for the dynamometer sensor.

Install the coolant temperature sensor.

![[14400034.png]]

Coolant Plumbing

Connect the coolant supply to the water inlet connection.

Connect the coolant return to the water outlet connection.

Connect all coolant vent lines to surge tank.

Install the drain plugs and close all the water drain cocks.

![[08400348.png]]

Charge Air Cooled Engines

The use of a remote charge-air cooler is mandatory whenever a Cummins® charge-air cooled engine is attached to an engine dynamometer for the purpose of engine run-in, performance testing and engine diagnostics. Do **not** attempt to run a Cummins® charge-air cooled engine without a means of controlling the intake manifold air temperature. [[89-010-024 — Air Leaks, Air Intake and Exhaust Systems|Refer to Procedure 010-024]] in Section 10 for more information on the charge-air cooled engines.

![[ca200kg.png]]

Test

The lubricating oil system **must** be primed before operating the engine after rebuild to avoid internal component damage.

Remove the large plug from the oil cooler rifle.

![[14400032.png]]

Use a pump capable of supplying 205 kPa \[ 30 psi \] continuous pressure. Connect the pump to the rear of the engine oil cooler, as shown.

Use a supply of clean 15W-40 engine oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

![[14400033.png]]

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[ 120°F \] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

Check the engine coolant level to be certain that it is filled to the proper level. [[89-008-018-tr — Cooling System|Refer to Procedure 008-018]] in Section 8.

![[ra200sa.png]]

Check the engine lubricating oil level to be certain that it is filled to the proper level.

![[oi900sb.png]]

Engine Throttle Control

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Disconnect the battery cables before beginning the following procedure.

Disconnect the OEM harness from the engine control module, if applicable.

![[22c00141.png]]

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.

Connect the engine control harness, Part Number 3163891.

Connect the engine control harness 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

> [!note] Note · Примечание
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.

Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™5 data link adapter kit (3), Part Number 4918416, and a personal computer to the data link connector of the engine control.

![[22c00125.png]]

Engines that are run on an engine dynamometer require the engine harness be installed and connected to the engine. Additionally, the engine control, Part Number 3163890, **must** be used to properly control the engine during the dynamometer run.

![[wr8coac.png]]

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

Return parameters to their original values when the test or run-in is complete.

Connect the keyswitch panel datalink cable to the Cummins electronic service tool.

Use INSITE™ electronic service tool to set the engine up for the dynamometer. [[89-014-008 — Engine Testing (In Chassis)|Refer to Procedure 014-008]] for more information on this feature.

The setup is now complete, and the auto/manual throttle can be used to control engine speed.

![[14c00040.png]]

Engine operating specifications are available from local Cummins authorized repair locations.

![[lt800ga.png]]

### Test

Engine Operation

The INSITE™ electronic service tool will provide most, if **not** all, of the parameters.

To properly monitor engine performance, record the following parameters. To limit dynamometer operating time, instrument the engine to make as many checks as possible.

- Engine speed rpm with a verified tachometer
- Fuel pressure
- Fuel rate (use service tool, Part Number 3376375, or equivalent)
- Fuel temperature (if needed to correct fuel rate)
- Fuel inlet restriction
- Fuel drain line restriction
- Intake manifold pressure
- Intake air restriction
- Exhaust restriction
- Coolant temperature
- Engine blowby
- Lubricating oil pressure
- Coolant pressure
- Intake manifold air temperature
- Turbocharger inlet air temperature.

![[00400162.png]]

Engine Speed

Use INSITE™ electronic service tool to monitor engine speed. Observe and record the engine speed.

Or use digital optical tachometer, Part Number 3377462, or equivalent, to check and verify engine speed.

![[er2tova.png]]

Fuel Rate

Use fuel measuring device, Part Number 3376375, to measure the rate of fuel consumption. See the manufacturers instructions.

![[eg8togf.png]]

Engine Blowby

Excessive blowby indicates an air compressor, a turbocharger, or an engine malfunction, allowing combustion gases or air to enter the crankcase and build a higher than normal pressure.

This procedure describes how to measure crankcase pressure and how to determine the component that is malfunctioning.

Use one of the three blowby service tools and a water manometer, Part Number ST-1111-3. Maximum gauge capacity is 1270 mm-H 2 O \[ 50 in-H 2 O \].

The engine blowby tools are similar in design. The difference between the tools is in the size of the orifice.

| Blowby Tool | Orifice Size |
|---|---|
| Part Number | inch |
| 3822566 | 0.302 |
| 3822567 | 0.354 |
| 3822568 | 0.406 |

![[eg8toga.png]]

Use a length of hose (1) to attach the blowby tool to one of the crankcase breathers.

Plug all the other breathers.

Attach a manometer to the location shown (2).

![[14400036.png]]

Operate the engine at rated rpm and full load (wide open throttle) until a steady reading is obtained.

Compare the blowby readings to previous readings on the engine. If previous readings for the engine are **not** available, compare the blowby reading to new engine specifications.

A sudden increase in blowby indicates a problem. A gradual increase over a period of time is normal (due to wear of internal engine components).

> [!note] Note · Примечание
> The used engine limit blowby numbers are intended to be used as a guideline **only**, **not** as a hard-set rebuild limit. A basis for engine rebuild can be derived by trending blowby over time.

> [!note] Note · Примечание
> For applications with two crankcase breathers, use an orifice (same size) on both breather tubes. Plug one orifice (manometer connection point). Flow through the orifice will still occur when manometer connector is plugged.

![[eg8toja.png]]

| QSK23 Blowby Limits (Using one 0.302-inch-diameter orifice at rated load and speed) |  |  |
|---|---|---|
| Engine hp rating | New/Rebuilt | Used Engine Limit |
| 0 to 860 hp | 453 mm H 2 0 \[ 17.8 in H 2 0 \] | 802 mm H 2 0 \[ 31.6 in H 2 0 \] |
| 861 to 950 hp | 543 mm H 2 0 \[ 21.4 in H 2 0 \] | 881 mm H 2 0 \[ 34.7 in H 2 0 \] |
| Greater than 950 hp | 624 mm H 2 0 \[ 24.6 in H 2 0 \] | 900 mm H 2 0 \[ 35.4 in H 2 0 \] |

| QSK23 Blowby Limits (Using one 0.354-inch-diameter orifice at rated load and speed) |  |  |
|---|---|---|
| Engine hp rating | New/Rebuilt | Used Engine Limit |
| 0 to 860 hp | 242 mm H 2 0 \[ 9.5 in H 2 0 \] | 451 mm H 2 0 \[ 17.8 in H 2 0 \] |
| 861 to 950 hp | 295 mm H 2 0 \[ 11.6 in H 2 0 \] | 500 mm H 2 0 \[ 19.7 in H 2 0 \] |
| Greater than 950 hp | 343 mm H 2 0 \[ 13.5 in H 2 0 \] | 512 mm H 2 0 \[ 20.2 in H 2 0 \] |

| QSK23 Blowby Limits (Using one 0.402-inch-diameter orifice at rated load and speed) |  |  |
|---|---|---|
| Engine hp rating | New/Rebuilt | Used Engine Limit |
| 0 to 860 hp | 109 mm H 2 0 \[ 4.3 in H 2 0 \] | 196 mm H 2 0 \[ 7.7 in H 2 0 \] |
| 861 to 950 hp | 131 mm H 2 0 \[ 5.2 in H 2 0 \] | 218 mm H 2 0 \[ 8.6 in H 2 0 \] |
| Greater than 950 hp | 152 mm H 2 0 \[ 6 in H 2 0 \] | 224 mm H 2 0 \[ 8.8 in H 2 0 \] |

If the blowby is higher than normal, check the crankcase breathers and breather tubes to see if they are plugged.

![[03400096.png]]

Isolate the turbocharger to determine if the high crankcase pressure is due to seal leakage in the turbocharger.

Disconnect the turbocharger drain line from the oil pan adapter.

Install a hose assembly with the two shutoff valves arranged as shown. Place the other hose in an 8 to 19 liter \[ 2 to 5 gallon \] bucket.

The valves **must** have a minimum inside diameter of 19 mm \[ 0.75 in \].

![[eg4tohe.png]]

Close the valve (A) that allows the oil to drain into the bucket.

![[eg4toka.png]]

Open the valve (B) that allows the oil to drain into the engine.

![[eg4tokb.png]]

> [!warning] CAUTION · Осторожно
> Do not operate the engine with valve A open and valve B closed for more than one minute. Operation for more than one minute can result in severe engine damage.

Operate the engine at rated speed.

Continue operating at rated speed and load. Open valve A and close valve B. Record the blowby reading.

![[tb4tosa.png]]

Compare the value to the original reading. If the blowby is now acceptable, replace the turbocharger. [[89-010-033 — Turbocharger|Refer to Procedure 010-033 in Section 10]].

![[tb400ma.png]]

Isolate the air compressor to determine if it is malfunctioning and causing the high blowby pressure.

Relieve the air pressure on the first air tank in the system after the air compressor (wet tank).

Disconnect the air inlet and outlet connections. Plug the intake manifold or air piping where the inlet connection was removed.

See equipment manufacturer service information.

![[cp4tbma.png]]

A sudden increase in blowby or a high reading that is **not** steady indicates that there is internal damage in the engine.

![[ew800sa.png]]

Lubricating Oil Pressure

Use Pressure Gauge, Part Number 3375275, to measure lubricating oil pressure.

Install the pressure gauge to the main oil rifle (1).

Oil pressure can be checked at other locations on the engine. [[89-100-002 — Engine Diagrams|Refer to Procedure 100-002]] for engine views.

| Lubricating Oil Pressure |  |  |
|---|---|---|
| kpa |  | psi |
| 76 | MIN | 11 |

![[07400239.png]]

Engine Coolant Pressure

Measure the coolant pressure at the pet cock on the water pump outlet pipe (1).

| Coolant Pressure |  |  |
|---|---|---|
| kpa |  | psi |
| 241 | MIN | 35 |

![[14400035.png]]
