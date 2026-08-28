---
aliases:
  - "Высокая температура охлаждающей жидкости — критично"
type: "Процедура"
doc: "01-fc151"
title_en: "Engine Coolant Temperature High - Critical"
title_ru: "Высокая температура охлаждающей жидкости — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc151.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc151.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Coolant Temperature High - Critical
**Высокая температура охлаждающей жидкости — критично**

> [!abstract] Процедура · `01-fc151`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc151.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc151.pdf)

### Fault Code: 151

### Engine Coolant Temperature High - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 151 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine coolant temperature has exceeded the alarm (shutdown) threshold for high coolant temperature. | Engine will shut down. High engine temperature (HET) relay driver is energized. |

![[19803592.png]]

Coolant Temperature Sensor Circuit

### Circuit Description

The coolant temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the engine coolant. The coolant temperature is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is low for more than 2 seconds, the ECM will log Fault Code 151.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Make sure the airflow through the radiator is **not** obstructed. The resistance of all the temperature sensors varies with the temperature.

Refer to Troubleshooting Fault Code t05-151
