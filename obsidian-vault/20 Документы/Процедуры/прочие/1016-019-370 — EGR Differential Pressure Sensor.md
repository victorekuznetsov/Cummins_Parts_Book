---
type: "Процедура"
doc: "1016-019-370"
title_en: "EGR Differential Pressure Sensor"
modified: "2022-11-23"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-370.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-370.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
---

# EGR Differential Pressure Sensor

> [!abstract] Процедура · `1016-019-370`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-11-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-370.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-370.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool, or equivalent

#### Additional Service Items

- No additional service items required.

### General Information

The Exhaust Gas Recirculation (EGR) valve differential pressure sensor has two ports that sense a pressure drop across the EGR gas entrance to the intake connection. The Engine Control Module (ECM) uses this pressure drop to calculate the amount of EGR gas entering the intake. This calculation helps to determine the commanded position of the EGR valve that will control the amount of EGR gas flow into the engine.

The EGR valve differential pressure sensor is mounted on the top of the venturi tube.

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.
- Clean the area around the EGR differential pressure sensor.

### Remove

Disconnect the engine harness connector from the EGR differential pressure sensor.

Remove the two capscrews from the base of the sensor and remove the sensor from the engine.

![[19s00192.png]]

### Clean and Inspect for Reuse

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

Clean the EGR differential pressure sensor and adapter mounting surfaces. Remove any dirt buildup or soot residue.

If the EGR differential pressure sensor has frozen, defrost the sensor using warm air that is below 60°C \[ 140°F \].

Dry with compressed air.

Inspect the EGR differential pressure sensor bracket for cracks or fretting. If damage is present, the sensor **must** be replaced. The bracket is **not** a serviceable component.

![[19b00265.png]]

Inspect the o-rings for cracks or other damage.

Replace the o-rings if cracks or other damage is found.

![[19c01419.png]]

### Install

Make sure that the o-rings are seated and place the EGR differential pressure sensor onto the venturi tube.

![[19s00193.png]]

Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 8 n•m [71 in-lb]

Connect the wiring harness to the sensor (1).

![[19s00194.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- Use the recommended Cummins® electronic service tool, or equivalent, to reset the fuel tables if EGR differential pressure sensor is replaced. Refer to Procedure 005-263 in Section 5.
- Operate the engine. Check for leaks.
