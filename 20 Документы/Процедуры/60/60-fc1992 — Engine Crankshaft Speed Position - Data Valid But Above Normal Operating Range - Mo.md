---
aliases:
  - "Частота/положение коленвала выше нормы — умеренный уровень"
type: "Процедура"
doc: "60-fc1992"
title_en: "Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Moderately Severe Level"
title_ru: "Частота/положение коленвала выше нормы — умеренный уровень"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1992.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1992.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Moderately Severe Level
**Частота/положение коленвала выше нормы — умеренный уровень**

> [!abstract] Процедура · `60-fc1992`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1992.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc1992.pdf)

### Fault Code: 1992

### Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1992 PID(P): P190 SPN: 190 FMI: 0/16 Lamp: Red SRT: | Engine crankshaft speed signal indicates engine speed above engine protection limit. | Engine will shut down. |

![[19a00864.png]]

Engine Crankshaft Speed Sensor Circuit

### Circuit Description

The crankshaft position and camshaft position sensors are Hall effect type sensors. The engine control module (ECM) provides a 5 volt supply to the position sensor and a return circuit. As the teeth on the crankshaft speed ring or the dimples in the back of the camshaft gear move past the position sensor, a signal is generated on the position sensor signal circuit. The ECM interprets this signal and converts it to an engine speed. A missing tooth on the crankshaft gear is used by the ECM to determine the position of the engine.

### Component Location

The engine crankshaft speed/position sensor is located on the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the engine crankshaft speed sensor is higher than the engine protection limits.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- The engine will be shut down.

- Fueling to the engine is stopped until the engine speed drops to normal operating speeds.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- External fuel sources drawn into the intake air passage

- Reverse powering (motoring) of the engine

- Tampering of the engine speed/position sensors.

Refer to Troubleshooting Fault Code 1992.
