---
aliases:
  - "Цепь датчика давления OEM"
type: "Процедура"
doc: "82-fc297"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc297.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# OEM Pressure Sensor Circuit
**Цепь датчика давления OEM**

> [!abstract] Процедура · `82-fc297`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc297.pdf)

### Fault Code: 297 (INDUSTRIAL)

### OEM Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 297 PID(P): S223 SPN: 1084 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the OEM pressure sensor signal pin. | No engine protection for OEM pressure. |

![[19200386.png]]

OEM Pressure Sensor Circuit

### Circuit Description

The OEM sensor signal is used by the ECM to monitor the OEM pressure. The OEM pressure is used by the ECM for the engine protection system. A sensor that has failed high can be caused by an open circuit in the signal or return wire, a voltage short in the signal or return wire, or a faulty sensor.

### Component Location

The location varies with the OEM. Refer to the OEM troubleshooting and repair manual.

### Shoptalk

The sensor voltage signal is supplied by the ECM on pin 18 of the sensor harness connector.

Refer to Troubleshooting Fault Code t05-297
