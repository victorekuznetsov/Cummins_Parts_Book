---
aliases:
  - "Цепь датчика давления OEM"
type: "Процедура"
doc: "19-fc297"
title_en: "OEM Pressure Sensor Circuit"
title_ru: "Цепь датчика давления OEM"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc297.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc297.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# OEM Pressure Sensor Circuit
**Цепь датчика давления OEM**

> [!abstract] Процедура · `19-fc297`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc297.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc297.pdf)

### Fault Code: 297

### OEM Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 297 PID(P): P223 SPN: 1084 FMI: 3 Lamp: Yellow SRT: | VDC detected at the OEM pressure sensor signal pin 15 of the OEM interface harness indicates the sensor has failed high. | No engine protection for OEM pressure. |

![[19400645.png]]

OEM Pressure Sensor Circuit

### Circuit Description

The OEM sensor signal is used by the ECM to monitor the OEM pressure. The OEM pressure is used by the ECM for the engine protection system. A sensor that has failed high can be caused by an open circuit in the signal or return wire, voltage shorts in the signal or return wire, or a faulty sensor.

### Component Location

The location varies with the OEM. Refer to the OEM manual.

### Shoptalk

The sensor voltage signal is the responsibility of the OEM. Refer to the OEM manual for specifications.

Refer to Troubleshooting Fault Code t05-297
