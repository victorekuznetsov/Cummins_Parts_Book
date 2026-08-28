---
aliases:
  - "Хотя бы один модуль имеет неисправность умеренного уровня — условие возникло"
type: "Процедура"
doc: "60-fc1518"
title_en: "At Least One Module Has A Moderately Severe Fault - Condition Exists"
title_ru: "Хотя бы один модуль имеет неисправность умеренного уровня — условие возникло"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1518.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1518.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# At Least One Module Has A Moderately Severe Fault - Condition Exists
**Хотя бы один модуль имеет неисправность умеренного уровня — условие возникло**

> [!abstract] Процедура · `60-fc1518`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc1518.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc1518.pdf)

### Fault Code: 1518

### At Least One Module Has A Moderately Severe Fault - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1518 PID(P): S254 SPN: 1484 FMI: 11/31 Lamp: Amber SRT: | A moderately severe fault code has been detected by at least one module | Possible reduced engine performance. |

![[19a00867.png]]

Engine Control Module (ECM)

### Circuit Description

The engine control module (ECM) is a computer that is responsible for engine control, diagnostics, and user features. A moderately severe fault code has been detected from a ECM on the J1939 datalink network.

### Component Location

The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) has detected one or more moderately severe faults.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- This fault code will go inactive once all amber lamp fault codes in secondary ECMs are inactive.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Each ECM has an individual source address that displays when the recommended Cummins® electronic service tool or equivalent is connected. When troubleshooting a fault code, use the source address displayed in the recommended Cummins® electronic service tool or equivalent to determine which ECM and circuit is affected.

Possible causes of this fault code include:

- A moderately severe fault code detected on another ECM

Refer to Troubleshooting Fault Code 1518.
