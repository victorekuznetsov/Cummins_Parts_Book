---
aliases:
  - "Цепь датчика давления во впускном коллекторе"
type: "Процедура"
doc: "87-fc123"
title_en: "Intake Manifold Pressure Sensor Circuit"
title_ru: "Цепь датчика давления во впускном коллекторе"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Intake Manifold Pressure Sensor Circuit
**Цепь датчика давления во впускном коллекторе**

> [!abstract] Процедура · `87-fc123`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc123.pdf)

### Fault Code: 123

### Intake Manifold Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 123 PID(P): P102 SPN: 102 FMI: 4 Lamp: Yellow SRT: | Less than 0.33 VDC detected at the intake manifold air pressure sensor signal pin 45 of the engine harness. | Engine power derate to no-air setting. |

![[19900354.png]]

Intake Manifold Pressure Sensor Circuit

### Circuit Description

The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM) through pin 45 of the engine harness.

The ECM monitors the voltage on pin 45 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation.

Voltage below 0.33 VDC on pin 45 will result in Fault Code 123.

### Component Location

Two intake manifold pressure sensors are found on the QST30 industrial engine, one on each side. They are located either in the intake manifold or in front of each ECM.

### Shoptalk

- The intake manifold pressure sensor measures gauge pressure. Confirm that the sensor is reading properly by comparing the reading seen in the ECM with a reading taken with a mechanical gauge. The sensor should read -1.5 to +1.5 in Hg using INSITE™, with the keyswitch turned to the ON position, but the engine **not** running.

- Check for high restriction in the intake air manifold due to clogged air filters or a shutdown device in the manifold (if the vehicle is equipped with one). Do **not** remove this device. If the engine is operated in a flammable atmosphere, the device is an essential safety feature.

- Make sure the turbocharger is working correctly. Check for a positive intake manifold pressure.

Refer to Troubleshooting Fault Code t05-123
