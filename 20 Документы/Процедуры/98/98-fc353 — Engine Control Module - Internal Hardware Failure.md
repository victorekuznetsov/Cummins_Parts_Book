---
type: "Процедура"
doc: "98-fc353"
title_en: "Engine Control Module - Internal Hardware Failure"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc353.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc353.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Control Module - Internal Hardware Failure

> [!abstract] Процедура · `98-fc353`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2021-09-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-fc353.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-fc353.pdf)

### Fault Code: 353

### Engine Control Module - Internal Hardware Failure

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 353 PID(P): S251 SPN: FMI: 12 Lamp: On SRT: 00-631 | Erasable programmable read-only memory memory read/write error. | None on performance. |

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

- The ECM logs the amber CHECK fault code immediately when the diagnostic runs and fails.

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

- Internal ECM failure.

Refer to Troubleshooting Fault Code t05-353
