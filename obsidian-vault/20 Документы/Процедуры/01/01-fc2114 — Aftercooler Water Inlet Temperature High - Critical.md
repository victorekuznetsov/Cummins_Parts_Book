---
aliases:
  - "Высокая температура воды на входе охладителя — критично"
type: "Процедура"
doc: "01-fc2114"
title_en: "Aftercooler Water Inlet Temperature High - Critical"
title_ru: "Высокая температура воды на входе охладителя — критично"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2114.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2114.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Aftercooler Water Inlet Temperature High - Critical
**Высокая температура воды на входе охладителя — критично**

> [!abstract] Процедура · `01-fc2114`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2114.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2114.pdf)

### Fault Code: 2114

### Aftercooler Water Inlet Temperature High - Critical

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2114 PID(P): SPN: FMI: Lamp: Shutdown SRT: | Engine coolant temperature 2 high - critical. Voltage signal indicates aftercooler water inlet temperature has exceeded the shutdown threshold for high aftercooler water inlet temperature. | Engine will shut down. |

![[19802424.png]]

Aftercooler Water Inlet Temperature Sensor Circuit

### Circuit Description

The aftercooler water inlet temperature sensor is used by the electronic control module (ECM) to monitor the ability of the engine cooling system to cool down the engine coolant. The aftercooler water inlet temperature value is used by the ECM for the engine protection system. The ECM monitors the voltage on the aftercooler water inlet temperature signal pin and expects to see a voltage vary between 0.5 and 4.5 VDC during normal engine operation.

### Component Location

Refer to Procedure 100-002 for the component location.

### Shoptalk

Make sure that the water inlet flow is **not** restricted. The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-2114
