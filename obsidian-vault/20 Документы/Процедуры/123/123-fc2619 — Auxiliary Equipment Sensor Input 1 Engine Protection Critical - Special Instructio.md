---
aliases:
  - "Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
type: "Процедура"
doc: "123-fc2619"
title_en: "Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions"
title_ru: "Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания"
modified: "2010-09-23"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2619.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc2619.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions
**Вход датчика вспомогательного оборудования 1, защита двигателя — особые указания**

> [!abstract] Процедура · `123-fc2619`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-23
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2619.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc2619.pdf)

### Fault Code: 2619

### Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2619 PID(P): SPN: 701 FMI: 31 Lamp: Amber SRT: | Auxiliary Equipment Sensor Input 1 Engine Protection Critical - Special Instructions. The air shutoff is activated from engine overspeed or operator's E-stop. | Engine shuts down if engine protection shutdown feature is enabled. |

![[19f00001.png]]

Air Shutoff (OEM Switch/Dual Output) and E-stop Circuit

### Circuit Description

The circuit uses the OEM E-stop signal or engine overspeed to activate the air shutoff.

### Component Location

The E-Stop button is located on the door of the customer interface box (CIB) panel.

### Shoptalk

This is for engines with one or more OEM supplied air shutoff valves.

The air shutoff uses the OEM switch input for the emergency air shutoff stop. A switch closure from either the operator's E-stop or engine overspeed will cause the air shutoff to activate. Causes of this fault code are:

- Operator pushes engine stop button.

- Overspeed shutdown event as commanded by the ECM.

Refer to Troubleshooting Fault Code t05-2619
