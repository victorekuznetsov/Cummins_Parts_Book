---
aliases:
  - "Цепь управления насосом прокачки масла — напряжение выше нормы"
type: "Процедура"
doc: "123-fc1774"
title_en: "Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь управления насосом прокачки масла — напряжение выше нормы"
modified: "2010-12-10"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1774.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc1774.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source
**Цепь управления насосом прокачки масла — напряжение выше нормы**

> [!abstract] Процедура · `123-fc1774`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-12-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1774.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc1774.pdf)

### Fault Code: 1774

### Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1774 PID(P): SPN: 3589 FMI: 3 Lamp: Amber SRT: | Engine Oil Priming Pump Control Circuit - Voltage Above Normal or Shorted to High Source. High SIGNAL voltage detected in the engine oil priming pump circuit. | None on performance. |

![[19e01001.png]]

QSK19 CM2150 - Engine Oil Priming Pump Control Circuit

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
