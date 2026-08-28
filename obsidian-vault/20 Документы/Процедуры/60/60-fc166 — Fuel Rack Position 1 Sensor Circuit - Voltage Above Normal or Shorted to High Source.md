---
aliases:
  - "Цепь датчика положения рейки 1 — напряжение выше нормы"
type: "Процедура"
doc: "60-fc166"
title_en: "Fuel Rack Position 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика положения рейки 1 — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc166.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Fuel Rack Position 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика положения рейки 1 — напряжение выше нормы**

> [!abstract] Процедура · `60-fc166`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc166.pdf)

### Fault Code: 166

### Fuel Rack Position 1 Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 166 PID(P): S24 SPN: 1210 FMI: 3/3 Lamp: Amber SRT: | High signal voltage detected on the fuel rack position sensor signal circuit. | Possible reduced engine performance. |

![[19a00845.png]]

Fuel Rack Position Sensor Circuit

### Circuit Description

The fuel rack position sensor circuit is supplied with a varying current source from the ECM. The fuel rack position uses this current to change the position of the control rack, which regulates the amount of fuel delivered from the fuel pump. The fuel rack position feedback sensor circuit relays the fuel rack position back to the ECM.

### Component Location

The fuel rack position sensor is internal to the fuel pump.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the fuel rack position sensor circuit voltage is out of range high.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Damaged or malfunctioning fuel rack position sensor

- Damaged or loose connections.

Refer to Troubleshooting Fault Code 166.
