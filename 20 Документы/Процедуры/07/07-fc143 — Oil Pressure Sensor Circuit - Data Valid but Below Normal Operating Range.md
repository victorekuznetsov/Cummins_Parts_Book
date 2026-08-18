---
aliases:
  - "Цепь датчика давления масла — данные достоверны, ниже нормы"
type: "Процедура"
doc: "07-fc143"
title_en: "Oil Pressure Sensor Circuit - Data Valid but Below Normal Operating Range"
title_ru: "Цепь датчика давления масла — данные достоверны, ниже нормы"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Oil Pressure Sensor Circuit - Data Valid but Below Normal Operating Range
**Цепь датчика давления масла — данные достоверны, ниже нормы**

> [!abstract] Процедура · `07-fc143`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc143.pdf)

### Fault Code: 143

### Oil Pressure Sensor Circuit - Data Valid but Below Normal Operating Range

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 143 PID(P): P100 SPN: 100 FMI: 18 Lamp: Amber SRT: | Oil pressure low - data valid but below normal operating range. | Engine protection shutdown enabled, engine will shut down. Engine protection derate enabled, power derate engine protection disabled, no action taken. |

![[19a00194.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this signal voltage to a pressure value. The oil pressure value is used by the ECM for the engine protection system.

### Component Location

Reference Section E for a detailed component location view. The oil pressure sensor is located between the coolant filter and the heater solenoids.

### Shoptalk

Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. Reference Fault Code 141.

Verify with the operator at what engine speed the fault occurs. If the engine is being operated at too low of a speed under load (lugging), the oil pressure can drop below the engine protection limits because of oil temperature.

Oil pressure is a function of engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot, the oil level is low, the regulator has malfunctioned, or a loss is occurring somewhere in the system.

A faulty sensor can also cause Fault Code 143.

The number of fault lamps can be reduced to two for certain OEMs. In this case, the engine protection and stop lamps are wired together as a red lamp. The warning lamp remains an amber lamp.

Refer to Troubleshooting Fault Code t05-143
