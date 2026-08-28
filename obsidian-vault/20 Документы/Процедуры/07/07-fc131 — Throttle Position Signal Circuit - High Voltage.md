---
aliases:
  - "Цепь сигнала положения органа подачи — высокое напряжение"
type: "Процедура"
doc: "07-fc131"
title_en: "Throttle Position Signal Circuit - High Voltage"
title_ru: "Цепь сигнала положения органа подачи — высокое напряжение"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Throttle Position Signal Circuit - High Voltage
**Цепь сигнала положения органа подачи — высокое напряжение**

> [!abstract] Процедура · `07-fc131`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc131.pdf)

### Fault Code: 131

### Throttle Position Signal Circuit - High Voltage

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 131 PID(P): P091 SPN: 91 FMI: 3 Lamp: Red SRT: | High voltage detected at the throttle position signal circuit. | Severe derate (power and speed). Limp home power **only**. |

![[19901356.png]]

Throttle Position Signal Circuit

### Circuit Description

The accelerator pedal/lever provides the driver's accelerator command to the electronic control module (ECM) through the marine OEM harness and the throttle extension harness. The ECM uses this signal to determine the fueling command for the P7100 fuel pump rack.

### Component Location

Reference Section E for a detailed component location view. The accelerator pedal/lever location varies with each OEM.

### Shoptalk

The accelerator pedal/lever position sensor is a potentiometer. The resistance specifications of the accelerator pedal/lever position sensor are as follows:

- Between supply and return = 2000 to 3000 ohms

- Between supply and signal:Released = 1500 to 3000 ohmsDepressed = 200 to 1500 ohms

If the accelerator pedal/lever or accelerator pedal/lever position sensor is changed, or after a calibration download, cycle the accelerator pedal/lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal/lever with the ECM.

Refer to Troubleshooting Fault Code t05-131
