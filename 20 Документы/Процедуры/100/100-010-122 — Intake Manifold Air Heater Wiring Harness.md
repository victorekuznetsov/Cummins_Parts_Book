---
aliases:
  - "Жгут проводов подогревателя впускного воздуха"
type: "Процедура"
doc: "100-010-122"
title_en: "Intake Manifold Air Heater Wiring Harness"
title_ru: "Жгут проводов подогревателя впускного воздуха"
modified: "2003-08-26"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
figures: 14
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/100-010-122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/100"
---

# Intake Manifold Air Heater Wiring Harness
**Жгут проводов подогревателя впускного воздуха**

> [!abstract] Процедура · `100-010-122`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/100-010-122.pdf)

### Initial Check

Remove and check the fuse in the power circuit to the heater control module.

![[10900319.png]]

With the keyswitch in the ON position, verify the voltage from the keyswitch circuit to the fuse.

| Voltage |  |
|---|---|
| System | VDC |
| 12-VDC | 10.5 to 17 |
| 24-VDC | 22 to 29 |

If no or low voltage is indicated, the wiring and connections from the keyswitch to the fuse holder **must** be checked.

The air heater will **not** function properly unless the specified voltage is obtained.

![[10900320.png]]

### Voltage Check

Connect the positive lead of the multimeter to the air heater element terminals.

Ground the negative lead to a good known ground.

![[10900306.png]]

> [!danger] WARNING · Опасно
> Heater grids and studs can get hot enough to burn skin.

> [!warning] CAUTION · Осторожно
> Do not recycle the keyswitch repeatedly in a short period of time. This may cause damage to the grids or the wiring.

Attach a multimeter to the heater element wires.

Clamp the multimeter current probe around both wires to the air heater.

The following test will **only** last up to 20 seconds. Refer to the preheat cycle time in the General Information section.

| System Voltage | Voltage Range | Amperage Range |
|---|---|---|
| 12 | 10.5 to 17 | 80 to 110 (1 grid) |
| 12 | 10.5 to 17 | 160 to 220 (2 grids) |
| 24 | 22 to 29 | 80 to 110 |

Turn the keyswitch to the ON position. Do **not** crank the engine.

Record both the voltage and amperage readings.

The keyswitch **must** be turned OFF and ON again in order to recycle.

Voltage and amperage readings **must** be within the specified limits.

![[10900322.png]]

If no voltage is detected, disconnect the intake temperature sensor.

Disconnecting the intake temperature sensor simulates intake manifold temperature of less than 0°C \[32°F\]. This overrides the temperature circuit if the intake manifold temperature is too hot to allow the heater to turn on.

Turn the keyswitch OFF, then ON again.

Recheck the voltage and ampere readings.

Refer to Section E for the sensor location.

![[10900298.png]]

Verify the preheat cycle. After 20 seconds the voltage and amperage should drop to zero when the cycle ends.

The WAIT TO START lamp, if equipped, will stay on for 20 seconds. After 20 seconds, the lamp will begin to flash indicating the heater cycle has turned off. The lamp will continue to flash as long as the intake temperature sensor is disconnected indicating an open circuit.

![[15200051.png]]

If no voltage is detected at the heater grid with the intake temperature sensor disconnected, check the voltage to the solenoid.

Connect the multimeter and check the supply voltage to the solenoid secondary circuit (large terminal).

If no voltage is present, repair the wiring to the solenoid.

If voltage is present, check the solenoid.

Refer to Procedure [[100-010-126 — Intake Manifold Air Heater Solenoid Switch|010-126]], Intake Manifold Air Heater Solenoid Switch.

![[10900323.png]]

Check the voltage on the primary side of the solenoid, small terminal to small terminal.

If no voltage is present, check the ground.

If voltage is present at both terminals, replace the solenoid.

![[10900324.png]]

Check the voltage from the solenoid positive primary circuit to a good known ground.

If no voltage is present, check the voltage to the heater control module.

If voltage is present, restore the ground to the solenoid.

![[10900325.png]]

The solenoid and heater control module share the same ground.

Check the wire or clean the connectors.

![[10900298.png]]

Check the voltage to the heater control module.

The WAIT TO START lamp, if equipped, will stay on if there is no voltage to the heater control module.

![[15200051.png]]

If there is no WAIT TO START lamp, check the voltage at the resistor in the supply wire from the fuse to the heater control module.

If no voltage is present, repair the wiring harness.

Refer to the wiring diagram.

![[10900326.png]]

If voltage is present, check the resistor with an ohmmeter.

Replace the resistor if necessary.

Resistance: 15.8k ohms at 12-VDC

![[10900327.png]]

Check the voltage at both positive leads at the connection to the heater control module.

If voltage is **not** present, repair the wiring harness.

If voltage is present, replace the heater control module.

![[10900325.png]]
