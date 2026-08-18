---
aliases:
  - "Диагностика драйвера реле «готов к приёму нагрузки»"
type: "Процедура"
doc: "01-fc1491"
title_en: "Ready to Load Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле «готов к приёму нагрузки»"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1491.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1491.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Ready to Load Output Relay Driver Diagnostic
**Диагностика драйвера реле «готов к приёму нагрузки»**

> [!abstract] Процедура · `01-fc1491`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1491.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1491.pdf)

### Fault Code: 1491

### Ready to Load Output Relay Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1491 PID(P): SPN: FMI: Lamp: Warning SRT: | The Ready to Load output relay driver diagnostic has detected an error. | Any customer systems/features dependent on the Ready to Load output will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802916.png]]

The Ready to Load Output Relay Driver Circuit

### Circuit Description

The ECM checks the Ready to Load output relay driver to ensure correct operation. The ECM uses the Ready to Load output to inform any customer systems/features dependent on the ECM for knowledge of when the generator set is ready to pick up load.

### Component Location

Refer to section E for location of the output for the Ready to Load.

### Shoptalk

The possible failure modes are open circuit, short circuit, short to ground, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1491
