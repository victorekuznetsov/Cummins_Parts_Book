---
aliases:
  - "Давление топлива в рампе опережения 1 — данные нестабильны или неверны"
type: "Процедура"
doc: "60-fc423"
title_en: "Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect"
title_ru: "Давление топлива в рампе опережения 1 — данные нестабильны или неверны"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc423.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc423.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect
**Давление топлива в рампе опережения 1 — данные нестабильны или неверны**

> [!abstract] Процедура · `60-fc423`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc423.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc423.pdf)

### Fault Code: 423

### Injector Timing Rail 1 Fuel Pressure - Data Erratic, Intermittent, or Incorrect

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 423 PID(P): P156 SPN: 156 FMI: 2/2 Lamp: Amber SRT: | Signal voltage indicates that the timing pressure sensor signal is irrational. | Possible reduced engine performance. |

![[19a00870.png]]

Engine Fuel Timing Actuator Circuit

### Circuit Description

The engine fuel timing actuator circuit is used to control the start of injection. The engine control module (ECM) monitors the current on the timing actuator pulse width modulated supply circuit.

### Component Location

The engine timing pressure actuator is internal to the fuel pump.

### Conditions For Running The Diagnostics

This diagnostic runs when the timing rail actuator is commanded ON.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) detected a fueling timing or quantity error for all injectors.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

### Conditions For Clearing The Fault Code

- To validate the repair, bring the engine up to operating temperature and run it in normal loaded conditions for 15 minutes.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Possible causes of this fault code include:

- Damaged or malfunctioning engine fuel timing actuator

- Damaged or loose connectors.

- Malfunctioning or damaged engine wiring harness.

- Drainline restriction

Refer to Troubleshooting Fault Code 423.
