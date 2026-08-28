---
aliases:
  - "Плата сети LonWorks — отсутствует"
type: "Процедура"
doc: "01-fc1351"
title_en: "LonWorks Network Board - Missing"
title_ru: "Плата сети LonWorks — отсутствует"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1351.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1351.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# LonWorks Network Board - Missing
**Плата сети LonWorks — отсутствует**

> [!abstract] Процедура · `01-fc1351`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1351.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1351.pdf)

### Fault Code: 1351

### LonWorks Network Board - Missing

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1351 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The LonWorks Network board is missing. | The generator set will **not** be able to communicate with other devices on the LonWorks Network. |

![[19802792.png]]

Generator Set ECM LonWorks Network Board

### Circuit Description

Once the software has been loaded into the ECM, the software will do a hardware check to make sure that all necessary cards are installed for the application.

This fault code is used by the ECM to tell the operator that the LonWorks Network board (slot 4) is missing.

### Component Location

Refer to Section E for location of the ECM card cage and the LonWorks Network board (slot 4).

### Shoptalk

The possible failure mode is that the LonWorks Network board has lost its independent power supply.

Refer to Troubleshooting Fault Code t05-1351
