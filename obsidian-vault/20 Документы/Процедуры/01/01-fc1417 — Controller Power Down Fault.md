---
aliases:
  - "Неисправность отключения питания контроллера"
type: "Процедура"
doc: "01-fc1417"
title_en: "Controller Power Down Fault"
title_ru: "Неисправность отключения питания контроллера"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1417.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1417.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Controller Power Down Fault
**Неисправность отключения питания контроллера**

> [!abstract] Процедура · `01-fc1417`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1417.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1417.pdf)

### Fault Code: 1417

### Controller Power Down Fault

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1417 PID(P): SPN: FMI: Lamp: Warning SRT: | A controller power-down error has been detected. | The ECM can **not** power down because of some unknown condition. Possible drain on battery. |

![[19802494.png]]

GCS ECM

### Circuit Description

The ECM checks during the power-down sequences to see if power is being shut off. If the power line is still hot, it checks for a reason for **not** shutting down. If no reason exists, then there **must** be a problem with the module that is **not** allowing it to power down.

### Component Location

Refer to the OEM manual for location of the ECM.

### Shoptalk

This fault indicates a hardware failure in the ECM.

Refer to Troubleshooting Fault Code t05-1417
