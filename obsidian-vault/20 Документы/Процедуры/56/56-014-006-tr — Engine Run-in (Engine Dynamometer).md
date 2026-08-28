---
aliases:
  - "Обкатка двигателя (на моторном стенде)"
type: "Процедура"
doc: "56-014-006-tr"
title_en: "Engine Run-in (Engine Dynamometer)"
title_ru: "Обкатка двигателя (на моторном стенде)"
modified: "2007-05-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "4021530"
figures: 33
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-006-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-006-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/56"
---

# Engine Run-in (Engine Dynamometer)
**Обкатка двигателя (на моторном стенде)**

> [!abstract] Процедура · `56-014-006-tr`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[4021530 — QSK45 and QSK60 Service Manual|4021530]]
> **Секции:** Section 14 - Engine Testing - Group 14
> **Даты:** изменён 2007-05-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-014-006-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/56-014-006-tr.pdf)

### Install

Test

> [!warning] CAUTION · Осторожно
> The lubricating oil system must be primed before operating the engine after rebuild to avoid internal component damage. Do not prime the system from the bypass filter as the filter will be damaged.

QSK45 and QSK60 industrial engines are equipped with an automatic prelube system from the factory. If the engine is **not** equipped with an automatic prelube system, follow the instructions to prelube the system manually.

![[14400011.png]]

For engines without automatic prelube, use a pump capable of supplying 205 kPa \[30 psi\] continuous pressure. Connect the pump to the front of the engine oil cooler as shown.

Use a supply of clean oil. Turn the pump to the ON position. Check the engine oil pressure gauge. When the gauge indicates oil pressure, begin monitoring the oil level in the oil pan.

![[pl4hoha.png]]

Check the engine lubricating oil level to be sure it is filled to the proper level.

![[oi8dsva.png]]

> [!danger] WARNING · Опасно
> Do not remove the pressure cap from a hot engine. Wait until the coolant temperature is below 50°C \[120°F\] before removing the pressure cap. Heated coolant spray or steam can cause personal injury.

> [!warning] CAUTION · Осторожно
> Do not add cold coolant to a hot engine. This can cause engine casting damage. Allow the engine to cool to below 50°C \[120°F\] before adding coolant.

Check the engine coolant level. [[56-008-018-tr — Cooling System|Refer to Procedure 008-018 (Cooling System) in Section 8]]

Use a known source of good-quality number 2 diesel fuel. Number 1 diesel fuels, along with most other alternate fuels, are lighter (lower specific gravity, higher API gravity) than number 2 diesel fuel. The lighter the fuel, the lower the energy content (BTU) per gallon (liter, etc.).

![[ra200sa.png]]

Engine Throttle Control

Mechanically Actuated Injectors

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Disconnect the battery cables before beginning the following procedure.

Disconnect the OEM harness from the electronic control module (ECM) (if applicable).

![[22c00141.png]]

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.

Connect the engine control harness, Part Number 4918643.

Connect the engine control harness 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

> [!note] Note · Примечание
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.

Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool equipped personal computer can be used to monitor circuits for proper operation. Connect the INLINE™5 datalink adapter kit (3), Part Number 4918416, and a personal computer to the datalink connector of the engine control.

![[22c00125.png]]

Engines that are run on an engine dynamometer require the engine harness be installed and connected to the engine. Additionally, the engine control, Part Number 3163890, **must** be used to properly control the engine during the dynamometer run.

