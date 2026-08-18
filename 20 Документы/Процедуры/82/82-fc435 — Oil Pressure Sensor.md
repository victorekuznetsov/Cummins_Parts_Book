---
aliases:
  - "Датчик давления масла"
type: "Процедура"
doc: "82-fc435"
title_en: "Oil Pressure Sensor"
title_ru: "Датчик давления масла"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc435.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc435.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Oil Pressure Sensor
**Датчик давления масла**

> [!abstract] Процедура · `82-fc435`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc435.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc435.pdf)

### Fault Code: 435

### Oil Pressure Sensor

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 435 PID(P): P100 SPN: 100 FMI: 2 Lamp: Yellow SRT: | An error in the oil pressure sensor signal was detected by the ECM. | None on performance; no engine protection for oil pressure. |

![[19c00506.png]]

Oil Pressure Sensor

### Circuit Description

### Component Location

The oil pressure/temperature sensor is located on the engine block to the left of the fuel filter, behind the air compressor.

### Shoptalk

At key-on, the readings for ambient pressure from the ambient air pressure sensor, intake manifold pressure sensor, and oil pressure sensor are compared. This fault code occurs if the oil pressure sensor reading is different from the other two.

Refer to Troubleshooting Fault Code t05-435
