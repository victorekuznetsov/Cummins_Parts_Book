---
aliases:
  - "Замена моторного масла и фильтра"
type: "Процедура"
doc: "87-fc649"
title_en: "Change Lubricating Oil and Filter"
title_ru: "Замена моторного масла и фильтра"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc649.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc649.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Change Lubricating Oil and Filter
**Замена моторного масла и фильтра**

> [!abstract] Процедура · `87-fc649`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc649.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-fc649.pdf)

### Fault Code: 649

### Change Lubricating Oil and Filter

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 649 PID(P): SPN: FMI: Lamp: Warning SRT: | Change lubricating oil and filter. The Centinel system has **not** been able to replace old oil with new. The condition has persisted long enough that the oil quality warrants a full change out. | No action is taken by the ECM. Possible damage to engine can occur. |

![[19802494.png]]

### Circuit Description

The oil make up tank provides clean oil to the make up valve of the Centinel system to replenish oil that was burned by the Centinel system.

### Component Location

Varies by installation. Refer to Centinel Master Repair Manual [[3666231 — Centinel™ Master Repair Manual\|3666231]] for further information.

### Shoptalk

This fault indicates that the old oil has **not** been replenished with new oil.

Refer to Troubleshooting Fault Code t05-649
