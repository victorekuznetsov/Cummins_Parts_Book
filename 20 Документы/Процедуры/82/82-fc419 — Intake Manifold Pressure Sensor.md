---
aliases:
  - "Датчик давления во впускном коллекторе"
type: "Процедура"
doc: "82-fc419"
title_en: "Intake Manifold Pressure Sensor"
title_ru: "Датчик давления во впускном коллекторе"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc419.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc419.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Intake Manifold Pressure Sensor
**Датчик давления во впускном коллекторе**

> [!abstract] Процедура · `82-fc419`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc419.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc419.pdf)

### Fault Code: 419

### Intake Manifold Pressure Sensor

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 419 PID(P): P102 SPN: 1319 FMI: 2 Lamp: Yellow SRT: | An error in the intake manifold pressure sensor signal was detected by the ECM. | Engine is derated to no-air setting. |

![[19200329.png]]

Intake Manifold Pressure Sensor

### Circuit Description

### Component Location

The intake manifold pressure sensor is located in the air intake manifold toward the front of the engine.

### Shoptalk

At key-on, the readings for ambient pressure from the ambient air pressure sensor, intake manifold pressure sensor, and oil pressure sensor are compared. This fault code occurs if the intake manifold pressure sensor reading is different from the other two.

Refer to Troubleshooting Fault Code t05-419
