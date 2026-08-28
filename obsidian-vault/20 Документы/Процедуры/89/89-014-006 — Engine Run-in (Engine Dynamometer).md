---
aliases:
  - "Обкатка двигателя (на моторном стенде)"
type: "Процедура"
doc: "89-014-006"
title_en: "Engine Run-in (Engine Dynamometer)"
title_ru: "Обкатка двигателя (на моторном стенде)"
modified: "2006-06-26"
engines:
  - "85017333"
families:
  - "QSK23"
manuals:
  - "4021375"
figures: 34
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-014-006.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-014-006.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "группа/89"
---

# Engine Run-in (Engine Dynamometer)
**Обкатка двигателя (на моторном стенде)**

> [!abstract] Процедура · `89-014-006`
> **Двигатели:** [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23
> **Входит в руководства:** [[4021375 — QSK23 Troubleshooting and Repair Manual|4021375]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-06-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/89/89-014-006.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/89-014-006.pdf)

### General Information

This document provides procedures for the use of an engine control, Part Number 3163890. The engine control is a portable, handheld electronic control, used to start and control engine speed on the following Cummins® electronic engine families. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a datalink provision to connect to an electronic service tool to monitor engine operation and fault codes. The engine control harnesses required for the engines are purchased separately. The engine control and engine control harnesses are designed to be used with both (+) 12-VDC and (+) 24-VDC battery systems.

> [!note] Note · Примечание
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the electronic control module (ECM). After the testing/repair is complete, reload the correct frequency throttle calibration.

![[ck800wa.png]]

### Install

> [!warning] CAUTION · Осторожно
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.

Remove the large plug from the oil cooler rifle.

![[14400032.png]]

Use a pump capable of supplying 205 kPa \[30 psi\] continuous pressure.

Connect the pump to the oil cooler rifle, as shown.

Use a supply of clean 15W-40 engine oil.

Turn the pump to the ON position.

Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

![[14400033.png]]

Check the engine lubricating oil level to be sure it is filled to the proper level.

![[oi8dsva.png]]

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

Check the engine coolant level to make sure it is filled to the proper level. Refer to Procedure 008-018.

![[ra200sa.png]]

Use a known source of good quality number 2 diesel fuel.

This is very important since number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuels. The lighter the fuel, the lower the energy content (BTU per gallon (liter, etc.).

![[ck800wa.png]]

Engine Throttle Control

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Disconnect the battery cables before beginning the following procedure.

Disconnect the OEM harness from the electronic control module (ECM) (if applicable).

![[22c00141.png]]

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.

Connect the engine control harness Part Number 3163891.

Connect the engine control harness 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

> [!note] Note · Примечание
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.

Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™5 datalink adapter kit (3), Part Number 4918416, and a personal computer to the datalink connector of the engine control.

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

> [!note] Note · Примечание
> Some engines are equipped with fittings used for Compucheck® testing sensors. The sensor probes used for Compucheck® and dynamometer testing are **not** compatible. If the same location is used, remove the Compucheck® fitting and install adapters for the dynamometer sensor.

Install the coolant pressure sensor (1).

Install the coolant temperature sensor (2).

![[19400310.png]]

Return parameters to their original value when the test or run-in is complete.

Connect the keyswitch panel datalink cable to the Cummins electronic service tool.

Use INSITE™ electronic service tool to set the engine up for the dynamometer. Refer to Procedure [[89-014-008 — Engine Testing (In Chassis)|014-008]] for more information on this feature.

The setup is now complete, and the auto/manual throttle can be used to control engine speed.

![[14c00040.png]]

Engine operating specifications are available from local Cummins authorized repair locations.

![[lt800ga.png]]

### Run-In Instructions

See the Engine Testing - Engine Dynamometer, Procedure [[89-014-005 — Engine Testing (Engine Dynamometer)|014-005]], for general operating procedures and safety precautions.

![[ck800wa.png]]

Use the following chart to determine the test load.

The run-in test **must** be performed with the engine operating at torque peak rpm. See the performance charts available through Cummins Inc.

| Rated RPM | Torque Peak |
|---|---|
| 2100 | 1300 |
| 2100 | 1400 |

> [!warning] CAUTION · Осторожно
> Do not crank the starting motor for more than 30 seconds. Excessive heat will damage the starter.

> [!warning] CAUTION · Осторожно
> If the oil pressure is not within specifications, stop the engine immediately. Both low and high oil pressure will cause engine damage.

Start the engine. If the engine does **not** begin operating after 30 seconds, allow two minutes for the starter motor to cool.

| kpa |  | psi |
|---|---|---|
| 70 | MIN | 10 |

![[oi800vi.png]]

> [!warning] CAUTION · Осторожно
> Do not operate the engine at idle longer than specified. Excessive carbon formation will cause engine damage.

Operate the engine in the idle position and check for leaks.

![[oi800vj.png]]

Adjust the engine rpm to 1200 rpm. Adjust the dynamometer load to the test load as previously determined. Operate the engine at this setting until the coolant temperature indicates 70°C \[160°F\].

Check for and fix all leaks.

Check all gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vk.png]]

Adjust the engine rpm to the torque peak rpm. Adjust the dynamometer load to equal two times the test load. Operate the engine for two minutes.

Check all gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vl.png]]

Maintain the engine rpm at torque peak rpm. Increase the dynamometer load to equal three times the test load.

Operate the engine at this load for two minutes.

Check all gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vm.png]]

Move the throttle lever to the full open position. Increase the load until the engine rpm is at torque peak rpm.

Operate the engine at this setting for 10 minutes or until the blowby becomes stable within specifications.

Check all gauges and record the readings.

![[oi800vn.png]]

Decrease the dynamometer load until the engine rpm increases to the rated rpm.

Operate the engine at this load for five minutes.

Check all gauges and record the readings.

![[oi800vo.png]]

> [!warning] CAUTION · Осторожно
> Do not turn the engine off immediately. The engine must be allowed to cool.

> [!warning] CAUTION · Осторожно
> Do not operate the engine at idle longer than specified. Excessive carbon formation can cause engine damage.

Decrease the dynamometer load completely.

Move the throttle lever to the low idle position. Operate the engine at this setting for three to five minutes. This will allow the turbocharger and the other engine components to cool.

![[oi800vj.png]]

Turn the engine off.

![[oi800vp.png]]
