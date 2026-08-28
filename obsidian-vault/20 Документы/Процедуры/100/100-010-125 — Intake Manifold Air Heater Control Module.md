---
aliases:
  - "Блок управления подогревателем впускного воздуха"
type: "Процедура"
doc: "100-010-125"
title_en: "Intake Manifold Air Heater Control Module"
title_ru: "Блок управления подогревателем впускного воздуха"
modified: "2003-08-26"
engines:
  - "93047320"
  - "93058669"
  - "93087701"
families:
  - "6B5.9"
  - "C8.3 · 6C8.3"
manuals:
  - "3666003"
  - "3666087"
figures: 20
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-125.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-125.pdf"
tags:
  - "документ/процедура"
  - "двигатель/6B5.9"
  - "двигатель/C8.3"
  - "группа/100"
---

# Intake Manifold Air Heater Control Module
**Блок управления подогревателем впускного воздуха**

> [!abstract] Процедура · `100-010-125`
> **Двигатели:** [[93047320 — 6B5.9 CPL 3111|93047320]], [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** 6B5.9, C8.3 · 6C8.3
> **Входит в руководства:** [[3666003 — C Troubleshooting and Repair Manual|3666003]], [[3666087 — B3.9, B4.5, B4.5 RGT, and B5.9 Service Manual|3666087]]
> **Секции:** Section 10 - Air Intake System - Group 10
> **Даты:** изменён 2003-08-26
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/100/100-010-125.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/100-010-125.pdf)

### Initial Check

Connect the positive lead of the multimeter to the heater terminals.

Ground the negative lead to the engine block.

![[10900306.png]]

Attach a multimeter to the heater wires.

Clamp the ammeter current probe around both wires to the air heater.

Turn the keyswitch to the ON position, but do **not** start the engine.

![[10900322.png]]

If there is no voltage to the heater control module, check the system voltage. Refer to Procedure [[100-010-122 — Intake Manifold Air Heater Wiring Harness|010-122]].

The air heater will preheat as long as the intake manifold temperature is below 35°C \[95°F\].

This will repeat each time the keyswitch is turned from the OFF to the ON position.

The multimeter and ammeter should indicate the cycle for proper voltage and amperage.

Refer to the Intake Manifold Air Heater System General Information in Section F to verify the proper cycle.

![[15200051.png]]

If no voltage was detected, disconnect the intake temperature sensor.

Disconnecting the intake temperature sensor simulates an intake manifold temperature of less than 0°C \[32°F\].

This overrides the temperature circuit if the intake manifold temperature is too hot to allow the heater to turn on.

Turn the keyswitch OFF, then ON again.

Recheck the voltage and ampere readings.

Refer to Section E for the sensor location.

| System Voltage | Voltage Range | Amperage Range |
|---|---|---|
| 12 | 10.5 to 17 | 80 to 110 (1 grid) |
| 12 | 10.5 to 17 | 160 to 220 (2 grids) |
| 24 | 22 to 29 | 80 to 110 |

If no voltage and no amperage are detected, check the following:

- Intake air heater solenoid switch, refer to Procedure [[100-010-126 — Intake Manifold Air Heater Solenoid Switch|010-126]]
- Intake manifold air heater element, refer to Procedure [[100-010-124 — Intake Manifold Air Heater Element|010-124]].

![[10900298.png]]

If all systems check out properly and the preheat does **not** cycle according to the heater cycle chart, replace the heater control module.

![[10900329.png]]

Post Heat Cycle

Connect the positive lead of the multimeter to the heater element terminal.

Ground the negative lead to the engine block.

![[10900306.png]]

Attach a multimeter to the heater wires.

Clamp the ammeter current probe around both wires to the air heater.

![[10900322.png]]

Before starting the engine, allow the preheat cycle to operate.

![[15200051.png]]

Start the engine.

Verify the voltage and amperage are cycling on and off according to the Heater Cycle Chart for Post Heat Cycle.

Refer to the Intake Manifold Air Heater System General Information in Section F to verify the proper cycle.

The intake manifold temperature **must** be below 35°C \[95°F\] for the air heater to operate.

![[10900330.png]]

If no voltage is detected, disconnect the intake manifold air temperature sensor.

Disconnecting the temperature sensor simulates intake manifold temperature of less than 0°C \[32°F\]. This overrides the temperature circuit if the intake manifold temperature is too hot to allow the heater to turn on.

Turn the keyswitch OFF, then ON again.

Recheck the voltage and ampere readings.

Refer to Section E for the sensor location.

| System Voltage | Voltage Range | Amperage Range |
|---|---|---|
| 12 | 10.5 to 17 | 80 to 110 (1 grid) |
| 12 | 10.5 to 17 | 160 to 220 (2 grids) |
| 24 | 22 to 29 | 80 to 110 |

Post heat cycle is dependent on temperature, voltage, and rpm. All **must** be in the specified normal operating range.

If the intake manifold temperature, voltage, or engine rpm exceed system parameters prior to the 20 second time cycle completion, the system will reset and a new 20 second heat cycle will begin.

Refer to the Intake Manifold Air Heater System General Information in Section F to verify the proper cycle.

If no voltage and no amperage are detected, check the following:

- Engine rpm is in the correct range
- Intake manifold air heater system voltage, refer to Procedure [[100-010-122 — Intake Manifold Air Heater Wiring Harness|010-122]]
- Intake air heater solenoid switch, refer to Procedure [[100-010-126 — Intake Manifold Air Heater Solenoid Switch|010-126]]
- Intake manifold air heater element, refer to Procedure [[100-010-124 — Intake Manifold Air Heater Element|010-124]].

![[10900298.png]]

If all systems check out properly and the post heat does **not** cycle according to the heater cycle chart, replace the heater control module.

![[10900329.png]]

Post Heat Recycle

If the intake manifold temperature, voltage, or engine rpm exceeds the test parameters prior to 20 minutes time cycle completion, the system will reset and a new 20 minute post heat recycle will be available.

Perform these checks with the engine running under the same engine rpm, intake manifold temperature, and voltage condition as during the post cycle check.

The post heat recycle will operate for 20 minutes, then shut off. Refer to the Intake Manifold Air Heater System General Information in Section F to verify the proper cycle.

Verify that the heater control module is functioning to the known temperature value being simulated for the intake manifold sensor.

If the system is **not** operating at these known values, replace the heater control modules.

![[10900329.png]]

### Remove

Disconnect the ground cable from the battery terminal.

![[ee8comk.png]]

Remove the two mounting capscrews that hold the bracket to the engine block.

![[10900331.png]]

Remove the plug from the heater control module.

![[10900332.png]]

Remove the nut from the top right solenoid bracket.

Remove the heater control module mounting capscrews and spacers.

![[10900329.png]]

### Install

Install the new heater control module on the bracket.

![[10900329.png]]

Install the bracket on the engine block.

![[10900331.png]]

Install the heater control module plug.

Torque the hold down screws hand tight.

![[10900332.png]]

Connect the ground cable to the battery terminals.

![[ea8coha.png]]
