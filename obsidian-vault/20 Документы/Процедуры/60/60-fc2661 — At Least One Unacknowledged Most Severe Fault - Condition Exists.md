---
aliases:
  - "Есть неподтверждённая неисправность наивысшего уровня — условие возникло"
type: "Процедура"
doc: "60-fc2661"
title_en: "At Least One Unacknowledged Most Severe Fault - Condition Exists"
title_ru: "Есть неподтверждённая неисправность наивысшего уровня — условие возникло"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc2661.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc2661.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# At Least One Unacknowledged Most Severe Fault - Condition Exists
**Есть неподтверждённая неисправность наивысшего уровня — условие возникло**

> [!abstract] Процедура · `60-fc2661`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc2661.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc2661.pdf)

### Fault Code: 2661

### At Least One Unacknowledged Most Severe Fault - Condition Exists

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2661 PID(P): SPN: 629 FMI: 11/31 Lamp: Red SRT: | One or more unacknowledged most severe fault codes has been detected. | Engine will shut down. |

![[19a00867.png]]

Engine Control Module (ECM)

### Circuit Description

The Engine Control Module (ECM) is a computer that is responsible for engine control, diagnostics, and user features.The ECM has internal diagnostics that continuously run and check the internal memory.

### Component Location

The reset button or switch location depends on the original equipment manufacturer (OEM).

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected a most severe fault.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a shutdown fault immediately when the diagnostics runs and fails.

- The engine will be shut down.

### Conditions For Clearing The Fault Code

- This fault code will go inactive once all amber lamp fault codes in secondary ECMs are inactive.

- The generator set controller will turn off the fault code immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

This is an information-only fault code that will **only** become active if other critical engine protection fault codes are active.Fault code will remain active until reset by the operator. The light is an indicator that will remain lit to inform the operator that there has been a fault code generated. The fault has no effect on engine performance.

Refer to Troubleshooting Fault Code 2661.
