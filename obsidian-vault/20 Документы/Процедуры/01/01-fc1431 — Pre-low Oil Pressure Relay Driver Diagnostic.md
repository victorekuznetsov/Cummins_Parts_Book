---
aliases:
  - "Диагностика драйвера реле предварительно низкого давления масла"
type: "Процедура"
doc: "01-fc1431"
title_en: "Pre-low Oil Pressure Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле предварительно низкого давления масла"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1431.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1431.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Pre-low Oil Pressure Relay Driver Diagnostic
**Диагностика драйвера реле предварительно низкого давления масла**

> [!abstract] Процедура · `01-fc1431`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1431.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1431.pdf)

### Fault Code: 1431

### Pre-low Oil Pressure Relay Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1431 PID(P): SPN: FMI: Lamp: Warning SRT: | Pre-low oil pressure relay driver diagnostic has detected an error. | The pre-low oil pressure relay will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802449.png]]

Pre-Low Oil Pressure Relay Driver Circuit

### Circuit Description

The ECM checks the pre-low oil pressure relay driver to sustain correct operation. The ECM uses the pre-low oil pressure relay to inform the operator of a noncritical fault. The ECM monitors the voltage, no voltage drop will trip Fault Code 1431, and can be caused by shorts, opens, bad relays, or a failed pre-low oil pressure relay driver in the ECM.

### Component Location

Refer to the OEM manual for location of the ECM. Refer to the OEM manual for location of the user interface panel and the pre-low oil pressure relay.

### Shoptalk

The possible failure modes are open circuit, short to ground, burned-out relay, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1431
