---
aliases:
  - "Клапан отсечки топлива"
type: "Процедура"
doc: "20-005-043-tr"
title_en: "Fuel Shutoff Valve"
title_ru: "Клапан отсечки топлива"
modified: "2026-02-13"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4021592"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-043-tr.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-005-043-tr.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/20"
---

# Fuel Shutoff Valve
**Клапан отсечки топлива**

> [!abstract] Процедура · `20-005-043-tr`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4021592 — QSK19, QSK19 CM850 MCRS, and QSK19 CM2150 MCRS Service Manual|4021592]]
> **Секции:** Section 5 - Fuel System - Group 05
> **Даты:** изменён 2026-02-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/20/20-005-043-tr.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/20-005-043-tr.pdf)

### Preparatory Steps

with Mechanically Actuated Injector

Remove the electronic control module (ECM). [[19-019-031 — Engine Control Module|Refer to Procedure 019-031 in Section 19.]]

![[05400015.png]]

### Remove

with Mechanically Actuated Injector

> [!danger] WARNING · Опасно
> When using solvents, acids, or alkaline materials for cleaning, follow the manufacturer's recommendations for use. Wear goggles and protective clothing to reduce the possibility of personal injury.

Use solvent to clean the fuel shutoff valve and surrounding area.

![[05400016.png]]

Remove the nut holding the electrical connection of the fuel shutoff valve coil.

Remove the connection.

![[05400020.png]]

Remove the four capscrews.

Remove the coil housing and the fuel shield.

Discard the o-ring.

Remove the spring washer, valve disc, actuator disc, and actuator spacer from the valve housing.

Discard the o-ring.

![[19800920.png]]

### Inspect for Reuse

with Mechanically Actuated Injector

Use mineral spirits. Clean all of the parts **except** the coil assembly.

> [!note] Note · Примечание
> Do **not** get solvent on the coil. Clean the coil with a dry cloth. Use a 200 grit emery cloth and a flat surface to polish the coil surface.

Check the valve disc, valve seat, and actuator disc for dirt, metal parts, bonding separation, corrosion, cracks, or wear. Replace if necessary.

![[gr8vaka.png]]

Use a wire brush to clean any corrosion from the coil terminal.

![[05400073.png]]

Check the coil assembly with a multimeter.

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
> If the coil assembly shows 0 ohms, there is an electrical short in the coil.

![[fv8etka.png]]

Tighten the nut that holds the electrical connection post on the fuel shutoff valve coil.

> [!tip] Момент затяжки · Torque Value
> 3 n•m [27 in-lb]

![[05400022.png]]

### Install

with Mechanically Actuated Injector

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

Install the electrical connection on the fuel shutoff valve.

Install the nut on the threaded post of the coil.

Use two 3/8 in wrenches to hold the post of the nut firmly while tightening the connection nut.

> [!tip] Момент затяжки · Torque Value
> 2 n•m [18 in-lb]

![[05400020.png]]

### Voltage Check

Use a multimeter to check the voltage to the coil. Measure the voltage from the solenoid's supply connection to the engine block ground. The multimeter **must** show battery voltage.

Crank the engine to provide voltage to the fuel shutoff valve terminals.

Once the ECM has received the 50-rpm signal, the voltage will remain supplied to the fuel shutoff valve until the keyswitch is cycled to the OFF position.

![[fv2swkb.png]]

### Finishing Steps

with Mechanically Actuated Injector

Install the ECM. [[19-019-031 — Engine Control Module|Refer to Procedure 019-031 in Section 19.]]

![[05400015.png]]
