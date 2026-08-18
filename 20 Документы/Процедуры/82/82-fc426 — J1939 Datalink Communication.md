---
aliases:
  - "Связь по шине данных J1939"
type: "Процедура"
doc: "82-fc426"
title_en: "J1939 Datalink Communication"
title_ru: "Связь по шине данных J1939"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc426.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc426.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# J1939 Datalink Communication
**Связь по шине данных J1939**

> [!abstract] Процедура · `82-fc426`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc426.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc426.pdf)

### Fault Code: 426

### J1939 Datalink Communication

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 426 PID(P): S231 SPN: 639 FMI: 2/2 Lamp: None SRT: | Communication between the electronic control module (ECM) and another device on the J1939 datalink has been lost. | None on performance. J1939 devices possibly do **not** operate. |

![[19c00340.png]]

J1939 Datalink Circuit

### Circuit Description

Devices such as ABS controllers, autoshift transmissions, ASR systems, electronic displays, electronic information systems, electronic service tools, and VECUs can communicate with the ECM over the J1939 datalink. Messages sent from the devices are received by the ECM and used for controlling the engine. The ECM also transmits information to these devices over the J1939 datalink.

### Component Location

The ECM is located on the intake side of the engine, near the front. The J1939 datalink wiring and the J1939 devices vary by OEM options.

### Shoptalk

This fault occurs whenever the ECM starts communicating with **any** other device using the J1939 datalink and then can no longer transmit on the datalink. Possible causes could be the following: Unplugging an electronic service tool before keying off the ECM, the J1939 datalink having an intermittent electrical problem, the ECM (or another J1939 device) tying up communications by an electrical problem, or by sending too many messages without stopping.

Refer to Troubleshooting Fault Code t05-426
