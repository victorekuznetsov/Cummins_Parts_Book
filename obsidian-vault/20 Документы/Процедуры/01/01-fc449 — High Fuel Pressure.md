---
aliases:
  - "Высокое давление топлива"
type: "Процедура"
doc: "01-fc449"
title_en: "High Fuel Pressure"
title_ru: "Высокое давление топлива"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc449.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc449.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# High Fuel Pressure
**Высокое давление топлива**

> [!abstract] Процедура · `01-fc449`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2010-07-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc449.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc449.pdf)

### Fault Code: 449

### High Fuel Pressure

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 449 PID(P): SPN: FMI: Lamp: Warning SRT: | High fuel supply pressure was detected at the fuel pressure sensor. | No action is taken by the ECM. Possible black smoke. |

![[05c00120.png]]

Fuel System Circuit

### Circuit Description

The gear pump draws fuel from the fuel tank through the fuel filter and anti-drainback valve. The gear pump develops 689 to 2206 kPa \[100 to 320 psi\] of fuel pressure. The fuel flows through the fuel filter screen and fuel shutoff valve to the fueling and timing actuators and the fuel pressure sensor. The 1724 kPa \[250 psi\] regulator controls the fuel pressure.

### Component Location

| Hydraulic Fuel System Circuit Components |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|
| 1 | Quick-disconnect pressure tap - suction side | 5 | Fuel inlet | 9 | Fuel shutoff valve solenoid | 13 | Front timing actuator |
| 2 | 2206 kPa \[320 psi\] pressure regulator | 6 | Fuel filter/water separator | 10 | Quick-disconnect pressure tap - pressure side | 14 | Rear timing actuator |
| 3 | Fuel return line fitting | 7 | Fuel/water separator drain valve/Water-in-fuel sensor | 11 | Fuel pressure sensor | 15 | Rear metering actuator |
| 4 | 36-micron filter screen | 8 | 1724 kPa \[250 psi\] pressure regulator | 12 | Front metering actuator |  |  |

### Shoptalk

The fuel pressure is monitored by the ECM. If the fuel pressure is outside of an acceptable range the fault code is activated.

Refer to Troubleshooting Fault Code t05-449
