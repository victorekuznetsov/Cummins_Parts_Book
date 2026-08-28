---
type: "Процедура"
doc: "19-fc296"
title_en: "OEM Pressure - Engine Protection"
modified: "2010-08-25"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc296.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc296.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# OEM Pressure - Engine Protection

> [!abstract] Процедура · `19-fc296`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-08-25
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc296.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc296.pdf)

### Fault Code: 296

### OEM Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 296 PID(P): P223 SPN: 1084 FMI: 14 Lamp: Engine Protection SRT: | OEM Pressure - Engine Protection - OEM pressure out-of-range has been detected. Voltage signal at OEM pressure signal pin 15 indicates OEM pressure beyond OEM-specified threshold. | OEM and calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |

![[19400645.png]]

OEM Pressure Circuit

### Circuit Description

The OEM pressure sensor monitors a pressure based on the application needs. OEM pressure readings are sent through pin 15 of the OEM interface harness to the ECM (electronic control module). The ECM expects to see the voltage vary between 0.5 and 4.5-VDC during normal engine operation.

### Component Location

The location varies with OEM. Refer to the OEM service manual.

### Shoptalk

If Fault Code 296 occurs during cold weather, allow the OEM fluid to warm up to operating temperature, turn the engine OFF, and restart. If the fault code remains active, troubleshoot the fault code.

Refer to Troubleshooting Fault Code 296.
