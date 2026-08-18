---
aliases:
  - "Диагностика драйвера реле приближения к перегреву"
type: "Процедура"
doc: "01-fc1432"
title_en: "Pre-High Engine Temperature Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле приближения к перегреву"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1432.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1432.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Pre-High Engine Temperature Relay Driver Diagnostic
**Диагностика драйвера реле приближения к перегреву**

> [!abstract] Процедура · `01-fc1432`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1432.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1432.pdf)

### Fault Code: 1432

### Pre-High Engine Temperature Relay Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1432 PID(P): SPN: FMI: Lamp: Warning SRT: | Pre-high engine temperature relay driver diagnostic has detected an error. | The pre-high engine temperature relay will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802449.png]]

Pre-High Engine Temperature Relay Driver Circuit

### Circuit Description

The ECM checks the pre-high engine temperature relay driver to sustain correct operation. The ECM uses the pre-high engine temperature relay to inform the operator of a non-critical fault. The ECM monitors the voltage, no voltage drop will trip Fault Code 1432, and can be caused by shorts, opens, bad relays, or a failed pre-high engine temperature relay driver in the ECM.

### Component Location

Refer to the OEM manual for location of the ECM. Refer to the OEM manual for location of the user interface panel and the Pre-High engine temperature relay.

### Shoptalk

The possible failure modes are open circuit, short to ground, burned-out relay, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1432
