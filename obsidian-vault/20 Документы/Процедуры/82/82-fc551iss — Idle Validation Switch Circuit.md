---
aliases:
  - "Цепь выключателя подтверждения холостого хода"
type: "Процедура"
doc: "82-fc551iss"
title_en: "Idle Validation Switch Circuit"
title_ru: "Цепь выключателя подтверждения холостого хода"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc551iss.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc551iss.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Idle Validation Switch Circuit
**Цепь выключателя подтверждения холостого хода**

> [!abstract] Процедура · `82-fc551iss`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-09-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc551iss.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-fc551iss.pdf)

### Fault Code: 551

ISS

### Idle Validation Switch Circuit

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 551 PID(P): S230 SPN: 558 FMI: 4/4 Lamp: Yellow SRT: | No voltage detected simultaneously on both the idle validation off-idle and on-idle circuits. | Engine will **only** idle. |

![[19c00644.png]]

Idle Validation Switch Circuit

### Circuit Description

The idle validation switch is used by the electronic control module (ECM) to indicate when the accelerator pedal is released (on-idle) or depressed (off-idle). The switch is adjusted at the factory to switch from on-idle to off-idle at the correct accelerator pedal position.

### Component Location

The integrated sensor/switch (ISS) is located on the accelerator pedal assembly.

### Shoptalk

- This fault code is usually caused by a loose connection, an accelerator pedal that is **not** calibrated, or an IVS that is wired wrong. Breakout cable, Part Number 3824892, is required to check the voltage levels of the SSS.

- If all wiring and sensor checks are good, replace the idle validation switch circuit wires, between the accelerator pedal and ECM, with new wires. Run the wires through or around the bulkhead without using the bulkhead connector. Test the truck with the test wires in place. If the fault clears, replace the OEM harness. Seal the openings in the bulkhead around the connector and wires to prevent toxic and noxious fumes from seeping into the cab.

- Verify that the three idle validation switch circuit wires are twisted together.

- The ECM and accelerator pedal assembly **must** be electrically calibrated to each other for proper engine response. The ECM and accelerator pedal assembly **must** be calibrated when an accelerator pedal is initially installed, replaced, when an ECM is replaced, when a new calibration is downloaded to the ECM, and when the accelerator pedal wiring is disconnected while the vehicle keyswitch is on.

- With keyswitch on, gradually push the accelerator to the floor and release. Depress and release the accelerator pedal three times. This procedure will recalibrate the ECM and accelerator pedal.

Refer to Troubleshooting Fault Code t05-551iss
