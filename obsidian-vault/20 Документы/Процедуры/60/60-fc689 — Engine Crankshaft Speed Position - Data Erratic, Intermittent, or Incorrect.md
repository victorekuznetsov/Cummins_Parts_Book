---
aliases:
  - "Частота/положение коленвала — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc689"
title_en: "Engine Crankshaft Speed/Position - Data Erratic, Intermittent, or Incorrect"
title_ru: "Частота/положение коленвала — данные нестабильны или неверны"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc689.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc689.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Crankshaft Speed/Position - Data Erratic, Intermittent, or Incorrect
**Частота/положение коленвала — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc689`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc689.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc689.pdf)

### Fault Code: 689

### Engine Crankshaft Speed/Position - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 689 PID(P): P190 SPN: 190 FMI: 2/2 Lamp: Amber SRT: | The ECM has detected an error in the engine speed signal. | Possible reduced performance or shutdown. |

![[19a00864.png]]

Engine Crankshaft Speed Sensor Circuit

### Circuit Description

The crankshaft position and camshaft position sensors are Hall effect type sensors. The engine control module (ECM) provides a 5 volt supply to the position sensor and a return circuit. As the teeth on the crankshaft speed ring or the dimples in the back of the camshaft gear move past the position sensor, a signal is generated on the position sensor signal circuit. The ECM interprets this signal and converts it to an engine speed. A missing tooth on the crankshaft gear is used by the ECM to determine the position of the engine.

### Component Location

The engine speed sensor and the engine position sensor are located in the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected a loss of the crankshaft speed/position sensor while the engine was running.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- Engine torque will be reduced if the engine is operated for an extended period of time with this fault active.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Damaged or malfunctioning engine speed sensor

- Damaged tone wheel

Refer to Troubleshooting Fault Code 689.
