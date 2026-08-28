---
aliases:
  - "Низкая частота выходного напряжения генератора"
type: "Процедура"
doc: "01-fc1449"
title_en: "Generator AC Output Frequency - Low"
title_ru: "Низкая частота выходного напряжения генератора"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1449.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1449.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator AC Output Frequency - Low
**Низкая частота выходного напряжения генератора**

> [!abstract] Процедура · `01-fc1449`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1449.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1449.pdf)

### Fault Code: 1449

### Generator AC Output Frequency - Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1449 PID(P): SPN: FMI: Lamp: Warning SRT: | Generator AC output frequency is high. | No action is taken by the ECM. |

![[17600025.png]]

Generator Set

### Circuit Description

The generator set produces electric power. This power is in the form of three-phase AC. The ECM monitors the performance and operation of the generator set. The threshold for a high AC output frequency condition is that the engine speed has dropped below 110 percent of nominal for at least 10 seconds.

The engine control module (ECM) uses this fault code to tell the operator when the generator set AC output frequency is low.

### Component Location

Refer to customer/facility/installation documentation for diagrams on the generator set/electric bus setup.

### Shoptalk

Check the fuel supply, intake air supply, and load.

Refer to Troubleshooting Fault Code t05-1449.
