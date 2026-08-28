---
aliases:
  - "Высокий выходной ток генератора — критично"
type: "Процедура"
doc: "01-fc1472"
title_en: "Generator AC Output Current High - Critical"
title_ru: "Высокий выходной ток генератора — критично"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1472.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1472.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator AC Output Current High - Critical
**Высокий выходной ток генератора — критично**

> [!abstract] Процедура · `01-fc1472`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1472.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1472.pdf)

### Fault Code: 1472

### Generator AC Output Current High - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1472 PID(P): SPN: FMI: Lamp: Shutdown SRT: | AC output current has exceeded the shutdown threshold for high current. | Generator set will shut down. |

![[19802906.png]]

AC Output Current Circuit

### Circuit Description

The generator set produces electric power. This power is in the form of three-phase AC. The engine control module (ECM) monitors the AC output current to make certain the generator set is performing and operating correctly. The threshold for a high AC output current condition is that the generator output current has exceeded 100 percent of rated for at least 120 seconds.

The ECM uses this fault code to tell the operator when the AC output current passes the shutdown threshold for high current.

### Component Location

Reference Section E for location of the voltage regulator and PT/CT board.

### Shoptalk

The alternator is beginning to become overloaded. The AC output current has passed the calibrated threshold for a shutdown level.

Check load-sharing lines for proper connection.

Refer to Troubleshooting Fault Code t05-1472.
