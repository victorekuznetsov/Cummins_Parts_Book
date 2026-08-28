---
aliases:
  - "Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения"
type: "Процедура"
doc: "98-fc121"
title_en: "Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change"
title_ru: "Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения"
modified: "2021-09-08"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc121.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc121.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change
**Потерян один из двух сигналов частоты/положения коленвала — недопустимая скорость изменения**

> [!abstract] Процедура · `98-fc121`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc121.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc121.pdf)

### Fault Code: 121

### Engine Magnetic Crankshaft Speed/Position Lost One of Two Signals - Abnormal Rate of Change

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 121 PID(P): 190 SPN: FMI: 10 Lamp: Flashing SRT: 00-621 | No engine speed signal detected from either the main or backup speed sensors. | None on performance. |

![[19802309.png]]

Engine Speed Sensor Circuit

### Circuit Description

The engine speed sensor is dual channel speed sensor used by the ECM to monitor the engine speed. The speed sensor has four circuits: two signal circuits, and two return circuits. As the teeth on the crankshaft flywheel move past the speed sensor, a signal is generated on the speed sensor signal circuits.

### Component Location

The engine speed sensor is located on the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected a signal failure with engine speed sensor.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

- Engine will run on backup speed signal provided by the camshaft position sensor.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.

For Power Generation Applications:

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine wiring harness.

• Malfunctioning or damaged engine speed sensor.

Refer to Troubleshooting Fault Code t05-121
