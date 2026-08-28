---
aliases:
  - "Давление масла — защита двигателя"
type: "Процедура"
doc: "19-fc143"
title_en: "Oil Pressure - Engine Protection"
title_ru: "Давление масла — защита двигателя"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc143.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc143.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Oil Pressure - Engine Protection
**Давление масла — защита двигателя**

> [!abstract] Процедура · `19-fc143`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc143.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc143.pdf)

### Fault Code: 143

### Oil Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 143 PID(P): P100 SPN: 100 FMI: 1 Lamp: Engine Protection SRT: 00-354 | Low oil pressure has been detected. Voltage signal at oil pressure signal pin 24 of the engine harness indicates oil pressure lower than 103 kPa \[15 psi\] at 600 rpm, 131 kPa \[19 psi\] at 800 rpm, 165 kPa \[24 psi\] at 1500 rpm, and 207 kPa \[30 psi\] above 2100 rpm. | Calibration-dependent progressive power derate and engine shutdown with increasing time after alert. Centinel™ system is disabled. |

![[19400133.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure sensor is used by the ECM to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.

### Component Location

The oil pressure sensor is located on the engine block, toward the front of the ECM.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine oil pressure sensor

- Low oil level

- External oil leaks

- Plugged lubricating oil filters

- Contaminated oil

- Oil aeration

- High oil temperature

- Malfunctioning or damaged main oil rifle pressure regulator

- Malfunctioning or damaged piston cooling nozzle

- Malfunctioning or damaged oil suction tube

- Malfunctioning or damaged oil transfer plumbing

- Malfunctioning or damaged oil pump

- Malfunctioning or damaged lubricating pump high pressure relief valve

- Internal engine damage

- Malfunctioning or damaged oil cooler element

Refer to Troubleshooting Fault Code t05-143
