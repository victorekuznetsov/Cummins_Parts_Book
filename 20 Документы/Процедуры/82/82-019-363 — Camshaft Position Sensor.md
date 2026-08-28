---
aliases:
  - "Датчик положения распределительного вала"
type: "Процедура"
doc: "82-019-363"
title_en: "Camshaft Position Sensor"
title_ru: "Датчик положения распределительного вала"
modified: "2022-02-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "3666322"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-363.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-363.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/82"
---

# Camshaft Position Sensor
**Датчик положения распределительного вала**

> [!abstract] Процедура · `82-019-363`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[3666322 — ISM, ISMe, and QSM11 Service Manual|3666322]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2022-02-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-363.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-363.pdf)

### General Information

The camshaft position sensor reports the speed and position of the camshaft to the engine control module (ECM).

Use the following procedure for the location of the camshaft position sensor. [[35-100-002-tr — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]

![[ck800wa.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. Refer to the original equipment manufacturer (OEM) service manual.

![[ck800wa.png]]

### Remove

Disconnect the sensor from the engine harness.

Remove the capscrew that secures the sensor to the cylinder block.

Remove the sensor from the mounting location.

![[19d02849.png]]

### Clean and Inspect for Reuse

Inspect the camshaft position sensor for debris, cracks, or other damage from contact with the tone wheel.

If there is debris on the camshaft position sensor, clean the sensor.

Inspect the engine harness connector and sensor for the following:

- Cracked or broken connector shell
- Missing or damaged connector
- Dirt, debris, or moisture in or on the connector pins
- Corroded, bent, broken, pushed back, or expanded pins
- Chipped, cracked, extruded, or damaged sensor.

Repair or replace parts, as necessary.

![[19c01380.png]]

Inspect the camshaft position sensor o-ring for the following:

- Swollen o-ring
- Nicks or cuts in or on the o-ring.

Replace the o-ring if any damage is found.

![[19d02997.png]]

### Test

Connect the camshaft position sensor to the engine harness.

Use an electronic service tool to monitor the value of the crankshaft position sensor with the key ON and the engine OFF.

Place the ratchet drive side of the socket tool that was used to remove the sensor from the engine, flush on the sensor so the edge of the socket is on the edge of the sensor. Slowly slide the socket along the edge of the sensor, as illustrated.

> [!note] Note · Примечание
> The tool or part used for this **must** be of a non-ferrous material (a magnet would attach itself to the sensor).

Monitor the sensor state while passing the socket over the sensor. Verify that the state changes from high to low or low to high.

If the sensor state does **not** change, replace the camshaft position sensor.

![[19d02998.png]]

### Install

Lubricate the o-ring with clean engine oil before installation.

Install the camshaft position sensor by pressing firmly on the top of the sensor until the o-ring is fully seated.

Install and tighten the capscrew.

> [!tip] Момент затяжки · Torque Value
> 10 n•m [89 in-lb]

Connect the engine harness to the sensor.

![[19d02849.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. Refer to the OEM service manual.
- Operate the engine and check for leaks.

![[ck800wa.png]]
