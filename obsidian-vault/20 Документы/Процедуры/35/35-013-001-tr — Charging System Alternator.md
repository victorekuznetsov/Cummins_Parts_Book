---
aliases:
  - "Генератор системы зарядки"
type: "Процедура"
doc: "35-013-001-tr"
title_en: "Charging System Alternator"
title_ru: "Генератор системы зарядки"
modified: "2024-11-11"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-001-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-001-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Charging System Alternator
**Генератор системы зарядки**

> [!abstract] Процедура · `35-013-001-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 13 - Electrical Equipment - Group 13
> **Даты:** изменён 2024-11-11
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-013-001-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-013-001-tr.pdf)

### Initial Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!danger] WARNING · Опасно
> Acid is extremely dangerous and can damage the machinery and can also cause serious burns. Always provide a tank of strong soda water as neutralizing agent when servicing the batteries. Wear goggles and protective clothing to reduce the possibility of serious personal injury.

Attach the carbon-pile tester and clip on ammeter as shown. Adjust the load from the carbon-pile tester to the rated performance of the alternator.

Measure the voltage drop in both the positive and negative circuits. Add these together. The sum can **not** exceed a maximum voltage drop of 0.5-VDC.

Repair or replace the wiring as required to meet the above specifications.

![[13800028.png]]

Attach the multimeter to the alternator as illustrated in the graphic.

With the batteries in fully charged condition and all the accessories off, start the engine and run it at high idle. Allow time for the voltage to stabilize before taking any readings.

Measure the alternator output voltage. The system maximum output limit is 15.5-VDC.

Repair or replace the alternator or regulator if the voltage limit exceeds the maximum output limit.

Refer to the manufacturer's specifications for minimum voltage output.

![[13800026.png]]

Connect the carbon-pile tester to the batteries in parallel.

Clamp the induction ammeter around the alternator output wire.

If more than one wire is connected to the alternator output terminal, clamp the ammeter around all wires.

Start the engine and operate at high idle.

Make sure all vehicle loads are turned off.

Check the speed of the alternator using a digital optical tachometer. A slipping alternator drive belt can result in a low output reading. The alternator output is directly related to the speed it is turning.

The alternator **must** be turning at approximate rated speed. Most heavy-duty alternators are rated at 5000 rpm. Check the manufacturer's specifications for the specific alternator being tested.

![[13800027.png]]

Turn on the carbon-pile tester and adjust until the ammeter reaches its highest reading. Record this value.

Turn off the carbon-pile tester and shut off the engine.

If the reading on the ammeter is zero (no output), magnetize the rotor with the alternator hooked up normally. Momentarily connect a jumper lead from the battery positive (+) to the alternator relay (R) or indicator (I) terminal. This procedure applies to both negative (-) and positive (+) ground systems, and will restore the normal residual magnetism.

Repeat the test. If the output is **not** within 10 percent of the rated output (stamped on the alternator case), replace the alternator.

![[13800027.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gasses. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Remove the battery cables. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 in Section 13.]]
- Remove the electrical connection from the alternator. Label the connections as they are removed.
- Remove the alternator drive belt. [[35-013-005-tr — Charging System Alternator Drive Belt|Refer to Procedure 013-005 in Section 13.]]

![[ck800wa.png]]

### Remove

Pad Mount

Remove the four alternator mounting capscrews.

Remove the alternator from the alternator bracket.

![[13200097.png]]

Spool Mount

Remove the adjusting link mounting capscrew (3) and the adjusting link.

Remove the alternator mounting capscrew (1), nut, washer (2), and alternator.

![[eh8bdha.png]]

### Clean and Inspect for Reuse

Inspect the alternator pulley for cracks or broken grooves.

Replace the pulley if damage is found.

![[13c00016.png]]

### Install

Pad Mount

Install the alternator and the four mounting capscrews.

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 36 n•m [27 ft-lb]

No alignment adjustment is required for the alternator to the alternator bracket.

![[13200097.png]]

Spool Mount

Install the adjusting link and mounting capscrew (3).

Tighten the mounting capscrew.

> [!tip] Момент затяжки · Torque Value
> 47 n•m [35 ft-lb]

Install the alternator, capscrew (1), washer, and nut (2) to the mounting bracket and adjusting link.

Do **not** tighten the capscrews and nuts until the alternator belt is adjusted.

![[eh8bdha.png]]

### Finishing Steps

- Install the alternator drive belt. [[35-013-005-tr — Charging System Alternator Drive Belt|Refer to Procedure 013-005 in Section 13.]]
- Connect the alternator electrical connections.
- Connect the battery cables. [[99-013-009 — Battery Cables and Connections|Refer to Procedure 013-009 in Section 13.]]
- Operate the engine and check for proper operation.

![[ck800wa.png]]
