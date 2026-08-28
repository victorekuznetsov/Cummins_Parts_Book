---
aliases:
  - "Цепь реле шины зажигания"
type: "Процедура"
doc: "82-fc338"
title_en: "Ignition Bus Relay Circuit"
title_ru: "Цепь реле шины зажигания"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc338.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc338.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Ignition Bus Relay Circuit
**Цепь реле шины зажигания**

> [!abstract] Процедура · `82-fc338`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc338.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc338.pdf)

### Fault Code: 338

### Ignition Bus Relay Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 338 PID(P): S087, 3 SPN: 1267 FMI: 3 Lamp: Yellow SRT: | High voltage detected at the ignition bus relay output circuit (ignition relay positive (+)) when low voltage was expected by the ECM. | The ICON™ will be disabled. **Only** mandatory shutdown will be enabled. Engine can be started normally. No power to the keyswitch ignition circuit. |

![[19803215.png]]

Idle Shutdown Vehicle Accessory/Ignition Bus Relay Circuit

### Circuit Description

The ignition bus relay controls ignition circuits powering the heating/air conditioning controls and other equipment connected to the ignition bus relay(s) (optional second relay can be installed for additional accessories). This relay(s) is controlled by ignition relay positive (+) signal from the ECM OEM 50-pin connector pin 35.

### Component Location

The ignition bus relay is located under the dash inside the vehicle cab.

### Shoptalk

This fault typically indicates a short circuit from the ignition relay positive (+) output of battery voltage. Ignition relay (+) pin outputs 12 VDC to open the ignition bus relay(s) when ICON™ has powered the vehicle down and needs to disconnect power going to the cab circuits. The ignition bus relay(s) is normally closed when no power is applied.

Refer to Troubleshooting Fault Code t05-338
