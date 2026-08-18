---
aliases:
  - "Цепь датчика давления коллектора — напряжение ниже нормы"
type: "Процедура"
doc: "07-fc123"
title_en: "Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь датчика давления коллектора — напряжение ниже нормы"
modified: "2012-12-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc123.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc123.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь датчика давления коллектора — напряжение ниже нормы**

> [!abstract] Процедура · `07-fc123`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc123.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-fc123.pdf)

### Fault Code: 123

### Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 123 PID(P): P102 SPN: 102 FMI: 4 Lamp: Amber SRT: | Intake Manifold Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low signal voltage detected at the intake manifold pressure circuit. | Derate dependant on calibration. |

![[19900354.png]]

Intake Manifold Pressure Sensor Circuit

### Circuit Description

The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM) through the intake manifold pressure signal pin of the engine harness.

### Component Location

Reference Section E for a detailed component location view. There is one intake manifold pressure sensor on the 480C E engine. It is located next to the air intake heater, behind the ECM.

### Shoptalk

- The intake manifold pressure sensor measures gauge pressure. Confirm the sensor is reading properly by comparing the reading seen in the ECM with a reading taken with a mechanical gauge. The sensor should read -38 to 38 mm Hg \[-1.5 to 1.5 in Hg\] using INSITE™, with the keyswitch turned to the ON position, but the engine **not** running.

- Check for high restriction in the intake manifold due to clogged air filters or a shutdown device in the manifold (if the vessel is equipped with one). Do **not** remove this device. If the engine is operated in a flammable atmosphere, the device is an essential safety feature.

- Make sure the turbocharger is working correctly. Check for a positive intake manifold pressure.

Refer to Troubleshooting Fault Code t05-123
