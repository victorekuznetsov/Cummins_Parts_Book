---
aliases:
  - "Цепь форсунки"
type: "Процедура"
doc: "82-fc312"
title_en: "Injector Circuit"
title_ru: "Цепь форсунки"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc312.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc312.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Injector Circuit
**Цепь форсунки**

> [!abstract] Процедура · `82-fc312`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc312.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc312.pdf)

### Fault Code: 312

### Injector Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 312 PID(P): S005 SPN: 655 FMI: 6/6 Lamp: Yellow SRT: | Current detected at the injector for cylinder No. 5 when the voltage is turned off. | The injector for cylinder No. 5 is turned off. |

![[19200151.png]]

Injector Circuit

### Circuit Description

The injector solenoid valves are actuated by the electronic control module (ECM) to control fuel metering and timing. Each injector solenoid is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the injector from the ECM on the supply wire and returns to the ECM on the return wire after actuating the solenoid. Each solenoid valve is normally open, and it is **only** closed by an electrical pulse from the ECM during fuel injection and metering.

### Component Location

There are two pieces to an ISM/QSM actuator harness - one internal and the other external. The external portion of the actuator harness extends from the connector port in the ECM to the backside of the rocker lever housing. The external harness connects to the internal harness with a 15-pin connector at the backside of the rocker lever housing. The internal actuator harness runs along the inside of the rocker lever housing on the right side. It has six connectors spaced along its length - one for each injector solenoid. These connectors attach to the pigtail connector on each injector.

### Shoptalk

Possible causes for this fault code include low injector solenoid resistance, a short to battery voltage, and a short between injector solenoid wires.

Refer to Troubleshooting Fault Code t05-312
