---
aliases:
  - "Давление охлаждающей жидкости — защита двигателя"
type: "Процедура"
doc: "87-fc233"
title_en: "Coolant Pressure - Engine Protection"
title_ru: "Давление охлаждающей жидкости — защита двигателя"
modified: "2010-07-29"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 1
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc233.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc233.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Coolant Pressure - Engine Protection
**Давление охлаждающей жидкости — защита двигателя**

> [!abstract] Процедура · `87-fc233`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-fc233.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/87-fc233.pdf)

### Fault Code: 233

### Coolant Pressure - Engine Protection

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 233 PID(P): P109 SPN: 109 FMI: 1 Lamp: Engine Protection SRT: | Low coolant pressure has been detected. Voltage signal at coolant pressure signal pin 24 of the engine harness indicates coolant pressure lower than 28 kPa \[4 psi\] at 800 rpm; 41 kPa \[6 psi\] at 1300 rpm; 76 kPa \[11 psi\] at 1800 rpm; 96 kPa \[14 psi\] at 2000 rpm; and 103 kPa \[15 psi\] at 2100 rpm. | Calibration-dependent progressive power and speed derate and engine shutdown with increasing time after alert. |

![[19a00129.png]]

Coolant Pressure Sensor Circuit

### Circuit Description

The coolant pressure sensor is used by the electronic control module (ECM) to monitor the coolant pressure. The ECM monitors the voltage on the signal pin and converts this to a pressure value. The coolant pressure value is used by the ECM for the engine protection system.

### Component Location

The coolant pressure sensor is located on the left side of the engine in the thermostat housing.

### Shoptalk

- Confirm that the coolant pressure sensor supply voltage is between 4.75 and 5.25 VDC at the sensor. Refer to Fault Code 232.

- Verify with the operator at what engine speed the fault occurs. If the engine is being operated at too low a speed under load, the coolant pressure can drop below the engine protection limits.

Note: The number of fault lamps could be reduced to two for certain OEMs. The engine protection and stop lamps are wired together as a red lamp. The warning lamp remains a yellow lamp.

Refer to Troubleshooting Fault Code t05-233
