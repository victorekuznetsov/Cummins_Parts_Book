---
aliases:
  - "Потеряны оба сигнала частоты/положения — данные нестабильны или неверны"
type: "Процедура"
doc: "98-fc115fa"
title_en: "Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect"
title_ru: "Потеряны оба сигнала частоты/положения — данные нестабильны или неверны"
modified: "2021-09-15"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc115fa.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc115fa.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect
**Потеряны оба сигнала частоты/положения — данные нестабильны или неверны**

> [!abstract] Процедура · `98-fc115fa`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc115fa.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc115fa.pdf)

### Fault Code: 115-fa

### Engine Magnetic Speed/Position Lost Both of Two Signals - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 115-fa PID(P): 190 SPN: FMI: 2 Lamp: Flashing SRT: 00-621 | Both signals failed to be detected at the engine position sensor circuit. | Derate power and engine can run at high idle **only.** |

![[19802308.png]]

Engine Speed Sensor Circuit

### Circuit Description

The engine speed sensor is dual channel speed sensor used by the ECM to monitor the engine speed. The speed sensor has four circuits: two signal circuits, and two return circuits. As the teeth on the crankshaft flywheel move past the speed sensor, a signal is generated on the speed sensor signal circuits.

### Component Location

The engine speed sensor is mounted in the flywheel housing on the rear of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected a signal failure with engine speed sensor.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the red STOP ENGINE lamp immediately when the diagnostic runs and fails.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- Turn the keyswitch OFF. Allow the ECM to completely power down and turn the keyswitch ON.

- The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.

For Power Generation Applications:

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

- Malfunction or damaged engine speed sensor.

Refer to Troubleshooting Fault Code t05-115
