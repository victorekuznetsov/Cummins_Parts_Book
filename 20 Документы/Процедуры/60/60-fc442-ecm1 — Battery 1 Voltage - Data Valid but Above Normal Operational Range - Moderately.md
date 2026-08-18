---
aliases:
  - "Напряжение АКБ 1 выше нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc442-ecm1"
title_en: "Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level"
title_ru: "Напряжение АКБ 1 выше нормы — умеренный уровень"
modified: "2012-12-20"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc442-ecm1.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc442-ecm1.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level
**Напряжение АКБ 1 выше нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc442-ecm1`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc442-ecm1.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc442-ecm1.pdf)

### Fault Code: 442-ECM1

### Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 442 PID(P): SPN: 168 FMI: 0/16 Lamp: Amber SRT: | Battery 1 Voltage - Data Valid but Above Normal Operational Range - Moderately Severe Level. ECM supply voltage is above the maximum system voltage level. | Possible electrical damage to all electrical components. |

![[19a00872.png]]

Battery 1 Voltage Circuit - QST30 Power Generation Interface Engine

### Circuit Description

The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There is one 10-ampere fuse in the unswitched battery wire to protect the OEM harness. The ECM receives switched battery input through the vehicle keyswitch wire when the vehicle keyswitch is turned on. The battery 1 RETURN wires are connected directly to the negative (-) battery post.

### Component Location

The engine has 3 ECMs. ECMs are located on a support bracket above the flywheel housing at the rear of the engine. ECM1 is the left most mounted ECM. ECM2 is in the middle and ECM3 is the right most mounted ECM. The ECMs are connected to the battery by the engine and OEM harnesses. This direct link provides a constant power supply for the ECM. The location of the battery will vary with the OEM. Reference the OEM troubleshooting and repair manual for battery location.

### Shoptalk

There are multiple ECMs. Each ECM has an individual source address that displays when the INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

This fault code is logged when the ECM battery 1 voltage exceeds +36-VDC. Causes of this fault code include:

- Faulty alternator or regulator that is overcharging the system

- Batteries connected in series instead of parallel

- Incorrect jump-starting procedure.

Refer to Troubleshooting Fault Code t05-442
