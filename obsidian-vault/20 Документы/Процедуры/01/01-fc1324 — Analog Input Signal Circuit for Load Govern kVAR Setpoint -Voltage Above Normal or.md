---
aliases:
  - "Цепь аналогового входа уставки кВАр — напряжение выше нормы"
type: "Процедура"
doc: "01-fc1324"
title_en: "Analog Input Signal Circuit for Load Govern kVAR Setpoint -Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь аналогового входа уставки кВАр — напряжение выше нормы"
modified: "2012-05-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 1
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1324.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1324.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Analog Input Signal Circuit for Load Govern kVAR Setpoint -Voltage Above Normal or Shorted to High Source
**Цепь аналогового входа уставки кВАр — напряжение выше нормы**

> [!abstract] Процедура · `01-fc1324`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1324.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1324.pdf)

### Fault Code: 1324

### Analog Input Signal Circuit for Load Govern kVAR Setpoint -Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1324 PID(P): SPN: FMI: Lamp: Warning SRT: | The analog input signal for the load governed kilovolt-ampere setpoint is shorted high. | No action is taken by the engine control module. Possible loss of performance. |

![[19802903.png]]

Load Govern Kilovolt-Ampere Setpoint - Remote Input Device Circuit

### Circuit Description

The load govern kilovolt-ampere setpoint analog input signal is an external input into the engine control module used to control and vary the kilovolt-ampere output of the alternator while the generator set is paralleled to the utility. The load govern kilovolt-ampere setpoint analog input signal is sent to the engine control module from a remote device, usually a PLC that is monitoring another source to determine the amount of power to be provided by the generator.

The engine control module monitors the voltage on the load govern kilovolt-ampere setpoint analog input signal pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal engine operation.

High voltage will trip Fault Code 1324 and can be caused by shorts in the signal wire or a failed input device.

### Component Location

Reference Section E for location of the engine control module card cage.

Reference the customer/facility/installation documentation for the location of the remote input device.

### Shoptalk

The possible failure modes are open circuit, short to battery positive (+), and failed input device.

Make sure shields and grounds are good.

Check input voltage using INSITE™ electronic service tool.

Can reduce kilovolt-amperes to zero and run the unit at a unity PF.

Refer to Troubleshooting Fault Code t05-1324.
