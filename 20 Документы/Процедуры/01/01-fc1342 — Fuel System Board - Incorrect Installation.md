---
aliases:
  - "Плата топливной системы — неверная установка"
type: "Процедура"
doc: "01-fc1342"
title_en: "Fuel System Board - Incorrect Installation"
title_ru: "Плата топливной системы — неверная установка"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1342.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1342.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel System Board - Incorrect Installation
**Плата топливной системы — неверная установка**

> [!abstract] Процедура · `01-fc1342`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1342.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1342.pdf)

### Fault Code: 1342

### Fuel System Board - Incorrect Installation

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1342 PID(P): SPN: FMI: Lamp: Shutdown SRT: | The fuel system board (slot 0) is missing or has **not** been installed correctly. | Engine will **not** start. |

![[19802788.png]]

Generator Set ECM Fuel Board

### Circuit Description

Once the software has been loaded into the ECM, the software will do a hardware check to make sure that all necessary cards are installed for the application.

This fault code is used by the ECM to tell the operator that the fuel system board (slot 0) is missing or has been installed incorrectly.

### Component Location

Refer to Section E for location of the ECM card cage and the fuel system board (slot 0).

### Shoptalk

The possible failure modes are incorrect installation of the fuel system board and loading an incorrect software calibration into the ECM.

Refer to Troubleshooting Fault Code t05-1342
