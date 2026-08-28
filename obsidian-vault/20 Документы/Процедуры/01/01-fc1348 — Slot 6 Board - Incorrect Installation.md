---
aliases:
  - "Плата слота 6 — неверная установка"
type: "Процедура"
doc: "01-fc1348"
title_en: "Slot 6 Board - Incorrect Installation"
title_ru: "Плата слота 6 — неверная установка"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1348.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1348.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Slot 6 Board - Incorrect Installation
**Плата слота 6 — неверная установка**

> [!abstract] Процедура · `01-fc1348`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1348.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1348.pdf)

### Fault Code: 1348

### Slot 6 Board - Incorrect Installation

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1348 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The slot 6 board is missing or has **not** been installed correctly. | Engine will **not** start. |

![[19802649.png]]

Generator Set ECM Card Cage

### Circuit Description

Once the software has been loaded into the ECM, the software will do a hardware check to make sure that all necessary cards are installed for the application.

This fault code is used by the ECM to tell the operator that the slot 6 board is missing or has been installed incorrectly.

### Component Location

Refer to Section E for location of the ECM card cage and the slot 6 board.

### Shoptalk

The possible failure modes are incorrect installation of the slot 6 board and loading an incorrect software calibration into the ECM.

Refer to Troubleshooting Fault Code t05-1348
