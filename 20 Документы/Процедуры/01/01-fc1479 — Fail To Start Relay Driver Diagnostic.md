---
aliases:
  - "Диагностика драйвера реле «отказ пуска»"
type: "Процедура"
doc: "01-fc1479"
title_en: "Fail To Start Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле «отказ пуска»"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1479.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1479.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fail To Start Relay Driver Diagnostic
**Диагностика драйвера реле «отказ пуска»**

> [!abstract] Процедура · `01-fc1479`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1479.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1479.pdf)

### Fault Code: 1479

### Fail To Start Relay Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1479 PID(P): SPN: FMI: Lamp: Warning SRT: | Fail to start relay driver diagnostic has detected an error. | The fail to start relay will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802449.png]]

Fail To Start Relay Driver Circuit

### Circuit Description

The engione control module (ECM) checks the fail-to-start relay driver to sustain correct operation. The ECM uses the fail-to-start relay to inform the operator of a noncritical fault. The ECM monitors the voltage, no voltage drop will trip Fault Code 1479, and can be caused by shorts, opens, bad relays, or a failed fail to start relay driver in the ECM.

### Component Location

Reference the OEM service manual for location of the ECM. Reference the OEM service manual for location of the user interface panel and the fail to start relay.

### Shoptalk

The possible failure modes are open circuit, short to ground, burned-out relay, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1479.
