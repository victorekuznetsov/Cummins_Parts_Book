---
aliases:
  - "Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс"
type: "Процедура"
doc: "87-fc2265"
title_en: "Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc2265.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc2265.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source
**Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс**

> [!abstract] Процедура · `87-fc2265`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc2265.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc2265.pdf)

### Fault Code: 2265

### Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2265 PID(P): SPN: 1075 FMI: 3 Lamp: Amber SRT: | Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source. High voltage or open detected at the fuel lift pump signal circuit. | Engine can be difficult to start. |

![[19a00821.png]]

Electric Lift Pump for Engine Fuel Supply Circuit

### Circuit Description

The circuit is a 24 volt high side driver in the ECM that controls the electric lift pump relay for engine fuel supply.

### Component Location

The electric lift pump is located on the right bank rear high position or on the left bank front high position.

### Shoptalk

- This fault becomes active if the ECM detects an open circuit at key-on. The cause of this fault code is an open circuit in the electric lift pump for engine fuel supply circuit between the Engine Fuel Supply Signal relay and the ECM connector.

- If the fault code is intermittent, look for the cause of an intermittent open circuit, such as loose pins or bad connections.

Refer to Troubleshooting Fault Code t05-2265
