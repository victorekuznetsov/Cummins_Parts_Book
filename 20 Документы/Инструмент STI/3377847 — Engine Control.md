---
aliases:
  - "Управление двигателем"
type: "Инструкция по инструменту"
doc: "3377847"
title_en: "Engine Control"
title_ru: "Управление двигателем"
released: "2006-10-05"
modified: "2006-10-06"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
figures: 36
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3377847.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/sti/3377847.pdf"
tags:
  - "документ/инструмент"
  - "двигатель/QST30"
---

# Engine Control
**Управление двигателем**

> [!abstract] Инструкция по инструменту · `3377847`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Даты:** выпущен 2006-10-05 · изменён 2006-10-06
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/sti/3377847.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/sti/3377847.pdf)

### Description

Engine Control

### Purpose

This document provides information for the use of engine control, Part Number 3163890. The engine control is a portable, handheld electronic control, used to start and control engine speed on the Cummins® electronic engine families, refer to Table 2. It replaces the throttle pedal, driver interface panel, and fault code monitoring circuits. The engine control has a datalink provision to connect to an electronic service tool to monitor engine operation and fault codes. The required engine control harnesses for the appropriate engines are purchased separately. The engine control and engine control harnesses are designed to be used with both +12-VDC and +24-VDC battery systems.

For additional information, see the following publications.

- Refer to Procedure [[20-014-005 — Engine Testing (Engine Dynamometer)|014-005]] or [[20-014-006 — Engine Run-in (Engine Dynamometer)|014-006]] in the QSK19 and QSK19 CM850 Modular Common Rail System Series Engines, Bulletin 4021592

- Refer to Procedure 014-005 or 014-006 in the Troubleshooting and Repair Manual QSK23 Series Engines, Bulletin 4021375

- Refer to Procedure 014-005 or 014-006 in the Service Manual K38, K50, and QSK50 Series Engines, Bulletin 4021528
- Refer to Procedure 014-005 or 014-006 in the Service Manual QSK45 and QSK60 Series Engines, Bulletin 4021530.

> [!note] Note · Примечание
> The engine control can be used on engines with frequency throttle calibrations by first downloading a linear throttle calibration to the electronic control module (ECM) and then performing the test as identified within this Service Tool Instruction. After the testing/repair is complete, reload the correct frequency throttle calibration.

![[22c00132.png]]

| Table 1, Engine Control, Part Number 3163890 |  |  |  |
|---|---|---|---|
| Item | Part Number | Description | Quantity |
| 1 | 3163890 | Engine control | 1 |

| Table 2, Items Used with the Engine Control, Purchased Separately |  |  |  |
|---|---|---|---|
| Item | Part Number | Description | Quantity |
| 2 | 3163891 | Engine control harness (QSK19, QSK23, QSK45, and QSK60) | 1 |
| 2 | 4918643 | Engine control harness (QSK19, QSK38, QSK50, and QSK60 with electronically actuated injectors) | 1 |
| 2 | 3163892 | Engine control harness (Signature, ISX, QSX15, and ISM) | 1 |
| 2 | 3164251 | Engine control harness (ISB, ISC, and ISL) | 1 |
| 2 | 3163894 | Engine control harness (M11 and N14 CELECT™ Plus) | 1 |
| 2 | 3163818 | Engine control harness (L10, M11, and N14 CELECT™) | 1 |
| 2 | 3164036 | Engine control harness (ISB e and ISB four-cylinder) | 1 |
| 2 | 3164324 | Engine control harness (QST30 Industrial) | 1 |
| 2 | 3164820 | Engine control harness (QST30 G-Drive) | 1 |
| 2 | 3164242 | Engine control harness (Signature and ISX with CM870, ISB with CM850, and ISM with CM870) | 1 |
| 2 | 3165084 | Engine control harness (480C-E Marine) | 1 |
| 2 | 4918272 | Engine control harness (B Gas Plus, C Gas Plus, L Gas Plus, and B LPG Plus) | 1 |
| 3 | 3163099 | INLINE™ adapter kit | 1 |
| 3 | 3163583 | INLINE™ 1 adapter kit | 1 |
| 3 | 3163682 | INLINE™ 2 adapter kit | 1 |
| 3 | 4918190 | INLINE™ 4 adapter kit | 1 |
| 3 | 4918416 | INLINE™ 5 adapter kit | 1 |
| 4 |  | INSITE™ electronic service tool-equipped personal computer | 1 |
| **Not** shown | 3163895 | Electrical cable (6.1-m \[20-ft\] extension cable) | 1 |
| **Not** shown | 3164630 | Ford/Sterling OEM connector adapter cable | 1 |
| **Not** shown | 3164653 | Harness, datalink adapter (ISB, ISC, and ISL with CM850 and ISM and ISX with CM870) | 1 |

