---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "60-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `60-019-050`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-050.pdf)

### Remove

[[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E for sensor location information.]]

Clean the fuel shutoff valve and surrounding area.

Disconnect the engine harness connectors from the fuel shutoff valve.

Remove the fuel shutoff valve mounting capscrews.

![[19800921.png]]

### Clean and Inspect for Reuse

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

> [!danger] WARNING · Опасно
> Some solvents are flammable and toxic. Read the manufacturer's instructions before using.

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Use mineral spirits to clean all of the parts except the solenoid.

Dry with compressed air.

Do **not** get cleaning solution on the solenoid. Clean the solenoid with a dry cloth. Use 200-grit emery cloth and a flat surface to polish the solenoid surface.

Check the fuel shield, spring washer, valve disc, actuator disc, and actuator housing for dirt, bonding separation, corrosion, cracks, or wear. Replace any parts if necessary.

![[gr8vaka.png]]

Inspect the fuel shutoff valve spacer for damage or wear.

If the fuel shutoff valve spacer is damaged or worn, it **must** be replaced.

![[19400741.png]]

Use a wire brush to clean any corrosion from the solenoid terminal.

![[19802551.png]]

### Install

Install a new o-ring (6) between the spacer (7) and the electronic control valve body (8).

Install the spacer (7) o-ring groove toward the coil. Install the actuator disc (5) with the cup side toward the solenoid. Install the spring washer (3) with the cup side toward the solenoid.

Align the actuator disc (5), spacer (7), and valve disc (4) on the electronic control valve body (8). Install a new o-ring (6).

Put the spring washer (3) on the valve disc (4), with the cavity side positioned upward, in a position around the valve locator.

The solenoid **must** be orientated with the electrical connection post on the bottom.

Install the fuel shield (2) and solenoid (1) on the electronic control valve body (8). Install a new o-ring and tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[19800921.png]]

Place the engine harness connectors on the fuel shutoff valve posts.

Install the nuts on the threaded posts of the solenoid.

Use two wrenches. Hold the post nut firmly while tightening the connection nut.

> [!tip] Момент затяжки · Torque Value
> 3 n•m [27 in-lb]

![[05400020.png]]

### Resistance Check

Make sure the shutoff valve coil is the correct voltage (24-VDC).

The coil voltage and part number are cast into the terminal connection end of the coil.

Remove the solenoid wire.

Use the multimeter to check the coil resistance.

| Fuel System Shutoff Valve Solenoid Specifications |  |  |
|---|---|---|
| Voltage | Resistance Minimum (Ohms) | Resistance Maximum (Ohms) |
| 24-VDC | 24 | 50 |

If the coil resistance does **not** meet specification, the coil **must** be replaced.

Install the solenoid wire when the repair is complete.

![[19a00840.png]]

### Voltage Check

Make sure the shutoff valve coil is the correct voltage (24-VDC).

The coil voltage and part number are cast into the terminal connection end of the coil.

![[19a00840.png]]

Set the RUN/STOP switch to the RUN position.

Use a multimeter to check the voltage to the coil.

The voltage **must** be the same as the battery voltage.

Set the RUN/STOP switch to the STOP position.

![[19802553.png]]
