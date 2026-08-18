---
aliases:
  - "Ошибка конфигурации"
type: "Процедура"
doc: "01-fc1413"
title_en: "Configuration Error"
title_ru: "Ошибка конфигурации"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1413.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1413.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Configuration Error
**Ошибка конфигурации**

> [!abstract] Процедура · `01-fc1413`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1413.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1413.pdf)

### Fault Code: 1413

### Configuration Error

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1413 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Configuration error has been detected. | Engine will **not** start. |

![[19802494.png]]

GCS ECM

### Circuit Description

The ECM checks to see what other components are installed at power-up, and if the list of installed components does **not** match the calibration, then the ECM will trip Fault Code 1413, Configuration Error.

### Component Location

Refer to the OEM manual for location of the ECM.

### Shoptalk

Verify that the correct calibration is loaded in the ECM. If it continues replace the ECM.

Refer to Troubleshooting Fault Code t05-1413
