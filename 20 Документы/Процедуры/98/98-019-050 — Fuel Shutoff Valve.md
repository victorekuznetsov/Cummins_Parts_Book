---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "98-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2004-12-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `98-019-050`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-050.pdf)

### General Information

The fuel shutoff valve is mounted on top of the electronic fuel control module.

Check the valve to make sure it has the correct voltage rating. The voltage and part number are stamped on the case of the valve.

![[19801709.png]]

### Initial Check

Check the override screw to be sure the valve is open.

- Turn the screw **clockwise** to lock the valve in the open position.
- Turn the screw **counterclockwise** to disable the valve mechanical override.

> [!note] Note · Примечание
> To start the engine, in case of an electrical failure, turn the valve knob on the shutoff valve **clockwise** to open the valve. This will manually open the valve.

![[19802008.png]]

Most of the valves are internally grounded. If the valve has a long post and a short post, the short post is internally grounded.

> [!note] Note · Примечание
> If there is **only** one post, the valve is internally grounded. Most CENTRY™ applications will use a single-post valve.

![[19802009.png]]

Make sure all of the wire connection nuts are tight, whether a wire is attached or **not**.

![[19802010.png]]

Use a wire brush to clean corroded terminal posts.

![[19802011.png]]

Make sure the shutoff valve coil is the correct voltage.

The coil voltage and part number are cast into the terminal connection end of the coil.

![[19802012.png]]

### Remove

Disconnect the fuel tubing from the fuel shutoff valve.

Disconnect the voltage supply wire from the fuel shutoff solenoid.

![[19801965.png]]

Remove the two capscrews, lockwashers, and washers securing the fuel shutoff valve to the EFC module.

Remove the fuel shutoff valve.

![[19801966.png]]

### Disassemble

Remove the four mounting capscrews securing the fuel shutoff valve solenoid to the fuel shutoff valve.

Remove the solenoid housing, fuel shield, spring washer, valve disc, actuator disc, and actuator housing. Discard the o-rings.

![[19800920.png]]

### Clean and Inspect for Reuse

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

> [!note] Note · Примечание
> Do **not** get solution on the solenoid. Clean the solenoid with a dry cloth. Use 200-grit emery cloth on a flat surface to polish the solenoid surface.

Use solvent to clean all of the parts **except** the solenoid.

Dry with compressed air.

Check the fuel shield, spring washer, valve disc, actuator disc, and actuator housing for dirt, bonding separation, corrosion, cracks, or wear. Inspect disk (5) and electronic control body (8) for excessive wear. Replace any parts if necessary.

![[gr8vaka.png]]

Measure the resistance of the fuel shutoff valve coil. Disconnect the voltage supply wire. Select the resistance function on the multimeter. Touch one of the multimeter leads to the fuel shutoff valve terminal. Touch the other multimeter lead to a good, clean surface on the engine block. Measure the resistance. If the resistance is **not** within specifications, replace the valve.

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

![[19801712.png]]

### Assemble

> [!warning] CAUTION · Осторожно
> Clean all components before assembly. Dirty components can cause the engine not to shut down.

Reassemble the shutoff valve as follows:

Install a new o-ring (6) between the spacer (7) and the electronic control valve body (8).

Install the spacer (7), o-ring groove toward the coil. Install the actuator disc (5) with the cup side toward the solenoid. Install the spring washer (3) with the cup side toward the solenoid.

Align the actuator disc (5), spacer (7), and valve disc (4) on the electronic control valve body (8). Install a new o-ring (6) between the spacer (7) and the actuator disc (5).

Put the spring washer (3) on the valve disc (4), with the cavity side positioned upward, in a position around the valve locator.

> [!note] Note · Примечание
> The solenoid **must** be orientated with the electrical connection post on the bottom.

Install the fuel shield (2) and solenoid (1) on the electronic control valve body (8). Install new capscrew o-rings and tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[19800921.png]]

### Install

Install the fuel shutoff solenoid and tighten the two capscrews.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

![[19801966.png]]

Connect the fuel tubing to the fuel shutoff valve.

Connect the voltage supply wire to the fuel shutoff solenoid.

![[19801965.png]]
