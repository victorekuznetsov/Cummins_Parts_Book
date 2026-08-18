---
aliases:
  - "Потеря возбуждения из-за обратной реактивной мощности — условие возникло"
type: "Процедура"
doc: "01-fc1461"
title_en: "Loss of Electric Field Due to Reverse KVAR - Condition Exists"
title_ru: "Потеря возбуждения из-за обратной реактивной мощности — условие возникло"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1461.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1461.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Loss of Electric Field Due to Reverse KVAR - Condition Exists
**Потеря возбуждения из-за обратной реактивной мощности — условие возникло**

> [!abstract] Процедура · `01-fc1461`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1461.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1461.pdf)

### Fault Code: 1461

### Loss of Electric Field Due to Reverse KVAR - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1461 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Loss of field (electric) due to reverse kVAR. | Generator set will shut down. |

![[19802905.png]]

Generator Circuit

### Circuit Description

Under normal operating conditions, the generator set connects to the bus. The generator set is producing power, and when it connects to the bus, power is added to the main electric bus. When some events occur, a condition can occur when the generator set is no longer producing power for the electric bus, but rather is drawing power from the electric bus. This condition is called reverse kilovolt-ampere reduction (kVAR). Sometimes a reverse kVAR condition can cause the alternator to lose its electric field.

This fault code is used by the engine control module to tell the operator that the engine control module has detected a loss of electric field in the alternator due to a reverse kVAR condition.

### Component Location

Reference Section E for location of the engine control module card cage.

Reference customer/facility/installation documentation for the location of the generator set circuit breaker and interface with the electric bus.

### Shoptalk

The possible failure mode is perhaps due to power factor correction capacitors or other power sources feeding kVAR into the generator set.

Beyond a certain threshold, reverse kVAR can lead to voltage output instability and pole slipping due to the fact that the alternator becomes self-excited.

Check load-sharing lines for proper connection.

Refer to Troubleshooting Fault Code t05-1461.
