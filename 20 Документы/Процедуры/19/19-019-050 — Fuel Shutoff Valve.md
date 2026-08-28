---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "19-019-050"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2004-12-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 15
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-050.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-050.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `19-019-050`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-050.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-050.pdf)

### Remove

Remove the ECM. Refer to Procedure [[19-019-031 — Engine Control Module|019-031]].

![[05400015.png]]

Clean the fuel shutoff valve and surrounding area.

![[05400016.png]]

Remove the nuts securing the electrical connections of the fuel shutoff valve solenoid. Remove the connections.

![[05400020.png]]

Remove the four mounting capscrews.

Remove the solenoid housing, fuel shield, spring washer, valve disc, actuator disc, and actuator housing.

Discard the o-rings.

![[19800920.png]]

### Inspect for Reuse

Use mineral spirits to clean all of the parts except the solenoid.

> [!note] Note · Примечание
> Do **not** get solution on the solenoid. Clean the solenoid with a dry cloth. Use 200-grit emery cloth and a flat surface to polish the solenoid surface.

Check the fuel shield, spring washer, valve disc, actuator disc, and actuator housing for dirt, bonding separation, corrosion, cracks, or wear. Replace any parts if necessary.

![[gr8vaka.png]]

Inspect the fuel shutoff valve spacer for damage or wear.

If damage or wear is present, replace the part.

![[19400741.png]]

Use a wire brush to clean any corrosion from the solenoid terminal posts.

![[fp8vaea.png]]

Check the solenoid with a multimeter. Replace the solenoid if the resistance is **not** to specification.

| Fuel System Shutoff Valve Specifications |  |  |
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

![[19400895.png]]

Tighten the nuts that hold the electrical connection posts on the fuel shutoff valve solenoid.

> [!tip] Момент затяжки · Torque Value
> 3 n•m [27 in-lb]

![[05400022.png]]

### Install

Install a new o-ring (6) into the electronic control valve body (8).

Install the actuator housing (7) with the o-ring groove toward the coil (1).

Install the actuator disc (5) with the cup side toward the coil (1).

Place the rubber side to the valve disc (4) on the actuator disc (5).

Install the valve spring (3) with the cup side toward the coil. The inner diameter of the spring (3) **must** rest on the pilot diameter of the valve disc (4).

Install a new o-ring (6) into the actuator housing (7).

Install the fuel shield (2) and coil (1) on to the front cover (8).

Tighten the four capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

![[19800921.png]]

Install the electrical connections on the fuel shutoff valve. Install the nut on the threaded post of the solenoid.

Use two 3/8 in wrenches. Hold the post of the nut firmly while tightening the connection nut. Repeat for second terminal.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

![[05400020.png]]

Install the ECM. Refer to Procedure [[19-019-031 — Engine Control Module|019-031]].

![[05400015.png]]

### Resistance Check

Make sure the shutoff valve coil is the correct voltage (24 VDC).

The coil voltage and part number are cast into the terminal connection end of the coil.

![[19400490.png]]

Remove the solenoid wires.

Use the multimeter to check the coil resistance.

| Fuel System Shutoff Valve Specifications |  |  |
|---|---|---|
| Voltage | Resistance Minimum (Ohms) | Resistance Maximum (Ohms) |
| 6 VDC | 1.72 | 2.02 |
| 12 VDC | 6 | 15 |
| 24 VDC | 24 | 50 |
| 32 VDC | 42 | 80 |
| 36 VDC | 54.5 | 61.5 |
| 48 VDC | 105 | 125 |
| 74 VDC | 323 | 367 |
| 115 VAC | 645 | 735 |

If the coil resistance does **not** meet specification, the coil **must** be replaced.

Install the solenoid wires after completing the repair.

![[19400895.png]]

### Voltage Check

Use a multimeter to check the voltage to the coil. Measure the voltage from the solenoid's supply connection to the engine block ground. The multimeter **must** show battery voltage.

Crank the engine to provide voltage to the fuel shutoff valve terminals.

Once the ECM has received the 50-rpm signal, the voltage will remain supplied to the fuel shutoff valve until the keyswitch is cycled to the OFF position.

![[fv2swkb.png]]
