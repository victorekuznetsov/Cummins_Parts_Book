---
aliases:
  - "Цепь термостата кабины ICON™"
type: "Процедура"
doc: "82-fc469"
title_en: "ICON™ Cab Thermostat Circuit"
title_ru: "Цепь термостата кабины ICON™"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc469.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc469.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# ICON™ Cab Thermostat Circuit
**Цепь термостата кабины ICON™**

> [!abstract] Процедура · `82-fc469`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc469.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc469.pdf)

### Fault Code: 469

### ICON™ Cab Thermostat Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 469 PID(P): S215 SPN: FMI: 2/2 Lamp: None SRT: | The ICON™ cab thermostat has logged a fault (E3 on the cab thermostat), or the cab thermostat signal to the ECM is lost. | E3 will cycle the engine between 20 minutes run and 15 minutes off or until the desired set-point is reached. (This is a selectable response of the E3 fault in the thermostat trim table.) The ICON™ system will **not** be disabled. Engine mode will remain active. |

![[19803218.png]]

ICON™ Cab Thermostat Circuit

### Circuit Description

The cab thermostat is used to control the cab temperature, either for heating or cooling. It is required for cab comfort mode operation. The thermostat communicates with the ECM to command when to autostart the engine to maintain cab temperature. Also, the thermostat is connected to the keyswitch to detect when the ignition is turned on.

### Component Location

The cab thermostat is mounted in the bunk area, on the wall above the bed.

### Shoptalk

E3 is an indication that one of the following has occurred: (1) Engine has run for more than 60 minutes, and cool or heat set point is **not** achieved, and external ambient temperature is within -18° to 43°C \[0 to 110°F\] (thermostat-adjustable trim 01 and 02, see thermostat trim table in the ICON™ Operation and Maintenance Manual, Bulletin [[3666422 — ICON™ Idle Control System\|3666422]]); (2) a cab thermostat request to start the engine has been requested four times in one hour, and the ambient temperature is within -18° to 43°C \[0 to 110°F\]. E3 can indicate potential tampering of the thermostat. For example, the operator has chosen cool mode but turned the heater on or opened the windows. The air-conditioning system will attempt to cool the truck below the cool set point for 60 minutes. At this time, an E3 fault (Fault Code 469) will be logged. A similar situation can occur for heat mode. Once an E3 is displayed on the thermostat, the engine will cycle on for 20 minutes and off for 15 minutes. If the desired temperature set-point is reached in the tamper mode operation (20 minutes on and 15 minutes off), it will return to normal cab mode operation. To clear E3, disable ICON™, key off for approximately 30 seconds, and then reactivate ICON™.

Note: The thermostat fault E1 (cab temperature sensor), E2 (external ambient air temperature sensor), and E3 (tamper mode) do **not** flash out on the ICON™ lamp, but merely display on the thermostat display screen. INSITE™ electronic service tool will log an active Fault Code 469 until cleared. Refer to the Cab Thermostat Displays a Fault Code troubleshooting symptom tree in Section TS. Investigate the related fault codes that also can possibly be active.

Refer to Troubleshooting Fault Code t05-469
