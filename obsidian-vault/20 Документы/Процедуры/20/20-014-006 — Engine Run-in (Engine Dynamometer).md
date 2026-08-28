---
aliases:
  - "Обкатка двигателя (на моторном стенде)"
type: "Процедура"
doc: "20-014-006"
title_en: "Engine Run-in (Engine Dynamometer)"
title_ru: "Обкатка двигателя (на моторном стенде)"
modified: "2006-06-30"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 35
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-006.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-014-006.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Engine Run-in (Engine Dynamometer)
**Обкатка двигателя (на моторном стенде)**

> [!abstract] Процедура · `20-014-006`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2006-06-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-014-006.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-014-006.pdf)

### General Information

This section outlines engine testing and engine run-in recommendations for QSK19 engines. All engines **must** be run-in after a rebuild or a repair involving the replacement of one or more piston ring sets, cylinder liners or pistons.

> [!note] Note · Примечание
> Incorrect or insufficient break-in of the piston rings will lead to early oil consumption or high blowby complaints. Adherence to these run-in guidelines will allow the full durability of new pistons, liners, and rings to be realized.

Before operating the engine, make sure the engine is filled with proper coolant. Also, make sure the lubricating oil system is filled and primed.

![[14400005.png]]

In Service Run-in

The following in-service run-in guidelines are recommended for QSK19 engines after a repair involving replacement of one or more of the piston ring sets, cylinder liners or pistons where an engine dynamometer and/or chassis dynamometer run-in **cannot** be performed.

The majority of heavy duty diesel applications will provide sufficient run-in under normal **loaded** operations. However, light load/high rpm operation **must** be avoided during the run-in period.

![[nobox.png]]

Engine Dynamometer Run-in

This is the preferred method of run-in for engines that have been rebuilt **out of chassis**. It is **not** practical, nor recommended, that an engine be removed from the application to conduct the run-in after a rebuild or cylinder repair has been performed in-chassis. There is no requirement, nor is it recommended, for an engine that has been run-in and tested on an engine dynamometer to be run-in again after it has been installed in the vehicle or equipment.

![[nobox.png]]

Chassis Dynamometer, Portable Dynamometer, or Load Bank Run-in

When it is **not** possible to load an engine immediately after rebuild or repair, (examples: on-highway tractor that **must** be “bobtailed” for delivery, a standby generator or fire pump that **cannot** be operated because of customer restrictions, a fire pump that **cannot** be loaded with the water pump, etc.). the engine **must** be run-in on a chassis dynamometer, portable dynamometer, or load bank, following the recommendations outlined in the attached procedures.

![[nobox.png]]

### Install

Test

> [!warning] CAUTION · Осторожно
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.

Remove the large plug from the oil cooler housing.

![[14400011.png]]

Use a pump capable of supplying 207 kPa \[30 psi\] continuous pressure. Connect the pump to the front of the engine oil cooler as shown.

Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

![[pl4hoha.png]]

Check the engine lubricating oil level to be sure it is filled to the proper level.

![[oi8dsva.png]]

Check the engine coolant level to make sure it is filled to the proper level. Refer to Procedure [[20-008-018-tr — Cooling System|008-018]].

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.

![[ra200sa.png]]

Use a known source of good quality Number 2 diesel fuel.

This is very important since Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than Number 2 diesel fuel. The lighter the fuel, the lower the energy content (BTU) per gallon (liter, etc.).

![[nobox.png]]

Engine Throttle Control

Engines that are run on an engine dynamometer require that the engine harness be installed, and connected to the engine. Additionally, a special engine dynamometer version of the OEM wiring harness and throttle control **must** be installed.

A special wiring harness and throttle control has been developed to enable engine operation out of the chassis.

Engine Dynamometer Kit, Part Number 3163890.

![[wr8coac.png]]

Engine operating specifications can be found in publications available from a Cummins Authorized Repair Location.

![[lt800ga.png]]

Mechanically Actuated Injectors

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness, if connected.

Connect the engine control harness Part Number 3163891.

Connect the 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

Electrically Actuated Injectors

Disconnect the OEM harness 16-pin and 23-pin Deutsch connectors from the engine harness, if connected.

Connect the engine control harness Part Number 4918643.

Connect the 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

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

If **not** already equipped, install and wire a magnetic starter switch.

Clip the alligator connector to the positive (+) coil terminal of the magnetic starter switch.

![[22400055.png]]

Air Starter

If an air starter is being used, coil the red wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.

![[19c01032.png]]

Engine Control and INLINE™ Datalink Adapter Connection

> [!note] Note · Примечание
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3168895.

Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™ 5 datalink adapter kit, Part Number 4918416, (3) and a personal computer to the datalink connector of the engine control.

