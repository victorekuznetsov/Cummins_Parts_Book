---
aliases:
  - "Температура генератора — защита генератора"
type: "Процедура"
doc: "01-fc1319"
title_en: "Alternator Temperature - Alternator Protection"
title_ru: "Температура генератора — защита генератора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1319.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1319.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Alternator Temperature - Alternator Protection
**Температура генератора — защита генератора**

> [!abstract] Процедура · `01-fc1319`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1319.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1319.pdf)

### Fault Code: 1319

### Alternator Temperature - Alternator Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1319 PID(P): SPN: FMI: Lamp: Warning SRT: | Alternator temperature has exceeded the warning threshold for high alternator temperature. | No action is taken by the ECM. Possible loss of generator performance. |

![[19802424.png]]

Alternator Temperature Sensor Circuit

### Circuit Description

The alternator temperature sensor is used by the electronic control module (ECM) for the generator set protection system. The ECM monitors the temperature of the alternator and informs the operator, via the warning lamp, that the alternator temperature has increased past the warning threshold for alternator temperature.The ECM monitors the voltage on the alternator temperature signal pin and expects to see a voltage vary between 0.5 and 4.5 VDC during normal engine operation.

### Component Location

Refer to the Engine Diagrams in Section E of this manual for the component location.

### Shoptalk

Make sure that the alternator is being properly cooled/ventilated.

The resistance of all the temperature sensors varies with the temperature.

Refer to Troubleshooting Fault Code t05-1319
