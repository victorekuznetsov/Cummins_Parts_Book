---
aliases:
  - "Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень"
type: "Процедура"
doc: "123-fc4615"
title_en: "Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень"
modified: "2015-03-09"
engines:
  - "41349633"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4615.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc4615.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level
**Давление подачи топливного насоса — данные достоверны, но выше нормы — наивысший уровень**

> [!abstract] Процедура · `123-fc4615`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2015-03-09
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc4615.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/123-fc4615.pdf)

### Fault Code: 4615

### Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 4615 PID(P): SPN: 94 FMI: 0/0 Lamp: Amber SRT: | Fuel Pump Delivery Pressure - Data Valid But Above Normal Operating Range - Most Severe Level. The fuel pump supply pressure is very high. | Low power or engine smoke. |

![[19401816.png]]

QSK19 CM2150 Industrial - Fuel Delivery Pressure Sensor Circuit

![[19401817.png]]

QSK19 CM2150 Marine- Fuel Delivery Pressure Sensor Circuit

![[r8f00011.png]]

QSK19 CM2150 Power Generation - Fuel Delivery Pressure Sensor Circuit

### Circuit Description

The fuel delivery pressure sensor is used by the engine control module (ECM) to monitor fuel delivery pressure directly before the Stage 2 filter. The ECM monitors the voltage on the SIGNAL pin and converts this to a pressure value.

### Component Location

The fuel delivery pressure sensor is located in the Stage 2 fuel filter head. [[123-100-002-tr — Engine Diagrams|Refer to Procedure 100-002 in Section E.]]

### Shoptalk

Possible causes of this fault code include:

- Stage 2 fuel filter restriction

- Pinched or damaged fuel supply line

- Stuck gerotor pump fuel pressure regulator located in the high-pressure pump.

Refer to Troubleshooting Fault Code t05-4615.
