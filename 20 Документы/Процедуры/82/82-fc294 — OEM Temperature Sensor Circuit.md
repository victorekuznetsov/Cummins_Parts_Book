---
aliases:
  - "Цепь датчика температуры OEM"
type: "Процедура"
doc: "82-fc294"
title_en: "OEM Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры OEM"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc294.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc294.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# OEM Temperature Sensor Circuit
**Цепь датчика температуры OEM**

> [!abstract] Процедура · `82-fc294`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc294.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc294.pdf)

### Fault Code: 294 (INDUSTRIAL)

### OEM Temperature Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 294 PID(P): S154 SPN: 1083 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the OEM temperature sensor signal pin of the 31-pin OEM connector. | No engine protection for OEM temperature. |

![[19c00675.png]]

OEM Temperature Sensor Circuit

### Circuit Description

The OEM sensor signal is used by the electronic control module (ECM) to monitor the OEM temperature. The OEM temperature is used by the ECM for the engine protection system. A sensor that has failed low can be caused by a short circuit to ground on a supply or return wire, or an internally grounded (faulty) sensor.

### Component Location

The location varies with the OEM. Refer to the OEM troubleshooting and repair manual.

### Shoptalk

The resistance of all temperature sensors varies with the temperature. Check the temperature thresholds using INSITE™.

Refer to Troubleshooting Fault Code t05-294
