---
aliases:
  - "Разнос двигателя (превышение частоты вращения)"
type: "Процедура"
doc: "87-fc234"
title_en: "Engine Overspeed"
title_ru: "Разнос двигателя (превышение частоты вращения)"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc234.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc234.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Overspeed
**Разнос двигателя (превышение частоты вращения)**

> [!abstract] Процедура · `87-fc234`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc234.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc234.pdf)

### Fault Code: 234

### Engine Overspeed

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 234 PID(P): P190 SPN: 190 FMI: 0 Lamp: Red SRT: | Engine speed signal on pin 17 and/or pin 9 of the engine harness indicated engine speed is greater than the calibrated value (2650 rpm). | The EHAB (fuel shutoff valve) is de-energized (closed). The EHAB (fuel shutoff valve) is reenergized (opened) when engine speed falls below the calibrated value (2130 rpm). |

![[19a00572.png]]

Engine Speed Sensor Circuit

### Circuit Description

The engine speed sensor monitors the engine position and the engine speed and passes this information to the electronic control module (ECM) through the engine harness.

### Component Location

The engine speed sensor and the engine position sensor are located in the flywheel housing.

### Shoptalk

- Inspect the intake manifold for sources of flammable vapors. Check the turbocharger seals to verify that there are no oil leaks.

- Inspect the engine speed sensor for signs of damage or tampering.

Refer to Troubleshooting Fault Code t05-234
