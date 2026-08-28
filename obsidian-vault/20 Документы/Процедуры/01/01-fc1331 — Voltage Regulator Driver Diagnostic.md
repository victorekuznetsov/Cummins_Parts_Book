---
aliases:
  - "Диагностика драйвера регулятора напряжения"
type: "Процедура"
doc: "01-fc1331"
title_en: "Voltage Regulator Driver Diagnostic"
title_ru: "Диагностика драйвера регулятора напряжения"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1331.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1331.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Voltage Regulator Driver Diagnostic
**Диагностика драйвера регулятора напряжения**

> [!abstract] Процедура · `01-fc1331`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1331.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1331.pdf)

### Fault Code: 1331

### Voltage Regulator Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1331 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The voltage regulator driver diagnostic has detected a short circuit condition. | Generator set will shut down. |

![[19802802.png]]

Voltage Regulator Driver Circuit

### Circuit Description

The ECM checks the voltage regulator driver to make certain it is operating correctly. The ECM uses fault code to inform the operator that the ECM is no longer driving the voltage regulator.

The ECM monitors the voltage (no voltage will trip Fault Code 1331) and can be caused by short circuits, failed voltage regulator, or a voltage regulator driver in the ECM.

### Component Location

Refer to Section E for location of the voltage regulator.

### Shoptalk

The possible failure modes are short circuit, short to ground, and loss of voltage inside the ECM.

The voltage regulator pulse width modulated circuit is either shorted high or low. The voltage regulator pulse width modulated driver is shorted itself or is driving into a shorted circuit.

The voltage regulator driver is on the base board. If the driver itself is bad, the base board **must** be replaced.

Refer to Troubleshooting Fault Code t05-1331
