---
aliases:
  - "Диагностика драйвера общего выходного реле предупреждения"
type: "Процедура"
doc: "01-fc1321"
title_en: "Common Warning Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера общего выходного реле предупреждения"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1321.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1321.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Common Warning Output Relay Driver Diagnostic
**Диагностика драйвера общего выходного реле предупреждения**

> [!abstract] Процедура · `01-fc1321`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1321.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1321.pdf)

### Fault Code: 1321

### Common Warning Output Relay Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1321 PID(P): SPN: FMI: Lamp: Warning SRT: | Common warning output relay driver diagnostic has detected an error. | Any customer systems/features dependent on the common warning output will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802776.png]]

Common Warning Output Relay Driver Circuit

### Circuit Description

The engine control module (ECM) checks the common warning output relay driver to make certain it is operating correctly. The ECM uses the common warning output to inform if any customer systems/features are dependent on the ECM for knowledge for noncritical fault with the generator set.

The ECM monitors the voltage (no voltage increase will trip Fault Code 1321) and can be caused by shorts, opens, or a failed common warning output relay driver in the ECM.

### Component Location

Refer to the customer/facility/installation/documentation for the location of the common relay warning output.

### Shoptalk

The possible failure modes are open circuit, short to ground, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1321.
