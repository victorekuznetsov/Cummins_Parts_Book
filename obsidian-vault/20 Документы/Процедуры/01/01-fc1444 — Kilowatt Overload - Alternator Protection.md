---
aliases:
  - "Перегрузка по мощности — защита генератора"
type: "Процедура"
doc: "01-fc1444"
title_en: "Kilowatt Overload - Alternator Protection"
title_ru: "Перегрузка по мощности — защита генератора"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1444.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1444.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Kilowatt Overload - Alternator Protection
**Перегрузка по мощности — защита генератора**

> [!abstract] Процедура · `01-fc1444`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1444.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1444.pdf)

### Fault Code: 1444

### Kilowatt Overload - Alternator Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1444 PID(P): SPN: FMI: Lamp: Warning SRT: | The kilowatt has reached overload. | No action is taken by the ECM. |

![[19802905.png]]

Generator Circuit

### Circuit Description

The generator set produces electric power. When the generator is connected to the bus, it can be governed by adjusting the kilowatt load or the kVAR load. The engine control module (ECM) monitors the three-phase generator output. The threshold for kilowatt overload is 115 percent of rated power output. The ECM uses this fault code to inform the operator that the kilowatt load is too high for the engine and needs to be reduced.

### Component Location

Refer to Section E for location of the alternator.

Refer to customer/facility/installation documentation for diagrams on the generator set/electric bus setup.

### Shoptalk

Check the load and load lead connections.

Refer to Troubleshooting Fault Code t05-1444.
