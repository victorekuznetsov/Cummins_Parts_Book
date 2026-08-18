---
aliases:
  - "Цепь датчика частоты/положения — потеря сигнала"
type: "Процедура"
doc: "01-fc236"
title_en: "Engine Speed/Position Sensor Circuit - Loss of Signal"
title_ru: "Цепь датчика частоты/положения — потеря сигнала"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc236.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc236.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Speed/Position Sensor Circuit - Loss of Signal
**Цепь датчика частоты/положения — потеря сигнала**

> [!abstract] Процедура · `01-fc236`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc236.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc236.pdf)

### Fault Code: 236

### Engine Speed/Position Sensor Circuit - Loss of Signal

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 236 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine speed/position sensors signal is **not** detected. | Engine will shut down. |

![[19802445.png]]

Engine Speed/Position Sensor Circuits

### Circuit Description

The crankshaft and camshaft engine position sensor provides engine speed and position information to the electronic control module (ECM) through the engine harness.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Possible causes of this fault code include damaged camshaft engine position sensor, open or shorted circuit, and power supply voltage failure.

Refer to Troubleshooting Fault Code t05-236
