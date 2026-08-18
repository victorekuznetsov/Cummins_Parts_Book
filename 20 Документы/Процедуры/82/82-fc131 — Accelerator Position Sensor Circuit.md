---
aliases:
  - "Цепь датчика положения акселератора"
type: "Процедура"
doc: "82-fc131"
title_en: "Accelerator Position Sensor Circuit"
title_ru: "Цепь датчика положения акселератора"
modified: "2010-09-02"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc131.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc131.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Accelerator Position Sensor Circuit
**Цепь датчика положения акселератора**

> [!abstract] Процедура · `82-fc131`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc131.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc131.pdf)

### Fault Code: 131

### Accelerator Position Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 131 PID(P): P091 SPN: 91 FMI: 3/3 Lamp: Red SRT: | High voltage detected at accelerator position sensor. | Severe derate (power and speed). Limp home power **only**. |

![[19c00644.png]]

Accelerator Position Sensor Circuit

### Circuit Description

The accelerator position sensor is attached to the accelerator pedal. The accelerator position sensor sends a signal to the electronic control module (ECM) when the driver pushes on the accelerator pedal. The accelerator position circuit contains three wires: + 5-VDC supply, return ground, and signal.

### Component Location

The accelerator position sensor is located on the accelerator pedal.

### Shoptalk

If all wiring and sensor checks look good, then replace the accelerator position sensor, and the idle validation switch circuit wires between the accelerator pedal and the ECM with new wires. Run the wires through or around the bulkhead without using the bulkhead connector. Test the truck with the test wires in place. If the fault goes away, replace the OEM harness. Seal the openings in the bulkhead around the connector and wires to prevent toxic and noxious fumes from entering the operator area.

**Note**: The three wires in the accelerator position sensor circuit **must** be twisted together. The same applies for the three wires in the idle validation switch circuit.

Refer to Troubleshooting Fault Code t05-131
