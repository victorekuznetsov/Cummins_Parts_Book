---
aliases:
  - "Высокое давление во впускном коллекторе — выше нормы"
type: "Процедура"
doc: "07-fc124"
title_en: "Intake Manifold Pressure High - Data Valid but Above Normal Operating Range"
title_ru: "Высокое давление во впускном коллекторе — выше нормы"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc124.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc124.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Intake Manifold Pressure High - Data Valid but Above Normal Operating Range
**Высокое давление во впускном коллекторе — выше нормы**

> [!abstract] Процедура · `07-fc124`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc124.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc124.pdf)

### Fault Code: 124

### Intake Manifold Pressure High - Data Valid but Above Normal Operating Range

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 124 PID(P): P102 SPN: 102 FMI: 16 Lamp: Amber SRT: | Intake manifold pressure high - data valid but above normal operating range - moderately severe level. | No action taken. |

![[19900354.png]]

Intake Manifold Pressure Sensor Circuit

### Circuit Description

The intake manifold pressure sensor is used by the electronic control module (ECM) to monitor the engine intake manifold pressure. The ECM monitors the voltage on the intake manifold pressure signal pin and converts this to a pressure value. The intake manifold pressure value is used by the ECM for the engine protection system.

### Component Location

Reference Section E for a detailed component location view. The intake manifold pressure sensor is located next to the air intake heater behind the ECM.

### Shoptalk

Possible causes:

- Malfunctioning turbocharger wastegate. [[41-010-050 — Turbocharger Wastegate Actuator|Refer to Procedure 010-050]] in the Troubleshooting and Repair Manual, C Series Engines, Bulletin [[3666003 — C Troubleshooting and Repair Manual\|3666003]].

- A faulty sensor.

Refer to Troubleshooting Fault Code t05-124
