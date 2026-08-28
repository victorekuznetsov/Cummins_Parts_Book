---
aliases:
  - "Диагностика драйвера реле автоматического режима"
type: "Процедура"
doc: "01-fc1496"
title_en: "Auto Mode Output Relay Driver Diagnostic"
title_ru: "Диагностика драйвера реле автоматического режима"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1496.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1496.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Auto Mode Output Relay Driver Diagnostic
**Диагностика драйвера реле автоматического режима**

> [!abstract] Процедура · `01-fc1496`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1496.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1496.pdf)

### Fault Code: 1496

### Auto Mode Output Relay Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1496 PID(P): SPN: FMI: Lamp: Warning SRT: | The Auto Mode output relay driver diagnostic has detected an error. | Any customer features dependent on Auto Mode output will **not** function correctly. No action taken by ECM. No loss of performance. |

![[19802921.png]]

Auto Mode Output Relay Driver Circuit

### Circuit Description

The ECM checks the Auto Mode output relay driver to ensure correct operation. The ECM uses the Auto Mode output to inform any customer/features dependent on the ECM for knowledge of when the generator set is running.The ECM monitors the voltage (no voltage increase will trip Fault Code 1496) caused by short circuits, open circuits, or failed Auto Mode output relay driver in the ECM.

### Component Location

Refer to Section E for location of the output Auto Mode.

### Shoptalk

When the control is in auto mode, the circuit will provide B positive (+) voltage. When the control is **not** in auto mode, the circuit will be open. Possible failure modes are short circuits, short to ground, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1496
