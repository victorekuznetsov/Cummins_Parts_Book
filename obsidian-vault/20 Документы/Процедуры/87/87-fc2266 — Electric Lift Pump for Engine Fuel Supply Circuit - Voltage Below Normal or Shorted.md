---
aliases:
  - "Цепь электроподкачивающего насоса — напряжение ниже нормы или замыкание на массу"
type: "Процедура"
doc: "87-fc2266"
title_en: "Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь электроподкачивающего насоса — напряжение ниже нормы или замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc2266.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc2266.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь электроподкачивающего насоса — напряжение ниже нормы или замыкание на массу**

> [!abstract] Процедура · `87-fc2266`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc2266.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc2266.pdf)

### Fault Code: 2266

### Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2266 PID(P): 73 SPN: 1075 FMI: 4 Lamp: Amber SRT: | Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Below Normal or Shorted to Low Source. Low signal voltage or open detected at the fuel lift pump circuit. | Engine can be difficult to start. |

![[19a00821.png]]

Electric Lift Pump for Engine Fuel Supply Circuit

### Circuit Description

The circuit is a 24 volt high side driver in the ECM that controls the electric lift pump relay for engine fuel supply. The lift pump is grounded in the ECM and runs at 100-percent duty cycle for approximately 30 seconds following key-on. The lift pump also runs during start-up and while the engine is running.

### Component Location

The electric lift pump is normally located on the right bank rear high position or on the left bank front high position.

### Shoptalk

This fault code becomes active if the ECM detects a short circuit to ground or high current in the electric lift pump circuit. Causes for this fault code are a short circuit to ground or low resistance (relay partially shorted).

Refer to Troubleshooting Fault Code t05-2266
