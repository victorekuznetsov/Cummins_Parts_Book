---
aliases:
  - "Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс"
type: "Процедура"
doc: "60-fc2265"
title_en: "Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc2265.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc2265.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source
**Цепь электроподкачивающего насоса — напряжение выше нормы или замыкание на плюс**

> [!abstract] Процедура · `60-fc2265`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc2265.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc2265.pdf)

### Fault Code: 2265

### Electric Lift Pump for Engine Fuel Supply Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2265 PID(P): S126 SPN: 1075 FMI: 3/3 Lamp: Amber SRT: | High voltage detected at the fuel lift pump relay signal circuit. | Engine may **not** start or may be difficult to start. |

![[19900397.png]]

Electronic Control Module (ECM)

### Circuit Description

The fuel pump relay is controlled by the engine control module (ECM), and provides power to the lift pump 1 and lift pump 2. The fuel pump relay has 4 circuits: battery 1 voltage supply, lift pump 1 supply, lift pump relay signal, and battery 1 voltage return. The ECM monitors the lift pump relay signal circuit.

### Component Location

The electric lift pump is located on the right bank rear high position or on the left bank front high position.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the lift pump relay signal circuit is out of range high.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

### Shoptalk

Possible causes of this fault code include:

A malfunctioning fuel lift pump relay.

- Malfunctioning or damaged engine wiring harness.

Refer to Troubleshooting Fault Code 2265.