> [!danger] WARNING · Опасно
> When using the engine control on an engine installed in a vehicle or equipment, make certain that the transmission is in neutral or the driveline is disengaged, the parking brake is on, and the wheels are blocked. Failure to do so can result in vehicle or equipment damage, serious personal injury, or death.

The engine control is designed for **diagnostic purposes only**. It can be used to operate an engine **only** under the following situations.

- An engine on an engine dynamometer
- An engine in a vehicle or equipment that is stationary
- An engine in a vehicle or equipment on a chassis dynamometer.

![[22d00166.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!note] Note · Примечание
> Disconnect the battery cables before beginning the following procedure.

Disconnect the OEM harness from the electronic control module (ECM) (if applicable).

![[22c00124.png]]

> [!warning] CAUTION · Осторожно
> Do not blow compressed air into the ECM ports or connectors. Compressed air can contain moisture (due to condensation) that can damage the ECM.

Use quick-dry electrical contact cleaner, Part Number 3824510, to remove all dirt and moisture from the ECM connector ports.

![[19800830.png]]

> [!note] Note · Примечание
> CELECT™ and CELECT™ Plus use different engine control harnesses. Use the appropriate engine control harness.

Insert the engine control harness 28-pin AMP connector (1) into the “B” receptacle of the ECM. Carefully align and start the connector mounting capscrews into the ECM by hand.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

![[22c00119.png]]

> [!note] Note · Примечание
> An active Fault Code 431 will be logged when using the engine control on a CELECT™ engine. It will have no effect on performance. Clear Fault Code 431 after the test.

Connect the engine control harness 3-pin Weather-Pack connector (2) to the mating actuator harness (unswitched battery power) connector.

Connect the engine control harness 9-pin Deutsch connector for CELECT™ or the 21-pin connector for CELECT™ Plus (3) to the mating sensor harness connector.

![[22c00121.png]]

Align the engine control harness 50-pin Deutsch connector slots with the “B” receptacle of the ECM and insert the connector into the ECM.

Carefully align and start the connector mounting capscrew into the ECM by hand.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

![[19901103.png]]

Connect the engine control harness 2-pin Metri-Pack connector to the mating water-in-fuel sensor connector.

Remove the shorting cap, Part Number 3164250, from the 4-pin Weather-Pack connector, if the need exists, to connect the grid heater.

Connect the 4-pin Weather-Pack connector to the grid heater connector.

![[19901104.png]]

> [!note] Note · Примечание
> Some engines installed in Ford and Sterling chassis use a Ford 16-pin OEM connector. If so equipped, use the Ford/Sterling OEM connector adapter cable, Part Number 3164630.

Connect the engine control harness 23-pin Deutsch connector to the engine wiring harness.

![[22c00140.png]]

Remove the 3-pin Deutsch terminating resistor cap (cap will have a blue insert) from the wiring harness.

Connect the engine control harness 3-pin Deutsch connector to the J1939 connector on the engine wiring harness.

The 3-pin Deutsch terminating resistor cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.

![[19901106.png]]

Align the engine control harness 50-pin Deutsch connector slots with the OEM receptacle of the ECM and insert the connector into the ECM.

Carefully align and start the connector mounting capscrew into the ECM by hand.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

![[19c01028.png]]

Disconnect the engine wiring harness from the OEM harness.

Connect the engine control harness to the engine wiring harness.

![[19c01029.png]]

Disconnect the OEM harness 21-pin and 31-pin Deutsch connectors from the engine harness.

Connect the engine control harness 21-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

Remove the 3-pin Deutsch terminating resistor cap (cap will have a blue insert) from the wiring harness.

Connect the engine control harness 3-pin Deutsch connector to the J1939 connector of the engine wiring harness.

The 3-pin Deutsch terminating resistor cap **must** be installed after the engine control harness is removed. If the cap is broken or has been misplaced, replace with resistor cap, Part Number 3163051.

![[19a00770.png]]

> [!note] Note · Примечание
> To monitor the QST30 G-Drive engine with INSITE™ electronic service tool, connect to the 9-pin datalink connector on the engine and **not** the connector on the engine control.

Align the engine control harness 40-pin Deutsch connector slots with the “B” receptacle of the ECM and insert the connector into the ECM. Carefully align and start the connector mounting capscrew into the ECM by hand.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

![[19400401.png]]

Disconnect the OEM harness 23-pin and 31-pin Deutsch connectors from the engine harness.

Connect the engine control harness 23-pin and 31-pin Deutsch connectors to the engine wiring harness.

![[19a00768.png]]

Carefully operate the connector latch and disconnect the connector.

Connect the engine control harness to the 89-pin OEM engine connector on the ECM.

![[22d00078.png]]

Connect the engine control harness 2-pin Metri-Pack connector to the mating water-in-fuel sensor connector.

Remove the shorting cap, Part Number 3164250, from the 4-pin Weather-Pack connector, if the need exists, to connect the grid heater.

Connect the 4-pin Weather-Pack connector to the grid heater connector.

![[19901104.png]]

Align the engine control harness 50-pin Deutsch connector slots with the OEM receptacle of the ECM and insert the connector into the ECM. Carefully align and start the connector mounting capscrew to the ECM by hand.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

Disconnect the engine wiring harness 4-pin Deutsch connector from the ECM and connect the 4-pin Deutsch connector on the engine control harness.

![[22100102.png]]

> [!warning] CAUTION · Осторожно
> Make certain that the cap is installed on the 1-pin Weather-Pack connector and/or the 2-pin Deutsch connector, if the connectors are not used. Failure to do so can cause electrical damage.

> [!note] Note · Примечание
> The 1-pin Weather-Pack connector can **not** be used on the ISX with CM870 or the ISB with CM850.

> [!note] Note · Примечание
> The 2-pin Deutsch lift pump power connection can **not** be used on the ISB with CM850.

Connect the 2-pin Deutsch connector on the engine control harness to the lift pump power connection on the engine wiring harness above the ECM on the ISX with CM870.

![[22c00168.png]]

Align the engine control harness 50-pin Deutsch connector slots with the OEM receptacle of the ECM and insert the connector into the ECM. Carefully align and start the connector mounting capscrew to the ECM by hand.

Tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

Disconnect the engine wiring harness 4-pin Deutsch connector from the ECM.

![[22400159.png]]

> [!warning] CAUTION · Осторожно
> Make certain that the cap is installed on the 2-pin Weather-Pack connector and/or the 2-pin Deutsch connector, if the connectors are not used. Failure to do so can cause electrical damage.

> [!note] Note · Примечание
> The 2-pin Deutsch lift pump power connection can **not** be used on the ISM with CM870.

Connect the 4-pin Deutsch and 1-pin Weather-Pack (1) connectors on the electrical wiring harness adapter, Part Number 3164653, to the mating connectors on the engine control harness, Part Number 3164242. Connect the 4-pin Deutsch connector on the adapter harness, Part Number 3164653, to the mating connector on the ECM.

![[22600214.png]]

Connect the 3-pin Weather-Pack connector (1) to the mating throttle connector on the engine harness. Connect the 3-pin Weather-Pack connector (2) to the mating idle validation switch connector on the engine harness. Connect the 4-pin Weather-Pack connector (3) to the mating ECM power connector on the engine harness. Connect the 40-pin Deutsch connector (4) to the mating connector on the 40-pin engine harness.

![[22d00180.png]]

Connect the black-wire alligator clip of the engine control harness to the engine block to achieve electrical ground.

![[19c01031.png]]

> [!warning] CAUTION · Осторожно
> Do not connect the alligator clip to the starter motor solenoid “S” terminal. Doing so can cause equipment damage.

If **not** already equipped, install and wire a magnetic starter switch.

Clip the alligator connector to the positive (+) coil terminal of the magnetic starter switch.

![[22400055.png]]

If an air starter is being used, coil the red wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.

![[19c01032.png]]

If equipped with a starter lockout relay connect the green wire alligator clip to the “S” terminal.

If **not** equipped with a starter lockout relay, coil the green wire into a loop and secure the loop to the engine control harness to protect it from an electrical short.

![[19c01032.png]]

> [!note] Note · Примечание
> If additional cable length is needed to connect the engine control, use electrical cable, Part Number 3163895.

Connect the engine control harness (2) to the engine control. An INSITE™ electronic service tool-equipped personal computer can be used to monitor circuits for proper operation. Connect the appropriate INLINE™ datalink adapter kit (3) and a personal computer to the datalink connector of the engine control.

![[22c00125.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

> [!note] Note · Примечание
> For Signature and ISX with CM870, ISB with CM850, or ISM with CM870 engine control harness, Part Number 3164242, connect the black wire to the block ground stud.

Attach the engine control harness using the ring terminal of the red wire to the positive (+) terminal of the battery.

Attach the engine control harness using the ring terminal of the black wire to the negative (-) terminal of the battery.

![[22c00141.png]]

> [!warning] CAUTION · Осторожно
> Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal. Failure to do so can result in equipment or engine damage.

The power light will illuminate when power is supplied and the keyswitch is turned to the accessory or ON position.

If the power light does **not** illuminate, return the keyswitch to the OFF position. Verify the red wire is connected to the positive (+) battery terminal and the black wire is connected to the negative (-) battery terminal.

Turn the keyswitch to the ON position.

![[22c00127.png]]

Light indicators on the engine control, STOP, WARN, MAINT, WIF, and WAIT TO START, will illuminate if applicable. The light indicators will illuminate for approximately 30 seconds. If no fault codes are found, the light indicators will extinguish.

If the STOP light indicator (red) or WARN light indicator (yellow) continues to illuminate, use INSITE™ electronic service tool and the appropriate service literature to diagnose the engine fault code.

![[22c00128.png]]

> [!note] Note · Примечание
> The throttle can be returned to the idle position by pushing down on the throttle knob at any time.

Return the throttle to the idle position.

Turn the keyswitch to the ON position.

![[22c00155.png]]

Rotate the throttle knob fully **counterclockwise**. Push down on the throttle knob to return the throttle to the idle position.

Repeat this step three times.

Turn the keyswitch to the OFF position for 30 seconds.

![[22c00156.png]]

> [!warning] CAUTION · Осторожно
> Check coolant and lubricating oil levels before starting and operating engine. Failure to do so can result in engine damage.

> [!note] Note · Примечание
> On the B Gas Plus, C Gas Plus, L Gas Plus and B LPG Plus engines equipped with a fuel solenoid, the vehicle ignition switch **must** be in the ON position.

Turn the keyswitch to the START position until the engine starts and release the keyswitch.

![[22c00129.png]]

> [!note] Note · Примечание
> The engine can be returned to idle at any time by pushing in on the throttle knob.

Slowly rotate the throttle knob **counterclockwise** to **increase** the engine rpm.

Slowly rotate the throttle knob **clockwise** to **decrease** the engine rpm.

![[22c00130.png]]

Turn the keyswitch to the OFF position to stop the engine.

![[22c00131.png]]
