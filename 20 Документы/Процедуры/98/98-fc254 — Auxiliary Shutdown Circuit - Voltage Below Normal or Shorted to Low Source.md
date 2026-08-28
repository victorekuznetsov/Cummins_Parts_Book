---
type: "Процедура"
doc: "98-fc254"
title_en: "Auxiliary Shutdown Circuit - Voltage Below Normal or Shorted to Low Source"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc254.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc254.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Auxiliary Shutdown Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `98-fc254`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc254.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc254.pdf)

### Fault Code: 254

### Auxiliary Shutdown Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 254 PID(P): S17 SPN: FMI: 4 Lamp: On SRT: 00-629 | Low voltage on the auxiliary shutdown/torque output driver circuit when the auxiliary shutdown is on. | Engine may **not** start. Engine may shut down. Possible reduced engine performance. |

![[19802304.png]]

Auxiliary Shutdown Circuit

### Circuit Description

The auxiliary shutdown/ torque output driver in the CENTRY™ system can be used to power auxiliary shutdown devices such as air intake flaps. The auxillary shutdown/ torque output driver has a single circuit; auxillary shutdown/ torque output driver. The ECM provides switched battery voltage to the auxiliary shutdown solenoid.

### Component Location

The auxiliary shutdown solenoid location may vary and is OEM dependent.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected the auxiliary shutdown/ torque output driver voltage was out of range low.

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

- Damaged or loose connectors.

- Malfunctioning or damaged auxiliary shutdown solenoid.

Refer to Troubleshooting Fault Code t05-254
