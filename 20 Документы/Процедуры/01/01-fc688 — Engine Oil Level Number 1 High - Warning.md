---
aliases:
  - "Высокий уровень масла №1 — предупреждение"
type: "Процедура"
doc: "01-fc688"
title_en: "Engine Oil Level Number 1 High - Warning"
title_ru: "Высокий уровень масла №1 — предупреждение"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc688.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc688.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Oil Level Number 1 High - Warning
**Высокий уровень масла №1 — предупреждение**

> [!abstract] Процедура · `01-fc688`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc688.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc688.pdf)

### Fault Code: 688

### Engine Oil Level Number 1 High - Warning

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 688 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine oil level Number 1 high - critical. Voltage signal indicates very high lubricating oil level in the engine. | Engine will shut down. |

![[19803584.png]]

Oil Level Sensor Circuit

### Circuit Description

The oil level sensor is used by the ECM to monitor the amount of oil in the engine. High oil level detected can cause the engine to shut down or **not** start.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

A 4-pin oil level sensor will **not** trigger Fault Code 688.

Refer to Troubleshooting Fault Code t05-688
