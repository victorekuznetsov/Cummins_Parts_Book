---
aliases:
  - "Цепь электромагнита форсунки цилиндра 3 — ток ниже нормы или обрыв"
type: "Процедура"
doc: "82-fc324"
title_en: "Injector Solenoid Driver Cylinder 3 Circuit - Current Below Normal, or Open Circuit"
title_ru: "Цепь электромагнита форсунки цилиндра 3 — ток ниже нормы или обрыв"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc324.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc324.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Injector Solenoid Driver Cylinder 3 Circuit - Current Below Normal, or Open Circuit
**Цепь электромагнита форсунки цилиндра 3 — ток ниже нормы или обрыв**

> [!abstract] Процедура · `82-fc324`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc324.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc324.pdf)

### Fault Code: 324

### Injector Solenoid Driver Cylinder 3 Circuit - Current Below Normal, or Open Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 324 PID(P): S006 SPN: 656 FMI: 5/5 Lamp: Amber SRT: | Injector Solenoid Driver Cylinder 3 Circuit - Current Below Normal, or Open Circuit. Current detected at injector number 3 when voltage is turned off. | The current to the injector is shut off. The engine can possibly misfire or run rough. |

![[19200153.png]]

Injector Solenoid Driver Cylinder 3 Circuit

### Circuit Description

The injector solenoid valves are actuated by the electronic control module (ECM) to control fuel metering and timing. Each injector solenoid is connected to the ECM by a supply and a return wire. An electrical pulse is sent to the injector from the ECM on the supply wire and it returns on the return wire after actuating the solenoid. Each solenoid valve is normally open, and it is **only** closed by an electrical pulse from the ECM during fuel injection and metering. The solenoid resistance specification is between 0.5 and 1.5 ohms.

### Component Location

The ISM has an internal actuator harness that connects to the external engine harness with a 15-pin connector at the front side of the rocker lever housing. The internal actuator harness is located on the inside of the rocker lever housing on the exhaust side. It has six connectors spaced along its length - one for each injector solenoid. These connectors attach to the pigtail connector on each injector.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the engine speed is greater than 0 rpm.

### Conditions For Setting The Fault Codes

The ECM detects that the injector circuit is shorted to ground, high injector solenoid resistance, or open circuit.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE light immediately when the diagnostic runs and fails.

- The injector will be disabled.

### Conditions For Clearing The Fault Code

The ECM will turn off the amber CHECK ENGINE light immediately after the diagnostic runs and passes.

### Shoptalk

Possible causes for this fault code include:

- Open circuit in the engine harness, connectors, or actuator

- Short circuit to ground in the engine harness or injector

- High resistance in the injector.

Refer to Troubleshooting Fault Code t05-324
