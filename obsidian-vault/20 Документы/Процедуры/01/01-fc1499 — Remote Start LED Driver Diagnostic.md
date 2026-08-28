---
aliases:
  - "Диагностика драйвера светодиода дистанционного пуска"
type: "Процедура"
doc: "01-fc1499"
title_en: "Remote Start LED Driver Diagnostic"
title_ru: "Диагностика драйвера светодиода дистанционного пуска"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1499.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1499.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Remote Start LED Driver Diagnostic
**Диагностика драйвера светодиода дистанционного пуска**

> [!abstract] Процедура · `01-fc1499`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1499.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1499.pdf)

### Fault Code: 1499

### Remote Start LED Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1499 PID(P): SPN: FMI: Lamp: Warning SRT: | Switch panel Remote Start LED driver diagnostic has detected an error. | The Remote Start LED will **not** function correctly. No action taken by ECM. No loss of performance. |

![[19802924.png]]

Remote Start LED Driver Circuit

### Circuit Description

The ECM checks the Remote Start LED driver to ensure correct operation. The ECM uses the Remote Start lamp to inform the operator if the generator set is in Remote Start mode. The ECM monitors the voltage (no voltage drop will trip Fault Code 1499) caused by short circuits, open circuits, bad LED, or failed Remote Start LED driver in the ECM.

### Component Location

Refer to section E for location of the switch panel and Remote Start lamp.

### Shoptalk

Possible failure modes are open circuits, short to ground, burned - out LED, and loss of supply voltage inside the ECM.

Proper diagnostic lamp operation can be verified by checking to see that the lamps briefly light when the ECM is powered up.

Refer to Troubleshooting Fault Code t05-1499
