---
aliases:
  - "Давление прорыва газов — уровень предупреждения"
type: "Процедура"
doc: "01-fc555"
title_en: "Blowby Pressure - Warning Level"
title_ru: "Давление прорыва газов — уровень предупреждения"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc555.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc555.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Blowby Pressure - Warning Level
**Давление прорыва газов — уровень предупреждения**

> [!abstract] Процедура · `01-fc555`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc555.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc555.pdf)

### Fault Code: 555

### Blowby Pressure - Warning Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 555 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine blowby - warning level. Voltage signal indicates blowby pressure has exceeded the warning threshold for high blowby. | Calibration-dependent engine shutdown or no action is taken by ECM. |

![[19803587.png]]

Blowby Pressure Sensor Circuit

### Circuit Description

The blowby pressure sensor is used by the electronic control module (ECM) to monitor the engine crankcase pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The blowby pressure value is used by the ECM for the engine protection system.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Confirm that the crankcase breathers and breather tubes are **not** obstructed.

Refer to Troubleshooting Fault Code t05-555
