---
aliases:
  - "Давление прорыва газов — критический уровень"
type: "Процедура"
doc: "01-fc556"
title_en: "Blowby Pressure - Critical Level"
title_ru: "Давление прорыва газов — критический уровень"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc556.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc556.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Blowby Pressure - Critical Level
**Давление прорыва газов — критический уровень**

> [!abstract] Процедура · `01-fc556`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc556.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc556.pdf)

### Fault Code: 556

### Blowby Pressure - Critical Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 556 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine blowby - critical level. Voltage signal indicates blowby pressure has exceeded the shutdown threshold for high blowby. | Engine will shut down. |

![[19803587.png]]

Blowby Pressure Sensor Circuit

### Circuit Description

The blowby pressure sensor is used by the electronic control module (ECM) to monitor the engine crankcase pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The blowby pressure value is used by the ECM for the engine protection system.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Confirm that the crankcase breathers and breather tubes are **not** obstructed.

Refer to Troubleshooting Fault Code t05-556
