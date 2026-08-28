---
aliases:
  - "Датчик положения рейки показывает значение выше калибровочного порога"
type: "Процедура"
doc: "07-fc166"
title_en: "Rack Position Sensor Indicates Rack Position Greater than Calibrated Threshold"
title_ru: "Датчик положения рейки показывает значение выше калибровочного порога"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc166.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc166.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Rack Position Sensor Indicates Rack Position Greater than Calibrated Threshold
**Датчик положения рейки показывает значение выше калибровочного порога**

> [!abstract] Процедура · `07-fc166`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc166.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc166.pdf)

### Fault Code: 166

### Rack Position Sensor Indicates Rack Position Greater than Calibrated Threshold

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 166 PID(P): S24 SPN: 733 FMI: 3 Lamp: Amber SRT: | The rack position sensor indicates the rack position is greater than the calibrated threshold. | No action taken by the electronic control module (ECM). |

![[19901354.png]]

Rack Actuator Circuit

### Circuit Description

The rack actuator is supplied with a varying current source from the ECM. The rack actuator uses this current to change the position of the control rack, which regulates the amount of fuel delivered from the fuel pump. The rack position feedback sensor relays the actuator rack position back to the ECM.

### Component Location

The rack actuator is an integral part of the P7100 fuel pump

### Shoptalk

- Confirm the actuator connector is firmly in place.

- When there is no power to the actuator, the actuator closes and fuel flow stops.

Refer to Troubleshooting Fault Code t05-166
