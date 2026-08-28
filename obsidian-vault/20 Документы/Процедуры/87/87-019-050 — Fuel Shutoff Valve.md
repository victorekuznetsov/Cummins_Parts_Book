---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "87-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2022-08-16"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `87-019-050`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Controls - Group 19 · Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2022-08-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-050.pdf)

### Test

This test checks the Bosch® EHAB internal solenoid. Turn the vehicle keyswitch to the OFF position.

Disconnect the 9-pin Deutsch fuel injection pump electrical connector. Do **not** disconnect the 2-pin EHAB connector.

![[19a00338.png]]

While listening closely to the Bosch® EHAB device, have someone turn the keyswitch to the ON position. You should hear a clicking sound as the internal solenoid energizes.

If a clicking sound is **not** heard, check the resistance as follows.

![[19a00752.png]]

Turn the vehicle keyswitch to the OFF position. Disconnect the 2-pin Bosch® EHAB device connector from the engine harness. Set the multimeter to measure resistance. Connect the alligator clips of the test leads to the multimeter probes.

![[19a00339.png]]

Measure the resistance between the pins of the Bosch® EHAB connector, EHAB device side. The resistance **must** measure between 38.5 and 43.5 ohms.

If the Bosch® EHAB device fails **either** of the above tests, it **must** be serviced by an authorized Bosch® repair location, or replace the device.

> [!note] Note · Примечание
> At the moment, the Bosch® EHAB device is replaceable **only** as an assembly.

![[19a00753.png]]

### Remove

Clean the EHAB fuel shutoff valve and surrounding area.

![[19a00282.png]]

Disconnect the EHAB fuel shutoff valve from the engine harness.

![[19a00249.png]]

Remove the mounting capscrews. Remove the solenoid housing, fuel shield, spring washer, valve disc, actuator disc, and actuator housing.

Discard the o-rings.

![[19a00283.png]]

### Install

Assemble the shutoff valve install and new o-ring.

Install the solenoid and the capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[19a00283.png]]

Connect the EHAB fuel shutoff valve to the engine harness.

![[19a00249.png]]

### Resistance Check

Disconnect the EHAB fuel shutoff valve from the engine harness.

Use the multimeter to check the coil resistance. The coil resistance **must** be 38.5 to 43.5 ohms for EHAB valves.

If the coil resistance does **not** meet specification, the coil **must** be replaced. [[87-019-050 — Fuel Shutoff Valve|Refer to Procedure 019-050]].

Connect the valve to the engine harness when the repair is complete.

![[19a00284.png]]

### Voltage Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use breakout cable, Part Number 3163531, when taking a measurement.

Disconnect the engine harness from the EHAB (fuel shutoff valve). Install the breakout cable between the engine harness and the EHAB connector. Set the multimeter to measure voltage. Turn the keyswitch to the ON position.

![[19a00741.png]]

Touch one of the multimeter leads to the red test lead of the breakout cable and the other lead to the black lead of the cable. Measure the voltage.

The voltage value **must** be unswitched battery voltage. If the voltage does **not** measure the same voltage as unswitched battery voltage and all other wiring checks have been performed and passed specification, the ECM has failed.

Replace the ECM. [[87-019-031 — Engine Control Module|Refer to Procedure 019-031]].

![[19a00741.png]]
