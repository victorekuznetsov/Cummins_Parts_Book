---
aliases:
  - "Тайм-аут PGN мультиплексирования SAE J1939 — недопустимая частота обновления"
type: "Процедура"
doc: "60-fc285"
title_en: "SAE J1939 Multiplexing PGN Timeout Error - Abnormal Update Rate"
title_ru: "Тайм-аут PGN мультиплексирования SAE J1939 — недопустимая частота обновления"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc285.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc285.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# SAE J1939 Multiplexing PGN Timeout Error - Abnormal Update Rate
**Тайм-аут PGN мультиплексирования SAE J1939 — недопустимая частота обновления**

> [!abstract] Процедура · `60-fc285`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section TF — Troubleshooting Fault Codes
> **Даты:** изменён 2020-09-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-fc285.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-fc285.pdf)

### Fault Code: 285

### SAE J1939 Multiplexing PGN Timeout Error - Abnormal Update Rate

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 285 PID(P): S231 SPN: 639 FMI: 9/9 Lamp: Amber SRT: | Communication between the engine control module (ECM) and another device on the J1939 datalink has been lost. | Possible reduced engine performance. |

![[19a00866.png]]

J1939 Datalink Circuit

### Circuit Description

The ECM identified another device on the J1939 datalink network has stopped communicating on the network. The devices on the J1939 datalink network include: ECMs', and the Generator Interface Module. The harness for the J1939 datalink network has a shielded twisted pair of wires that connect each of the network devices and termination resistor.

### Component Location

The J1939 datalink wiring and the J1939 devices vary by OEM options.

### Conditions For Running The Diagnostics

This diagnostic runs continuously when the generator set controller is active.

### Conditions For Setting The Fault Codes

The Engine Control Module (ECM) did **not** receive a message from a multiplexed device.

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

- Malfunctioning or damaged OEM wiring harness.

Refer to Troubleshooting Fault Code 285.
