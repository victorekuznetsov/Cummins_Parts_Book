---
aliases:
  - "Датчик температуры впускного коллектора — защита двигателя"
type: "Процедура"
doc: "87-fc155"
title_en: "Intake Manifold Temperature Sensor - Engine Protection"
title_ru: "Датчик температуры впускного коллектора — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc155.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc155.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Intake Manifold Temperature Sensor - Engine Protection
**Датчик температуры впускного коллектора — защита двигателя**

> [!abstract] Процедура · `87-fc155`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc155.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc155.pdf)

### Fault Code: 155

### Intake Manifold Temperature Sensor - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 155 PID(P): P105 SPN: 105 FMI: 0 Lamp: Engine Protection SRT: | High intake air manifold temperature has been detected. Voltage signal at intake manifold air temperature sensor signal pin 34 indicates intake manifold air temperature above the calibrated value 104°C \[219°F\]. | Depending on the calibration, a progressive power and speed derate and engine shutdown as the temperature increases over thresholds. |

![[19900359.png]]

Intake Manifold Temperature Sensor Circuit

### Circuit Description

The intake manifold temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on pin 34. The ECM expects to see the voltage vary between 0.5 and 4.5 VDC.

### Component Location

Two intake manifold temperature sensors are used on the QST30 industrial engine, one on each side. The sensors are located in the intake manifold at the rear of the engine.

### Shoptalk

The signal voltage varies between 0.5 and 4.5 VDC as the internal resistance of the sensor changes due to changing coolant temperature. When the sensor signal voltage indicates a temperature exceeding a set limit, Fault Code 155 is logged.

The following chart shows resistance of the intake manifold temperature sensor at various temperature readings.

| Temperature (°C) | Temperature \[°F\] | Resistance (ohms) |
|---|---|---|
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

Refer to Troubleshooting Fault Code t05-155
