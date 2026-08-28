---
aliases:
  - "Цепь датчика температуры OEM"
type: "Процедура"
doc: "19-fc293"
title_en: "OEM Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры OEM"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc293.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc293.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# OEM Temperature Sensor Circuit
**Цепь датчика температуры OEM**

> [!abstract] Процедура · `19-fc293`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc293.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc293.pdf)

### Fault Code: 293

### OEM Temperature Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 293 PID(P): P223 SPN: 1083 FMI: 3 Lamp: Yellow SRT: | VDC detected at the OEM temperature sensor signal pin 27 of the OEM interface harness indicates the sensor has failed high. | No engine protection for OEM temperature. |

![[19400674.png]]

OEM Temperature Circuit

### Circuit Description

The OEM sensor signal is used by the ECM to monitor the OEM temperature. The OEM temperature is used by the ECM for the engine protection system. A sensor that has failed high can be caused by opens in the signal or return wire, voltage shorts in the signal or return wire, or a faulty sensor.

### Component Location

The location varies with the OEM. Refer to the OEM manual.

### Shoptalk

The resistance of all temperature sensors varies with the ambient temperature.

Refer to Troubleshooting Fault Code t05-293
