---
aliases:
  - "Датчик атмосферного давления"
type: "Процедура"
doc: "82-fc295"
title_en: "Ambient Air Pressure Sensor"
title_ru: "Датчик атмосферного давления"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc295.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc295.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Ambient Air Pressure Sensor
**Датчик атмосферного давления**

> [!abstract] Процедура · `82-fc295`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc295.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc295.pdf)

### Fault Code: 295

### Ambient Air Pressure Sensor

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 295 PID(P): P108 SPN: 108 FMI: 2 Lamp: Yellow SRT: | An error in the ambient air pressure sensor signal was detected by the ECM. | Engine is derated to no air setting. |

![[19c00652.png]]

Ambient Air Pressure Sensor

### Circuit Description

### Component Location

The ambient air pressure sensor is located below the ECM.

### Shoptalk

At key-on, the readings for ambient pressure from the ambient air pressure sensor, intake manifold pressure sensor, and oil pressure sensor are compared. This fault code occurs if the ambient air pressure sensor reading is different from the other two.

Refer to Troubleshooting Fault Code t05-295
