---
aliases:
  - "Драйвер электронного управления подачей (EFC) — замыкание на массу"
type: "Процедура"
doc: "01-fc1485"
title_en: "Electronic Fuel Control (EFC) Driver - Grounded Circuit"
title_ru: "Драйвер электронного управления подачей (EFC) — замыкание на массу"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1485.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1485.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Electronic Fuel Control (EFC) Driver - Grounded Circuit
**Драйвер электронного управления подачей (EFC) — замыкание на массу**

> [!abstract] Процедура · `01-fc1485`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1485.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1485.pdf)

### Fault Code: 1485

### Electronic Fuel Control (EFC) Driver - Grounded Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1485 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Electronic fuel control driver diagnostic has detected a grounded circuit condition. | Generator set will shut down. |

![[19802200.png]]

Electronic Fuel Control

### Circuit Description

The engine control module (ECM) checks the electronic fuel control (EFC) driver to make certain it is operating correctly. The ECM uses this fault code to inform the operator that the ECM is no longer driving the electronic fuel control.

The electronic fuel control unit is **only** used on hydromechanical fuel systems. This fault code will **not** be active on any other types (electronic full-authority) fuel systems.

The ECM monitors the voltage (no voltage will trip Fault Code 1486) and can be caused by shorts, a failed voltage regulator, or a failed voltage regulator driver in the ECM.

### Component Location

Reference Section E for location of the electronic fuel control unit.

### Shoptalk

The possible failure modes are short circuit, short to ground, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1485.
