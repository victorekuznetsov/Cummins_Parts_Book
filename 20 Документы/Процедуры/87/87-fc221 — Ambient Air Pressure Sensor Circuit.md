---
aliases:
  - "Цепь датчика атмосферного давления"
type: "Процедура"
doc: "87-fc221"
title_en: "Ambient Air Pressure Sensor Circuit"
title_ru: "Цепь датчика атмосферного давления"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc221.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc221.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Ambient Air Pressure Sensor Circuit
**Цепь датчика атмосферного давления**

> [!abstract] Процедура · `87-fc221`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc221.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc221.pdf)

### Fault Code: 221

### Ambient Air Pressure Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 221 PID(P): P108 SPN: 108 FMI: 3 Lamp: Yellow SRT: | More than 4.69 VDC detected at the ambient air pressure sensor signal pin 32 of the engine harness. | No action is taken by the electronic control module (ECM). |

![[19a00125.png]]

Ambient Air Pressure Sensor Circuit

### Circuit Description

The ambient air pressure sensor provides the ambient air pressure signal to the ECM, through the engine harness. The ECM uses the ambient air pressure sensor to adjust fueling based on the altitude.

### Component Location

The ambient air pressure sensor is located on the left-hand side of the engine, on the ECM bracket.

### Shoptalk

Monitor the ambient air pressure reading with an electronic service tool to confirm that the pressure reading matches the actual air pressure.

Refer to Troubleshooting Fault Code t05-221
