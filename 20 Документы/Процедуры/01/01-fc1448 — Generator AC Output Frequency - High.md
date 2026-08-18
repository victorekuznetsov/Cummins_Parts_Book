---
aliases:
  - "Высокая частота выходного напряжения генератора"
type: "Процедура"
doc: "01-fc1448"
title_en: "Generator AC Output Frequency - High"
title_ru: "Высокая частота выходного напряжения генератора"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1448.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1448.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator AC Output Frequency - High
**Высокая частота выходного напряжения генератора**

> [!abstract] Процедура · `01-fc1448`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1448.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1448.pdf)

### Fault Code: 1448

### Generator AC Output Frequency - High

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1448 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Generator AC output frequency is low. | Generator set will shut down. |

![[17600025.png]]

Generator Set

### Circuit Description

The generator set produces electrical power. This power is in the form of three-phase AC. The ECM monitors the performance and operation of the generator set. The threshold for a low AC output frequency condition is that the engine speed has dropped below 90 percent of nominal for at least 10 seconds.

The engine control module (ECM) uses this fault code to tell the operator when the generator set AC output frequency is low.

### Component Location

Refer to customer/facility/installation documentation for diagrams on the generator set/electrical bus setup.

### Shoptalk

Check the fuel supply, intake air supply, and load.

Refer to Troubleshooting Fault Code t05-1448.
