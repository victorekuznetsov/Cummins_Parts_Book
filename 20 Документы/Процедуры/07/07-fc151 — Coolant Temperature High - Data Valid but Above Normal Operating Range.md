---
aliases:
  - "Высокая температура ОЖ — данные достоверны, выше нормы"
type: "Процедура"
doc: "07-fc151"
title_en: "Coolant Temperature High - Data Valid but Above Normal Operating Range"
title_ru: "Высокая температура ОЖ — данные достоверны, выше нормы"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc151.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc151.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Coolant Temperature High - Data Valid but Above Normal Operating Range
**Высокая температура ОЖ — данные достоверны, выше нормы**

> [!abstract] Процедура · `07-fc151`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc151.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc151.pdf)

### Fault Code: 151

### Coolant Temperature High - Data Valid but Above Normal Operating Range

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 151 PID(P): P110 SPN: 110 FMI: 0 Lamp: Red SRT: | Coolant temperature high - data valid but above normal operating range (most severe level). | Engine protection shutdown enabled, engine will shut down. Engine protection derate enabled, power derate engine protection disabled, no action taken. |

![[19900358.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature sensor is used by the ECM for the engine protection system, timing, and fueling control. The ECM monitors the voltage on coolant temperature sensor signal pin.

### Component Location

Reference Section E for a detailed component location view. The coolant temperature sensor is located in the thermostat housing.

### Shoptalk

The signal voltage varies between 0.5 and 4.5 VDC as the internal resistance of the sensor changes due to changing coolant temperature. When the sensor signal voltage indicates a temperature exceeding a set limit, Fault Code 151 is logged.

This fault is often associated with a damaged sea water pump, a clogged aftercooler or sea strainer, a fouled heat exchanger or a malfunctioning thermostat.

A faulty sensor can cause Fault Code 151.

The following chart shows resistance of the coolant temperature sensor at various temperature readings.

| Temperature (°F) | Temperature (°C) | Resistance (ohms) |
|---|---|---|
| 32 | 0 | 30k to 36k |
| 77 | 25 | 9k to 11k |
| 122 | 50 | 3k to 4k |
| 167 | 75 | 1350 to 1500 |
| 212 | 100 | 600 to 675 |

The number of fault lamps can be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains an amber lamp.

Refer to Troubleshooting Fault Code t05-151
