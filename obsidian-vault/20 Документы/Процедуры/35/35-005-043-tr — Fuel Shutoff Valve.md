---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "35-005-043-tr"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2022-08-29"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
  - "4021942"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-043-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-043-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/35"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `35-005-043-tr`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]], [[4021942 — QSM11 Industrial Operation and Maintenance Manual|4021942]]
> **Секции:** Section 5 - Fuel System - Group 05 · Section A - Adjustment, Repair, and Replacement
> **Даты:** изменён 2022-08-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/35/35-005-043-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/35-005-043-tr.pdf)

### Resistance Check

Verify the shutoff valve coil is the correct voltage (12 or 24 VDC).

The shutoff valve coil voltage and part number are cast into the terminal connection end of the shutoff valve coil.

![[19c01393.png]]

Remove the wire.

Verify the remaining wire connection nut is tight. Tighten the nut, if required.

> [!tip] Момент затяжки · Torque Value
> 3 n•m [27 in-lb]

Verify the post is tight and secure in the coil.

> [!note] Note · Примечание
> Only single post coils can be used on the fuel system. Two post coils will interfere with the cooling line.

![[fv2swka.png]]

Use a wire brush to clean any corrosion from the coil terminal.

![[fp8vaea.png]]

Verify the coil wire is **not** connected before checking the coil resistance.

Measure the coil resistance with a multimeter, Part Number 3377161, or equivalent.

| Fuel System Shutoff Valve Solenoid Specifications |  |  |
|---|---|---|
| Voltage | Resistance Minimum (Ohms) | Resistance Maximum (Ohms) |
| 6 VDC | 1 | 5 |
| 12 VDC | 6 | 15 |
| 24 VDC | 24 | 50 |
| 32 VDC | 42 | 80 |
| 36 VDC | 46 | 87 |
| 48 VDC | 92 | 145 |
| 74 VDC | 315 | 375 |
| 115 VAC | 645 | 735 |

> [!note] Note · Примечание
> If the solenoid resistance is 0 ohms, there is an electrical short in the coil.

If the shutoff valve coil resistance is correct, the assembly of the valve **must** be checked. If the shutoff valve coil resistance does **not** meet specification, the shutoff valve coil **must** be replaced.

![[fv2swkc.png]]

Turn the vehicle keyswitch to the ON position.

Touch the wire to the coil terminal.

Listen for the valve to click when the wire is touched to the coil terminal. If the valve does **not** click, repair or replace the fuel shutoff valve.

![[fv8elka.png]]

### Voltage Check

> [!warning] CAUTION · Осторожно
> To avoid damage to the ECM, connect only one wire to the fuel shut off solenoid.

Connect the wire.

The coil voltage and part number are cast into the terminal connection end of the coil.

![[05200178.png]]

Turn the vehicle keyswitch to the ON position.

Check the voltage to the coil with a multimeter, Part Number 3377161 or equivalent.

The voltage **must** be the same as the battery voltage.

Turn the vehicle keyswitch to the OFF position.

![[fv2swkb.png]]

### Remove

Clean the fuel shutoff valve and surrounding area.

Disconnect the ring terminal from the fuel shutoff valve solenoid.

Remove the mounting capscrews securing the shutoff valve solenoid.

Remove the shutoff valve solenoid.

![[19200408.png]]

### Install

Install a new o-ring on the fuel shutoff valve.

Install the fuel shutoff valve and the capscrews.

> [!tip] Момент затяжки · Torque Value
> 4 n•m [35 in-lb]

Connect the fuel shutoff valve to the actuator harness.

> [!tip] Момент затяжки · Torque Value
> 3 n•m [27 in-lb]

![[19200408.png]]
