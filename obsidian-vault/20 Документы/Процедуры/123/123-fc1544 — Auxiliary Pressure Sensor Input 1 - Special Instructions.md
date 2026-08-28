---
aliases:
  - "Вход вспомогательного датчика давления 1 — особые указания"
type: "Процедура"
doc: "123-fc1544"
title_en: "Auxiliary Pressure Sensor Input 1 - Special Instructions"
title_ru: "Вход вспомогательного датчика давления 1 — особые указания"
modified: "2012-01-17"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 2
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1544.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc1544.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Auxiliary Pressure Sensor Input 1 - Special Instructions
**Вход вспомогательного датчика давления 1 — особые указания**

> [!abstract] Процедура · `123-fc1544`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-01-17
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc1544.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc1544.pdf)

### Fault Code: 1544

### Auxiliary Pressure Sensor Input 1 - Special Instructions

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1544 PID(P): SPN: 1387 FMI: 14 Lamp: Maintenance SRT: | Auxiliary Pressure Sensor Input 1 - Special Instructions | Possible engine power derate. |

![[19401823.png]]

QSK19 CM2150 Industrial - Auxiliary Pressure Sensor Input 1 Sensor Circuit

![[19401851.png]]

QSK19 CM2150 Marine- Auxiliary Pressure Sensor Input 1 Sensor Circuit

### Circuit Description

The OEM has the option of wiring a pressure sensor input to the electronic control module (ECM). A specific calibration is then created to recognize this pressure sensor input. This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. In marine applications, this sensor monitors gear oil pressure and the fault code is activated when the pressure falls below a threshold which is an INSITE™ electronic service tool adjustable parameter. Depending on the OEM requirements, an engine protection derate can be associated with the fault code.

### Component Location

The OEM pressure sensor input will vary, depending on application. Refer to the OEM service manual for sensor location.

### Shoptalk

This fault code is activated when the pressure input from the OEM sensor exceeds the engine protection limit defined by the OEM. An engine power derate is possible, depending on the OEM application.

In marine applications, the default setting is intentionally set higher than any possible gear oil pressure. This is so the fault code will become active immediately after recalibration where the adjustable parameters were not overlaid on the new calibration. This prevents the customer from the assumption that he is protected by this lamp when the parameters were not adjusted properly. When the gear oil pressure sensor is not installed, the factory installed resistor is designed to signal to the ECM that gear oil pressure conditions are satisfactory at all times.

Note: The fault code will only go inactive if the ECM sees a known condition for a period (about five seconds) and with the engine running above 1000 RPM.

Refer to Troubleshooting Fault Code 1544.
