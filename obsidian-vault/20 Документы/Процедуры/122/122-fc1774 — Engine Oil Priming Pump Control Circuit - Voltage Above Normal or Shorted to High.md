---
aliases:
  - "Цепь управления насосом прокачки масла — напряжение выше нормы"
type: "Процедура"
doc: "122-fc1774"
title_en: "Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь управления насосом прокачки масла — напряжение выше нормы"
modified: "2010-11-30"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1774.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1774.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source
**Цепь управления насосом прокачки масла — напряжение выше нормы**

> [!abstract] Процедура · `122-fc1774`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-11-30
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc1774.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc1774.pdf)

### Fault Code: 1774

### Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1774 PID(P): SPN: 3589 FMI: 3 Lamp: Amber SRT: | Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source. High signal voltage detected in the Engine Oil Priming Pump Circuit. | None on performance. |

![[19e01005.png]]

QSK38 CM2150 Industrial - Engine Oil Priming Pump Control Circuit

![[19e01006.png]]

QSK50 and QSK60 CM2150 Industrial - Engine Oil Priming Pump Control Circuit

### Circuit Description

The ECM monitors the engine oil priming circuit. If the ECM sees the engine oil priming pump is activated and oil pressure does **not** build to a pre-set level, Fault Code 1774 will become active and the amber lamp will illuminate.

### Component Location

The engine oil priming pump can be located on either side of the engine block.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when the INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

The engine oil priming pump circuit monitors oil pressure and OEM pump switch input.

Possible causes of this fault code include:

- Open RETURN circuit in the engine harness, connectors, or sensor

- SIGNAL wire shorted to sensor supply or battery voltage

- Engine oil priming pump **not** operating.

Refer to Troubleshooting Fault Code t05-1774.
