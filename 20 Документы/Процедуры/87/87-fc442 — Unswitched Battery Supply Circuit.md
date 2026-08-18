---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "87-fc442"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc442.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc442.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `87-fc442`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc442.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc442.pdf)

### Fault Code: 442

### Unswitched Battery Supply Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 442 PID(P): P168 SPN: 168 FMI: 0 Lamp: Yellow SRT: | More than 35.0-VDC battery voltage detected at the electronic control module (ECM). | ECM damage will occur. |

![[19a00581.png]]

Unswitched Battery Supply Circuit

### Circuit Description

The ECM receives unswitched battery voltage through the OEM harness and engine harness. There is an in-line 15-amp fuse in the unswitched battery wire of the OEM interface harness to protect the ECM. The battery return wires in the engine harness are connected to the engine block ground.

### Component Location

The location of the battery will vary with the OEM. Refer to the OEM manual for the battery location.

### Shoptalk

This fault is usually caused by improper wiring of the battery circuit.

Refer to Troubleshooting Fault Code t05-442
