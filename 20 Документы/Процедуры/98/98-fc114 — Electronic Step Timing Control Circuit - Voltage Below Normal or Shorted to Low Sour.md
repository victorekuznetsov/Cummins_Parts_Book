---
type: "Процедура"
doc: "98-fc114"
title_en: "Electronic Step Timing Control Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2021-09-09"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc114.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc114.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Electronic Step Timing Control Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc114`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc114.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc114.pdf)

### Fault Code: 114

### Electronic Step Timing Control Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 114 PID(P): S20 SPN: FMI: 4 Lamp: On SRT: 00-620 | Low voltage detected at the electronic step timing control circuit. | Possible reduced engine performance. |

![[19802315.png]]

Electronic Step Timing Control (STC) Circuit

### Circuit Description

The electronic step timing control actuator controls the step timing control valve on the fuel pump. The electronic step timing control actuator has a single circuit; step timing control driver/ torque output driver. The Engine Control Module (ECM) adjusts the engine timing from advance to normal with the electronic step timing control actuator.

### Component Location

The electronic step timing control valve is mounted on the left side of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the electronic step timing control voltage was out of range low.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.

- The engine may **not** start.

- The electronic step timing control valve is in normal timing advance.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

- The electronic step timing control valve is in normal timing advance.

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

- Malfunctioning or damaged electronic step timing control actuator.

- Loose or damaged connectors.

Refer to Troubleshooting Fault Code t05-114
