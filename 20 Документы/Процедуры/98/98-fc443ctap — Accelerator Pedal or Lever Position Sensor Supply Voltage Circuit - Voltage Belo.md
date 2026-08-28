---
type: "Процедура"
doc: "98-fc443ctap"
title_en: "Accelerator Pedal or Lever Position Sensor Supply Voltage Circuit - Voltage Below Normal or Shorted to Low Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc443ctap.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc443ctap.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Accelerator Pedal or Lever Position Sensor Supply Voltage Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc443ctap`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc443ctap.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc443ctap.pdf)

### Fault Code: 443-ctap

### Accelerator Pedal or Lever Position Sensor Supply Voltage Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 443-ctap PID(P): S254 SPN: FMI: 4 Lamp: Flashing SRT: 00-637 | Low voltage detected at the sensor supply for the throttle position sensor circuit. | Possible reduced engine performance. |

![[19802316.png]]

Throttle Position Sensor Circuit - (CELECT™ Type Accelerator Pedal)

### Circuit Description

The throttle position sensor is a variable resistance sensor used by the ECM to monitor the throttle command. This sensor has three circuits: 5 volt supply, return and signal circuits. The signal circuit voltage indicates the position of the throttle position sensor.

### Component Location

Throttle position sensor location varies with each OEM.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the sensor supply to the throttle position sensor was out of range low.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

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

- Malfunctioning or damaged throttle position sensor.

- Damaged or loose connectors.

Refer to Troubleshooting Fault Code t05-443
