---
aliases:
  - "Цепь датчика воды в топливе (WIF)"
type: "Процедура"
doc: "82-fc428"
title_en: "Water-In-Fuel (WIF) Sensor Circuit"
title_ru: "Цепь датчика воды в топливе (WIF)"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc428.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc428.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Water-In-Fuel (WIF) Sensor Circuit
**Цепь датчика воды в топливе (WIF)**

> [!abstract] Процедура · `82-fc428`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc428.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc428.pdf)

### Fault Code: 428

### Water-In-Fuel (WIF) Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 428 PID(P): P097 SPN: 97 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at water-in-fuel (WIF) sensor circuit. | None on performance. |

![[19c00273.png]]

WIF Sensor Circuit

### Circuit Description

The WIF sensor is attached to the fuel filter. The WIF sensor sends a signal to the electronic control module (ECM) when a set volume of water has accumulated in the fuel filter. The WIF circuit contain two wires: A return ground (pin 10) and a signal wire (pin 9).

### Component Location

The WIF sensor is installed in the fuel filter and is located on the side of the head, approximately midengine.

### Shoptalk

Possible causes for this fault code include: Short circuit to a + 5-VDC supply wire.

Refer to Troubleshooting Fault Code t05-428
