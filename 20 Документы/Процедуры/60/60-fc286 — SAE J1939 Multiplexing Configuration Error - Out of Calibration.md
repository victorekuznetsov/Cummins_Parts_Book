---
aliases:
  - "Ошибка конфигурации мультиплексирования SAE J1939 — вне калибровки"
type: "Процедура"
doc: "60-fc286"
title_en: "SAE J1939 Multiplexing Configuration Error - Out of Calibration"
title_ru: "Ошибка конфигурации мультиплексирования SAE J1939 — вне калибровки"
modified: "2020-09-28"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc286.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc286.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# SAE J1939 Multiplexing Configuration Error - Out of Calibration
**Ошибка конфигурации мультиплексирования SAE J1939 — вне калибровки**

> [!abstract] Процедура · `60-fc286`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc286.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-fc286.pdf)

### Fault Code: 286

### SAE J1939 Multiplexing Configuration Error - Out of Calibration

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 286 PID(P): S231 SPN: 639 FMI: 13/13 Lamp: Amber SRT: | The ECM expected information from a multiplexed device but **only** received a portion of the necessary information. | At least one multiplexed device will **not** operate properly. |

![[19a00866.png]]

J1939 Datalink Circuit

### Circuit Description

The ECM identified another device on the J1939 datalink network has stopped communicating on the network. The devices on the J1939 datalink network include: ECMs', and the Generator Interface Module. The harness for the J1939 datalink network has a shielded twisted pair of wires that connect each of the network devices and termination resistor.

### Component Location

The Engine Control Modules (ECM) are located on a plate that is above the flywheel housing.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) received an invalid J1939 data link message from a multiplexed device.

### Action Taken When The Fault Code Is Active

- The generator set controller displays a warning fault immediately when the diagnostics runs and fails.

- The multiplexed device will **not** operate.

### Conditions For Clearing The Fault Code

- To validate the repair, start the engine and let it run for 1 minute at no load.

- The generator set controller will turn off the warning indicator immediately after the user presses reset.

- The “Reset All Faults” command in the recommended Cummins® electronic service tool or equivalent can be used to clear active faults.

### Shoptalk

Each smart device on the J1939 datalink network need power and ground to turn on, after the smart device turns on, it can then communicate on the J1939 datalink network.

Possible causes of this fault code include:

- Malfunctioning or damaged J1939 datalink wiring harness.

- Communication failure between J1939 devices

Refer to Troubleshooting Fault Code 286.
