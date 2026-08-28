---
aliases:
  - "Давление охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "19-fc233"
title_en: "Coolant Pressure - Engine Protection"
title_ru: "Давление охлаждающей жидкости — защита двигателя"
modified: "2026-05-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc233.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc233.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Coolant Pressure - Engine Protection
**Давление охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `19-fc233`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc233.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc233.pdf)

### Fault Code: 233

### Coolant Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 233 PID(P): P109 SPN: 109 FMI: 1 Lamp: Engine Protection SRT: 00-389 | Low coolant pressure has been detected. Voltage signal at coolant pressure signal pin 16 of the engine harness indicates coolant pressure lower than 28 kPa \[4 psi\] at 800 rpm, 41 kPa \[6 psi\] at 1300 rpm, 76 kPa \[11 psi\] at 1800 rpm, 96 kPa \[14 psi\] at 2000 rpm, and 103 kPa \[15 psi\] above 2100 rpm. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |

![[19800988.png]]

Coolant Pressure Sensor Circuit

### Circuit Description

The coolant pressure sensor is used by the ECM to monitor the coolant pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The coolant pressure value is used by the ECM for the engine protection system.

### Component Location

The coolant pressure sensor is located on the exhaust side of the engine, below the oil cooler.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged coolant pressure sensor

Refer to Troubleshooting Fault Code t05-233
