---
aliases:
  - "Диагностика драйвера топливоподающего насоса выявила ошибку"
type: "Процедура"
doc: "01-fc2297"
title_en: "Fuel Supply Pump Driver Diagnostic has Detected an Error"
title_ru: "Диагностика драйвера топливоподающего насоса выявила ошибку"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2297.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Supply Pump Driver Diagnostic has Detected an Error
**Диагностика драйвера топливоподающего насоса выявила ошибку**

> [!abstract] Процедура · `01-fc2297`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2297.pdf)

### Fault Code: 2297

### Fuel Supply Pump Driver Diagnostic has Detected an Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2297 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel supply pump driver diagnostic has detected an error. | Priming pump is disabled. Possible loss of performance. |

![[19803605.png]]

Fuel Supply Circuit

### Circuit Description

The priming pumps supply fuel to the left and right bank fuel pumps through the fuel filter. The ECM activates the priming pumps at start up while the engine is cranking to prime the left and right bank fuel pumps for the engine to start.

### Component Location

Refer to Procedure 100-002 for the component location. There is one fuel lift pump housing that contains dual lift pumps. The housing is located on the right bank of the engine above the flywheel and next to the fuel filter.

### Shoptalk

This fault code is caused by a short circuit in the harness or priming pump. It can also be caused by a failed ECM.

This fault code will **only** go active when the engine is cranking or running. To clear the fault code, the fail mode needs to be fixed and the engine will have to crank again to clear.

The service tool can be used to enable the fuel pump and check the fuel supply pressure as a system check.

Refer to Troubleshooting Fault Code t05-2297
