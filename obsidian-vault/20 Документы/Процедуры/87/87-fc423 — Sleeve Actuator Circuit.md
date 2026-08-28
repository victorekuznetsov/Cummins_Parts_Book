---
aliases:
  - "Цепь исполнительного механизма гильзы"
type: "Процедура"
doc: "87-fc423"
title_en: "Sleeve Actuator Circuit"
title_ru: "Цепь исполнительного механизма гильзы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Sleeve Actuator Circuit
**Цепь исполнительного механизма гильзы**

> [!abstract] Процедура · `87-fc423`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc423.pdf)

### Fault Code: 423

### Sleeve Actuator Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 423 PID(P): 156 SPN: 156 FMI: 2 Lamp: Yellow SRT: | Unable to achieve the requested pump timing. This fault can be caused by incorrect static pump timing, clogged fuel filters or inlet screen, a stuck timing sleeve, air in the fuel lines, or calibration errors. | No action is taken by the electronic control module. Power output can be low and engine can produce white or black smoke. |

![[19a00103.png]]

Sleeve Actuator Circuit

### Circuit Description

The sleeve actuator circuit is used to control the start of injection through pin 6 of the engine harness. The electronic control module monitors the current on pin 6 and expects the amperage to vary between 1.0 and 6.2 amperes during normal engine operation.

### Component Location

The sleeve actuator circuit is an integral part of the RP39 fuel pump.

### Shoptalk

Increasing the current supplied to the sleeve actuator circuit increases the timing advancement of injection.

A stuck timing sleeve can be the result of fuel contamination.

High fuel inlet restriction and/or low fuel level may cause a low power condition.

Refer to Troubleshooting Fault Code t05-423
