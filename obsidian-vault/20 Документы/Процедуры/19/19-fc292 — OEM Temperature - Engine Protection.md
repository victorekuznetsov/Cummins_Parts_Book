---
type: "Процедура"
doc: "19-fc292"
title_en: "OEM Temperature - Engine Protection"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc292.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc292.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# OEM Temperature - Engine Protection

> [!abstract] Процедура · `19-fc292`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc292.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc292.pdf)

### Fault Code: 292

### OEM Temperature - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 292 PID(P): P223 SPN: 1083 FMI: 14 Lamp: Engine Protection SRT: | OEM temperature out-of-range has been detected. Voltage signal at OEM temperature signal pin 27 indicates OEM temperature beyond the OEM-specified threshold. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |

![[19400893.png]]

OEM Temperature Circuit

### Circuit Description

The OEM resistive signal is used by the ECM to monitor an OEM temperature. The OEM temperature is used by the ECM for the engine protection system.

### Component Location

The location varies with the OEM. Refer to the OEM manual.

### Shoptalk

The resistance of all temperature sensors varies with the ambient temperature.

Refer to Troubleshooting Fault Code t05-292
