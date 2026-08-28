---
aliases:
  - "Цепь выключателя выбора альтернативной кривой момента"
type: "Процедура"
doc: "87-fc528"
title_en: "Alternate Torque Curve Select Switch Circuit"
title_ru: "Цепь выключателя выбора альтернативной кривой момента"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc528.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc528.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Alternate Torque Curve Select Switch Circuit
**Цепь выключателя выбора альтернативной кривой момента**

> [!abstract] Процедура · `87-fc528`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc528.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc528.pdf)

### Fault Code: 528

### Alternate Torque Curve Select Switch Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 528 PID(P): P093 SPN: 093 FMI: 2 Lamp: Yellow SRT: | The electronic control module (ECM) has detected an invalid value from the alternate torque selection switch at pin 39 of the OEM interface harness, indicating the value is out of range. | Alternate torque selection is disabled. Torque curve setting defaults to switch position 2 (or lowest) preprogrammed torque curve. |

![[19801022.png]]

Alternate Torque Curve Select Switch Signal Circuit

### Circuit Description

The torque curve switch circuit allows the operator to select from three preprogrammed torque curves using a tristate switch.

### Component Location

The location of the torque curve switch circuit varies with each OEM and equipment model. Refer to the OEM manual.

### Shoptalk

The switch should be monitored for proper operation in INSITE™. If the switch is changing state correctly on the service tool, then the problem is **not** in the switch circuit. The tristate switch has three states:

- Position 1 - open

- Position 2 - closed

- Position 3 - 1500-ohm resistance.

Refer to Troubleshooting Fault Code t05-528
