---
aliases:
  - "Новый датчик-реле частоты вращения"
type: "Инструкция по установке"
doc: "4907733"
title_en: "New Speed Switch"
title_ru: "Новый датчик-реле частоты вращения"
released: "2007-09-09"
modified: "2009-11-18"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/install_inst/4907733.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/install_inst/4907733.pdf"
tags:
  - "документ/установка"
  - "двигатель/C8.3"
---

# New Speed Switch
**Новый датчик-реле частоты вращения**

> [!abstract] Инструкция по установке · `4907733`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Даты:** выпущен 2007-09-09 · изменён 2009-11-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/install_inst/4907733.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/install_inst/4907733.pdf)

## New Speed Switch

### Purpose

This installation instruction provides general information and documents the conversion of AMBAC International SWA675A1 to SWA675D1. Both parts were released in the Cummins Inc. parts system under Part Number 3050323.

General Information

The SWA675D1 speed switch is designed to monitor the speed of an engine or piece of rotating machinery by detecting the pulses from a magnetic pick-up device.

The module can be set to operate the independent relays at different speed settings. Either relay can be adjusted to operate from between 10 to 140 percent of the engine rate running speed.

This flexibility allows the module to be used for many different applications, including underspeed or overspeed protection or crank disconnect facilities.

Adjustment

Adjustment of the trip points is done using two preset potentiometers. Turning **clockwise** increases the appropriate trip point and turning **counterclockwise** decreases the appropriate trip point. The appropriate LED will be illuminated to indicate that the trip has been activated.

On application of a continuous DC supply voltage, the module will start counting pulses from the magnetic pick-up. If these pulses exceed the preset rpm levels, the trips will be activated and the relay contacts will change state.

A latch is provided to prevent the release of the relays. This speed switch can be made to be automatically latched and disabled by applying a continuous negative signal to terminal 5.

The SWA675D1 will allow a remote key or toggle switch reset function by simply connecting terminal 2 and terminal 5 and placing the switch in the desired location.

Meter calibration is done using a preset potentiometer, which enables the meter output to be scaled to match the optional rpm meter. Rotating the preset potentiometer **clockwise** increases the meter reading.

| Conversion from Model SWA675A1 to SWA675D1 |  |  |
|---|---|---|
|  | SWA675A1 | SWA675D1 |
| Function | Pins | Pins |
| Magnetic Pick-up (+) | 1 | 3 |
| Magnetic Pick-up (-) | 2 | 4 |
| Battery (+) | 4 | 1 |
| Battery (-) | 3 | 2 |
| Tachometer out (+) | 5 | 6 |
| Tachometer out (-) | 3 | 2 |
| Crank | 6 | 7 |
| Crank | 7 | 8 |
| Crank | 8 | 9 |
| Jump | N/A | 2 + 5 |
| **Not** used | 9 | N/A |
| **Not** used | 10 | N/A |
| **Not** used | 11 | N/A |
| Overspeed | 12 | 10 |
| Overspeed | 13 | 11 |
| Overspeed | 14 | 12 |

> [!warning] CAUTION · Осторожно
> When replacing the old unit with the new unit, if the speed switch is used in conjunction with a control panel and that control panel has a manual reset button, it is very important that the reset button is disabled. The new SWA675D1 has an automatic latching reset feature, terminal 5 must be connected to terminal 2 to engage the feature. This allows the latch to reset while stopping or when the power drops.

![[19901541.png]]

Model SWA675A1

![[19901542.png]]

Model SWA675D1

![[19901543.png]]

Model SWA675D1 - Wiring Diagram
