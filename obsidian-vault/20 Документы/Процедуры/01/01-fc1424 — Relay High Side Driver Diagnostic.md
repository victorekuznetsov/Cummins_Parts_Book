---
aliases:
  - "Диагностика верхнего ключа драйвера реле"
type: "Процедура"
doc: "01-fc1424"
title_en: "Relay High Side Driver Diagnostic"
title_ru: "Диагностика верхнего ключа драйвера реле"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1424.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1424.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Relay High Side Driver Diagnostic
**Диагностика верхнего ключа драйвера реле**

> [!abstract] Процедура · `01-fc1424`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1424.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1424.pdf)

### Fault Code: 1424

### Relay High Side Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1424 PID(P): SPN: FMI: Lamp: Warning SRT: | Relay high side driver diagnostic has detected an error. | The user interface relay drivers will **not** function correctly. No action is taken by the ECM. No loss of performance. |

![[19802500.png]]

Relay High Side Driver Circuit

### Circuit Description

The relay driver supply pin supplies power for all of the user interface relay drivers. The ECM monitors the voltage, no voltage/low voltage will trip Fault Code 1424, and can be caused by shorts, opens, or a failed driver in the ECM.

### Component Location

Refer to the OEM manual for location of the ECM. Refer to the OEM manual for location of the user interface panel.

### Shoptalk

The possible failure modes are open circuit, short to ground, and loss of supply voltage inside the ECM.

Refer to Troubleshooting Fault Code t05-1424
