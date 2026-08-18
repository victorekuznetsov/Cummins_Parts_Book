---
aliases:
  - "Низкое давление масла редуктора двигателя — критично"
type: "Процедура"
doc: "01-fc2561"
title_en: "Engine Gear Box Oil Pressure Low - Critical"
title_ru: "Низкое давление масла редуктора двигателя — критично"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2561.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2561.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Gear Box Oil Pressure Low - Critical
**Низкое давление масла редуктора двигателя — критично**

> [!abstract] Процедура · `01-fc2561`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2561.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2561.pdf)

### Fault Code: 2561

### Engine Gear Box Oil Pressure Low - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2561 PCODE(P): SPN: FMI: Lamp: Shutdown SRT: | Voltage signal indicates the engine gear box oil pressure has dropped below the shutdown threshold for low engine gear box oil pressure. | Generator set will shutdown. |

![[19600393.png]]

Engine Gear Box Oil Pressure Sensor Circuit

### Circuit Description

The engine gear box oil pressure sensor is a switch type sensor. After the pressure drops below the switch point, the sensor will close the circuit. This closed circuit will cause the LonWorks digital input module to send a signal on the LonWorks network to the generator set ECM indicating an engine gear box oil pressure low - critical condition exists.

### Component Location

The engine gear box oil pressure sensor is located on the gear box.

### Shoptalk

This fault can be caused by a low pressure condition, or a short circuit in the engine gear box oil pressure switch to digital input module circuit. Both pressure of the gearbox oil and a check for a short circuit **must** be performed to troubleshoot this fault.

Refer to Troubleshooting Fault Code t05-2561
