---
aliases:
  - "Цепь привода перепускного клапана турбины №2"
type: "Процедура"
doc: "82-fc491"
title_en: "Wastegate Actuator Number 2 Circuit"
title_ru: "Цепь привода перепускного клапана турбины №2"
modified: "2012-07-05"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc491.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc491.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Wastegate Actuator Number 2 Circuit
**Цепь привода перепускного клапана турбины №2**

> [!abstract] Процедура · `82-fc491`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-07-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc491.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc491.pdf)

### Fault Code: 491

### Wastegate Actuator Number 2 Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 491 PID(P): S088 SPN: 1189 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the wastegate actuator number 2 circuit when no voltage was being supplied by the engine control module (ECM). | Engine will run derated. |

![[19c00620.png]]

Wastegate Actuator Number 2 Circuit

### Circuit Description

The wastegate actuators are devices used by the ECM to control boost pressure.

### Component Location

The wastegate controller is located on the air inlet horn. Actuator number 2 is the front-most solenoid on the controller.

### Shoptalk

Possible causes of this fault code include:

- A short circuit to voltage source in the harness

- An open circuit in the harness, connector, or wastegate control valve

- Improperly mounted wastegate actuator solenoid.

Refer to Troubleshooting Fault Code t05-491
