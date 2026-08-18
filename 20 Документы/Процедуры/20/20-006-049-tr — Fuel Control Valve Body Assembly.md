---
aliases:
  - "Корпус клапана управления подачей топлива в сборе"
type: "Процедура"
doc: "20-006-049-tr"
title_en: "Fuel Control Valve Body Assembly"
title_ru: "Корпус клапана управления подачей топлива в сборе"
modified: "2006-07-14"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 13
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-049-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-049-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Fuel Control Valve Body Assembly
**Корпус клапана управления подачей топлива в сборе**

> [!abstract] Процедура · `20-006-049-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 6 - Injectors and Fuel Lines - Group 06
> **Даты:** изменён 2006-07-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-006-049-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/20-006-049-tr.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Depending on the circumstance, fuel is flammable. When performing any or all of the following procedures to remove fuel supply lines and related components, keep all cigarettes, flames, pilot lights, arcing equipment, and switches out of the work area and areas sharing ventilation to reduce the possibility of severe personal injury or death when working on a fuel system.

> [!danger] WARNING · Опасно
> When using solvents, acids or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> Do not spill or drain fuel into the bilge area when disconnecting or removing fuel lines, replacing filters, and priming the fuel system. Do not drop or throw filter elements into the bilge area. The fuel and fuel filters must be disposed of in accordance with local environmental regulations.

- Disconnect the battery. Refer to Procedure 013-009.
- Remove the crankcase vent hose from the camshaft follower cover. Refer to Procedure [[20-004-001-tr — Cam Follower Assembly|004-001]]
- Remove the ECM. Refer to Procedure 019-031 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engine, Bulletin 4021493.
- Clean the control valve body and the surrounding area.

![[ck800wa.png]]

### Remove

with Mechanically Actuated Injector

Disconnect the fuel supply hose (1), timing pressure line (2), and rail pressure line (3), at the control valve body.

![[05400017.png]]

> [!note] Note · Примечание
> It is a good service practice to label parts during removal. Identification of the connections at time of removal with a label will aid the installation process.

Label the electrical connections to the actuators, fuel pressure sensors, and ambient air pressure sensor.

![[05400018.png]]

Disconnect the actuators and pressure sensor connections.

![[05400019.png]]

Remove the nut holding the electrical connection of the fuel shutoff valve coil. Remove the connection.

![[05400020.png]]

Remove the four mounting capscrews. Move the wire harness and brackets away from the control valve body to gain access.

Remove the control valve body assembly.

![[05400021.png]]

### Install

with Mechanically Actuated Injector

Install the four capscrews to secure the control valve body assembly and the wire harness and brackets.

> [!tip] Момент затяжки · Torque Value
> 45 n•m [33 ft-lb]

![[05400021.png]]

Tighten the nut that holds the electrical connection post on the fuel shutoff valve coil.

> [!tip] Момент затяжки · Torque Value
> 3 n•m [27 in-lb]

![[05400022.png]]

Install the electrical connection on the fuel shutoff valve.

Install the nut on the threaded post of the coil.

Use two 3/8-inch wrenches. Hold the post of the nut firmly while tightening the connection nut.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

![[05400020.png]]

Inspect the actuator and pressure sensor connections for dirt and debris.

Use dielectric lithium grease, Part Number 3822934, and QD® contact cleaner, Part Number 3824510. Clean and lubricate the connections and actuator if cleaning is required.

![[05400024.png]]

> [!note] Note · Примечание
> If the electrical connections were **not** labeled for identification purposes during disassembly, verify the types of connections on the wiring diagram.

Connect the actuator and pressure sensor connections.

![[05400019.png]]

Connect the fuel supply hose (1), the timing rail pressure line (2), and the metering rail pressure lines (3) to the control valve body.

Tighten the fuel supply hose (1).

Tighten the timing pressure (2) and rail pressure lines (3).

| Fuel Supply Hose (1) | 61 n.m | \[45 ft-lb\] |
|---|---|---|

| Timing and Rail Pressure Lines (2 and 3) | 27 n.m | \[20 ft-lb\] |
|---|---|---|

![[05400017.png]]

### Finishing Steps

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Install the ECM. Refer to Procedure 019-031 in the Troubleshooting and Repair Manual, Electronic Control System, QSK19 CM850 Modular Common Rail System Series Engine, Bulletin 4021493.
- Install the crankcase vent hose. Refer to Procedure [[20-004-001-tr — Cam Follower Assembly|004-001]].
- Connect the batteries. Refer to Procedure 013-009.
- Prime the fuel system (if necessary). Refer to Procedure [[20-005-016-tr — Fuel Pump|005-016]].

Operate the engine and check for leaks.

![[ck800wa.png]]
