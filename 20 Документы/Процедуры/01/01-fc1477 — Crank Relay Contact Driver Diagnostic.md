---
aliases:
  - "Диагностика контакта реле стартера"
type: "Процедура"
doc: "01-fc1477"
title_en: "Crank Relay Contact Driver Diagnostic"
title_ru: "Диагностика контакта реле стартера"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1477.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1477.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Crank Relay Contact Driver Diagnostic
**Диагностика контакта реле стартера**

> [!abstract] Процедура · `01-fc1477`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1477.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1477.pdf)

### Fault Code: 1477

### Crank Relay Contact Driver Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1477 PID(P): SPN: FMI: Lamp: Warning SRT: | Crank relay contact diagnostic has detected and error. | ECM will possibly **not** be able to crank the engine. |

![[19802911.png]]

Crank Relay Contact Circuit

### Circuit Description

The engine control module (ECM) checks the crank relay contact to make certain it is operating correctly. The ECM uses the fault code to inform the operator that the generator set is commanding “cranking,” but the feedback from the crank relay contact is **not** confirming.

### Component Location

Reference Section E for location of the crank relay contact and the ECM.

### Shoptalk

The possible failure modes are open circuit, short to ground, bad crank relay, bad crank slave relay, and loss of supply voltage inside the ECM.

If the engine will crank, the problem is with the crank status circuit.

If the engine will not crank, the problem is with the crank supply circuit, the crank signal circuit, a bad crank relay, or bad crank slave relay.

If the 20 amp fuse (battery side of Inline E) blows when attempting to crank, check the diode on the crank slave coil circuit for proper installation and operation.

Refer to Troubleshooting Fault Code t05-1477.
