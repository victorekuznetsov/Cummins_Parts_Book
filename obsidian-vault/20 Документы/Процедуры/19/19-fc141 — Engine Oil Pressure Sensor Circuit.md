---
type: "Процедура"
doc: "19-fc141"
title_en: "Engine Oil Pressure Sensor Circuit"
modified: "2026-05-28"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Oil Pressure Sensor Circuit

> [!abstract] Процедура · `19-fc141`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2026-05-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-fc141.pdf)

### Fault Code: 141

### Engine Oil Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 141 PID(P): P100 SPN: 100 FMI: 4 Lamp: Yellow SRT: 00-353 | Less than 0.31-VDC detected at the engine oil pressure sensor signal pin 24 of the engine harness. | No engine protection for oil pressure. Centinel™ system is disabled. |

![[19400133.png]]

Engine Oil Pressure Sensor Circuit

### Circuit Description

The engine oil pressure sensor monitors oil pressure and passes information to the ECM through pin 24 of the engine harness. The ECM monitors the voltage on pin 24 and expects to see the voltage vary between 0.5 and 4.5-VDC during normal engine operation. Voltage below 0.31-VDC on pin 24 will trip Fault Code 141 and can be caused by shorts in the supply, signal, or return wires, an open in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.

### Component Location

The engine oil pressure sensor is located on the engine block to the upper left of the ECM.

### Shoptalk

Possible causes of this fault code include:

- Malfunctioning or damaged engine oil pressure sensor

- Malfunctioning or damaged engine wiring harness

Refer to Troubleshooting Fault Code t05-141
