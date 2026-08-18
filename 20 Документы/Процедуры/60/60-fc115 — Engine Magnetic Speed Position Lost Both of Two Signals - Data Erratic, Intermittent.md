---
aliases:
  - "Потеряны оба сигнала частоты/положения — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc115"
title_en: "Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect"
title_ru: "Потеряны оба сигнала частоты/положения — данные нестабильны или неверны"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect
**Потеряны оба сигнала частоты/положения — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc115`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc115.pdf)

### Fault Code: 115

### Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 115 PID(P): P190 SPN: 612 FMI: 2/2 Lamp: Red SRT: | Both signals failed to be detected at the engine position sensor circuit. | The engine will shut down or will **not** start. |

![[19a00846.png]]

Engine Crankshaft Speed Sensor Circuit

### Circuit Description

The crankshaft position and camshaft position sensors are Hall effect type sensors. The engine control module (ECM) provides a 5 volt supply to the position sensor and a return circuit. As the teeth on the crankshaft speed ring or the dimples in the back of the camshaft gear move past the position sensor, a signal is generated on the position sensor signal circuit. The ECM interprets this signal and converts it to an engine speed. A missing tooth on the crankshaft gear is used by the ECM to determine the position of the engine.

### Component Location

The engine speed sensor and the engine position sensor are located in the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the crankshaft position and camshaft position signal inputs to the ECM are missing or reversed.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- Engine torque will be reduced if the engine is operated for an extended period of time with this fault active.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the shutdown indicator immediately after the user presses the reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Crankshaft position sensor and the camshaft position sensor wiring harness connectors are reversed.

- Damaged or loose connectors.

- Malfunctioning or damaged engine wiring harness.

Refer to Troubleshooting Fault Code 115.
