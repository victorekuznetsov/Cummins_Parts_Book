---
type: "Процедура"
doc: "19-fc432"
title_en: "CELECT™-Type Accelerator Pedal or Lever"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc432.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc432.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# CELECT™-Type Accelerator Pedal or Lever

> [!abstract] Процедура · `19-fc432`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2011-03-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc432.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc432.pdf)

### Fault Code: 432

### CELECT™-Type Accelerator Pedal or Lever

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 432 PID(P): P91 SPN: 091 FMI: 13 Lamp: Red SRT: 00-371 | Voltage detected at the idle validation on idle signal pin 13 of the OEM harness when voltage at accelerator position signal pin 29 of the OEM harness indicates pedal is **not** at idle or voltage detected at idle validation off-idle signal pin 12 of the OEM harness when voltage at accelerator position signal pin 29 of the OEM harness indicates pedal is at rest. | Engine will default to 0-percent accelerator. |

![[19400175.png]]

CELECT™-Type Accelerator Pedal or Lever

### Circuit Description

The accelerator pedal or lever provides the driver's accelerator command to the ECM through the OEM harness and the OEM interface harness. The ECM uses this signal to determine the fueling command for the fuel rail actuator valve.

### Component Location

The accelerator pedal or lever location varies with each OEM. Refer to the OEM manual.

### Shoptalk

- This fault code is usually caused by the improper wiring of the accelerator circuit, the idle validation circuit, or the OEM harness.

Note: If the accelerator or accelerator position sensor is changed or after a calibration download, cycle the accelerator pedal or lever (turn keyswitch ON) through its complete travel three times. This procedure calibrates the new accelerator pedal or lever with the ECM.

Refer to Troubleshooting Fault Code t05-432
