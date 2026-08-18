---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "82-fc241"
title_en: "Vehicle Speed Sensor Circuit"
title_ru: "Цепь датчика скорости машины"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc241.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc241.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `82-fc241`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc241.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc241.pdf)

### Fault Code: 241

### Vehicle Speed Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 241 PID(P): P084 SPN: 84 FMI: 2/2 Lamp: Yellow SRT: | The ECM lost the vehicle speed signal. | Engine speed limited to Maximum Engine Speed without Vehicle Speed Sensor parameter value. Cruise control, gear-down protection, and road speed governor will **not** work (automotive **only**). |

![[19c00033.png]]

Vehicle Speed Sensor Circuit

### Circuit Description

The vehicle speed sensor (VSS) uses two separate coils of wire to count gear teeth as they pass in front of the sensor. One coil is used by the electronic control module (ECM) to sense vehicle speed. The other coil is sometimes used to send a vehicle speed signal to the speedometer.

### Component Location

The VSS is installed in the rear of the transmission.

### Shoptalk

- Disconnect the vehicle speed sensor connector that connects to the OEM speedometer, or trip recorder, and move the truck. If the fault goes inactive, there is probably electrical noise being fed into the vehicle speed sensor circuit from the OEM device.

- Verify the vehicle speed sensor wires in the OEM harness are twisted pairs.

Refer to Troubleshooting Fault Code t05-241
