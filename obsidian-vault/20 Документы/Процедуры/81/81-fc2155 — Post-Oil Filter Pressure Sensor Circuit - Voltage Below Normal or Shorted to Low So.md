---
type: "Процедура"
doc: "81-fc2155"
title_en: "Post-Oil Filter Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source"
modified: "2015-07-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
families:
  - "QSK60"
manuals:
  - "3666410"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc2155.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc2155.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK60"
  - "группа/81"
---

# Post-Oil Filter Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source

> [!abstract] Процедура · `81-fc2155`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]]
> **Семейство:** QSK60
> **Входит в руководства:** [[3666410 — QSK45 and QSK60 CENSE™ Electronic Control System Troubleshooting and Repair Manual|3666410]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-07-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/81/81-fc2155.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/81-fc2155.pdf)

### Fault Code: 2155

### Post-Oil Filter Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2155 PID(P): 100 SPN: 611 FMI: 4 Lamp: None SRT: 00-686 | Post-Oil Filter Pressure Sensor Circuit - Voltage Below Normal or Shorted to Low Source. Low voltage detected on SIGNAL pin 09 of the main harness A ECM connector. | Fault Code 612 is disabled. |

![[19802529.png]]

Post-Filter Oil Pressure Sensor Circuit

### Circuit Description

The post-filter oil pressure is the engine oil pressure after the oil has passed through the oil filters. The post-filter oil pressure sensor sends the post-filter oil pressure signal to the CENSE™ ECM.

### Component Location

The post-filter oil pressure sensor is located on the oil outlet side of the lubricating oil system filter head.

### Shoptalk

- If the fault occurs **only** in a cold environment, allow the oil to warm up and see if the fault becomes inactive.

Refer to Troubleshooting Fault Code t05-2155
