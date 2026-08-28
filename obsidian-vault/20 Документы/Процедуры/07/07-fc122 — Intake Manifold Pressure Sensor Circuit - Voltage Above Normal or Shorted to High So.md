---
aliases:
  - "Цепь датчика давления коллектора — напряжение выше нормы"
type: "Процедура"
doc: "07-fc122"
title_en: "Intake Manifold Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика давления коллектора — напряжение выше нормы"
modified: "2012-12-18"
engines:
  - "93058669"
  - "93087701"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc122.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc122.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Intake Manifold Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика давления коллектора — напряжение выше нормы**

> [!abstract] Процедура · `07-fc122`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]], [[93087701 — 6C8.3 CPL 3105|93087701]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-12-18
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-fc122.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/07-fc122.pdf)

### Fault Code: 122

### Intake Manifold Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 122 PID(P): P102 SPN: 102 FMI: 3 Lamp: Amber SRT: | Intake Manifold Pressure Sensor Circuit - Voltage Above Normal or Shorted to High Source. High signal voltage detected at the intake manifold pressure circuit. | Derate dependant on calibration. Possible black smoke during acceleration. |

![[19900354.png]]

Intake Manifold Pressure Sensor Circuit

### Circuit Description

The intake manifold pressure sensor monitors boost pressure and passes information to the electronic control module (ECM) through the intake manifold pressure signal pin of the engine harness.

### Component Location

Reference Section E for a detailed component location view. There is one intake manifold pressure sensor on the 480C E engine. It is located next to the air intake heater, behind the ECM.

### Shoptalk

- The intake manifold pressure sensor measures gauge pressure. Confirm the sensor is reading properly by comparing the reading seen in the ECM with a reading taken with a mechanical gauge. The sensor should read -38 to 38 mm Hg \[-1.5 to 1.5 in Hg\] using INSITE™, with the keyswitch turned to the ON position, but the engine **not** running.

- Determine if the engine is being overfueled.

- Confirm the correct intake manifold pressure sensor part number is being used.

- Confirm the correct turbocharger is being used.

- If it is suspected that cold intake air can be the cause of the high intake manifold pressure, test the engine while feeding it warm intake air.

- Inspect the intake manifold pressure sensor circuit for signs of tampering. Remove any extra wires from the circuit.

Refer to Troubleshooting Fault Code t05-122
