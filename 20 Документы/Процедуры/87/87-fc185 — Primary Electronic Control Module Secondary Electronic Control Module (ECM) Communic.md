---
aliases:
  - "Связь основного и резервного ЭБУ"
type: "Процедура"
doc: "87-fc185"
title_en: "Primary Electronic Control Module/Secondary Electronic Control Module (ECM) Communication"
title_ru: "Связь основного и резервного ЭБУ"
modified: "2016-07-27"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc185.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc185.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Primary Electronic Control Module/Secondary Electronic Control Module (ECM) Communication
**Связь основного и резервного ЭБУ**

> [!abstract] Процедура · `87-fc185`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-07-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc185.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc185.pdf)

### Fault Code: 185

### Primary Electronic Control Module/Secondary Electronic Control Module (ECM) Communication

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 185 PID(P): 231 SPN: 639 FMI: 2 Lamp: Yellow SRT: | Communication between the primary electronic control module (ECM) and secondary ECM has been interrupted. | Engine can **only** run on the left or right bank. Possible loss of performance. |

![[19a00457.png]]

J1939 Backbone Harness Circuit Diagram

### Circuit Description

The QST30 electronic control system utilizes an SAE J1939 backbone harness for communication between the primary and secondary ECMs. If this backbone fails, communication between the ECMs will stop, causing the engine to run poorly.

### Component Location

The primary ECM is located on the left bank of the engine, in front of the fuel pump. The secondary ECM is located on the right bank of the engine. The SAE J1939 backbone harness is a separate, three-wire harness located on the engine.

### Shoptalk

The secondary ECM receives its fueling and timing commands from the primary ECM.

Refer to Troubleshooting Fault Code t05-185
