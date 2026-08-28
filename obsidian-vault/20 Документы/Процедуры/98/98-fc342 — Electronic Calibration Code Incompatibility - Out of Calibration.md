---
aliases:
  - "Несовместимость калибровочного кода — вне калибровки"
type: "Процедура"
doc: "98-fc342"
title_en: "Electronic Calibration Code Incompatibility - Out of Calibration"
title_ru: "Несовместимость калибровочного кода — вне калибровки"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc342.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc342.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Electronic Calibration Code Incompatibility - Out of Calibration
**Несовместимость калибровочного кода — вне калибровки**

> [!abstract] Процедура · `98-fc342`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc342.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc342.pdf)

### Fault Code: 342

### Electronic Calibration Code Incompatibility - Out of Calibration

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 342 PID(P): S253 SPN: FMI: 12 Lamp: On SRT: 00-631 | Erasable programmable read-only memory memory checksum error. | Engine may **not** start. Engine may shut down. Possible reduced engine performance. |

![[19802469.png]]

Engine Control Module (ECM)

### Circuit Description

The ECM has internal diagnostics that continuously run and check the internal memory.

### Component Location

The ECM is bolted to the fuel pump on the left side of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected a read or write error internal to the ECM.

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

- Internal ECM failure.

Refer to Troubleshooting Fault Code t05-342