![[22c00125.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Attach the engine control harness using the ring terminal of the red wire to the positive (+) terminal of the battery.

Attach the engine control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.

![[22c00141.png]]

Operation of Engine Control

> [!warning] CAUTION · Осторожно
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Equipment or engine damage can result if not connected properly.

The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.

If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.

Turn the keyswitch to the ON position.

![[22c00127.png]]

Light indicators on the engine control, STOP, WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.

If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the OEM troubleshooting and repair manual to diagnose the engine fault code.

![[22c00128.png]]

Calibrate the Engine Control Throttle

The engine can be returned to idle at any time by pushing in on the throttle knob.

Return the throttle to the idle position.

Turn the keyswitch to the ON position.

![[22c00155.png]]

Rotate the throttle knob fully counterclockwise. Push down on the throttle knob to return the throttle to the idle position.

Repeat this step three times.

Turn the keyswitch to the OFF position for 30 seconds.

![[22c00130.png]]

Engine Operation

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

The engine can be returned to idle at any time by pushing in on the throttle knob.

Slowly rotate the throttle knob **counterclockwise** to increase the engine rpm.

Slowly rotate the throttle knob **clockwise** to decrease the engine rpm.

![[22c00130.png]]

Turn the keyswitch to the OFF position to stop the engine.

![[22c00131.png]]

### Run-In Instructions

Refer to Engine Testing-Engine Dynamometer, Procedure [[20-014-005 — Engine Testing (Engine Dynamometer)|014-005]], for general operating procedures and safety precautions.

![[00400005.png]]

Use this chart to determine the test load.

The run-in test **must** be performed with the engine operating at torque peak rpm. Operate a generator set engine at rated rpm.

Example: The test load for a 475 HP engine rated at 2000 rpm with a 15 percent torque rise is \[300 ft-lb\].

> [!note] Note · Примечание
> This chart assumes the dynamometer constant is 5252. If the dynamometer constant is **not** 5252, use the following formula to determine the correct test load:

Correct test load = (Dynamometer constant) x (Test load) /d 5252.

Example: The dynamometer constant for testing the engine in the above example is 4000.

Correct test load = (4000 x 300) /d 5252 = \[228 ft-lb\].

> [!note] Note · Примечание
> This chart assumes vehicle run-in on a chassis dynamometer.

| Rated RPM | Rated Horsepower | Torque Rise | Test Load |
|---|---|---|---|
| 1200 | All | All | 405 N•m \[300 ft-lb\] |
| 1500 | All | All | 405 N•m \[300 ft-lb\] |
| 1800 | 0 to 499 | All | 405 N•m \[300 ft-lb\] |
| 1800 | 500 and ABOVE | All | 510 N•m \[375 ft-lb\] |
| 1900 | 0 to 474 | All | 405 N•m \[300 ft-lb\] |
| 1900 | 475 and ABOVE | All | 510 N•m \[375 ft-lb\] |
| 2000 | 0 to 499 | 0 to 24% | 405 N•m \[300 ft-lb\] |
| 2000 | 0 to 499 | 25% and ABOVE | 510 N•m \[375 ft-lb\] |
| 2000 | 500 and ABOVE | All | 510 N•m \[375 ft-lb\] |
| 2100 | 0 to 474 | 0 to 32% | 405 N•m \[300 ft-lb\] |
| 2100 | 0 to 474 | 33% Plus | 405 N•m \[300 ft-lb\] |
| 2100 | 475 to 530 | 0 to 15% | 405 N•m \[300 ft-lb\] |
| 2100 | 475 to 530 | 16% and ABOVE | 510 N•m \[375 ft-lb\] |
| 2100 | 531 to 649 | All | 510 N•m \[375 ft-lb\] |
| 2100 | 650 and ABOVE | All | 540 N•m \[400 ft-lb\] |

> [!warning] CAUTION · Осторожно
> Do not crank the starting motor for more than 30 seconds. Excessive heat will damage the starter.

START the engine. If the engine does **not** begin operating after 30 seconds, allow two minutes for the starting motor to cool.

> [!warning] CAUTION · Осторожно
> If the oil pressure is not within specifications, STOP the engine immediately. Both low and high oil pressure will cause engine damage.

| Main Oil Rifle Pressure (At Idle) |  |  |
|---|---|---|
| kPa |  | psi |
| 138 | MIN | 20 |
| 483 | MAX | 70 |

![[oi800vi.png]]

Operate the engine at the IDLE position. Check for leaks.

> [!warning] CAUTION · Осторожно
> Do not operate the engine at IDLE longer than specified. Excessive carbon formation will cause engine damage.

![[oi800vj.png]]

Adjust the engine rpm to 1200 rpm. Adjust the dynamometer load to the test load as previously determined.

Operate the engine at this setting until the coolant temperature indicates 71°C \[160°F\].

Check for leaks. Fix all leaks.

Check all of the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vk.png]]

Adjust the engine rpm to the torque peak rpm. Adjust the dynamometer load to equal two times the test load.

Operate the engine at this load for two minutes.

Check all the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vl.png]]

Maintain the engine rpm at torque peak rpm. Increase the dynamometer load to equal three times the test load.

Operate the engine at this load for 2 minutes.

Check all the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[oi800vm.png]]

Move the throttle lever to the FULL OPEN position. Increase the load until the engine rpm is at torque peak rpm.

Operate the engine at this setting for 10 minutes or until the blowby becomes stable within specifications.

Check all the gauges and record the readings.

![[oi800vn.png]]

Decrease the dynamometer load until the engine rpm increases to the rated rpm.

Operate the engine at this load for 5 minutes.

Check all the gauges and record the readings.

![[oi800vo.png]]

Decrease the dynamometer load completely.

> [!warning] CAUTION · Осторожно
> Do not turn the engine OFF immediately. The engine must be allowed to cool.

Move the throttle lever to the LOW IDLE position. Operate the engine at this setting for 3 to 5 minutes. This will allow the turbocharger and the other engine components to cool.

> [!warning] CAUTION · Осторожно
> Do not operate the engine at IDLE longer than specified. Excessive carbon formation can cause engine damage.

![[oi800vj.png]]

Turn the engine OFF.

![[oi800vp.png]]
