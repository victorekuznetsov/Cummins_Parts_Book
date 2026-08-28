---
aliases:
  - "Генератор системы зарядки"
type: "Процедура"
doc: "40-013-001-tr"
title_en: "Charging System Alternator"
title_ru: "Генератор системы зарядки"
modified: "2024-11-11"
engines:
  - "93047320"
families:
  - "6B5.9"
manuals:
  - "3666087"
figures: 22
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "группа/40"
---

# Charging System Alternator
**Генератор системы зарядки**

> [!abstract] Процедура · `40-013-001-tr`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]]
> **Семейство:** 6B5.9
> **Входит в руководства:** [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2024-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/40/40-013-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/40-013-001-tr.pdf)

### General Information

Due to the number of different alternator brands and configurations, the following procedure has been generalized to cover the most common configurations. Consult the alternator manufacturer for any information that is **not** covered in this procedure.

Typical Delco™ Alternator Wiring System

Indicator (I) Terminal

The main function of the indicator (I) terminal is to indicate if the alternator is working correctly. Typically, an indicator light is wired to this terminal. If the alternator is **not** charging properly, the light turns on. Another function of the indicator (I) terminal is that it can be used to supply up to 1 ampere of output at system voltage.

Lamp (L) Terminal

Similar to the I terminal, the L terminal is used to indicate if the alternator is working correctly. The difference between the L terminal and the I terminal is that the L terminal is a current sink **only** and can **not** be used to reduce turn on speed.

Relay (R) Terminal

The function of the relay (R) terminal varies. It can supply up to 4 amperes of output at one-half nominal alternator voltage to power items such as a tachometer or an hour meter.

One-Wire System

This is the simplest of the wiring systems because the **only** wires connected to the alternator are at the battery (BAT) and ground terminals. (See Table 5.) Connecting to the R terminal, L terminal, and I terminal is optional.

Three-Wire System

This system requires more wiring because it has a battery (BAT) terminal, R terminal, two blade terminals identified as number 1 and number 2, and a ground terminal. Typically, in the three-wire system, the number 1 blade terminal serves as the I terminal. (See Table 5.) The advantage of the three-wire system is that it provides the same features as the one-wire system, plus remote sense. By connecting the number 2 blade terminal to the battery's positive (+) terminal, the voltage is both sensed and regulated at the battery, instead of at the alternator. This eliminates the potential for voltage losses in the wiring from the alternator to the battery.

![[13900200.png]]

One Wire System, Typical Alternator (Delco-Remy™) with Combined Metri-Pack™ Connector

| One Wire System, Typical Alternator (Delco-Remy™) with Combined Metri-Pack™ Connector |  |  |  |
|---|---|---|---|
| 1 | GRD\* | Ground |  |
| 4 | R\* | Charge indicator, automatic lockout system, tachometer\*\* |  |
| 5 | BAT | Battery |  |
| 7 | L | Lamp Terminal |  |

\* **Not** all alternators have this feature.

\*\*Provides voltage pulses at about one-half system voltage at a frequency of one-tenth of generator rpm.

![[13900134.png]]

One Wire System, Typical Alternator (Delco-Remy™)

| One Wire System, Typical Alternator (Delco-Remy™) |  |  |
|---|---|---|
| 3 | GRD\* | Ground |
| 4 | R\* | Charge indicator, automatic lockout system, tachometer\*\* |
| 5 | BAT | Battery |
| 6 | I\* | Indicator light |

\* **Not** all alternators have this feature.

\*\*Provides voltage pulses at about one-half system voltage at a frequency of one-tenth of alternator rpm.

![[13900135.png]]

Three Wire System, Typical Alternator (Delco-Remy™)

| Three Wire System, Typical Alternator (Delco-Remy™) |  |  |
|---|---|---|
| Key | Terminal | Connected To |
| 1 | Blade number 1\* | Indicator light |
| 2 | Blade number 2 | Voltage sense |
| 3 | GRD\* | Ground |
| 4 | R\* | Charge indicator, automatic lockout system, tachometer\*\* |
| 5 | BAT | Battery |
| 6 | I\* | Indicator light |

\* **Not** all alternators have this feature.

\*\*Provides voltage pulses at about one-half system voltage at a frequency of one-tenth of generator rpm.

![[13900133.png]]

Table 6, Typical Alternator (Bosch™ K1)

| Typical Bosch™ K1 Wiring System |  |  |
|---|---|---|
| Key | Terminal | Connected to |
| 1 | D+ | Electrical charging system status light |
| 2 | B+ | Positive battery |
| 3 | W | Tachometer |
| 4 | — | Ground/assembly |

### Initial Check

Check the drive belt and alternator pulley to be sure the alternator is rotating properly.

