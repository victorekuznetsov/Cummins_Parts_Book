---
aliases:
  - "Цепь датчика давления во впускном коллекторе"
type: "Процедура"
doc: "87-fc122"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Intake Manifold Pressure Sensor Circuit
**Цепь датчика давления во впускном коллекторе**

> [!abstract] Процедура · `87-fc122`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc122.pdf)

### Fault Code: 122

### Intake Manifold Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 122 PID(P): P102 SPN: 102 FMI: 3 Lamp: Yellow SRT: | More than 4.72 VDC detected at the intake manifold air pressure sensor signal pin 45 of the engine harness. | Engine power derate to no-air setting. |

![[19900354.png]]

Intake Manifold Pressure Sensor Circuit

### Circuit Description

The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM) through pin 45 of the engine harness. The ECM monitors the voltage on pin 45 and expects to see the voltage vary between 0.5 and 4.5 VDC during normal engine operation. Voltage above 4.72 VDC on pin 45 will trip Fault Code 122.

### Component Location

Two intake manifold pressure sensors are found on the QST30 industrial engines, one on each side. They are located in the intake manifold in front of each ECM.

### Shoptalk

- The intake manifold pressure sensor measures gauge pressure. Confirm that the sensor is reading properly by comparing the reading seen in the ECM with a reading taken with a mechanical gauge. The sensor should read -1.5 to +1.5 in Hg using INSITE™, with the keyswitch turned to the ON position, but the engine **not** running.

- Determine if the engine is being overfueled.

- Confirm that the correct intake manifold pressure sensor part number is being used.

- Confirm that the correct turbocharger is being used.

- If it is suspected that cold intake air can be the cause of the high intake manifold pressure, test the engine while feeding it warm intake air.

- Inspect the intake manifold pressure sensor circuit for signs of tampering. Remove any extra wires from the circuit.

Refer to Troubleshooting Fault Code t05-122
