---
aliases:
  - "Цепь педали акселератора и выключателя подтверждения холостого хода"
type: "Процедура"
doc: "87-fc432"
title_en: "Accelerator Pedal/Idle Validation Switch Circuit"
title_ru: "Цепь педали акселератора и выключателя подтверждения холостого хода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc432.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc432.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Accelerator Pedal/Idle Validation Switch Circuit
**Цепь педали акселератора и выключателя подтверждения холостого хода**

> [!abstract] Процедура · `87-fc432`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc432.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc432.pdf)

### Fault Code: 432

### Accelerator Pedal/Idle Validation Switch Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 432 PID(P): P091 SPN: 091 FMI: 13 Lamp: Red SRT: | Voltage detected at the idle validation on-idle signal pin 26 of the OEM harness when voltage at the accelerator position signal pin 30 of the OEM harness indicates the pedal is **not** at idle, or voltage detected at idle validation off-idle signal pin 25 of the OEM harness when voltage at accelerator position signal pin 30 of the OEM harness indicates pedal is at rest. | Engine will **not** respond to accelerator. Engine will idle **only**. |

![[19a00759.png]]

Accelerator Pedal Circuit

### Circuit Description

The accelerator pedal provides the driver's accelerator command to the electronic control module (ECM) through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the fuel pump.

### Component Location

The accelerator pedal location varies with each OEM. Refer to the OEM manual.

### Shoptalk

This fault code is usually caused by the improper wiring of the accelerator circuit, the idle validation circuit, or the OEM harness.

Note: If the accelerator or accelerator position sensor is changed, or after a calibration download, cycle the accelerator pedal (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator with the ECM.

Refer to Troubleshooting Fault Code t05-432
