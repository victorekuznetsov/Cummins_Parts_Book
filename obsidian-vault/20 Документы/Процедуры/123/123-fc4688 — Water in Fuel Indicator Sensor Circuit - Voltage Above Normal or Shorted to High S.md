---
aliases:
  - "Цепь датчика воды в топливе — напряжение выше нормы"
type: "Процедура"
doc: "123-fc4688"
title_en: "Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь датчика воды в топливе — напряжение выше нормы"
modified: "2017-01-02"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4688.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc4688.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source
**Цепь датчика воды в топливе — напряжение выше нормы**

> [!abstract] Процедура · `123-fc4688`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-01-02
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4688.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc4688.pdf)

### Fault Code: 4688

### Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 4688 PID(P): SPN: 97 FMI: 3 Lamp: Maintenance SRT: | Water in Fuel Indicator Sensor Circuit - Voltage Above Normal or Shorted to High Source. High voltage detected at the water in fuel indicator circuit. | None on performance. No water in fuel warning available. |

![[19r99369.png]]

QSK19 CM2150 Marine - Water In Fuel Indicator 2 Sensor Circuit

### Circuit Description

The water-in-fuel indicator sensor is fitted by the original equipment manufacturer (OEM). The water in fuel indicator 2 sensor sends a signal to the engine control module (ECM) when a set volume of water has accumulated in the fuel filter. The water in fuel indicator 2 sensor circuit contains two wires; a water in fuel indicator RETURN (sensor return 1) ground wire and a water in fuel indicator SIGNAL wire.

### Component Location

The water in fuel indicator sensor is mounted by the OEM. Refer to the OEM service manual.

### Shoptalk

The water in fuel sensor is integrated into the fuel filter. It is automatically replaced whenever the fuel filter is replaced.

Possible causes for this fault code include:

- Open return or signal circuit in the harness, connectors, or sensor

- SIGNAL wire shorted to sensor supply or battery voltage.

Refer to Troubleshooting Fault Code t05-4688.
