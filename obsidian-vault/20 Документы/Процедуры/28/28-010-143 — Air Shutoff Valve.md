---
aliases:
  - "Воздушная отсечная заслонка"
type: "Процедура"
doc: "28-010-143"
title_en: "Air Shutoff Valve"
title_ru: "Воздушная отсечная заслонка"
modified: "2023-08-30"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "3810497"
figures: 16
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-010-143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-010-143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/28"
---

# Air Shutoff Valve
**Воздушная отсечная заслонка**

> [!abstract] Процедура · `28-010-143`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[3810497 — K38, K50, QSK38 and QSK50 Operation and Maintenance Manual|3810497]]
> **Секции:** Section - Maintenance Procedures at 10000 Hours
> **Даты:** изменён 2023-08-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/28/28-010-143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/28-010-143.pdf)

### General Information

> [!danger] WARNING · Опасно
> Do not operate a diesel engine where there are or can be combustible vapors. These vapors can be sucked through the air intake system and cause engine acceleration and over speeding that can result in a fire, an explosion, and extensive property damage. Numerous safety devices are available, such as air intake shutoff devices, to minimize the risk of over speeding where an engine, due to the application, is operating in a combustible environment, such as due to a fuel spill or gas leak. Remember, Cummins Inc. has no way of knowing the use you have for your engine. The equipment owner and operator are responsible for safe operation in a hostile environment. Consult a Cummins® Authorized Repair Location for further information.

> [!warning] CAUTION · Осторожно
> Operation of the air shutoff valves is an emergency response and may result in possible damage to the engine.

> [!note] Note · Примечание
> This package has air intake shutoff valves installed as a safety device to minimize the risk of over speeding where an engine will be operated in a potentially combustible environment.

The air shutoff valves (1) are located between the turbocharger and air intake crossover to the aftercoolers. One shutoff valve is available per cylinder bank.

![[10g00023.png]]

Early models have a manual reset handle located under the main valve body (1).

![[10q00215.png]]

Later models have a hexagon drive reset in the same location (2). This operates in the same way as the reset handle, but a wrench **must** be used to turn the hexagon drive.

![[10q00216.png]]

### Basic Description

The purpose of the air shutoff valve is intended to close the airflow off to the engine intake system during an emergency situation.

The air shutoff valve has four major components:

1. Valve body- Includes integrated male/female Marmon flanges.
2. Actuator- Sealed housing that includes a solenoid activated latch system. The actuator also includes a position switch to indicate the state of the valve (open/closed).
3. Manual Reset/Torsional Spring- Provides the necessary force to close the gate using the handle or hexagon drive.
4. Gate- Moving metal disc that blocks airflow when the valve is activated (shown in the open position).

![[10g00024.png]]

The air shutoff valve is a power-to-close device. When the valve solenoid is energized, the actuator unlatches allowing the gate to close under the force of the torsional spring.

The valves **must** be manually reset by rotating the manual reset (1) until the actuator "clicks" and holds the gate open.

The engine controller will **not** allow the engine to be started when one or more air shutoff valves is closed.

![[10g00025.png]]

The air shutoff valves operate under two conditions:

If a normal overspeed shutdown signal from the controller does **not** shut off the engine, a secondary overspeed signal triggers an air shut off shutdown. Fuel is shut off at the same time and the beacon on top of the Customer Interface Box (C.I.B.) will come on.

![[10g00026.png]]

The air shutoff valves can be manually closed by pushing the E-stop button on the power module control panel. This is an emergency action that can result in engine damage.

> [!note] Note · Примечание
> Emergency shutdown can **not** be used for normal shutdown of the engine.

![[10g00027.png]]

When an emergency shut off has occurred, the manual reset (1) will be in the closed position. Check the engine for damage before restarting.

Check for evidence of flammable vapors near the intake air source.

Check the turbocharger seals to verify there are no oil leaks. Refer to Procedure 010-040 in Section 10.

Inspect the engine crankshaft speed/position and camshaft position sensors for signs of damage or tampering.

![[10g00025.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Verify the air shutoff valve is in the closed position prior to removal and handling to reduce the possibility of personal injury.

> [!note] Note · Примечание
> This procedure is used for removing just one of the air shutoff valves from the engine. The remaining air shutoff valve can be removed using similar steps.

- De-energize the system and follow all safety procedures (Lock Out/Tag Out). See equipment manufacturer service information.
- Disconnect the air/fuel supply to the air starter, if equipped. [[102-012-022 — Air Starting Motor|Refer to Procedure 012-022 in Section 12.]]
- With the engine stopped, manually activate the E-Stop to close the air shutoff valves before removing them.
- Reset the E-Stop. Disconnect power supply. See equipment manufacturer service information.

> [!note] Note · Примечание
> The E-Stop **must** be reset before disconnecting the power, otherwise the air shutoff valve will automatically close when the electrical connection is made.

### Remove

> [!danger] WARNING · Опасно
> Verify the air shutoff valve is in the closed position prior to removal and handling to reduce the possibility of personal injury.

Loosen the clamps (3) and remove the air intake pipe (2) from the turbocharger to the air shutoff valve.

Disconnect the wiring harness (1) from the air shutoff valve near the solenoid.

Remove the V-band clamp (4) from the air crossover connection.

Remove the air shutoff valve (5).

Remove and discard the o-rings (6).

![[10g00028.png]]

Cover the air crossover and turbocharger connection points to prevent debris contamination.

Repeat the removal steps for the opposite side.

![[10l00030.png]]

### Clean and Inspect for Reuse

Inspect the air intake pipe, connection hose, hose clamps, and V-band clamps.

Replace any damaged parts.

![[10l00031.png]]

Do **not** disassemble the valve body. The valve body is **not** a serviceable part.

![[10g00029.png]]

### Install

> [!danger] WARNING · Опасно
> Verify the air shutoff valve is in the closed position prior to removal and handling to reduce the possibility of personal injury.

![[10g00030.png]]

Remove any protective covers from the air crossover and turbocharger connections.

Install a new o-ring onto the air shutoff valve (1).

With the reset handle facing down; loosely install the air shutoff valve (2) to the air crossover on the engine using a V-band clamp (3).

![[10g00031.png]]

Rotate the air shutoff valve (1) so the reset handle is facing away from the engine, as shown.

Tighten the V-band clamp holding the air shutoff valve to the air crossover.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

![[10g00032.png]]

Install a new o-ring (1) and the air crossover pipe (2) onto the air shutoff valve using a V-band clamp (3) and to the turbocharger with the flexible hose. Tighten the V-band clamp (3). Tighten the clamps (4) on the air crossover hose.

> [!tip] Момент затяжки · Torque Value
> 9 n•m [80 in-lb]

Connect the wiring harness for the air shutoff valve near the solenoid (5).

> [!note] Note · Примечание
> Avoid routing the wiring harness near high temperature components.

Repeat for the opposite side.

![[10g00033.png]]

### Finishing Steps

> [!warning] CAUTION · Осторожно
> Do not check the air shutoff valve function with engine running.

- Energize the system and follow all safety procedures (Lock Out/Tag Out). See equipment manufacturer service information.

Check the air shutoff valve operation:

- Test the air shutoff valve function by pressing the system emergency stop with the engine stopped.
- Reset the valves to an open position. Inspect the valves for obvious signs of damage/loose fasteners.
- Use the manual release to actuate the valves. Reset the valve to an open position.
- Connect the air/fuel supply to the air starter, if equipped. [[102-012-022 — Air Starting Motor|Refer to Procedure 012-022 in Section 12.]]
- Start and operate the engine. Check for leaks and faults.
