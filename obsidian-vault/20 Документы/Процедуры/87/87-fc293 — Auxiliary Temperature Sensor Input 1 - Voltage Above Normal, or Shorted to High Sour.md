---
aliases:
  - "Вспомогательный вход датчика температуры 1 — напряжение выше нормы"
type: "Процедура"
doc: "87-fc293"
title_en: "Auxiliary Temperature Sensor Input 1 - Voltage Above Normal, or Shorted to High Source"
title_ru: "Вспомогательный вход датчика температуры 1 — напряжение выше нормы"
modified: "2020-01-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc293.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc293.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Auxiliary Temperature Sensor Input 1 - Voltage Above Normal, or Shorted to High Source
**Вспомогательный вход датчика температуры 1 — напряжение выше нормы**

> [!abstract] Процедура · `87-fc293`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2020-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc293.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc293.pdf)

### Fault Code: 293

### Auxiliary Temperature Sensor Input 1 - Voltage Above Normal, or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 293 PID(P): P441 SPN: 441 FMI: 3/3 Lamp: Amber SRT: | Voltage detected at the original equipment manufacturer (OEM) auxiliary temperature sensor supply pin of the left bank OEM interface wiring harness indicates the sensor has failed high. | None on performance. |

![[19n00476.png]]

Auxiliary Temperature Sensor Input 1 Circuit

### Circuit Description

The OEM auxiliary temperature sensor supply is used by the engine control module (ECM) to monitor OEM auxiliary temperature. An OEM auxiliary temperature sensor that has failed low can be caused by shorts to ground or opens in the supply and return wires, or an internally grounded sensor.

### Component Location

The component location will vary depending on the OEM. See equipment manufacturer service information.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position and the engine is running.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the OEM temperature signal circuit is out of range high.

### Action Taken When The Fault Code Is Active

The ECM illuminates the amber CHECK ENGINE lamp and/or the malfunction indicator lamp (MIL) immediately when the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by the recommended Cummins electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.

- It is necessary to use the "Reset All Faults" command in the recommended Cummins electronic service tool or equivalent to clear this fault.

### Shoptalk

Possible causes of this fault code include:

- Open return circuit in the harness, connectors, or sensor

- Open signal circuit or shorted to a voltage source.

Refer to Troubleshooting Fault Code t05-293
