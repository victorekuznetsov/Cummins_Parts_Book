---
aliases:
  - "Датчик уровня масла №1 — неверные данные"
type: "Процедура"
doc: "01-fc252"
title_en: "Engine Oil Level Number 1 Sensor - Data Incorrect"
title_ru: "Датчик уровня масла №1 — неверные данные"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc252.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc252.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Oil Level Number 1 Sensor - Data Incorrect
**Датчик уровня масла №1 — неверные данные**

> [!abstract] Процедура · `01-fc252`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc252.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc252.pdf)

### Fault Code: 252

### Engine Oil Level Number 1 Sensor - Data Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 252 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil level Number 1 sensor circuit - data incorrect. | No engine protection for low oil level. Centinel system is disabled. |

![[19803584.png]]

Oil Level Sensor Circuit

### Circuit Description

The lubricating oil level sensor is used by the ECM to monitor the amount of oil in the engine. Low oil level detected can cause the engine protection system to shut down the engine.

### Component Location

The lubricating oil level sensor is in the engine oil pan.

Refer to Troubleshooting Fault Code t05-252
