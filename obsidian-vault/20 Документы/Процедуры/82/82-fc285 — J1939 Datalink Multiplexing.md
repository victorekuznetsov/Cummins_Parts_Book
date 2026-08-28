---
aliases:
  - "Мультиплексирование шины J1939"
type: "Процедура"
doc: "82-fc285"
title_en: "J1939 Datalink Multiplexing"
title_ru: "Мультиплексирование шины J1939"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc285.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc285.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# J1939 Datalink Multiplexing
**Мультиплексирование шины J1939**

> [!abstract] Процедура · `82-fc285`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc285.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc285.pdf)

### Fault Code: 285

### J1939 Datalink Multiplexing

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 285 PID(P): S231 SPN: 639 FMI: 9/9 Lamp: Yellow SRT: | The ECM expected information from a multiplexed device but did **not** receive it soon enough, or did **not** receive it at all. | At least one multiplexed device will **not** operate properly. |

![[19c00340.png]]

J1939 Datalink Multiplexing Circuit

### Circuit Description

Inputs such as throttle pedals, switches, and sensors can be communicated to the ECM over the J1939 datalink. Messages sent from the vehicle electronic control units (VECU) are received by the ECM and used for controlling the engine. Both the ECM and VECU **must** be properly configured so that each device's information is transmitted by the VECU and received by the ECM.

### Component Location

The ECM is located on the intake side of the engine, near the front. The J1939 datalink wiring and VECU(s) vary by OEM options.

### Shoptalk

This fault occurs when the ECM is set up to receive information about a multiplexed device from a VECU over the J1939 datalink and does **not** receive a message with that information. This fault can also be caused if the ECM does **not** get the information fast enough to control the engine properly. This condition can be caused by the following:

- The J1939 datalink having an electrical problem

- A lack of terminating plugs on the J1939 datalink backbone

- The ECM **not** being set up to receive information

- A multiplexed device that truly is **not** multiplexed

- A VECU **not** being correctly set up to transmit information on one of its multiplexed devices.

Refer to Troubleshooting Fault Code t05-285
