---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "94-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 13
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `94-019-050`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/94-019-050.pdf)

### Remove

Clean the fuel shutoff valve and surrounding area.

![[05400016.png]]

Remove the nut holding the electrical connection of the fuel shutoff valve solenoid. Remove the connection.

![[05400020.png]]

Remove the four mounting capscrews. Remove the solenoid housing, fuel shield, spring washer, valve disc, actuator disc, and actuator housing. Discard the o-rings.

![[19800920.png]]

### Inspect for Reuse

> [!note] Note · Примечание
> Do **not** get solution on the solenoid. Clean the solenoid with a dry cloth. Use 200 grit emery cloth and a flat surface to polish the solenoid surface.

Use mineral spirits to clean all of the parts except the solenoid.

Visually check the fuel shield, spring washer, valve disc, actuator disc, and actuator housing for dirt, bonding separation, corrosion, cracks, or wear. Replace any parts if necessary.

![[gr8vaka.png]]

Use a wire brush to clean any corrosion from the solenoid terminal.

![[19a00093.png]]

Check the solenoid with a multimeter. Replace the solenoid if the resistance is not between 28 to 32 ohms.

> [!note] Note · Примечание
> If the solenoid shows 0 ohms, there is an electrical short in the coil.

![[fv8etka.png]]

Tighten the nut that holds the electrical connection post on the fuel shutoff valve solenoid.

![[19a00094.png]]

### Install

Assemble the shutoff valve as shown. Install these parts as follows.

Install a new o-ring (6) between the spacer (7) and the electronic control valve body (8).

Install the spacer (7) o-ring groove toward the coil. Install the actuator disc (5) with the cup side toward the solenoid. Install the spring washer (3) with the cup side toward the solenoid.

![[19800921.png]]

Align the actuator disc (5), spacer (7), and valve disc (4) on the electronic control valve body (8). Install a new o-ring (6).

Put the spring washer (3) on the valve disc (4), with the cavity side positioned upward, in a position around the valve locator.

> [!note] Note · Примечание
> The solenoid **must** be orientated with the electrical connection post on the bottom.

Install the fuel shield (2) and solenoid (1) on the electronic control valve body (8). Install a new o-ring and tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [72 in-lb]

![[19800921.png]]

Install the electrical connection of the fuel shutoff valve. Install the nut on the threaded post of the solenoid.

Use two wrenches. Hold the post of the nut firmly while tightening the connection nut.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [15 in-lb]

![[05400020.png]]

### Resistance Check

Make sure the shutoff valve coil is the correct voltage (24 volts).

The coil voltage and part number are cast into the terminal connection end of the coil.

![[19400490.png]]

Remove the solenoid wire.

Use the multimeter to check the coil resistance. The coil resistance **must** be 28 to 32 ohms for 24 VDC solenoids.

If the coil resistance does **not** meet specification, the coil **must** be replaced. Refer to Procedure [[94-019-050 — Fuel Shutoff Valve|019-050]].

Install the solenoid wire when the repair is complete.

![[fv8etka.png]]

### Voltage Check

Place the Stop/Run switch in the RUN position.

Controller **not** in the diagnostic mode.

Use a multimeter to check the DC voltage to the coil.

The voltage **must** be the same as the battery voltage.

Place the Stop/Run switch in the STOP position.

![[19a00034.png]]
