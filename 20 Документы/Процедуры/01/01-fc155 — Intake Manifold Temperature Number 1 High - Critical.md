---
aliases:
  - "Высокая температура впускного коллектора 1 — критично"
type: "Процедура"
doc: "01-fc155"
title_en: "Intake Manifold Temperature Number 1 High - Critical"
title_ru: "Высокая температура впускного коллектора 1 — критично"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc155.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc155.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Intake Manifold Temperature Number 1 High - Critical
**Высокая температура впускного коллектора 1 — критично**

> [!abstract] Процедура · `01-fc155`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc155.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc155.pdf)

### Fault Code: 155

### Intake Manifold Temperature Number 1 High - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 155 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine intake manifold air temperature has exceeded the alarm (shutdown) threshold for high intake manifold temperature. | Engine will shut down. High engine temperature (HET) relay driver is energized |

![[19803592.png]]

Intake Manifold Temperature Sensor Circuit

### Circuit Description

The intake manifold temperature sensor is used by the ECM to monitor the temperature of the air in the intake manifold after the aftercooler. The intake manifold temperature sensor is used by the ECM for the engine protection system, timing, and fueling control. If the voltage is low, the ECM will log Fault Code 155. Low voltage can be caused by a cooling system failure or an in-range sensor failure.

### Component Location

Refer to the Engine Diagrams in Section E of this manual for the component location.

### Shoptalk

The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-155
