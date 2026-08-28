---
type: "Процедура"
doc: "98-fc431"
title_en: "Accelerator Pedal or Lever Idle Validation Switch - Data Erratic, Intermittent, or Incorrect"
modified: "2021-09-10"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Accelerator Pedal or Lever Idle Validation Switch - Data Erratic, Intermittent, or Incorrect

> [!abstract] Процедура · `98-fc431`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc431.pdf)

### Fault Code: 431

### Accelerator Pedal or Lever Idle Validation Switch - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 431 PID(P): P91 SPN: FMI: 2 Lamp: On SRT: 00-633 | Voltage detected simultaneously on both idle validation and off-idle validation switches. | Possible reduced engine performance. |

![[19802311.png]]

Idle Validation Circuit

### Circuit Description

The idle validation signal is a safety feature that disables throttle control while an improper validation signal is detected by the ECM. The idle validation switch provides an on-idle and off-idle validation signal to the ECM through the OEM wiring harness and engine wiring harness.

### Component Location

The idle validation switch is mounted on the throttle pedal. The throttle pedal location varies with each OEM.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected on-idle signal and off-idle signal were both on or both off at the same time.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.

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

- Malfunctioning or damaged OEM wiring harness.

- Malfunctioning or damaged throttle position sensor.

- Damaged or loose connectors.

Refer to Troubleshooting Fault Code t05-431
