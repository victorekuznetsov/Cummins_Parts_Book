---
aliases:
  - "Цепь датчика дистанционного органа подачи — замыкание на массу"
type: "Процедура"
doc: "07-fc134"
title_en: "Remote Throttle Position Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика дистанционного органа подачи — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc134.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc134.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Remote Throttle Position Sensor Circuit - Shorted Low
**Цепь датчика дистанционного органа подачи — замыкание на массу**

> [!abstract] Процедура · `07-fc134`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc134.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc134.pdf)

### Fault Code: 134

### Remote Throttle Position Sensor Circuit - Shorted Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 134 PID(P): P029 SPN: 91 FMI: 4 Lamp: Red SRT: | Backup throttle position sensor shorted low. | None on performance if remote throttle is **not** used. |

![[19901355.png]]

Remote Throttle Position Sensor Circuit

### Circuit Description

The remote accelerator pedal/lever provides a second accelerator command to the electronic control module (ECM) through the marine OEM harness and the main extension harness. The ECM uses this signal in place of the primary accelerator pedal/lever to determine the fueling command for the P7100 fuel pump rack.

### Component Location

Reference Section E for a detailed component location view. The remove accelerator pedal/lever location varies with each OEM.

### Shoptalk

The accelerator pedal/lever position sensor is a potentiometer. The resistance specifications of the accelerator pedal/lever position sensor are as follows:

- Between supply and return = 2000 to 3000 ohms

- Between supply and signal:Released = 1500 to 3000 ohmsDepressed = 200 to 1500 ohms

If the accelerator pedal/lever or accelerator pedal/lever position sensor is changed, or after a calibration download, cycle the accelerator pedal/lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal/lever with the ECM.

Refer to Troubleshooting Fault Code t05-134