![[wr8coac.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Connect battery power to the starter.

Connect the dynamometer test OEM wiring harness starter solenoid lead (yellow) to the starter solenoid. Connect the ground lead (black) to the starter solenoid. Connect the ground lead (black) to the starter or battery negative (-) or ground side. Connect the (+) 12-VDC power lead (red) to either the starter or battery positive (+) 12-VDC side.

![[sb8coma.png]]

Rotate the throttle knob fully **counterclockwise**. Push down on the throttle knob to return the throttle to the idle position.

Repeat this step three times.

Turn the keyswitch to the OFF position for 30 seconds.

![[22c00156.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

Electronically Actuated Injectors

Disconnect the OEM harness 16-pin and 23-pin Deutsch connectors from the engine harness if connected.

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
> Batteries can emit explosive gases. To avoid personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

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

Light indicators on the engine control, STOP, WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.

If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the OEM service literature to diagnose the engine fault code.

![[22c00128.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. If coolant and lubricating oil are not at the proper level, engine damage can result.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

> [!note] Note · Примечание
> The engine can be returned to idle at any time by pushing in on the throttle knob.

Slowly rotate the throttle knob **counterclockwise** to increase the engine rpm.

Slowly rotate the throttle knob **clockwise** to decrease the engine rpm.

![[22c00130.png]]

Turn the keyswitch to the OFF position to stop the engine.

![[22c00131.png]]

Return the parameters to their original values when the test or run-in is complete.

Connect the keyswitch panel datalink cable to the Cummins® electronic service tool.

Use INSITE™ electronic service tool to set the engine up for the dynamometer. [[56-014-008-tr — Engine Testing (In Chassis)|Refer to Procedure 014-008 (Engine Testing (In Chassis)) in Section 14 for more information on this feature.]]

The setup is now complete, and the auto/manual throttle can be used to control engine speed.

![[14c00040.png]]

Engine operating specifications are available from Cummins® authorized repair locations.

![[lt800ga.png]]

### Run-In Instructions

Consult the dynamometer manufacturer's literature for relevant dynamometer constant values and calculations.

Table 1 provides a summary of the break-in procedure; information in Table 1 is used in this procedure.

| Table 1 |  |  |  |  |
|---|---|---|---|---|
| Step | Time (Minutes) | Industrial (50 Hz, 60 Hz) | Power Generation (50 Hz) | Power Generation (60 Hz) |
| 1 | 5 | 35% Torque Peak @ Torque Peak Speed | 25% of Standby @ 1300 rpm | 35% of Standby @ 1500 rpm |
| 2 | 10 | 75% Torque Peak @ Torque Peak Speed | 50% of Standby @ 1300 rpm | 50% of Standby @ 1500 rpm |
| 3 | 10 | 100% Torque Peak @ Torque Peak Speed | 75% of Standby @ 1300 rpm | 75% of Standby @ 1500 rpm |
| 4 | 10 | 100% of Full Load @ Rated Speed | 100% of Prime @ 1500 rpm | 100% of Prime @ 1800 rpm |

Table 2 provides the relevant loading information for the QSK45 and QSK60 Industrial engines.

| Table 2 |  |  |  |  |
|---|---|---|---|---|
| Rated rpm | Rated Horsepower Hp (kw) | Peak Torque rpm lb-ft (Nm) | Peak Torque rpm | Engine Model |
| 1900 | 2700 (2013) | 7839 (10268) | 1500 | QSK60 |
| 1900 | 2500 (1864) | 7260 (9843) | 1500 | QSK60 |
| 1800 | 2200 (1641) | 6618 (8973) | 1500 | QSK60 |
| 1900 | 2300 (1715) | 6677 (9053) | 1500 | QSK60 |
| 1900 | 2000 (1491) | 6169 (8364) | 1500 | QSK60 |
| 1900 | 1875 (1398) | 6169 (8364) | 1500 | QSK60 |
| 1900 | 1800 (1342) | 6274 (8506) | 1500 | QSK60 |
| 1900 | 2250 (1678) | 6300 (8542) | 1500 | QSK45 |
| 1900 | 2000 (1491) | 5805 (7871) | 1500 | QSK45 |
| 1900 | 1600 (1193) | 5042 (6836) | 1500 | QSK45 |
| 1900 | 1500 (1119) | 5042 (6836) | 1300 | QSK45 |
| 1900 | 1500 (1119) | 4727 (6049) | 1500 | QSK45 |
| 1800 | 1350 (1007) | 4525 (6135) | 1300 | QSK45 |
| 1900 | 1200 (895) | 4425 (5999) | 1300 | QSK45 |
| 1900 | 2850 (2125) | 8274 (11218) | 1600 | QSK60 Tier 2 |
| 1900 | 2700 (2013) | 7839 (10628) | 1500 | QSK60 Tier 2 |
| 1900 | 2500 (1864) | 7528 (9841) | 1500 | QSK60 Tier 2 |
| 1800 | 2000 (1491) | 6169 (8363) | 1500 | QSK60 Tier 2 |

[[56-014-005-tr — Engine Testing (Engine Dynamometer)|Refer to Procedure 014-005 (Engine Testing - Engine Dynamometer) in Section 14, for general operating procedures and safety precautions.]]

The run-in test **must** be performed with the engine operating at torque peak rpm. Operate a generator set engine at rated rpm. See the performance charts available through Cummins Inc.

Use this chart to determine the test load.

![[00400005.png]]

> [!warning] CAUTION · Осторожно
> Do not crank the starting motor for more than 30 seconds. Excessive heat will damage the starter.

> [!warning] CAUTION · Осторожно
> If the oil pressure is not within specifications, stop the engine immediately. Both low and high oil pressure will cause engine damage.

Start the engine. If the engine does **not** begin operating after 30 seconds, allow 2 minutes for the starting motor to cool.

Check the oil pressure.

| kpa |  | psi |
|---|---|---|
| 138 | MAX | 20 |
| 483 | MAX | 70 |

If the oil pressure is **not** within specifications, the engine **must** be shut down.

![[oi800vi.png]]

> [!warning] CAUTION · Осторожно
> Do not operate the engine at idle longer than specified. Excessive carbon formation will cause engine damage.

Operate the engine in the idle position and check for leaks.

![[oi800vj.png]]

Adjust the engine rpm to 1200 rpm. Adjust the dynamometer load to the test load as previously determined. Operate the engine at this setting until the coolant temperature indicates 71°C \[160°F\].

Inspect for leaks.

Repair any leaks found during inspection.

Check **all** of the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[14600050.png]]

Adjust the engine rpm to the torque peak rpm. Adjust the dynamometer load to equal two times the test load. Operate the engine for two minutes.

Check **all** the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[14600051.png]]

Maintain the engine rpm at torque peak rpm. Increase the dynamometer load to equal three times the test load.

Operate the engine at this load for 2 minutes.

Check **all** of the gauges and record the readings.

Do **not** proceed to the next step until the blowby becomes stable within specifications.

![[14600052.png]]

Move the throttle lever to the full-open position. Increase the load until the engine rpm is at torque peak rpm.

Operate the engine at this setting for 10 minutes or until the blowby becomes stable within specifications.

Check **all** of the gauges and record the readings.

![[14600053.png]]

Decrease the dynamometer load until the engine rpm increases to the rated rpm.

Operate the engine at this load for 5 minutes.

Check **all** of the gauges and record the readings.

![[14600054.png]]

> [!warning] CAUTION · Осторожно
> Do not turn the engine off immediately. The engine must be allowed to cool.

> [!warning] CAUTION · Осторожно
> Do not operate the engine at idle longer than specified. Excessive carbon formation can cause engine damage.

Decrease the dynamometer load completely.

Switch the engine to low idle. Operate the engine at this setting for 3 to 5 minutes. This will allow the turbocharger and the other engine components to cool.

![[oi800vj.png]]

Shut the engine off.

![[oi800vp.png]]
