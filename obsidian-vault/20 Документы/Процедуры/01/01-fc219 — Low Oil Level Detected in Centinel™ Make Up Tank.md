---
aliases:
  - "Низкий уровень масла в баке подпитки Centinel™"
type: "Процедура"
doc: "01-fc219"
title_en: "Low Oil Level Detected in Centinel™ Make Up Tank"
title_ru: "Низкий уровень масла в баке подпитки Centinel™"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc219.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc219.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Low Oil Level Detected in Centinel™ Make Up Tank
**Низкий уровень масла в баке подпитки Centinel™**

> [!abstract] Процедура · `01-fc219`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc219.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc219.pdf)

### Fault Code: 219

### Low Oil Level Detected in Centinel™ Make Up Tank

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 219 PID(P): P17 SPN: 1380 FMI: Lamp: Warning SRT: | Engine oil level 2 (remote) low - maintenance. Low oil level is detected in the remote oil reservoir used in the Centinel™ system. | Centinel™ system is deactivated. |

![[19802494.png]]

ECM

### Circuit Description

The oil make up tank provides clean oil to the make up valve of the Centinel™ system to replenish oil that was burned by the Centinel™ system.

### Component Location

Varies by installation. Refer to Centinel™ Master Repair Manual [[3666231 — Centinel™ Master Repair Manual\|3666231]] for further information.

### Shoptalk

This fault indicates that the oil is low in the makeup tank.

Refer to Troubleshooting Fault Code t05-219
