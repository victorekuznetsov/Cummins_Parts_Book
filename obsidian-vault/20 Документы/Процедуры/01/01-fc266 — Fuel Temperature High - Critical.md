---
aliases:
  - "Высокая температура топлива — критично"
type: "Процедура"
doc: "01-fc266"
title_en: "Fuel Temperature High - Critical"
title_ru: "Высокая температура топлива — критично"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc266.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc266.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Temperature High - Critical
**Высокая температура топлива — критично**

> [!abstract] Процедура · `01-fc266`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc266.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc266.pdf)

### Fault Code: 266

### Fuel Temperature High - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 266 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine fuel temperature has exceeded the shutdown threshold for high fuel temperature. | Engine will shut down. |

![[19803592.png]]

Fuel Temperature Sensor Circuit

### Circuit Description

The fuel temperature sensor is used by the electronic control module (ECM) to monitor the temperature of the fuel. The fuel temperature value is used by the ECM for the engine protection system.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

The resistance of all the temperature sensors varies with the temperature.

Refer to Troubleshooting Fault Code t05-266
