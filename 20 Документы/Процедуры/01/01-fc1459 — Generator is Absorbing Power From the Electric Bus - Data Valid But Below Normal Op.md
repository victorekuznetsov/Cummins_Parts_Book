---
aliases:
  - "Генератор потребляет мощность из сети — ниже нормы — наивысший уровень"
type: "Процедура"
doc: "01-fc1459"
title_en: "Generator is Absorbing Power From the Electric Bus - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Генератор потребляет мощность из сети — ниже нормы — наивысший уровень"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1459.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1459.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator is Absorbing Power From the Electric Bus - Data Valid But Below Normal Operating Range - Most Severe Level
**Генератор потребляет мощность из сети — ниже нормы — наивысший уровень**

> [!abstract] Процедура · `01-fc1459`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1459.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1459.pdf)

### Fault Code: 1459

### Generator is Absorbing Power From the Electric Bus - Data Valid But Below Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1459 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Reverse kW detected (generator is absorbing voltage from the electric bus). | The generator set will shut down. |

![[19802905.png]]

Generator Circuit

### Circuit Description

Under normal operating conditions, the generator set connects to the bus. Generator set is producing power, and when it connects to the bus, power is added to the main electric bus. When some events occur, a condition can occur when the generator set is no longer producing power for the electric bus, but rather is drawing power from the electric bus. This condition is called reverse kW.

### Component Location

Reference Section E for location of the engine control module (ECM) card cage. Reference customer/facility/installation documentation for the location of the generator set circuit breaker and interface with the electric bus.

### Shoptalk

The system (electric bus) is driving the engine using the alternator as a motor.

If the problem occurs at initial start-up, verify proper connection of the generator's current transformers.

Verify proper connection of load-sharing lines.

Verify that the generator is operating at the correct frequency and voltage.

Verify that there are no new fuel system problems that are causing the engine **not** to be able to pick up the load.

Refer to Troubleshooting Fault Code t05-1459.
