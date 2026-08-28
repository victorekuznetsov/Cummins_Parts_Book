---
aliases:
  - "Датчик температуры воды на входе охладителя — замыкание на массу"
type: "Процедура"
doc: "01-fc2112"
title_en: "Aftercooler Water Inlet Temperature Sensor - Shorted Low"
title_ru: "Датчик температуры воды на входе охладителя — замыкание на массу"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2112.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2112.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Aftercooler Water Inlet Temperature Sensor - Shorted Low
**Датчик температуры воды на входе охладителя — замыкание на массу**

> [!abstract] Процедура · `01-fc2112`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc2112.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc2112.pdf)

### Fault Code: 2112

### Aftercooler Water Inlet Temperature Sensor - Shorted Low

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 2112 PID(P): SPN: FMI: Lamp: Warning SRT: | Engine coolant temperature 2 sensor circuit - shorted low. This was formerly called the aftercooler water inlet temperature sensor. | No engine protection for aftercooler water inlet temperature. |

![[19803592.png]]

Aftercooler Water Inlet Temperature Sensor Circuit

### Circuit Description

The aftercooler water inlet temperature sensor is used by the electronic control module (ECM) to monitor the ability of the engine cooling system to cool down the engine coolant. The aftercooler water inlet temperature is used by the ECM for the engine protection system. The ECM monitors the voltage on the aftercooler water inlet temperature signal pin and expects to see a voltage vary between 0.5 and 4.5 VDC during normal engine operation. Low voltage will trip Fault Code 2112 and can be caused by shorts in the signal, or return wires, an open in the signal wire, or a failed sensor.

### Component Location

Refer to Procedure 100-002 for the component location.

### Shoptalk

The possible failure modes are open circuit, short to ground, failed sensor, and loss of supply voltage inside the ECM. The resistance of the sensor varies with the temperature.

Refer to Troubleshooting Fault Code t05-2112
