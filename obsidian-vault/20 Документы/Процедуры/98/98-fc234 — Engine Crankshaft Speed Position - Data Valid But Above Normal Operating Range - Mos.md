---
type: "Процедура"
doc: "98-fc234"
title_en: "Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level

> [!abstract] Процедура · `98-fc234`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc234.pdf)

### Fault Code: 234

### Engine Crankshaft Speed/Position - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 234 PID(P): P190 SPN: FMI: 0 Lamp: Flashing SRT: 00-628 | Engine speed signal indicates engine speed above engine protection limit. | Engine will shut down. |

![[19802309.png]]

Engine Speed Sensor Circuit

### Circuit Description

The engine speed sensor is dual channel speed sensor used by the ECM to monitor the engine speed. The speed sensor has four circuits: two signal circuits, and two return circuits. As the teeth on the crankshaft flywheel move past the speed sensor, a signal is generated on the speed sensor signal circuits.

### Component Location

The engine speed sensor is located in the flywheel housing at the rear of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine is running.

### Conditions For Setting The Fault Codes

The ECM detects the engine speed has exceeded the calibration limit for excessive engine speed.

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

- External fuel sources drawn into the intake air pressure.

- Reverse powering (motering) of the engine.

- Tampering of the engine speed sensors.

- Malfunctioning or damaged fuel pump.

- Malfunctioning or damaged turbocharger oil seals.

Refer to Troubleshooting Fault Code t05-234
