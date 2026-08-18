---
aliases:
  - "Критический внутренний отказ ЭБУ — неисправное устройство"
type: "Процедура"
doc: "122-fc111"
title_en: "Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component"
title_ru: "Критический внутренний отказ ЭБУ — неисправное устройство"
modified: "2016-08-08"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc111.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc111.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component
**Критический внутренний отказ ЭБУ — неисправное устройство**

> [!abstract] Процедура · `122-fc111`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-08-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc111.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/122-fc111.pdf)

### Fault Code: 111

### Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 111 PID(P): S254 SPN: 629 FMI: 12 Lamp: Red SRT: | Engine Control Module Critical Internal Failure - Bad Intelligent Device or Component. Error internal to the engine control module (ECM) related to memory hardware malfunctions or internal ECM voltage supply circuits. | Engine may **not** start or may be difficult to start. |

![[19d02662.png]]

ECM

### Circuit Description

The ECM has internal diagnostics that continuously run and check the internal memory.

### Component Location

The ECMs are located on the left (fuel pump) side of the engine.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position.

### Conditions For Setting The Fault Codes

The ECM detected a read or write error internal to the ECM.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the red STOP ENGINE lamp immediately after the diagnostic runs and fails.

- The engine may **not** start.

### Conditions For Clearing The Fault Code

- To validate the repair, perform a key cycle, start the engine and let it idle for 1 minute.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the red STOP ENGINE lamp immediately after the diagnostic runs and passes.

- The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

This fault code can **only** be caused by an internal ECM malfunction. Repairs are **not** possible for the ECM.

Refer to Troubleshooting Fault Code t05-111
