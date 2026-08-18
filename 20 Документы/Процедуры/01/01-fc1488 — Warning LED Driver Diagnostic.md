---
aliases:
  - "Диагностика драйвера предупреждающего светодиода"
type: "Процедура"
doc: "01-fc1488"
title_en: "Warning LED Driver Diagnostic"
title_ru: "Диагностика драйвера предупреждающего светодиода"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1488.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1488.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Warning LED Driver Diagnostic
**Диагностика драйвера предупреждающего светодиода**

> [!abstract] Процедура · `01-fc1488`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1488.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1488.pdf)

### Fault Code: 1488

### Warning LED Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1488 PID(P): SPN: FMI: Lamp: Warning SRT: | Switch panel warning LED driver diagnostic has detected an error. | The warning LED will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802914.png]]

Warning LED Driver Circuit

### Circuit Description

The ECM checks the warning LED driver to make certain it is operating correctly. The ECM uses the warning lamp to inform the operator that a noncritical fault has occurred with the generator set.

The ECM monitors the voltage, (no voltage drop will trip Fault Code 1488) and can be caused by shorts, opens, bad bulbs, or a failed warning LED driver in the ECM.

### Component Location

Refer to Section E for location of the switch panel and the warning lamp.

### Shoptalk

The possible failure modes are open circuit, short to ground, burned out bulb, and loss of supply voltage inside the ECM.

Proper diagnostic lamp operation can be verified by checking to see that the lamps briefly light when the ECM is powered up.

Refer to Troubleshooting Fault Code t05-1488
