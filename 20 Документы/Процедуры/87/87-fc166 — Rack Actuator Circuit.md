---
aliases:
  - "Цепь привода рейки"
type: "Процедура"
doc: "87-fc166"
title_en: "Rack Actuator Circuit"
title_ru: "Цепь привода рейки"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc166.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Rack Actuator Circuit
**Цепь привода рейки**

> [!abstract] Процедура · `87-fc166`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc166.pdf)

### Fault Code: 166

### Rack Actuator Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 166 PID(P): S024 SPN: 733 FMI: 3 Lamp: Yellow SRT: | The rack actuator feedback, measured by the electronic control module (ECM), is greater than the calibrated value. | No action is taken by the ECM. |

![[19a00103.png]]

Rack Actuator Circuit

### Circuit Description

The rack actuator is supplied with a varying current source from the ECM. The rack actuator uses this current to change the position of the control rack, which regulates the amount of fuel delivered from the fuel pump. The rack position feedback sensor relays the actuator rack position back to the ECM.

### Component Location

The rack actuator is an integral part of the RP39 fuel pump.

### Shoptalk

- Confirm that the actuator connector is firmly in place.

- When there is no power to the actuator, the actuator closes and fuel flow stops.

Refer to Troubleshooting Fault Code t05-166
