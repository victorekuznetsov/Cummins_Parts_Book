---
type: "Процедура"
doc: "19-fc555"
title_en: "Blowby Pressure - Engine Protection"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc555.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc555.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Blowby Pressure - Engine Protection

> [!abstract] Процедура · `19-fc555`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc555.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc555.pdf)

### Fault Code: 555

### Blowby Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 555 PID(P): P101 SPN: 1264 FMI: 0 Lamp: Engine Protection SRT: 00-676 | High blowby pressure has been detected. Voltage signal at blowby pressure signal pin 25 indicates blowby pressure above 368 mm H 2 O \[14.5 in H 2 O\]. | Calibration-dependent. Progressive power and speed derate and engine shutdown as pressure increases over thresholds. |

![[19800996.png]]

Blowby Pressure Sensor Circuit

### Circuit Description

The blowby pressure sensor is used by the ECM to monitor the engine crankcase pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The blowby pressure value is used by the ECM for the engine protection system.

### Component Location

The blowby pressure sensor is located on the exhaust side of the engine, below the water pump on the QSK19 series engines. See engine component views in Section E for location information for the QSK23, QSK45, QSK60, and QSK78 series engines.

### Shoptalk

- Confirm that the crankcase breathers and breather tubes are **not** obstructed.

Refer to Troubleshooting Fault Code t05-555
