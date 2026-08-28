---
aliases:
  - "Высокая температура впускного коллектора 1 — предупреждение"
type: "Процедура"
doc: "01-fc488"
title_en: "Intake Manifold Temperature Number 1 High - Warning"
title_ru: "Высокая температура впускного коллектора 1 — предупреждение"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc488.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc488.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Intake Manifold Temperature Number 1 High - Warning
**Высокая температура впускного коллектора 1 — предупреждение**

> [!abstract] Процедура · `01-fc488`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc488.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc488.pdf)

### Fault Code: 488

### Intake Manifold Temperature Number 1 High - Warning

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 488 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine intake manifold air temperature has exceeded the warning threshold for high intake manifold temperature. | Calibration-dependent. No action is taken by the engine control module, or engine shutdown as temperature increases over thresholds. Pre-HET relay driver is energized. |

![[19803595.png]]

Intake Manifold Temperature Sensor Circuit

### Circuit Description

The intake manifold temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature is used by the ECM for the engine protection system, timing, and fueling control.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-488
