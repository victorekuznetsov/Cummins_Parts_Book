---
aliases:
  - "Температура во впускном коллекторе 1 выше нормы — наивысший уровень"
type: "Процедура"
doc: "82-fc155"
title_en: "Intake Manifold 1 Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура во впускном коллекторе 1 выше нормы — наивысший уровень"
modified: "2018-10-16"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc155.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc155.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Intake Manifold 1 Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура во впускном коллекторе 1 выше нормы — наивысший уровень**

> [!abstract] Процедура · `82-fc155`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2018-10-16
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc155.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc155.pdf)

### Fault Code: 155

### Intake Manifold 1 Temperature - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 155 PID(P): P105 SPN: 105 FMI: 0/0 Lamp: Red SRT: | Intake Manifold 1 Temperature - Data Valid But Above Normal Operating Range - Most Severe Level. Intake manifold air temperature signal indicates intake manifold air temperature above engine protection critical limit. | Engine power derate. |

![[19a00954.png]]

Intake Manifold Temperature Sensor Circuit

### Circuit Description

The engine control module (ECM) provides 5 volts to the intake manifold temperature signal circuit, and monitors the change in voltage caused by changes in the resistance of the sensor to determine the intake manifold temperature. When the intake air is cold, the sensor (or thermistor) resistance is high. The ECM signal voltage **only** pulls down a small amount through the sensor to a ground. Therefore, the ECM senses a high signal voltage or low temperature. When the intake air is warm, the sensor resistance is low. The signal voltage pulls down a large amount. Therefore, the ECM senses a low signal voltage, or a high temperature.

### Component Location

The intake manifold 1 temperature sensor is located in the air intake horn.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The engine control module (ECM) detected the intake manifold temperature was greater than 105°C \[221°F\] for 5 seconds.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the red STOP ENGINE light immediately after the diagnostic runs and fails.

- The torque output of the engine will be reduced.

- Maximum engine operating speed will be decreased.

- The engine will be shut down if the Engine Protection Shutdown feature is enabled.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine, and let it idle for 1 minute.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

Possible causes of this fault code include:

- High turbocharger compressor outlet temperature.

Refer to Troubleshooting Fault Code 155.
