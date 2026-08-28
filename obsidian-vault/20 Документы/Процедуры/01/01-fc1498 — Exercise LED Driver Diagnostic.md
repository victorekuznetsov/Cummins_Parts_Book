---
aliases:
  - "Диагностика драйвера светодиода контрольной наработки"
type: "Процедура"
doc: "01-fc1498"
title_en: "Exercise LED Driver Diagnostic"
title_ru: "Диагностика драйвера светодиода контрольной наработки"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1498.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1498.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Exercise LED Driver Diagnostic
**Диагностика драйвера светодиода контрольной наработки**

> [!abstract] Процедура · `01-fc1498`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1498.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1498.pdf)

### Fault Code: 1498

### Exercise LED Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1498 PID(P): SPN: FMI: Lamp: Warning SRT: | Switch panel Exercise LED driver diagnostic has detected an error. | The Exercise LED will **not** function correctly. No action taken by ECM. No loss of performance. |

![[19802923.png]]

Exercise LED Driver Circuit

### Circuit Description

The ECM checks the Exercise LED driver to ensure correct operation. The ECM uses Exercise lamp to inform the operator if the generator set is in exercise mode.

### Component Location

Refer to section E for location of the switch panel, and Exercise lamp.

### Shoptalk

Possible failure modes are open circuits, short to ground, burned-out LED, and loss of supply voltage inside the ECM.

Proper diagnostic lamp operation can be verified by checking to see that the lamps briefly light when the ECM is powered up.

Refer to Troubleshooting Fault Code t05-1498
