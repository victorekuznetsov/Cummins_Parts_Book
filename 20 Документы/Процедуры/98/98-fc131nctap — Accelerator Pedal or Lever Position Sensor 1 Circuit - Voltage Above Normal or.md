---
type: "Процедура"
doc: "98-fc131nctap"
title_en: "Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc131nctap.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc131nctap.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source

> [!abstract] Процедура · `98-fc131nctap`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc131nctap.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc131nctap.pdf)

### Fault Code: 131-nctap

### Accelerator Pedal or Lever Position Sensor 1 Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 131-nctap PID(P): P91 SPN: FMI: 3 Lamp: Flashing SRT: 00-622 | High voltage detected at throttle position signal circuit. | Possible reduced engine performance. |

![[19802318.png]]

Throttle Position Sensor Circuit - (Non-CELECT™ Type Accelerator Pedal)

### Circuit Description

The throttle position sensor is a variable resistance sensor used by the ECM to monitor the throttle command. This sensor has three circuits: 5 volt supply, return and signal circuits. The signal circuit voltage indicates the position of the throttle position sensor.

### Component Location

Throttle position sensor location may vary and is OEM dependent.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the throttle position signal voltage was out of range high.

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

- Malfunctioning or damaged OEM wiring harness.

- Malfunctioning or damaged throttle position sensor.

- Damaged or loose connectors.

Refer to Troubleshooting Fault Code t05-131
