---
aliases:
  - "Диагностика драйвера реле сброса нагрузки"
type: "Процедура"
doc: "01-fc1492"
title_en: "Load Dump Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле сброса нагрузки"
modified: "2011-11-03"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1492.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1492.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Load Dump Output Relay Driver Diagnostic
**Диагностика драйвера реле сброса нагрузки**

> [!abstract] Процедура · `01-fc1492`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-11-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1492.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1492.pdf)

### Fault Code: 1492

### Load Dump Output Relay Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1492 PID(P): SPN: FMI: Lamp: Warning SRT: | The Load Dump output relay driver diagnostic has detected an error. | Any customer system/features dependent on the Load Dump output will **not** function correctly. No action taken by ECM. No loss of performance. |

![[19802917.png]]

The Load Dump Output Relay Driver Circuit

### Circuit Description

The ECM checks the Load Dump output relay driver to ensure correct operation. The ECM uses the Load Dump output to inform any customers/feature dependent on the ECM for knowledge of when the generator set has to dump a load. The ECM monitors the voltage (no voltage increase will trip Fault Code 1492) caused by short circuits, open circuits, or failed Load Dump output relay driver in the ECM.

### Component Location

Refer to Section E for location of the output for the Load Dump.

### Shoptalk

Possible failure modes are open circuits, short circuits, short to ground, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1492
