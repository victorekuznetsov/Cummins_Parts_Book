---
aliases:
  - "Цепь датчика давления масла — замыкание на массу"
type: "Процедура"
doc: "01-fc141"
title_en: "Engine Oil Pressure Sensor Circuit - Shorted Low"
title_ru: "Цепь датчика давления масла — замыкание на массу"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc141.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc141.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Oil Pressure Sensor Circuit - Shorted Low
**Цепь датчика давления масла — замыкание на массу**

> [!abstract] Процедура · `01-fc141`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc141.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc141.pdf)

### Fault Code: 141

### Engine Oil Pressure Sensor Circuit - Shorted Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 141 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine oil pressure sensor circuit - shorted low. | No engine protection for oil pressure. |

![[19803594.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure sensor monitors oil pressure and passes information to the electronic control module (ECM). The ECM monitors the voltage on the oil pressure signal pin and expects to see the voltage vary between 0.46 and 4.56 VDC during normal engine operation. Low voltage will trip Fault Code 141 and can be caused by shorts in the supply, signal, or return wires, an open in the supply or signal wires, low supply voltage from the ECM, or a failed sensor.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

If Fault Code 143 or 415 is **not** present, the problem is **not** base engine related.

Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-141
