---
aliases:
  - "Выключатель синхронизации агрегатов — данные нестабильны или неверны"
type: "Процедура"
doc: "82-fc497"
title_en: "Multiple Unit Synchronization Switch - Data Erratic, Intermittent, or Incorrect"
title_ru: "Выключатель синхронизации агрегатов — данные нестабильны или неверны"
modified: "2015-05-18"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc497.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc497.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Multiple Unit Synchronization Switch - Data Erratic, Intermittent, or Incorrect
**Выключатель синхронизации агрегатов — данные нестабильны или неверны**

> [!abstract] Процедура · `82-fc497`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-05-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc497.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc497.pdf)

### Fault Code: 497

### Multiple Unit Synchronization Switch - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 497 PID(P): S114 SPN: 1377 FMI: 2/2 Lamp: Amber SRT: | Multiple Unit Synchronization Switch - Data Erratic, Intermittent, or Incorrect. | Various optional switch inputs to the engine control module (ECM) may **not** operate correctly. |

![[19r00275.png]]

Multiple Unit Synchronization Switch Circuit

### Circuit Description

The Multiple Unit Synchronization feature uses an ON/OFF switch and a complementary switch. The complementary switch is used by the ECM to determine the type of coupling (hard or soft) to use between multiple engines when the multiple unit synchronization switch is engaged. This feature is installed by the original equipment manufacturer (OEM) to support this feature.

### Component Location

The multiple unit synchronization switch is mounted by the OEM. Refer to the OEM manual for the specific location.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the keyswitch is in the ON position or when the engine is running.

### Conditions For Setting The Fault Codes

The ECM detected the multiple unit synchronous ON/OFF switch and multiple unit synchronous complimentary ON/OFF switch have different values.

### Action Taken When The Fault Code Is Active

- The ECM illuminates the amber CHECK ENGINE lamp immediately when the diagnostic runs and fails.

### Conditions For Clearing The Fault Code

To validate the repair, start the engine and let it idle for 1 minute.

- The fault code status displayed by INSITE™ electronic service tool will change to INACTIVE immediately after the diagnostic runs and passes.

- The ECM will turn off the amber CHECK ENGINE lamp immediately after the diagnostic runs and passes.

The Reset All Faults command in INSITE™ electronic service tool can be used to clear active and inactive faults.

### Shoptalk

The Multiple Unit Synchronization feature allows two or more engines to be controlled by a single throttle signal and run at a similar speed. There are three engine configurations available with this feature: soft-coupled, hard-coupled, and soft-coupled marine.

The hard-coupled configuration has the primary and all secondary engines in series with each other. The primary engine outputs a throttle signal, which is received by the first secondary engine. This secondary engine then outputs the throttle signal to the next secondary engine in the series. This process repeats until the primary engine receives the throttle signal.

Refer to Troubleshooting Fault Code t05-497
