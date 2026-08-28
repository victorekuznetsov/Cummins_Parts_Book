---
aliases:
  - "Цепь питания датчиков 2 — напряжение ниже нормы или замыкание на массу"
type: "Процедура"
doc: "60-fc187"
title_en: "Sensor Supply 2 Circuit - Voltage Below Normal or Shorted to Low Source"
title_ru: "Цепь питания датчиков 2 — напряжение ниже нормы или замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc187.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc187.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Sensor Supply 2 Circuit - Voltage Below Normal or Shorted to Low Source
**Цепь питания датчиков 2 — напряжение ниже нормы или замыкание на массу**

> [!abstract] Процедура · `60-fc187`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc187.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc187.pdf)

### Fault Code: 187

### Sensor Supply 2 Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 187 PID(P): S211 SPN: 3510 FMI: 4/4 Lamp: Amber SRT: | Low voltage detected at the sensor supply 2 circuit. | Possible reduced engine performance, shutdown or loss of engine protection. |

![[19a00855.png]]

Sensor Supply 2 Circuit.

### Circuit Description

The sensor supply 2 circuit of the engine control module (ECM) provides a 5 volt supply to various sensors on the engine wiring harness.

### Component Location

The sensor supply 2 circuit is located in the engine wiring harness.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active or when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the sensor supply 2 signal voltage was out of range low.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- A default value is used for all of the sensors on the sensor supply 2 circuit.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Damaged or loose connections.

- Malfunctioning sensor

Refer to Troubleshooting Fault Code 187.
