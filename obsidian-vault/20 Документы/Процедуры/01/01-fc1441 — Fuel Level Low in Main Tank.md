---
aliases:
  - "Низкий уровень топлива в основном баке"
type: "Процедура"
doc: "01-fc1441"
title_en: "Fuel Level Low in Main Tank"
title_ru: "Низкий уровень топлива в основном баке"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1441.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1441.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Level Low in Main Tank
**Низкий уровень топлива в основном баке**

> [!abstract] Процедура · `01-fc1441`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1441.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1441.pdf)

### Fault Code: 1441

### Fuel Level Low in Main Tank

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1441 PID(P): SPN: FMI: Lamp: Warning SRT: | Fuel level low in main tank. | No action is taken by the ECM. Possible loss of performance. |

![[19802815.png]]

Main Tank Fuel Level Sensor Circuit

### Circuit Description

The fuel level sensor monitors the fuel level within the main tank and passes information to the electronic control module (ECM).

### Component Location

Refer to customer/facility/installation documentation for the location of the fuel main tank and the fuel level sensor used on the main tank.

### Shoptalk

When the fuel level drops below a certain level in the tank, it could cause the fuel pump to work harder to obtain the desired fuel pressure.

If a shorting plug is used in the fuel level circuit, verify that it is wired correctly.

Inspect all connectors and the sensor pins for damage.

Refer to Troubleshooting Fault Code t05-1441
