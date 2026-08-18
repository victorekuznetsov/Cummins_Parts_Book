---
aliases:
  - "Базовая плата — несоответствие ПО расширенного ввода-вывода"
type: "Процедура"
doc: "01-fc1474"
title_en: "Base Board - Extended I/O Software Mismatch"
title_ru: "Базовая плата — несоответствие ПО расширенного ввода-вывода"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1474.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1474.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Base Board - Extended I/O Software Mismatch
**Базовая плата — несоответствие ПО расширенного ввода-вывода**

> [!abstract] Процедура · `01-fc1474`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1474.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1474.pdf)

### Fault Code: 1474

### Base Board - Extended I/O Software Mismatch

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1474 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Software version mismatch between the base board and the extended I/O board. | Generator set will shut down. |

![[19802649.png]]

Generator Set ECM Card Cage

### Circuit Description

This fault code is used by the ECM to tell the operator that the base board software version does not correspond to the version of software loaded into the extended I/O board.

### Component Location

Refer to section E for location of the ECM card cage, the base board, and the extended I/O board.

### Shoptalk

The possible failure modes are incorrect installation of the base board or extended I/O board, and loading an incorrect software calibration into the ECM.

Refer to Troubleshooting Fault Code t05-1474
