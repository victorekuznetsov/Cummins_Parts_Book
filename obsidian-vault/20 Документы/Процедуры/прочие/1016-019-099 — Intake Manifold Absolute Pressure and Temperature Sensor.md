---
type: "Процедура"
doc: "1016-019-099"
title_en: "Intake Manifold Absolute Pressure and Temperature Sensor"
modified: "2022-12-14"
engines:
  - "77804810"
families:
  - "15N"
manuals:
  - "5659763"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-099.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-099.pdf"
tags:
  - "документ/процедура"
  - "двигатель/15N"
---

# Intake Manifold Absolute Pressure and Temperature Sensor

> [!abstract] Процедура · `1016-019-099`
> **Двигатели:** [[77804810 — 15N CM2380 M104B CPL 5977|77804810]]
> **Семейство:** 15N
> **Входит в руководства:** [[5659763 — 15N CM2380 M104B Service Manual|5659763]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/1016/1016-019-099.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/1016-019-099.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Cummins® electronic service tool, or equivalent

#### Additional Service Items

- No additional service items required.

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.

### Remove

The intake manifold absolute pressure/temperature sensor measures the pressure/temperature of the intake manifold.

Lift up on the locking tab and pull the electrical connectors apart.

Remove the sensor from the engine by turning the sensor **counterclockwise**.

![[19s00155.png]]

### Clean and Inspect for Reuse

> [!danger] WARNING · Опасно
> Wear appropriate eye and face protection when using compressed air. Flying debris and dirt can cause personal injury.

If the intake manifold absolute pressure and temperature sensor has frozen, defrost the sensor using warm air that is below 60°C \[ 140°F \].

Dry with compressed air.

Inspect the engine wiring harness connector and the sensor for the following:

- Cracked or broken connector shell
- Missing or damaged connector seals
- Dirt, debris, or moisture in or on the connector pins
- Corroded, bent, broken, pushed back, or expanded pins.

Repair or replace the engine wiring harness connector and sensor.

![[19s00234.png]]

### Test

Disconnect the intake manifold absolute pressure/temperature sensor from the engine wiring harness.

Measure the resistance between the temperature signal pin and return pin at the intake manifold absolute pressure/temperature sensor connector.

If the resistance does **not** meet the specification, replace the intake manifold absolute pressure/temperature sensor.

| Temperature vs Resistance |  |  |  |
|---|---|---|---|
| Temperature | Resistance (Ohms) |  |  |
| °C | °F | MIN | MAX |
| -50 | -58 | 607,265 | 843,786 |
| -40 | -40 | 302,255 | 419,979 |
| -30 | -22 | 157,596 | 218,978 |
| -20 | -4 | 85,643 | 119,000 |
| -10 | 14 | 48,298 | 67,109 |
| 0 | 32 | 30,683 | 36,605 |
| 10 | 50 | 18,472 | 22,036 |
| 20 | 68 | 11,462 | 13,674 |
| 30 | 86 | 7456 | 8578 |
| 40 | 104 | 4876 | 5610 |
| 50 | 122 | 3263 | 3754 |
| 60 | 140 | 2233 | 2569 |
| 70 | 158 | 1560 | 1795 |
| 80 | 176 | 1111 | 1278 |
| 90 | 194 | 814 | 917 |
| 100 | 212 | 605 | 669 |
| 110 | 230 | 450 | 502 |
| 120 | 248 | 339 | 383 |
| 130 | 266 | 259 | 396 |
| 140 | 284 | 201 | 231 |
| 150 | 302 | 157 | 183 |

![[3377161.png]]

### Install

Make sure the new sensor has an o-ring installed on it.

Install the new sensor into the engine by turning the sensor **clockwise**.

> [!tip] Момент затяжки · Torque Value
> 24 n•m [212 in-lb]

Push the connectors together until they lock.

![[19s00155.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- Use the recommended Cummins® electronic service tool, or equivalent, to reset the fuel tables if intake manifold absolute pressure/temperature sensor is replaced. Refer to Procedure 005-263 in Section 5.
- Operate the engine. Check for proper operation.
