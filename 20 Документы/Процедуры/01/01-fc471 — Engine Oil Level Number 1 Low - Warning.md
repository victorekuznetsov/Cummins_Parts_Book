---
aliases:
  - "Низкий уровень масла №1 — предупреждение"
type: "Процедура"
doc: "01-fc471"
title_en: "Engine Oil Level Number 1 Low - Warning"
title_ru: "Низкий уровень масла №1 — предупреждение"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc471.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc471.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Oil Level Number 1 Low - Warning
**Низкий уровень масла №1 — предупреждение**

> [!abstract] Процедура · `01-fc471`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc471.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc471.pdf)

### Fault Code: 471

### Engine Oil Level Number 1 Low - Warning

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 471 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine oil level has dropped below the warning threshold for low oil level. | Calibration-dependent. No action is taken by the ECM, or engine shutdown. |

![[19803623.png]]

Oil Level Sensor Circuit

### Circuit Description

The oil level sensor monitors the oil level within the oil system and passes information to the electronic control module (ECM). Low oil level can cause the engine to **not** start.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Some engine configurations will use a 3-pin oil level sensor and others will use a 4-pin oil level sensor.

Refer to Troubleshooting Fault Code t05-471
