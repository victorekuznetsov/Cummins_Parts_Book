---
type: "Процедура"
doc: "19-fc132"
title_en: "Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever"
modified: "2011-03-01"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc132.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc132.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever

> [!abstract] Процедура · `19-fc132`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc132.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc132.pdf)

### Fault Code: 132

### Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 132 PID(P): P91 SPN: 091 FMI: 4 Lamp: Red SRT: 00-351 | Less than 0.13 VDC detected at the accelerator pedal or lever position signal pin 29 of the OEM interface harness ECM connector. | Calibration-dependent power and speed derate. |

![[19400817.png]]

Accelerator Position Sensor: CELECT™-Type Accelerator Pedal or Lever

### Circuit Description

The accelerator pedal or lever provides the operator's accelerator pedal or lever command to the ECM through the OEM harness and OEM interface harness. The ECM uses this signal to determine the fueling command for the fuel rail actuator valve.

### Component Location

The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.

### Shoptalk

The accelerator pedal or lever position sensor is a potentiometer. The resistance specifications of the accelerator pedal or lever position sensor are the following:

- Between the supply and the return = 2000 to 3000 ohms

- Between the supply and the signal: Released = 1500 to 3000 ohms. Depressed = 200 to 1500 ohms.

Note: If the accelerator pedal or lever or accelerator pedal or lever position sensor is changed, or after a calibration download, cycle the accelerator pedal or lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal or lever with the ECM.

Refer to Troubleshooting Fault Code t05-132
