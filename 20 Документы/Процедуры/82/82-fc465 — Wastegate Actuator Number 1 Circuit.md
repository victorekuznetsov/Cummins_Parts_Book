---
aliases:
  - "Цепь привода перепускного клапана турбины №1"
type: "Процедура"
doc: "82-fc465"
title_en: "Wastegate Actuator Number 1 Circuit"
title_ru: "Цепь привода перепускного клапана турбины №1"
modified: "2012-07-05"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc465.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc465.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Wastegate Actuator Number 1 Circuit
**Цепь привода перепускного клапана турбины №1**

> [!abstract] Процедура · `82-fc465`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-07-05
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc465.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc465.pdf)

### Fault Code: 465

### Wastegate Actuator Number 1 Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 465 PID(P): S032 SPN: 1188 FMI: 3/3 Lamp: Yellow SRT: | High voltage detected at the wastegate actuator number 1 circuit when no voltage was being supplied by the engine control module (ECM). | Engine will run derated. |

![[19c00361.png]]

Wastegate Actuator number 1 Circuit

### Circuit Description

The wastegate actuators are devices used by the ECM to control boost pressure.

### Component Location

The wastegate controller is located on the air inlet horn. Actuator number 1 is the rear-most solenoid on the controller.

### Shoptalk

Possible causes of this fault code include:

- A short circuit to voltage source in the harness

- An open circuit in the harness, connector, or wastegate control valve

- Improperly mounted wastegate actuator solenoid.

Refer to Troubleshooting Fault Code t05-465
