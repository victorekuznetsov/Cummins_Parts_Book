---
aliases:
  - "Диагностика контакта реле работы"
type: "Процедура"
doc: "01-fc1414"
title_en: "Run Relay Contact Diagnostic"
title_ru: "Диагностика контакта реле работы"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1414.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1414.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Run Relay Contact Diagnostic
**Диагностика контакта реле работы**

> [!abstract] Процедура · `01-fc1414`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1414.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-fc1414.pdf)

### Fault Code: 1414

Run Relay Contact Diagnostic

### Run Relay Contact Diagnostic

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1414 PID(P): SPN: FMI: Lamp: Warning SRT: | Run relay contact diagnostic has detected an error. | The ECM will **not** be able to enter Run mode. |

![[19802814.png]]

Run Relay Contact Circuit

### Circuit Description

The ECM checks the run relay contact to make certain it is operating correctly. The ECM uses the contacts to determine that the engine is now in the Run mode. The ECM monitors the feedback from the status line to give the position of the run relay contact.

### Component Location

Refer to Section E for the location of the run relay contact and the ECM.

### Shoptalk

The possible modes are open circuit, short to ground, bad run contact, and loss of supply voltage inside the ECM. When the Manual Run/Stop button is in the Run mode, if there is 24 VDC present at the Inline F switched B+ pin, then the circuit is working properly.

Refer to Troubleshooting Fault Code t05-1414
