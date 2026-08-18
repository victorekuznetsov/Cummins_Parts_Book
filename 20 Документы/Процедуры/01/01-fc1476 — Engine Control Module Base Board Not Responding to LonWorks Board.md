---
aliases:
  - "Базовая плата ЭБУ не отвечает плате LonWorks"
type: "Процедура"
doc: "01-fc1476"
title_en: "Engine Control Module Base Board Not Responding to LonWorks Board"
title_ru: "Базовая плата ЭБУ не отвечает плате LonWorks"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1476.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1476.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Control Module Base Board Not Responding to LonWorks Board
**Базовая плата ЭБУ не отвечает плате LonWorks**

> [!abstract] Процедура · `01-fc1476`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1476.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1476.pdf)

### Fault Code: 1476

### Engine Control Module Base Board Not Responding to LonWorks Board

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1476 PID(P): SPN: FMI: Lamp: Warning SRT: | ECM base board is **not** responding to the LonWorks board. | No action is taken by the ECM. |

![[19802649.png]]

Generator Set ECM Card Cage

### Circuit Description

This fault code is used by the engine control module (ECM) to tell the operator that the base board is **not** responding to commands sent via the LonWorks board.

### Component Location

Reference Section E for location of the ECM card cage, the base board, and the LonWorks Network board.

### Shoptalk

The possible failure modes are incorrect installation of the base board, LonWorks board, and loading an incorrect software calibration into the ECM.

Refer to Troubleshooting Fault Code t05-1476.
