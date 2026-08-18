---
aliases:
  - "Давление масла в главной магистрали ниже нормы — наивысший уровень"
type: "Процедура"
doc: "82-fc415"
title_en: "Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level"
title_ru: "Давление масла в главной магистрали ниже нормы — наивысший уровень"
modified: "2017-06-19"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level
**Давление масла в главной магистрали ниже нормы — наивысший уровень**

> [!abstract] Процедура · `82-fc415`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2017-06-19
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-fc415.pdf)

### Fault Code: 415

### Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 415 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine Oil Rifle Pressure - Data Valid But Below Normal Operating Range - Most Severe Level. Voltage signal indicates oil pressure has dropped below the shutdown threshold for low oil pressure. | Engine will shut down. Low oil pressure relay driver is energized. |

![[19c00506.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the SIGNAL pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.

### Component Location

Refer to the Engine Diagrams. [[82-100-002 — Engine Diagrams|Refer to Procedure 100-002 in Section E]] for the component location.

### Shoptalk

Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. See Fault Code 141. Verify with the operator at what engine speed the fault occurs. If the engine is being operated a speed to low under load (lugging), the oil pressure can drop below the engine protection limits because of the oil temperature. Oil pressure is a function of engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot, at a low level, regulator has malfunctioned, or a loss is occurring somewhere in the system.

- Refer to specific engine wiring diagram for the output voltage of the pressure sensor.

- NOTE: Some engine models will use the Metri-Pack type connector on this pressure sensor, and some will use the Danfoss™ type connector. The Metri-Pack connector pin designators are alpha and the Danfoss™ connector pin designators are numeric. The steps depicted in this fault code show the Metri-Pack type connector with alpha pin callouts. Refer to specific engine wiring diagrams to determine the correct pin designators for the type of connector.

Refer to Troubleshooting Fault Code t05-415.
