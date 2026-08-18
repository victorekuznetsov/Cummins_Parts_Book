---
aliases:
  - "Цепь исполнительного механизма гильзы"
type: "Процедура"
doc: "87-fc113"
title_en: "Sleeve Actuator Circuit"
title_ru: "Цепь исполнительного механизма гильзы"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Sleeve Actuator Circuit
**Цепь исполнительного механизма гильзы**

> [!abstract] Процедура · `87-fc113`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc113.pdf)

### Fault Code: 113

### Sleeve Actuator Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 113 PID(P): S020 SPN: 635 FMI: 3 Lamp: Yellow SRT: | More than 6.2 amps detected at timing sleeve actuator circuit pin 6 of the engine harness. | No action by the electronic control module (ECM) is taken. The engine can have low-power outputs, loud combustion noise, and produce black smoke. |

![[19a00103.png]]

Sleeve Actuator Circuit

### Circuit Description

The sleeve actuator circuit is used to control the start of injection through pin 6 of the engine harness. The ECM monitors the current on pin 6 and expects to see the amperage vary between 1.0 and 6.2 amps during normal engine operation. Amperage above 6.2 amps on pin 6 will trip Fault Code 113.

### Component Location

The sleeve actuator circuit is an integral part of the RP39 fuel pump.

### Shoptalk

This fault can be caused by an internal ECM problem or an alternate power source. There are no repairs possible for the module in the field.

Refer to Troubleshooting Fault Code t05-113
