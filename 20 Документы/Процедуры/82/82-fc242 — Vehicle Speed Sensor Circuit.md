---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "82-fc242"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc242.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc242.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `82-fc242`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc242.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc242.pdf)

### Fault Code: 242

### Vehicle Speed Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 242 PID(P): P084 SPN: 84 FMI: 10/10 Lamp: Yellow SRT: | Invalid or inappropriate vehicle speed signal detected. Signal indicates an intermittent connection or VSS tampering. | Engine speed limited to maximum engine speed without vehicle speed sensor parameter value. Cruise control, progressive shifting, gear-down protection, and road speed governor will **not** work. |

![[19c00033.png]]

Vehicle Speed Sensor Circuit

### Circuit Description

The vehicle speed sensor (VSS) uses two separate coils of wire to count gear teeth as they pass in front of the sensor. One coil is used by the ECM to sense vehicle speed. The other is sometimes used by the OEM to send a vehicle speed signal to the speedometer.

### Component Location

The vehicle speed sensor is installed in the rear of the transmission.

### Shoptalk

- Verify that the feature settings for VSS Anti-tampering (Fault Code 242), Application Type, and Automatic Transmission are set correctly. If any of these are set incorrectly, Fault Code 242 could occur erroneously.

Note: Driving techniques, such as driving for extended periods of time in lower gears, could log Fault Code 242.

- Fault Code 242 can be logged if the driver attempts to defeat the road speed governor by repeatedly cycling the keyswitch.

- Interview the driver to discover what occurred when the fault code was logged. Explain the driver actions that can cause Fault Code 242 to be logged.

- When deactivating the fault, verify that the vehicle is stopped and the engine is shut down.

- Verify that the keyswitch has been cycled and has remained in the ON position for 30 seconds after the invalid signal has been corrected. This fault will remain active until the keyswitch is cycled and the ECM sees zero vehicle speed and zero engine speed for 30 seconds.

Refer to Troubleshooting Fault Code t05-242
