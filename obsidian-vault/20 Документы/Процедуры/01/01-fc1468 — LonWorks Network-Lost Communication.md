---
aliases:
  - "Сеть LonWorks — потеря связи"
type: "Процедура"
doc: "01-fc1468"
title_en: "LonWorks Network-Lost Communication"
title_ru: "Сеть LonWorks — потеря связи"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1468.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1468.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# LonWorks Network-Lost Communication
**Сеть LonWorks — потеря связи**

> [!abstract] Процедура · `01-fc1468`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1468.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1468.pdf)

### Fault Code: 1468

### LonWorks Network-Lost Communication

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1468 PID(P): SPN: FMI: Lamp: Warning SRT: | Loss of communication from the LonWorks Network. | No action taken by ECM. |

![[19802908.png]]

LonWorks Network Circuit

### Circuit Description

If a LonWorks Network is installed, the ECM checks communication to make sure it is operating correctly. The ECM uses the LonWorks Network to inform other controllers on the LonWorks Network about generator set operation, performance, setup, and diagnostics.The ECM monitors the LonWorks Network, no communication with the LonWorks Network will trip Fault Code 1468, caused by shorts or open circuits.

### Component Location

Refer to Section E for location of the LonWorks board.

### Shoptalk

Refer to the LonWorks Network publications for more specific troubleshooting methods.

Refer to Troubleshooting Fault Code t05-1468
