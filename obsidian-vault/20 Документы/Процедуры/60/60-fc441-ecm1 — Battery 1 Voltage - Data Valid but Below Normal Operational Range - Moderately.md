---
aliases:
  - "Напряжение АКБ 1 ниже нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc441-ecm1"
title_en: "Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level"
title_ru: "Напряжение АКБ 1 ниже нормы — умеренный уровень"
modified: "2012-12-20"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc441-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc441-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level
**Напряжение АКБ 1 ниже нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc441-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc441-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc441-ecm1.pdf)

### Fault Code: 441-ECM1

### Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 441 PID(P): SPN: 168 FMI: 1/18 Lamp: Amber SRT: | Battery 1 Voltage - Data Valid but Below Normal Operational Range - Moderately Severe Level. ECM supply voltage is below the minimum system voltage level. | Engine can stop running or be difficult to start. |

![[19a00872.png]]

Unswitched Battery Supply - QST30 Power Generation Interface Engine

### Circuit Description

The ECM receives constant voltage from the batteries through the battery 1 voltage wires that are connected directly to the positive (+) battery post. There is one 10-ampere fuse in the battery 1 voltage wires to protect the harness and ECM. The ECM receives switched battery input through the ignition wire when the ignition is turned on. The battery return wires are connected directly to the negative (-) battery post.

### Component Location

The ECMs are located on a support bracket above the flywheel housing at the rear of the engine. ECM1 is the front most left mounted ECM. ECM2 is in the middle and ECM3 is the right most mounted ECM. The ECMs are connected to the battery by the OEM harness and engine harness. This direct link provides a constant power supply for the ECMs. The location of the battery will vary with the OEM. Reference the OEM troubleshooting and repair manual for battery location.

### Shoptalk

There are multiple ECMs. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

This fault code is logged when the ECM battery supply voltage drops below the minimum system voltage level.

- Verify that the ECM unswitched power is coming from the batteries and **not** the starter or other device. Check for possible weak batteries.

- Low voltage during cranking can cause the ECM power supply to drop below specifications and log Fault Code 441.

Refer to Troubleshooting Fault Code t05-441
