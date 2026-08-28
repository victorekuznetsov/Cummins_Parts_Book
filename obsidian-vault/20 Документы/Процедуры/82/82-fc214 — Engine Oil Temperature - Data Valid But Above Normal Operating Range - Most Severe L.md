---
aliases:
  - "Температура моторного масла выше нормы — наивысший уровень"
type: "Процедура"
doc: "82-fc214"
title_en: "Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура моторного масла выше нормы — наивысший уровень"
modified: "2019-06-21"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc214.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc214.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура моторного масла выше нормы — наивысший уровень**

> [!abstract] Процедура · `82-fc214`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2019-06-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc214.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc214.pdf)

### Fault Code: 214

### Engine Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 214 PID(P): P175 SPN: FMI: 0/0 Lamp: Red SRT: | Engine oil temperature signal indicates engine oil temperature above threshold for high oil temperature. | Engine will shut down. |

![[19a00956.png]]

Engine Oil Temperature Sensor Circuit

### Circuit Description

The engine oil temperature sensor is a variable resistor sensor and is used to measure the temperature of the engine oil. The engine control module (ECM) supplies 5 volts to the engine oil temperature signal circuit. The ECM monitors the change in voltage caused by changes in the resistance of the sensor to determine the engine oil temperature. When the oil temperature is cold, the sensor or thermistor resistance is high. The ECM signal voltage **only** pulls down a small amount through the sensor to a ground. Therefore, the ECM senses a high signal voltage or low temperature. When the oil temperature is warm, the sensor resistance is low. The signal voltage pulls down a large amount. Therefore, the ECM senses a low signal voltage or high temperature.

### Component Location

The combination oil pressure and oil temperature sensor is located on the cylinder block directly above the accessory drive.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The engine control module (ECM) detected the engine oil temperature was greater than the engine protection limit.

### Action Taken When The Fault Code Is Active

The ECM illuminates the red STOP ENGINE lamp immediately after the diagnostic runs and fails.

Engine torque will be reduced if the engine is operated for an extended period of time with this fault active

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine, and let it idle for 1 minute.

- The fault code status displayed by the recommended Cummins electronic service tool, or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool, or equivalent, can be used to clear active and inactive faults.

### Shoptalk

This fault code indicates that the engine oil temperature has exceeded the maximum engine protection limit for oil temperature. Troubleshoot the cause of high engine oil temperature.

Refer to Troubleshooting Fault Code 214
