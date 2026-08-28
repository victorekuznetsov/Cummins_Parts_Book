---
aliases:
  - "Диагностика драйвера светодиода «Не в авторежиме»"
type: "Процедура"
doc: "01-fc1487"
title_en: "Not in Auto LED Driver Diagnostic"
title_ru: "Диагностика драйвера светодиода «Не в авторежиме»"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1487.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1487.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Not in Auto LED Driver Diagnostic
**Диагностика драйвера светодиода «Не в авторежиме»**

> [!abstract] Процедура · `01-fc1487`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1487.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1487.pdf)

### Fault Code: 1487

### Not in Auto LED Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1487 PID(P): SPN: FMI: Lamp: Warning SRT: | Switch panel **Not** in Auto LED driver diagnostic has detected an error. | The **Not** in Auto LED will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802913.png]]

Not in Auto LED Driver Circuit

### Circuit Description

The ECM checks the **Not** in Auto LED driver to make certain it is operating correctly. The ECM uses the **Not** in Auto lamp to inform the operator that the generator set is **not** in manual mode but rather it is currently in auto (remote start enabled) mode.

The ECM monitors the voltage (no voltage drop will trip Fault Code 1487) and can be caused by shorts, opens, bad bulbs, or a failed **Not** in Auto LED driver in the ECM.

### Component Location

Refer to section E for location of the switch panel and the **Not** in Auto lamp.

### Shoptalk

The possible failure modes are open circuit, short to ground, burned-out bulb, and loss of supply voltage inside the ECM.

Proper diagnostic lamp operation can be verified by checking to see that the lamps briefly light when the ECM is powered up.

Refer to Troubleshooting Fault Code t05-1487
