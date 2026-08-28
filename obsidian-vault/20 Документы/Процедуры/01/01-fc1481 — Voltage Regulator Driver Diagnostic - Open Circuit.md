---
aliases:
  - "Диагностика драйвера регулятора напряжения — обрыв"
type: "Процедура"
doc: "01-fc1481"
title_en: "Voltage Regulator Driver Diagnostic - Open Circuit"
title_ru: "Диагностика драйвера регулятора напряжения — обрыв"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1481.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1481.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Voltage Regulator Driver Diagnostic - Open Circuit
**Диагностика драйвера регулятора напряжения — обрыв**

> [!abstract] Процедура · `01-fc1481`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1481.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1481.pdf)

### Fault Code: 1481

### Voltage Regulator Driver Diagnostic - Open Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1481 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Voltage regulator driver diagnostic has detected an open circuit condition. | Generator set will shut down. |

![[19802802.png]]

Voltage Regulator Driver Circuit

### Circuit Description

The engine control module (ECM) checks the voltage regulator (VR) driver to make certain it is operating correctly. The ECM uses this fault code to inform the operator that the ECM is no longer driving the voltage regulator.

The ECM monitors the voltage (no voltage will trip Fault Code 1481) and can be caused by shorts, opens, a failed voltage regulator, or a failed voltage regulator driver in the ECM.

### Component Location

Reference Section E for location of the voltage regulator.

### Shoptalk

The possible failure modes are short circuit, open circuit, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1481.
