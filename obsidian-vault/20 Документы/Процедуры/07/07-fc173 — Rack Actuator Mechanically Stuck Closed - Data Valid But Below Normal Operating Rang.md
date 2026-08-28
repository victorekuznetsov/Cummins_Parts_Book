---
aliases:
  - "Привод рейки заклинил в закрытом положении — ниже нормы — умеренный уровень"
type: "Процедура"
doc: "07-fc173"
title_en: "Rack Actuator Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level"
title_ru: "Привод рейки заклинил в закрытом положении — ниже нормы — умеренный уровень"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc173.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc173.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Rack Actuator Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level
**Привод рейки заклинил в закрытом положении — ниже нормы — умеренный уровень**

> [!abstract] Процедура · `07-fc173`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc173.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc173.pdf)

### Fault Code: 173

### Rack Actuator Mechanically Stuck Closed - Data Valid But Below Normal Operating Range - Moderately Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 173 PID(P): S23 SPN: 638 FMI: 18 Lamp: Amber SRT: | Rack actuator mechanically stuck closed - data valid but below normal operating range - moderately severe level. | No action taken by the electronic control module (ECM). |

![[19901354.png]]

Rack Actuator Circuit

### Circuit Description

The fuel control rack and solenoid determine the quantity of fuel metered to the engine.

### Component Location

The fuel control rack and solenoid are integral parts of the P7100 fuel pump

### Shoptalk

- Confirm the actuator connector is firmly in place.

- A defective fuel pump can cause Fault Code 173.

Refer to Troubleshooting Fault Code t05-173
