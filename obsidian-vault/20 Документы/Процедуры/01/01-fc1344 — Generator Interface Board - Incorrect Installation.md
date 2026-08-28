---
aliases:
  - "Интерфейсная плата генератора — неверная установка"
type: "Процедура"
doc: "01-fc1344"
title_en: "Generator Interface Board - Incorrect Installation"
title_ru: "Интерфейсная плата генератора — неверная установка"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1344.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1344.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator Interface Board - Incorrect Installation
**Интерфейсная плата генератора — неверная установка**

> [!abstract] Процедура · `01-fc1344`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1344.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1344.pdf)

### Fault Code: 1344

### Generator Interface Board - Incorrect Installation

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1344 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The generator interface board(slot 2) is missing or has **not** been installed correctly. | Engine will **not** start. |

![[19802790.png]]

Generator Set ECM Generator Interface Board

### Circuit Description

Once the software has been loaded into the ECM, the software will do a hardware check to make sure that all necessary cards are installed for the application.

This fault code is used by the ECM to tell the operator that the generator interface board (slot 2) is missing or has been installed incorrectly.

### Component Location

Refer to Section E for location of the ECM card cage and the generator interface board (slot 2).

### Shoptalk

The possible failure modes are incorrect installation of the generator interface board and loading an incorrect software calibration into the ECM.

Refer to Troubleshooting Fault Code t05-1344
