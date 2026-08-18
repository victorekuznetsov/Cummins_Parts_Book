---
aliases:
  - "Цепь датчика уровня масла №1 — замыкание на плюс"
type: "Процедура"
doc: "01-fc498"
title_en: "Engine Oil Level Number 1 Sensor Circuit - Shorted High"
title_ru: "Цепь датчика уровня масла №1 — замыкание на плюс"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc498.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc498.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Oil Level Number 1 Sensor Circuit - Shorted High
**Цепь датчика уровня масла №1 — замыкание на плюс**

> [!abstract] Процедура · `01-fc498`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc498.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc498.pdf)

### Fault Code: 498

### Engine Oil Level Number 1 Sensor Circuit - Shorted High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 498 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil level Number 1 sensor circuit - shorted high. | No engine protection for low oil level. Centinel system is disabled. |

![[19803584.png]]

Oil Level Sensor Circuit

### Circuit Description

The oil level sensor is used by the electronic control module (ECM) to monitor the lubricating oil level. The ECM monitors the voltage on the oil level signal pin and converts this to an electronic value. The oil level value is used by the ECM for the engine protection system.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

High voltage can be caused by the signal wire shorting to another wire in the harness, an open circuit in the return wire, or a faulty sensor.

Refer to Troubleshooting Fault Code t05-498
