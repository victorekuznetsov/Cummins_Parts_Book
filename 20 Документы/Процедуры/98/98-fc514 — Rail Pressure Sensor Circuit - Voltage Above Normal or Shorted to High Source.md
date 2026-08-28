---
type: "Процедура"
doc: "98-fc514"
title_en: "Rail Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc514.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc514.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Rail Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `98-fc514`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc514.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc514.pdf)

### Fault Code: 514

### Rail Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 514 PID(P): S18 SPN: FMI: 7 Lamp: Flashing SRT: 00-644 | High rail pressure detected. | Engine can run at high idle **only.** |

![[19802313.png]]

Rail Pressure Sensor Circuit

### Circuit Description

The rail pressure sensor is a variable resistance sensor used by the ECM to monitor the fuel rail pressure. This sensor has three circuits: 5 volt supply, return and signal circuits. This rail pressure sensor signal voltage changes based on the pressure in the fuel rail.

### Component Location

The rail pressure sensor location may vary and is dependent on the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected high rail pressure.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by the recommended Cummins® electronic service tool or equivalent will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active and inactive faults.

For Power Generation Applications:

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged electronic fuel control solenoid.

- Malfunctioning or damaged electronic fuel control valve.

Refer to Troubleshooting Fault Code t05-514
