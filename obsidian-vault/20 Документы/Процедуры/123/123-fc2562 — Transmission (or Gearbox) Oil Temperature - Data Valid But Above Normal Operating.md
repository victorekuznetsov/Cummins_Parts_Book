---
aliases:
  - "Температура масла трансмиссии выше нормы — наивысший уровень"
type: "Процедура"
doc: "123-fc2562"
title_en: "Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level"
title_ru: "Температура масла трансмиссии выше нормы — наивысший уровень"
modified: "2016-12-12"
engines:
  - "41349633"
  - "41353297"
families:
  - "QSK19"
manuals:
  - "4022094"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2562.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc2562.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK19"
  - "группа/123"
---

# Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level
**Температура масла трансмиссии выше нормы — наивысший уровень**

> [!abstract] Процедура · `123-fc2562`
> **Двигатели:** [[41349633 — QSK19 CM2150 MCRS CPL 3666|41349633]], [[41353297 — QSK19 CM2150 MCRS CPL 3666|41353297]]
> **Семейство:** QSK19
> **Входит в руководства:** [[4022094 — QSK19 CM2150 and CM2670 Electronic Control System Troubleshooting and Repair Manual|4022094]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2016-12-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/123/123-fc2562.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/123-fc2562.pdf)

### Fault Code: 2562

### Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2562 PCODE(P): SPN: 175 FMI: 0 Lamp: Red SRT: | Transmission (or Gearbox) Oil Temperature - Data Valid But Above Normal Operating Range - Most Severe Level. Transmission (or gearbox) oil temperature sensor indicates the transmission (or gearbox) oil temperature is above the protection limit. | **No** engine protection for transmission oil temperature. |

![[19r99370.png]]

Transmission (or Gearbox) Oil Temperature Sensor Circuit

### Circuit Description

Transmission (or gearbox) oil temperature sensor is used by the engine control module (ECM) to monitor the transmission oil temperature. The ECM monitors the voltage on the SIGNAL pin and converts it to a temperature value.

### Component Location

The transmission (or gearbox) oil temperature sensor is located in the transmission.

### Shoptalk

There are multiple ECMs for the engine models included in this manual. Each ECM has an individual source address that displays when INSITE™ electronic service tool is connected. When troubleshooting a fault code, use the source address displayed in INSITE™ electronic service tool to determine which ECM and circuit is affected.

This fault code indicates that the transmission (or gearbox) temperature has exceeded the protection limits for high transmission (or gearbox) temperature.

Refer to Troubleshooting Fault Code 2562.
