---
aliases:
  - "Цепь драйвера привода опережения впрыска — напряжение выше нормы"
type: "Процедура"
doc: "60-fc113"
title_en: "Engine Timing Actuator Driver Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь драйвера привода опережения впрыска — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Timing Actuator Driver Circuit - Voltage Above Normal or Shorted to High Source
**Цепь драйвера привода опережения впрыска — напряжение выше нормы**

> [!abstract] Процедура · `60-fc113`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc113.pdf)

### Fault Code: 113

### Engine Timing Actuator Driver Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 113 PID(P): S20 SPN: 635 FMI: 3/3 Lamp: Amber SRT: | Open circuit or high voltage detected at the timing actuator driver circuit. | Possible reduced engine performance. |

![[19a00845.png]]

Engine Timing Actuator Driver Circuit

### Circuit Description

The timing actuator circuit supplies current to the timing actuator. The ECM commands a varying amount of current to the timing actuator to control the amount of timing pressure to the injectors.

### Component Location

The timing actuator is located on the electronic control valve assembly.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the timing actuator circuit voltage is out of range high.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Damaged or malfunctioning timing actuator.

- Damaged or loose connections.

- Malfunctioning or damaged engine wiring harness.

Refer to Troubleshooting Fault Code 113.
