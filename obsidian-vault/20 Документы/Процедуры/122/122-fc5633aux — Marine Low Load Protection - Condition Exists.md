---
aliases:
  - "Судовая защита от малой нагрузки — условие возникло"
type: "Процедура"
doc: "122-fc5633aux"
title_en: "Marine Low Load Protection - Condition Exists"
title_ru: "Судовая защита от малой нагрузки — условие возникло"
modified: "2016-11-02"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5633aux.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5633aux.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Marine Low Load Protection - Condition Exists
**Судовая защита от малой нагрузки — условие возникло**

> [!abstract] Процедура · `122-fc5633aux`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-11-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-fc5633aux.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-fc5633aux.pdf)

### Fault Code: 5633 (Auxiliary)

### Marine Low Load Protection - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 5633 PID(P): SPN: 520891 FMI: 31 Lamp: Maintenance SRT: | Marine Low Load Protection - Condition Exists. Low load condition has been detected by the engine control module (ECM). | None on performance. |

![[19d02662.png]]

### Circuit Description

Marine Low Load Protection monitors the engine operating in a low load condition of less than 15 percent of rated torque. This feature is needed to limit engine exposure in such working conditions by alerting the operator.

### Component Location

Not Applicable

### Conditions For Running The Diagnostics

- This diagnostic runs when the engine torque falls below the low load threshold.

### Conditions For Setting The Fault Codes

- The ECM detected speed and torque values in the low load region for more than a calibratable time.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the white MAINTENANCE lamp immediately when the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

- The ECM detected speed and torque values in a normal operating region during a sea trial.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE after the diagnostic runs and passes.

- The ECM will turn off the white MAINTENANCE lamp immediately after the diagnostic runs and passes.

### Shoptalk

- This is an information- **only** fault code that becomes active if the engine torque falls below the low load threshold for a calibratable time.

- High counts of inactive Fault Code 5633 can indicate the engine is often operated beyond the normal expected region. Vessel operating duty cycle or equipment may need to be investigated to understand fault condition.

- No repairs are necessary.

Refer to Troubleshooting Fault Code 5633.
