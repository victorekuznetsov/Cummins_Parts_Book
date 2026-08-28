---
aliases:
  - "Ошибка датчика частоты вращения коленвала"
type: "Процедура"
doc: "01-fc689"
title_en: "Crankshaft Engine Speed Sensor Error"
title_ru: "Ошибка датчика частоты вращения коленвала"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc689.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc689.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Crankshaft Engine Speed Sensor Error
**Ошибка датчика частоты вращения коленвала**

> [!abstract] Процедура · `01-fc689`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc689.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc689.pdf)

### Fault Code: 689

### Crankshaft Engine Speed Sensor Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 689 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Primary engine speed sensor error. No engine speed signal detected from the crankshaft engine speed sensor. | No action taken by the ECM. Engine will continue to run on the camshaft engine position sensor. Possible loss of performance. |

![[19803588.png]]

Crankshaft Engine Speed Sensor Circuit

### Circuit Description

The crankshaft engine speed sensor provides engine speed and position information to the electronic control module (ECM). The sensor **must** be powered up by +5 VDC to operate. The sensor generates the signal by sensing the movement of target teeth machined into a tone wheel that is mounted to the crankshaft.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Possible causes of this fault code include damaged crankshaft engine speed sensor, open or shorted circuit, or power supply voltage failure.

Refer to Troubleshooting Fault Code t05-689
