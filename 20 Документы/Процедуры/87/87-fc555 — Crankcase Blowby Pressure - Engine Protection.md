---
aliases:
  - "Давление прорыва газов в картер — защита двигателя"
type: "Процедура"
doc: "87-fc555"
title_en: "Crankcase Blowby Pressure - Engine Protection"
title_ru: "Давление прорыва газов в картер — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc555.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc555.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Crankcase Blowby Pressure - Engine Protection
**Давление прорыва газов в картер — защита двигателя**

> [!abstract] Процедура · `87-fc555`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc555.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc555.pdf)

### Fault Code: 555

### Crankcase Blowby Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 555 PID(P): 101 SPN: 101 FMI: 0 Lamp: Engine Protection SRT: | High crankcase blowby pressure has been detected. Voltage signal at blowby pressure signal pin 25 indicates blowby pressure above 368 mm H 2 O \[14.5 in H 2 O\]. | Calibration-dependent progressive power, speed derate, and engine shutdown as pressure increases over thresholds. |

![[19a00237.png]]

Crankcase Blowby Pressure Sensor Circuit

### Circuit Description

The blowby pressure sensor is used by the electronic control module (ECM) to monitor the engine crankcase pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The blowby pressure value is used by the ECM for the engine protection system.

### Component Location

The blowby pressure sensor is located in the gear case on the left side of the engine.

### Shoptalk

- Confirm that the crankcase breathers and breather tubes are **not** obstructed.

- The crankcase blowby pressure sensor is used in conjunction with the CENSE™ engine monitoring system.

Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

Refer to Troubleshooting Fault Code t05-555
