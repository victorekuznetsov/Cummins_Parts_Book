---
aliases:
  - "Высокая температура масла редуктора двигателя — критично"
type: "Процедура"
doc: "01-fc2562"
title_en: "Engine Gear Box Oil Temperature High - Critical"
title_ru: "Высокая температура масла редуктора двигателя — критично"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2562.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2562.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Gear Box Oil Temperature High - Critical
**Высокая температура масла редуктора двигателя — критично**

> [!abstract] Процедура · `01-fc2562`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2562.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc2562.pdf)

### Fault Code: 2562

### Engine Gear Box Oil Temperature High - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2562 PCODE(P): SPN: FMI: Lamp: Shutdown SRT: | Voltage signal indicates the engine gear box oil temperature has exceeded the shutdown threshold for high engine gear box oil temperature. | Generator set will shutdown. |

![[19600392.png]]

Engine Gear Box Oil Temperature Sensor Circuit

### Circuit Description

The engine gear box oil temperature sensor is a switch type sensor. After the temperature increases above the switch point, the sensor will close the circuit. This closed circuit will cause the LonWorks digital input module to send a signal on the LonWorks network to the generator set ECM indicating an engine gear box oil temperature high - critical condition exists.

### Component Location

The engine gear box oil temperature sensor is located on the gear box.

### Shoptalk

This fault code can be caused by a high temperature condition, or a short circuit in the engine gear box oil temperature switch to digital input module circuit. Both temperature of the gear box oil and a check for a short circuit **must** be performed to troubleshoot this fault.

Refer to Troubleshooting Fault Code t05-2562
