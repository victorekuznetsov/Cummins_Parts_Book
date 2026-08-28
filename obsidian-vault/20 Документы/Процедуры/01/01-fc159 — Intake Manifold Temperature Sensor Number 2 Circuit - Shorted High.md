---
aliases:
  - "Цепь датчика температуры коллектора 2 — замыкание на плюс"
type: "Процедура"
doc: "01-fc159"
title_en: "Intake Manifold Temperature Sensor Number 2 Circuit - Shorted High"
title_ru: "Цепь датчика температуры коллектора 2 — замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc159.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc159.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Intake Manifold Temperature Sensor Number 2 Circuit - Shorted High
**Цепь датчика температуры коллектора 2 — замыкание на плюс**

> [!abstract] Процедура · `01-fc159`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc159.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc159.pdf)

### Fault Code: 159

### Intake Manifold Temperature Sensor Number 2 Circuit - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 159 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine intake manifold temperature sensor signal is shorted high. | No engine protection for the intake manifold air temperature. Possible white smoke. |

![[19803595.png]]

Intake Manifold Temperature Sensor Circuit

### Circuit Description

The intake manifold temperature sensor Number 2 is used by the ECM to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor Number 2 is used by the ECM for the timing and fueling control. If the voltage is high, the ECM will log Fault Code 159. Voltage high can be caused by opens in the signal or return wires, voltage shorts to the signal or return wires, or a failed open sensor.

### Component Location

Refer to the Engine Diagrams in Section E of this manual for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-159
