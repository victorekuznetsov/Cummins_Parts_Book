---
aliases:
  - "Цепь аналогового входа уставки мощности (кВт) — напряжение выше нормы"
type: "Процедура"
doc: "01-fc1322"
title_en: "Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to High Source"
title_ru: "Цепь аналогового входа уставки мощности (кВт) — напряжение выше нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1322.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1322.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to High Source
**Цепь аналогового входа уставки мощности (кВт) — напряжение выше нормы**

> [!abstract] Процедура · `01-fc1322`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1322.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1322.pdf)

### Fault Code: 1322

### Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to High Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1322 PID(P): SPN: FMI: Lamp: Warning SRT: | The analog input signal for the load governed Kilowatt set point is shorted high. | No effect on performance. |

![[19802902.png]]

Load Govern Kilowatt Set Point - Remote Input Device Circuit

### Circuit Description

The load govern kilowatt set point analog input signal is an external input into the engine control module used to control and vary the alternator kilowatt output while the generator set is parallel to the utility. The load govern kilowatt set point analog input signal is sent to the engine control module from the remote input device.

The engine control module monitors the voltage on the load govern kilowatt set point analog input SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal engine operation.

High voltage will trip Fault Code 1322 and can be caused by shorts in the SIGNAL wire or a failed input device.

### Component Location

Reference Section E for location of the engine control module card cage.

Reference the customer/facility/installation documentation for the location of the remote input device.

### Shoptalk

The possible failure modes are open circuit, short to battery positive (+), and failed input device.

Verify that normal operating range of input device is 0.1 to 5.0-VDC.

Make sure shields and grounds are good.

The remote input device **must** be set up to provide a 0 to 5-VDC signal. If this device is set up to provide a 0 to 24-VDC signal, the load govern range checking set point **must** be disabled using INSITE™ electronic service tool.

Refer to Troubleshooting Fault Code t05-1322.
