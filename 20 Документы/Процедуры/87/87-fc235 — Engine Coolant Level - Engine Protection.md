---
aliases:
  - "Уровень охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "87-fc235"
title_en: "Engine Coolant Level - Engine Protection"
title_ru: "Уровень охлаждающей жидкости — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc235.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc235.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Coolant Level - Engine Protection
**Уровень охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `87-fc235`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc235.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc235.pdf)

### Fault Code: 235

### Engine Coolant Level - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 235 PID(P): P111 SPN: 111 FMI: 1 Lamp: Engine Protection SRT: | Low coolant level has been detected. Voltage signal on the coolant level signal pin 37 of the engine harness indicates low radiator coolant level on the vehicle. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |

![[19a00217.png]]

Coolant Level Sensor Circuit

### Circuit Description

The coolant level sensor monitors the coolant level within the coolant system and passes information to the electronic control module (ECM) through the engine harness.

### Component Location

The coolant level sensor is located in the radiator top tank or surge tank.

### Shoptalk

This is an OEM-supplied component and will vary in sensor location.

- When the coolant level drops below a certain level, a power derate, speed derate, or shutdown will be activated.

- If a shorting plug is used in the coolant level circuit, verify that it is wired correctly.

- Inspect the wiring harness between the 4-pin Weather-Pack connector and the coolant level sensor for damage.

- Make sure the coolant level sensor is located in the middle of the tank rather than off to one side where the coolant level can change when the vehicle turns a corner.

Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

Refer to Troubleshooting Fault Code t05-235
