---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "82-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2004-12-15"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `82-019-050`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2004-12-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-050.pdf)

### Resistance Check

Make sure the shutoff valve coil is the correct voltage (12 or 24 VDC).

The coil voltage and part number are cast into the terminal connection end of the coil.

![[19c01393.png]]

Remove the solenoid wire.

Use the multimeter meter to check the coil resistance.

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
> If the solenoid shows 0 ohms, there is an electrical short in the coil.

If the coil resistance is correct, the assembly of the valve **must** be checked. If the coil resistance does **not** meet specification, the coil **must** be replaced. Refer to Procedure [[35-005-043 — Fuel Shutoff Valve|005-043]] in the ISM/QSM11 Troubleshooting and Repair Manual, Bulletin [[3666322 — ISM, ISMe, and QSM11 Service Manual\|3666322]], for inspection of the valve.

Install the solenoid wire after completing the repair.

![[19c00709.png]]

### Voltage Check

Make sure the shutoff valve coil is the correct voltage (12 or 24 VDC).

The coil voltage and part number are cast into the terminal connection end of the coil.

![[19c01393.png]]

Turn the vehicle keyswitch on.

Use a multimeter to check the voltage to the coil.

The voltage **must** be the same as the battery voltage.

Turn the vehicle keyswitch off.

![[19c00708.png]]

### Remove

Disconnect the ring terminal from the fuel shutoff valve solenoid.

Remove the mounting capscrews securing the solenoid.

Remove the solenoid.

![[19200408.png]]

### Install

Install a new o-ring on the solenoid.

Install the solenoid and capscrews.

> [!tip] Момент затяжки · Torque Value
> 3.4 n•m [30 in-lb]

Connect the ring terminal to the fuel shutoff valve solenoid.

![[19200408.png]]
