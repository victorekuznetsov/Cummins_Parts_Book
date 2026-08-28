---
type: "Процедура"
doc: "40-005-014-tr"
title_en: "Fuel Injection Pump, Rotary"
modified: "2022-09-27"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 69
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-014-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-014-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Fuel Injection Pump, Rotary

> [!abstract] Процедура · `40-005-014-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2022-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-005-014-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-005-014-tr.pdf)

### General Information

Fuel System Identification

The B Series engine uses many different fuel injection pumps, depending on the horsepower rating and application.

The Lucas CAV DPA distributor-type fuel injection pump can be found on the following engine applications:

- Marine
- Industrial.

![[fp901gp.png]]

The Lucas CAV DPS distributor-type fuel injection pump can be found on the following engine application:

- European and U.K. automotive ratings.

![[fp901gq.png]]

The Delphi DP210 distributor-type fuel injection pump can be found on the following applications:

- Industrial (Tier 2/Stage II Certified).

![[05900794.png]]

The Bosch® VE distributor-type fuel injection pump can be found on the following engine applications:

- Industrial
- 1991 low-horsepower automotive ratings.

![[fp901gr.png]]

The Stanadyne DB4 distributor-type fuel injection pump can be found on the following engine application:

- Gen Sets

![[ip900gj.png]]

Fuel Injection Pump (Distributor Type)

The fuel injection pumps, Bosch® VE, Lucas CAV DPA, Stanadyne DB4, Lucas CAV DPS, and Delphi DP210, are rotary distributor pumps. These pumps perform the four basic functions of:

1. Producing the high fuel pressure required for injection
2. Metering the exact amount of fuel for each injection cycle
3. Distributing the high-pressure, metered fuel to each cylinder at the precise time
4. Varying the timing relative to engine speed.

![[fp901gy.png]]

Distributor-Type Pump Governor

Balance between the governor flyweights and control lever position controls the metering of the amount of fuel to be injected.

The fuel injection pump governor performance and setting can affect engine power. Special equipment and qualified personnel are required to verify governor performance. If the seals are broken on the external Bosch® VE adjustment screw, the fuel rate can, perhaps, be out of adjustment.

![[fp902gb.png]]

The Lucas CAV DPA/DPS fuel injection pump uses a coded spring connection to change the governor setting. Incorrect connection of the governor spring can affect performance.

Adjustments and rating changes are described in the Master Repair Manual, Injector Pumps and Injectors, Bulletin 3666037.

![[fp9spga.png]]

Manual Shutdown Levers

Both fuel injection pumps are equipped with mechanical shutdown levers. These levers are spring-loaded in the run position. **Not** all applications will use these manual shutdown controls and there will be no cable or rod connected to the lever.

> [!note] Note · Примечание
> Partial actuation of the mechanical shutdown levers will affect fuel flow and engine power.

![[fp9lvwb.png]]

Advance Timing Mechanism

Regulated pressure produced by a vane supply pump in both fuel injection pumps is used to advance the timing as the engine speed increases. A return spring is used to retard the timing as the engine speed is reduced. If a spring breaks, the timing will go to the advance position, resulting in torque loss, fuel knock, and possible engine overheating.

Retarded (late) timing will result in torque loss, high fuel consumption, and white to black smoke.

![[fp902gc.png]]

The Lucas CAV DPA/DPS advance timing mechanism uses a check ball in the circuit which, if omitted during assembly, will result in no timing advance. If the fuel injection pump has been replaced or the mechanism has been removed to fix a leak, the problem can be that the check ball is missing.

![[fp9cbga.png]]

Electrical Shutoff Valves

The fuel injection pumps are equipped with electrical shutoff valves. These solenoid-operated valves block the supply of fuel to the high-pressure pumping and distribution components.

The Bosch® VE shutoff valve is located at the top rear of the pump.

![[fv900gi.png]]

The Lucas CAV DPA/DPS shutoff valve is located at the bottom rear of the pump.

Both 12- and 24-VDC activate-to-run and activate-to-stop solenoids are available.

![[fv901ga.png]]

The Stanadyne DB4 shutdown solenoid is located under the governor cover.

Both 12-VDC and 24-VDC activate-to-run and activate-to-stop solenoids are available.

![[ip900kb.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries.

![[13900050.png]]

> [!warning] CAUTION · Осторожно
> Do not remove the control lever. The fuel control lever on the Bosch® VE fuel injection pump is indexed to the shaft during pump calibration. If the lever has been removed and reinstalled incorrectly, engine speed and power will be affected.

Rotary Distributor Type Fuel Injection Pumps

Bosch® VE, Lucas CAV DPA, Stanadyne DB4, and Delphi DP210

- Disconnect the fuel drain manifold. [[40-006-021-tr — Fuel Manifold (Drain)|Refer to Procedure 006-021]].
- Remove the injection pump supply line. [[40-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024]].
- Remove the high-pressure lines. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051]].
- Disconnect the electrical wire to the fuel shutoff valve. [[40-005-043 — Fuel Shutoff Valve|Refer to Procedure 005-043]].
- Remove the fuel air control tube, if used. [[40-006-001-tr — AFC Air Tube|Refer to Procedure 006-001]].

- Disconnect all control linkage. Refer to the OEM service manual
- Remove the pump support bracket. [[40-005-033-tr — Fuel Pump Support Bracket|Refer to Procedure 005-033]].

![[ck800wa.png]]

### Remove

Front Gear Train

Remove the access cap, gear retaining nut, and washer.

![[gc9cama.png]]

> [!note] Note · Примечание
> Be **sure** to disengage the pin after locating top dead center.

Locate top dead center for cylinder Number 1 by barring the engine slowly, while pushing in on the top dead center pin.

![[bc900wa.png]]

Lucas CAV DPA Pump and Delphi DP210

Loosen the CAV fuel injection pump lock screw and position the special washer; then tighten the lock screw against the pump drive shaft.

> [!tip] Момент затяжки · Torque Value
> 7 n•m [62 in-lb]

![[fs9loua.png]]

Stanadyne DB4 Pump

Loosen the Stanadyne DB4 fuel injection pump lock screw and position the special washer. Tighten the lock screw until contact is made with the fuel injection pump drive shaft.

> [!tip] Момент затяжки · Torque Value
> 12 n•m [106 in-lb]

![[ip9waha.png]]

Bosch® VE

The special washer on the Bosch® VE injection pump **must** be removed so the lock screw can be tightened against the drive shaft.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

> [!note] Note · Примечание
> Wire the washer to the pump.

![[fs9wama.png]]

Pull the fuel injection pump drive gear loose from the pump drive shaft.

Use fuel pump gear puller, Part Number 3163381 or Part Number 3824469, with M8-1.25 x 50 capscrews, Grade 8.8 or equivalent.

![[fs9gema.png]]

> [!warning] CAUTION · Осторожно
> Do not drop drive gear key when removing the pump. Failure to do so can result in severe engine damage.

Remove the three mounting nuts and take off the fuel injection pump.

> [!note] Note · Примечание
> Fuel pumps on engines designed to meet Tier 2/Stage II Industrial emissions levels have straight holes (**not** kidney slots) and do **not** use a timing key.

![[fs9keaa.png]]

Remove the gasket and clean the surface.

![[gh9hsea.png]]

Rear Gear Train

Permanently mark the injection pump flange to match the mark on the fuel pump mounting plate.

![[05m00173.png]]

Unlike the front gear train engine, do **not** remove the timing pin until completion of the repair. Failure to do so can result in difficult reassembly and incorrect timing of the fuel pump.

![[bc900wa.png]]

Locate top dead center (TDC) for cylinder number 1 by barring the crankshaft slowly while pressing on the engine timing pin. Barring the engine is recommended from the flywheel on the rear of the engine.

Using the barring tool Part Number 3824591, rotate the crankshaft slowly while pressing on the engine timing pin to locate TDC for cylinder number 1.

![[bc9piua.png]]

> [!warning] CAUTION · Осторожно
> Failure to properly torque the lock screw will result in improper timing of the pump during reassembly.

Bosch® VE

The special washer on the Bosch® VE injection pump **must** be removed so the lock screw can be tightened against the drive shaft.

> [!tip] Момент затяжки · Torque Value
> 40 n•m [22 ft-lb]

> [!note] Note · Примечание
> Wire the washer to the pump.

> [!note] Note · Примечание
> The torque specification for the rear gear train engine is higher than the front gear train engine, to prevent rotation of the pump shaft during installation of the fuel pump gear retaining nut.

![[fs9wama.png]]

Remove the mounting nuts and bolts affixing the fuel pump mounting plate to the rear gear housing.

Take off the fuel injection pump, fuel pump mounting plate, and fuel pump gear as an assembly.

> [!note] Note · Примечание
> Make sure the gear does **not** rotate during removal; failure to do so can result in incorrect timing of the pump during installation.

![[05900886.png]]

Remove the gasket and clean the surface.

![[05900887.png]]

Mark a tooth on the fuel gear pump relative to the fuel pump mounting plate.

![[05900888.png]]

Remove the fuel pump retaining nut and washer.

Remove the fuel pump gear.

Loosen the three mounting nuts attaching the fuel pump to the fuel pump mounting plate.

Remove the fuel pump from the fuel pump mounting plate.

![[05900889.png]]

Remove the gasket material and clean the surface.

![[05900890.png]]

### Install

Front Gear Train

Verify cylinder Number 1 is at top dead center by barring the engine slowly while pushing in on the top dead center pin.

![[bc900wa.png]]

Install a new gasket.

![[fp9gkha.png]]

> [!warning] CAUTION · Осторожно
> The drive shaft must be clean and free of all oil before installation. Failure to make certain the drive shaft is free of oil can result in the drive gear slipping on the shaft.

> [!note] Note · Примечание
> The shaft of a new or reconditioned pump is locked so the key aligns with the drive gear keyway when cylinder Number 1 is at top dead center on the compression stroke.

Install the pump. Make sure the key does **not** fall into the gear housing.

> [!note] Note · Примечание
> Fuel pumps on engines designed to meet Tier 2/Stage II Industrial emission levels do **not** use a timing key.

![[fs9keaa.png]]

Hand tighten the three mounting nuts. The pump **must** be free to move in the slots.

> [!note] Note · Примечание
> Fuel pumps on engines designed to meet Tier 2/Stage II Industrial emissions levels have straight holes (**not** kidney slots) and do **not** use a timing key.

![[fp900wi.png]]

> [!warning] CAUTION · Осторожно
> Be sure the timing pin is disengaged before the final torque step to avoid damage to the timing pin.

Install the pump drive shaft nut and spring washer. The pump will rotate slightly because of gear helix and clearance. This is acceptable, provided the pump is free to move on the flange slots and the crankshaft does **not** move.

> [!tip] Момент затяжки · Torque Value
> 15 to 20 n•m [132 to 177 in-lb]

![[fp9nuhd.png]]

If installing the original pump, rotate the pump to align the scribe marks.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [18 ft-lb]

![[fp900wk.png]]

If installing a new or rebuilt pump without scribe marks, take up gear lash by rotating the pump against the direction of drive rotation. Tighten the flange mounting nuts.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [18 ft-lb]

![[fp9nuna.png]]

Permanently mark the injection pump flange to match the mark on the gear housing.

![[fp9hswa.png]]

Lucas CAV DPA Pump and Delphi DP210

For CAV fuel injection pumps, loosen the lockscrew and position the special washer behind the lockscrew head.

> [!tip] Момент затяжки · Torque Value
> 20 n•m [177 in-lb]

![[fs9loub.png]]

Stanadyne DB4 Pump

For Stanadyne DB4 fuel injection pumps, loosen the lock screw and position the special washer behind the lock screw head.

Tighten the lock screw.

![[ip9wama.png]]

Bosch® VE

Loosen the Bosch® fuel pump lock timing screw and install the special washer that is wired to the fuel pump.

Tighten the Bosch® fuel pump lock timing screw.

> [!tip] Момент затяжки · Torque Value
> 13 n•m [115 in-lb]

![[05900792.png]]

Disengage the timing pin before rotating the crankshaft.

![[bc9piba.png]]

Tighten the pump retaining nut.

Torque Value:

Bosch® VE (M14-1.5 nut)

Torque Value:

Bosch® VE (M12 nut)

Torque Value:

Lucas CAV/DPA

Torque Value:

Stanadyne

Torque Value:

Delphi DP21

![[fp9nuhe.png]]

Install the access cap.

![[gc9cvha.png]]

Rear Gear Train

Unlike the front gear train engine, do **not** remove the timing pin until completion of the repair. Failure to do so can result in difficult reassembly and incorrect timing of the fuel pump.

Verify cylinder number 1 is at top dead center by barring the engine slowly while pushing in on the top dead center pin.

Barring the engine is recommended from the flywheel on the rear of the engine.

Using the barring tool Part Number 3824591, rotate the crankshaft slowly while pressing on the engine timing pin to locate TDC for cylinder number 1.

![[bc9piua.png]]

Install a new fuel pump gasket on the fuel pump mounting plate.

![[05900891.png]]

Install the fuel pump to the fuel pump mounting plate.

> [!tip] Момент затяжки · Torque Value
> 18 n•m [159 in-lb]

![[05900892.png]]

If installing the original fuel pump, rotate the pump to align the scribe marks on the fuel pump mounting plate.

> [!tip] Момент затяжки · Torque Value
> 18 n•m [159 in-lb]

![[05v00069.png]]

> [!warning] CAUTION · Осторожно
> The drive shaft must be clean and free from oil before installation. Failure to make certain the drive shaft is free of oil can result in the drive gear slipping on the shaft.

Install the fuel pump gear on the fuel pump shaft.

Align the mark on the fuel pump gear with the mark on the fuel pump mounting plate.

Install the fuel pump drive shaft nut and spring washer.

Tighten the pump retaining nut.

> [!tip] Момент затяжки · Torque Value
> 98 n•m [72 ft-lb]

![[05900894.png]]

With a new fuel pump cover plate gasket, install the fuel pump, fuel pump mounting plate, and fuel pump gear assembly onto the rear gear housing.

Torque Value:

M8

Torque Value:

M10

![[05900895.png]]

Loosen the Bosch® fuel pump lock timing screw and install the special washer that is wired to the pump.

Tighten the Bosch® fuel pump lock timing screw.

> [!tip] Момент затяжки · Torque Value
> 13 n•m [115 in-lb]

![[fp9wahb.png]]

Disengage the timing pin before rotating the crankshaft.

![[bc9piba.png]]

### Time

Tier 2/Stage II Timing Adjustment

If the pump timing is out by more than the specified tolerance as determined in Procedure Refer to Procedure 005-037 it is possible on Tier 2/Stage II engines, which no longer use the keyway in the fuel pump shaft, that the fuel pump gear has slipped on the fuel pump shaft. The fuel pump gear to pump shaft taper will need to be broken so the pump timing can be reset.

> [!note] Note · Примечание
> This procedure applies to front gear train Tier 2/Stage II engines **only**. directions in Refer to Procedure 005-037, when adjusting the fuel pump timing of engines equipped with kidney slots.

![[nobox.png]]

The top dead center timing pin **must** be disengaged. Bar the engine in the **clockwise** direction, when viewed from the front of the engine, until the dial indicator reading reflects the plunger travel specified on the engine dataplate. This point will be beyond top dead center. Lock the pump drive shaft at this position. [[40-100-001-tr — Engine Identification|Refer to Procedure 100-001]] Engine Identification in Section E, for the engine dataplate location.

> [!note] Note · Примечание
> If barring the engine past the specified timing plunger travel value, turn the engine in an **counterclockwise** direction, when viewed from the front of the engine, past top dead center at least one quarter turn, then bring the engine back toward top dead center in a **clockwise** direction when viewed from the front of the engine, until the desired timing value is achieved.

The special washer on the Bosch® VE injection pump **must** be removed so the lock screw can be tightened against the drive shaft.

> [!tip] Момент затяжки · Torque Value
> 30 n•m [22 ft-lb]

> [!note] Note · Примечание
> Wire the washer to the fuel pump.

![[fs9wama.png]]

Remove the access cap.

Remove the fuel pump gear retaining nut and washer.

![[gc9cama.png]]

To remove the fuel pump gear, use gear puller, Part Number ST647 or 3163381, to separate the fuel pump gear from the shaft.

With the gear loose from the fuel pump drive shaft, bar the engine in the opposite direction of rotation, when viewed from the front of the engine, past top dead center at least one quarter turn. Then bar engine in the direction of rotation to top dead center until the timing pin engages the camshaft.

![[05900807.png]]

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Clean the fuel injection pump drive shaft taper and drive gear bore with a residue-free cleaner. Dry both surfaces with compressed air.

Failure to clean and dry the shaft thoroughly can result in further timing slip after the engine is run.

![[05900253.png]]

> [!warning] CAUTION · Осторожно
> Prior to torquing the fuel pump gear nut, make sure the engine is locked and can not rotate during final torquing of the fuel pump nut.

This can be achieved by using the engine barring tool to prevent the engine from rotating. Make sure the fuel pump is locked at this stage.

![[er900ws.png]]

Push the fuel pump gear onto the shaft and assemble the washer and nut.

Remove the top dead center timing pin from the camshaft and the timing pin on the damper, if used.

Tighten the fuel pump retaining nut.

Torque Value:

Bosch® VE (M14-1.5 nut)

Torque Value:

Bosch® VE (M12 nut)

Torque Value:

Lucas CAV/DPA

Torque Value:

Stanadyne

Torque Value:

Delphi DP21

![[fp9nuhd.png]]

Bosch® VE

Loosen the Bosch® fuel pump lock timing screw and install the special washer that is wired to the fuel pump.

Tighten the Bosch® fuel pump lock timing screw.

> [!tip] Момент затяжки · Torque Value
> 13 n•m [115 in-lb]

![[05900792.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of engine or timing pin damage, you must disengage the timing pin before attempting to bar or crank the engine.

Disengage the timing pin before rotating the crankshaft.

![[bc9piba.png]]

Install the access cap and check to make sure the engine barring tool is removed, then recheck the timing as described in the previous steps.

If the timing is within tolerance, remove the timing gauge from the fuel pump and replace the plug.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

![[fp9toma.png]]

Tighten the gear pump retaining nut.

Torque Value:

Bosch® VE (M14-1.5 nut)

Torque Value:

Bosch® VE (M12 nut)

Torque Value:

Lucas CAV/DPA

Torque Value:

Stanadyne

Torque Value:

Delphi DP21

![[fp9nuhe.png]]

Install the access cap.

![[gc9cvha.png]]

### Finishing Steps

Rotary Distributor Type Fuel Injection Pumps

Bosch® VE, Lucas CAV DPA, Stanadyne DB4, and Delphi DP210

- Install the injection pump support bracket. [[40-005-033-tr — Fuel Pump Support Bracket|Refer to Procedure 005-033]]
- Install all high-pressure fuel lines. [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051]]
- Install the injection pump supply line. [[40-006-024-tr — Fuel Supply Lines|Refer to Procedure 006-024]]
- Connect the fuel drain manifold. [[40-006-021-tr — Fuel Manifold (Drain)|Refer to Procedure 006-021]]
- Connect the electrical wire to the fuel shutoff valve. [[40-005-043-tr — Fuel Shutoff Valve|Refer to Procedure 005-043]]
- If required, install the air-to-fuel control valve. [[40-006-001-tr — AFC Air Tube|Refer to Procedure 006-001]]
- Disconnect all control linkage. Refer to OEM service manual.

> [!note] Note · Примечание
> When connecting the cable and rod to the control lever, adjust the length so the lever has stop-to-stop movement. Adjust the length of the cable or rod to the mechanical shutdown lever so there is stop-to-stop movement.

Replacing the fuel supply lines, fuel filters, fuel injection pump, high-pressure fuel lines, and injectors will let air enter the fuel system. Follow the specified procedure to bleed the air from the system.

- [[40-006-015-tr — Fuel Filter (Spin-On Type)|Refer to Procedure 006-015]], Fuel Filter, Spin-On, for proper venting of the low pressure side of the fuel system
- [[40-006-051-tr — Injector Supply Lines (High Pressure)|Refer to Procedure 006-051]], Injector Supply Lines (High Pressure), for venting of the high-pressure side of the fuel system.

![[ck800wa.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries
- Operate the engine and check for leaks.

![[13900050.png]]
