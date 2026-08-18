---
aliases:
  - "Давление масла — защита двигателя"
type: "Процедура"
doc: "87-fc415"
title_en: "Oil Pressure - Engine Protection"
title_ru: "Давление масла — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc415.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc415.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Oil Pressure - Engine Protection
**Давление масла — защита двигателя**

> [!abstract] Процедура · `87-fc415`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc415.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc415.pdf)

### Fault Code: 415

### Oil Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 415 PID(P): P100 SPN: 100 FMI: 1 Lamp: Engine Protection SRT: | Low oil pressure has been detected. Voltage signal at oil pressure signal pin 33 of the engine harness indicates the oil pressure is lower than calibrated limits (less than 34 kPa \[5 psi\] at engine speeds less than 600 rpm; 207 kPa \[30 psi\] at engine speeds greater than 1600 rpm). | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after the alert. |

![[19900357.png]]

Oil Pressure Sensor Circuit

### Circuit Description

The oil pressure sensor is used by the electronic control module (ECM) to monitor the lubricating oil pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The oil pressure value is used by the ECM for the engine protection system.

### Component Location

The oil pressure sensor is located on the left-hand side of the engine block, behind the fuel pump.

### Shoptalk

- Confirm that the oil pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. Refer to Fault Code 141.

- Verify with the driver at what engine speed the fault occurs. If the engine is being operated at too low a speed under load (lugging), the oil pressure can drop below the engine protection limits because of the oil temperature.

- Oil pressure is a function of the engine speed, oil level, and regulator function. Operating the engine at a low speed under load will **not** cause the oil pressure to be low unless the oil is hot at a low level, regulator has malfunctioned, or a loss is occurring somewhere in the system.

Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

Refer to Troubleshooting Fault Code t05-415
