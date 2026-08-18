---
aliases:
  - "Цепь датчика давления коллектора 2 — замыкание на плюс (правый ряд)"
type: "Процедура"
doc: "01-fc128"
title_en: "Intake Manifold Pressure Sensor 2 Circuit - Shorted High (Right Bank)"
title_ru: "Цепь датчика давления коллектора 2 — замыкание на плюс (правый ряд)"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc128.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc128.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Intake Manifold Pressure Sensor 2 Circuit - Shorted High (Right Bank)
**Цепь датчика давления коллектора 2 — замыкание на плюс (правый ряд)**

> [!abstract] Процедура · `01-fc128`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc128.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc128.pdf)

### Fault Code: 128

### Intake Manifold Pressure Sensor 2 Circuit - Shorted High (Right Bank)

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 128 PID(P): SPN: FMI: Lamp: Warning SRT: | Intake manifold pressure sensor 2 circuit - shorted high (right bank). | No action is taken by the ECM. Possible loss of performance. |

![[19803594.png]]

Intake Manifold Pressure Sensor 2 Circuit

### Circuit Description

The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM). High voltage will trip Fault Code 128 and can be caused by shorts in the supply, signal, or return wires, an open in the return wire, or a failed sensor.

### Component Location

Refer to the Engine Diagrams. 100-002 for the component location.

### Shoptalk

Determine if the engine is being over fueled.

Confirm that the correct Intake Manifold Pressure Sensor part number is being used, and that the correct turbocharger is being used.

If it is suspected that cold intake air can be the cause of the high intake manifold pressure, test the engine while feeding it warm intake air.

Inspect the intake manifold pressure sensor circuit for signs of tampering. Remove any extra wires from the circuit.

Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

Note: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-128
