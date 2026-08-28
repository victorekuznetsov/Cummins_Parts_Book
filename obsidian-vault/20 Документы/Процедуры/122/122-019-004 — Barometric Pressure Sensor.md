---
aliases:
  - "Датчик барометрического давления"
type: "Процедура"
doc: "122-019-004"
title_en: "Barometric Pressure Sensor"
title_ru: "Датчик барометрического давления"
modified: "2020-07-17"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-004.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-004.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Barometric Pressure Sensor
**Датчик барометрического давления**

> [!abstract] Процедура · `122-019-004`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2020-07-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-004.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-004.pdf)

### General Information

**With Mechanically Actuated Injectors**:

In general, a barometric sensor can be fitted to the engine close to or around the ECM. However, the barometric sensor could move depending on

engine and application.

**With Electronically Actuated Injectors**:

A barometric sensor can be fitted to any of the engines wiring harnesses. Generally mounted towards the front of the engine

on the left bank main wiring harness, but can be fitted on the Right Bank Main Wiring Harness or even the Front and Rear

Crossover harnesses. There are two ways to mount the sensor depending on the type of harness installed on the engine.

- Bolted – Aluminium Extrusion Harnesses
- Zip/Cable tied – Braided/ Flexible Harnesses.

### Initial Check

Connect an electronic service tool to the vehicle data link.

Turn the keyswitch to the ON position.

Monitor the barometric pressure. If the barometric pressure is less than or equal to 523 mm Hg \[20.6 in Hg\] and the present elevation is less than 10,000 feet, replace the barometric pressure sensor.

![[19400357.png]]

### Remove

**With Mechanically Actuated Injectors**:

Lift up on the tab and disconnect the connector from the sensor.

Remove the mounting capscrews and sensor from the engine.

![[19400379.png]]

**With Electronically Actuated Injectors and Bolted Barometric Sensors:**

Locate the barometric sensor, and disconnect it from the wiring harness connector.

Remove the three ‘nyloc nuts' holding retaining plate and sensor to the aluminium extrusion harness, and put the nyloc nuts and retaining plate to one side for reinstallation. The nyloc nuts can be used up to 5 times before requiring replacement. If unsure replace the ‘nyloc nuts' with new ones.

Discard the failed Barometric Sensor.

![[19300068.png]]

**With Electronically Actuated Injectors and Zip/Cable Tied Barometric Sensors:**

Locate the barometric sensor, and disconnect it from the wiring harness connector.

Using a set of side cutters snip the zip/ cable tie to release the failed barometric sensor.

Discard the failed barometric sensor.

![[19300068.png]]

### Install

**With Mechanically Actuated Injectors**:

Install a new sensor on the engine. Tighten the capscrews.

> [!tip] Момент затяжки · Torque Value
> 23 n•m [204 in-lb]

Push the connectors together until they lock.

![[19400379.png]]

**With Electronically Actuated Injectors and Bolted Barometric Sensors:**

Slide the new Barometric sensor over the M3 stud post and place the retaining plate over the top of the senor using the two

M6 and single M3 stud posts for orientation.

Secure the nuts using the torque specifications below, as this will ensure there is enough clearance for the Air Gap between

the sensor and the wiring harness.

M3: 3 N⋅m (2 ft-lb) – Secure First

M6: 8 N⋅m (6 ft-lb) – Secure Last

Reconnect the barometric pressure sensor to the wiring harness connector.

![[19300068.png]]

**With Electronically Actuated Injectors and Zip/Cable Tied Barometric Sensors:**

In the same location as the discarded barometric sensor, secure the new barometric sensor to the wiring harness with a cable tie securely.

![[19300068.png]]
