---
aliases:
  - "Высокое выходное напряжение генератора"
type: "Процедура"
doc: "01-fc1446"
title_en: "Generator AC Output Voltage - High"
title_ru: "Высокое выходное напряжение генератора"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1446.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1446.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator AC Output Voltage - High
**Высокое выходное напряжение генератора**

> [!abstract] Процедура · `01-fc1446`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1446.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1446.pdf)

### Fault Code: 1446

### Generator AC Output Voltage - High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1446 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Generator AC output voltage is high. | Generator set will shut down. |

![[19802905.png]]

Generator Circuit

### Circuit Description

The generator set produces electric power. This power is in the form of three-phase AC. The engine control module (ECM) monitors the performance and operation of the generator set. The threshold for a high AC output voltage condition is that one or more of the phase voltages has exceeded 130 percent of nominal or has exceeded 110 percent of nominal for at least 10 seconds. The ECM uses this fault code to tell the operator when the generator set AC output voltage is high.

### Component Location

Refer to customer/facility/installation documentation for diagrams on the generator set/electric bus setup.

### Shoptalk

This fault can be caused by a failed voltage regulator, PT/CT board, open circuit, or short circuit in one of the harnesses.

If the voltages at the output leads of the alternator do **not** correspond to the voltages read by the electronic service tool, the problem can be in the voltage sensing circuits.

At idle, if INSITE™ electronic service tool shows greater than residual voltages from the alternator, the problem can be with either the PMG, field wiring, or voltage regulator. If you unplug connector 10 and the AC output voltage drops to residual, the problem is with the voltage regulator. If the voltage does **not** drop, the problem is with the PMG or field wiring.

Refer to Troubleshooting Fault Code t05-1446.
