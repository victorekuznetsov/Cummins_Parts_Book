---
aliases:
  - "Цепь датчика положения акселератора"
type: "Процедура"
doc: "82-fc132"
title_en: "Accelerator Position Sensor Circuit"
title_ru: "Цепь датчика положения акселератора"
modified: "2010-09-02"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc132.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc132.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Accelerator Position Sensor Circuit
**Цепь датчика положения акселератора**

> [!abstract] Процедура · `82-fc132`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc132.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc132.pdf)

### Fault Code: 132

### Accelerator Position Sensor Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 132 PID(P): P091 SPN: 91 FMI: 4/4 Lamp: Red SRT: | Low voltage detected at the accelerator position sensor circuit. | Severe derate (power and speed). Limp home power **only**. |

![[19c00644.png]]

Accelerator Position Sensor Circuit

### Circuit Description

The accelerator position sensor is attached to the accelerator pedal. The accelerator position sensor sends a signal to the electronic control module (ECM) when the driver pushes on the accelerator pedal. The accelerator position circuit contains three wires: + 5-VDC supply, return, and signal.

### Component Location

The accelerator position sensor is located on the accelerator pedal.

### Shoptalk

- Check for external circuits hooked into the accelerator position sensor circuit and for tampering in the circuit.

- If all the wiring and the sensor checks are good, replace the accelerator position sensor and the idle validation switch circuit wires, between the accelerator pedal and ECM, with new wires. Run the wires through or around the bulkhead without using the bulkhead connector. Test the truck with the test wires. If the fault code goes away, replace the OEM harness. Seal openings in the bulkhead to prevent toxic and noxious fumes from entering the operator area.

- Verify that the three accelerator position sensor circuit wires are twisted together. Verify that the three idle validation switch circuit wires are twisted together.

Refer to Troubleshooting Fault Code t05-132
