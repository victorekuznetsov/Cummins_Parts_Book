---
aliases:
  - "Судовая защита от малой нагрузки — условие возникло"
type: "Процедура"
doc: "123-fc5633prop"
title_en: "Marine Low Load Protection - Condition Exists"
title_ru: "Судовая защита от малой нагрузки — условие возникло"
modified: "2016-11-03"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc5633prop.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc5633prop.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Marine Low Load Protection - Condition Exists
**Судовая защита от малой нагрузки — условие возникло**

> [!abstract] Процедура · `123-fc5633prop`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-11-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc5633prop.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc5633prop.pdf)

### Fault Code: 5633 (Propulsion)

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

- The ECM detected speed and torque values in the normal operating region during a sea trial.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE after the diagnostic runs and passes.

- The ECM will turn off the white MAINTENANCE lamp immediately after the diagnostic runs and passes.

### Shoptalk

- This is an information- **only** fault code that becomes active if the engine torque falls below the low load threshold for a calibratable time.

- High counts of inactive Fault Code 5633 can indicate the engine is often operated below the normal expected region. Vessel operating duty cycle or equipment may need to be investigated to understand fault condition.

- No repairs are necessary.

Refer to Troubleshooting Fault Code 5633.
