---
aliases:
  - "Датчик положения акселератора"
type: "Процедура"
doc: "87-fc131"
title_en: "Accelerator Position Sensor"
title_ru: "Датчик положения акселератора"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Accelerator Position Sensor
**Датчик положения акселератора**

> [!abstract] Процедура · `87-fc131`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc131.pdf)

### Fault Code: 131

### Accelerator Position Sensor

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 131 PID(P): P091 SPN: 091 FMI: 3 Lamp: Red SRT: | Excessive voltage detected at the accelerator position signal pin 30 of the OEM interface harness. | Calibration-dependent power and speed derate. |

![[19a00603.png]]

Accelerator Position Sensor

### Circuit Description

The accelerator pedal provides the driver's accelerator command to the electronic control module (ECM) through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the RP39 fuel pump rack.

### Component Location

The accelerator pedal location varies with each OEM. Refer to the OEM troubleshooting and repair manual.

### Shoptalk

The accelerator position sensor is a potentiometer. The resistance specifications of the accelerator position sensor are as follow:

- Between supply and return = 2000 to 3000 ohms

- Between supply and signal: Released = 1500 to 3000 ohms, Depressed = 200 to 1500 ohms.

Note: If the accelerator or accelerator position sensor is changed, or after a calibration download, cycle the accelerator pedal (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator with the ECM.

Refer to Troubleshooting Fault Code t05-131
