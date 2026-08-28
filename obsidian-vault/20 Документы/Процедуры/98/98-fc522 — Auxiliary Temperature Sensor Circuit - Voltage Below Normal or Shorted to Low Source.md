---
type: "Процедура"
doc: "98-fc522"
title_en: "Auxiliary Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc522.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc522.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Auxiliary Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc522`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc522.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc522.pdf)

### Fault Code: 522

### Auxiliary Temperature Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 522 PID(P): P177 SPN: FMI: 4 Lamp: On SRT: 00-646 | Low signal voltage detected at the auxiliary temperature sensor circuit. | None on performance. |

![[19802303.png]]

Auxiliary Temperature Sensor Circuit

### Circuit Description

The auxiliary temperature sensor is a variable resistor sensor used by the ECM to monitor the auxiliary temperature. The auxiliary temperature sensor has two circuits: signal, and return circuits. The signal voltage indicates the auxiliary temperature.

### Component Location

The location of the auxiliary temperature sensor may vary and is OEM dependent.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected that the auxiliary temperature sensor signal voltage was out of range low.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE light when the diagnostic runs and fails.

- There is no engine protection system for auxiliary temperature on CENTRY™.

For Power Generation Applications:

- The generator set controller displays the fault immediately when the diagnostics runs and fails.

- There is no engine protection system for auxiliary temperature on CENTRY™.

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

- Damaged OEM wiring harness.

- Damaged or loose connectors.

- Malfunctioning auxiliary temperature sensor.

Refer to Troubleshooting Fault Code t05-522
