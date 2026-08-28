---
aliases:
  - "Втягивающее реле стартера"
type: "Процедура"
doc: "40-013-019"
title_en: "Starter Solenoid"
title_ru: "Втягивающее реле стартера"
modified: "2006-03-31"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 21
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Starter Solenoid
**Втягивающее реле стартера**

> [!abstract] Процедура · `40-013-019`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2006-03-31
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-019.pdf)

### Initial Check

Before troubleshooting the starting motor, make sure the battery terminals are **not** loose or corroded.

![[ea8cosa.png]]

If the starting motor solenoid does **not** make a sound, check for loose wiring connections.

![[es900ka.png]]

Use a digital multimeter, Part Number 3377161, or equivalent, to set the voltage scale.

Check for system voltage at the starting motor solenoid battery terminal.

![[es900wk.png]]

If the multimeter indicates system voltage at the starting motor battery terminal, check the voltage at the starting motor solenoid "S" terminal, while the starting switch is energized.

If the multimeter indicates system voltage at "S" terminal but the starter does **not** engage, the starting motor solenoid is malfunctioning and the starter **must** be replaced.

![[13900056.png]]

If the multimeter does **not** indicate system voltage at the "S" terminal, check:

- Fuses
- Voltage to the ignition switch and magnetic switch.
- Application safety shutoff systems.

![[es900wm.png]]

### Voltage Check

Set the digital multimeter, Part Number 3377161, to measure DC volts.

Connect the multimeter positive (+) lead to the starter solenoid positive cable terminal and the negative (-) lead to a chassis or engine ground location.

The multimeter **must** show voltage with the starter switch in the OFF position to be normal.

![[es900wc.png]]

If the multimeter does **not** indicate voltage, check the cable connecting the starter solenoid and battery for breaks. Also, check for loose or corroded connections.

![[sb800kk.png]]

If the multimeter indicates voltage but the starter will **not** operate, check the wire connecting the starter solenoid to the starter switch for breaks, and also check for loose or corroded connections.

In addition be sure to check for:

- Fuses
- Application engine shutoff systems.

![[sb800kl.png]]

If the wire connecting the starter solenoid and starter switch is **not** loose or damaged and the starter will **not** operate:

- Remove the cable connecting the starter and starter solenoid from the solenoid terminal.
- Connect the multimeter positive (+) lead to the solenoid positive terminal and the negative (-) lead to the chassis or an engine ground location.

![[sb800km.png]]

- Turn the starter switch to the START position.
- If the multimeter indicates voltage, the starter solenoid is malfunctioning and **must** be replaced.

![[sb800kn.png]]

- If the multimeter does **not** indicate voltage, check the wire connecting the starter solenoid to the magnetic switch for breaks, and for loose or corroded connections.

![[sb800ko.png]]

If the wire connecting the starter solenoid to the magnetic switch is **not** loose or damaged and the starter will **not** operate:

- Check the cable connecting the starter solenoid to the starter motor for breaks, and for loose or corroded connections.

![[sb200kb.png]]

- Check the cable connecting the starter motor to the battery for breaks, and for loose or corroded connections.

![[sb8cosa.png]]

- If the cables are **not** loose or damaged, the starter motor is defective and **must** be replaced. Refer to [[40-013-020-tr — Starting Motor|Procedure 013-020]].

![[sb2cosa.png]]

Solenoid Control Circuit Voltage Drop on Delco® Starters.

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Disconnect the battery.

![[13900050.png]]

Remove all cables and connections from the battery terminal of the cranking motor.

Clamp all cables and connections together (a 1/2-inch bolt and nut works for clamping connections). Wrap a heavy cloth around the battery terminal of the cranking motor to be certain it does **not** touch any metal.

![[13900051.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Connect the battery.

![[13900050.png]]

Connect a digital multimeter, Part Number 3377161, between battery positive (+) and the “S” terminal (the multimeter should show battery open circuit voltage, about 12.5 to 12.6 VDC).

![[13900052.png]]

Close the vehicle start switch and the very first reading is the voltage drop. If you wait, the voltage reading will drop rapidly as the solenoid heats up and raises the solenoid resistance. Be certain to record the very first reading.

> [!note] Note · Примечание
> The motor will **not** crank if there is no voltage supplied to the motor.

Repeat the step with the multimeter connected between the battery negative (-) and motor negative (-). Add the voltages from the previous step and this step to get the control circuit voltage drop. Values are included in the table below.

With the hold-in and pull-in circuits both activated the maximum allowable voltage drop at 20°C \[68°F\] is:

| VDC | Voltage Drop (maximum) |
|---|---|
| 12 | 1.0 VDC |
| 24 | 2.0 VDC |
| 32 | 2.6 VDC |

| Solenoid Average Amperage Draw |  |  |  |
|---|---|---|---|
| Motor | VDC | PI & HI Amps | HI Amps |
| 28MT | 12 | 69 | 13 |
|  | 24 | 120 | 13 |
| 37MT | 12 | 74 | 19 |
|  | 24 | 36 | 6 |
| 41/42MT | 12 | 97 | 18 |
|  | 24 | 57 | 13 |
| 50MT | 12 | 86 | 15 |
|  | 24 | 49 | 6 |
|  | 32 | 38 | 6 |
|  | 64 | 10 | 2 |
| For 12 -DC systems, apply 10 VDC to the "S" terminal. |  |  |  |
| For 24-VDC systems, apply 20 VDC to the "S" terminal. |  |  |  |
| For some 32-VDC systems, apply 30 VDC to the "S" terminal. |  |  |  |
| For some 32-VDC and all 64-VDC systems, apply 30 VDC to the "B+" terminal. |  |  |  |

![[13900053.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Disconnect the battery.

![[13900050.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Replace all connections to the battery terminal of the motor and then reconnect the battery.

![[13900054.png]]