If any problems exist, check the following:

1. If the drive belt is slipping on the alternator pulley, use the following procedure to inspect the drive belt. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]] Use the following procedure to inpect the belt tensioner. [[40-008-087-tr — Cooling Fan Belt Tensioner|Refer to Procedure 008-087 in Section 8.]]
2. Remove the drive belt. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8]]. Check if the alternator pulley is loose on the shaft. If loose, remove the pulley and inspect for damage. [[40-013-006-tr — Alternator Pulley|Refer to Procedure 013-006 in Section 13.]]
3. If the alternator will **not** rotate or does **not** rotate freely, the alternator **must** be replaced. See the Remove and Install sections of this procedure.

![[13d00028.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Check the battery and all wiring connections.

Inspect the wiring for defects.

Check all connections for tightness and cleanliness, including the slip connectors at the alternator and engine compartment bulkhead, and the connections at the battery.

![[13d00008.png]]

### Test

> [!note] Note · Примечание
> Any multimeter reading of zero voltage indicates an open circuit.

Check for open circuits.

Turn the keyswitch to the ON position.

Connect a multimeter, Cummins® Part Number 3164488 or 3164489, to the following locations:

Delco™ Alternators

1. Alternator “BAT” terminal to ground
2. Alternator blade terminal “Number 1” to ground
3. Alternator blade terminal “Number 2” to ground.

Locate and repair the open circuit.

![[es900kz.png]]

Connect a carbon-pile load (battery/alternator tester) across the batteries in one of the battery boxes.

Clamp an induction pickup-type ampere-hour meter around the battery cable; or use the digital multimeter, Part Number 3164488 or 3164489, with the clamp-on current probe, Part Number 3164490.

![[ea8tohc.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.

Disconnect any cables that lead to any other battery boxes in the circuit, negative (-) cables first.

Operate the engine at high idle; and measure the alternator voltage output to the batteries with digital multimeter, Part Number 3164488 or 3164489. Refer to the OEM service manual.

![[ea800kc.png]]

Operate the engine at high idle and adjust the carbon-pile load-testing equipment to apply the maximum rated amperage load to the alternator. Refer to the OEM service manual.

> [!note] Note · Примечание
> The alternator maximum rated amperage output is normally stamped or labeled on the alternator.

Measure the alternator amperage output. Refer to the OEM service manual.

If the alternator output (amps) is **not** within 10 percent of rated output, repair or replace the alternator. Refer to the OEM service manual for repair procedures.

![[ea800kd.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.

Shut off the engine and remove the test equipment.

Connect all battery cables, negative (-) cable last.

![[ea8toma.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.

- Disconnect the batteries.

![[13900050.png]]

- Remove the drive belt from the alternator pulley. [[40-008-002-tr — Drive Belt, Cooling Fan|Refer to Procedure 008-002 in Section 8.]].
- Tag and label all wires on the alternator.
- Disconnect the wires.

![[ck800wa.png]]

### Remove

Spool Mount.

Remove the upper alternator link capscrew.

Remove the mounting capscrew and nut at the bottom of the alternator and alternator mounting bracket.

Remove the alternator.

![[13d00057.png]]

Hinge Mount

Remove the alternator link capscrew.

![[13d00019.png]]

Remove the alternator mounting capscrew.

Remove the alternator.

![[13d00020.png]]

### Install

Spool Mount

Install the alternator and the bottom alternator mounting capscrew and nut.

Install the upper alternator link mounting capscrew at the top of the alternator.

Tighten the capscrews.

Torque Value:

Lower Mounting Capscrew

Torque Value:

Upper Link Mounting Capscrew

![[13d00057.png]]

Hinge Mount

Install the alternator.

Install and tighten the alternator mounting capscrew.

> [!tip] Момент затяжки · Torque Value
> 40 n•m [30 ft-lb]

![[13d00020.png]]

Install the alternator link capscrew.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [212 in-lb]

![[13d00019.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To avoid arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as a neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.

Delco-Remy™ Alternator

- Connect all wires to the alternator.
- Install the drive belt. Refer to Procedure 008-002 in Section 8.

![[ck800wa.png]]

Bosch™ K1 Alternator

- Connect all wires to the alternator.

> [!tip] Момент затяжки · Torque Value
> 2.7 to 9.8 n•m [23.9 to 86.7 in-lb]

> [!tip] Момент затяжки · Torque Value
> 7.5 to 8.0 n•m [66.4 to 70.8 in-lb]

- Install the drive belt. Refer to Procedure 008-002 in Section 8.

![[nobox.png]]

- Connect the batteries.
- Start the engine and check for correct operation.

![[13900050.png]]
