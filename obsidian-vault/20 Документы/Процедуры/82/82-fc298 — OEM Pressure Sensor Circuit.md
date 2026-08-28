---
aliases:
  - "Цепь датчика давления OEM"
type: "Процедура"
doc: "82-fc298"
title_en: "OEM Pressure Sensor Circuit"
title_ru: "Цепь датчика давления OEM"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc298.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc298.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# OEM Pressure Sensor Circuit
**Цепь датчика давления OEM**

> [!abstract] Процедура · `82-fc298`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc298.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc298.pdf)

### Fault Code: 298 (INDUSTRIAL)

### OEM Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 298 PID(P): S223 SPN: 1084 FMI: 4/4 Lamp: Yellow SRT: | Low voltage detected at the OEM pressure sensor signal pin of the 31-pin OEM connector. | No engine protection for OEM pressure. |

![[19200386.png]]

OEM Pressure Sensor Circuit

### Circuit Description

The OEM sensor signal is used by the ECM to monitor the OEM pressure. The OEM pressure is used by the ECM for the engine protection system. A sensor that has failed low can be caused by a short circuit to ground on the signal wire, or an internally grounded (faulty) sensor.

### Component Location

The location varies with the OEM. Refer to the OEM troubleshooting and repair manual.

### Shoptalk

The resistance of all pressure sensors varies with the pressure. Refer to the OEM troubleshooting and repair manual for specifications.

Refer to Troubleshooting Fault Code t05-298
