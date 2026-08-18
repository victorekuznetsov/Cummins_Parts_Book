---
aliases:
  - "Генераторная установка не синхронизируется по фазе"
type: "Процедура"
doc: "01-fc1458"
title_en: "Generator Set - Cannot Synchronize Phase"
title_ru: "Генераторная установка не синхронизируется по фазе"
modified: "2012-05-09"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1458.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1458.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Generator Set - Cannot Synchronize Phase
**Генераторная установка не синхронизируется по фазе**

> [!abstract] Процедура · `01-fc1458`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1458.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1458.pdf)

### Fault Code: 1458

### Generator Set - Cannot Synchronize Phase

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1458 PID(P): SPN: FMI: Lamp: Warning SRT: | Generator and electric bus phase sequences differ. | Generator will continue to run, but will **not** pick up load. |

![[19802905.png]]

Generator Circuit

### Circuit Description

The generator set picks up the electrical load from the bus. For the generator to connect to a bus (other than a dead bus), it **must** match, in phase sequences as well as with a threshold, the voltage and frequency of the bus. The generator set can **not** connect to the bus while voltage and frequency are outside the threshold, or the phase sequences of the generator set do **not** match the electric bus; otherwise, damage can occur to the generator set.

This fault code is used by the ECM to tell the operator that the generator set failed to synchronize to the electric bus.

### Component Location

Refer to Section E for location of the ECM card cage.

Refer to customer/facility/installation documentation for the location of the generator set circuit breaker and interface with the electric bus.

### Shoptalk

Check the bus feedback wires to the bus PT.

Verify phase rotation of generator and bus.

Refer to Troubleshooting Fault Code t05-1458
