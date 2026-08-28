---
aliases:
  - "Цепь аналогового входа уставки мощности (кВт) — напряжение вне нормы"
type: "Процедура"
doc: "01-fc1323"
title_en: "Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to Low Source"
title_ru: "Цепь аналогового входа уставки мощности (кВт) — напряжение вне нормы"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1323.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1323.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to Low Source
**Цепь аналогового входа уставки мощности (кВт) — напряжение вне нормы**

> [!abstract] Процедура · `01-fc1323`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section TF - Troubleshooting Fault Codes
> **Даты:** изменён 2012-05-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-fc1323.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/01-fc1323.pdf)

### Fault Code: 1323

### Analog Input Signal Circuit for Load Govern Kilowatt Setpoint - Voltage Above Normal or Shorted to Low Source

Printable Version

### Overview

| Codes | Reason | Effect |
|---|---|---|
| Fault Code: 1323 PID(P): SPN: FMI: Lamp: Warning SRT: | The analog input signal for the load governed Kilowatt set point is shorted low. | No effect in performance. |

![[19802902.png]]

Load Govern Kilowatt Setpoint - Remote Input Device Circuit

### Circuit Description

The load govern kilowatt setpoint analog input signal is an external input into the engine control module used for load governing of the engine/generator set. The load govern kilowatt setpoint analog input signal is sent to the engine control module from the remote input device.

The engine control module monitors the voltage on the load govern kilowatt setpoint analog input SIGNAL pin and expects to see a voltage vary between 0.5 and 4.5-VDC during normal engine operation. This fault can trip, however, even if the generator set is **not** paralleled.

Low voltage will trip Fault Code 1323 and can be caused by shorts in the SIGNAL wire, an open in the signal, or a failed input device.

### Component Location

Reference Section E for location of the engine control module card cage.

Reference the customer/facility/installation documentation for the location of the remote input device.

### Shoptalk

The possible failure modes are open circuit, short to ground, and failed input device.

Check input voltage with the electronic service tool.

The remote input device **must** be set up to provide a 0 to 5-VDC signal. If this device is set up to provide a 0 to 24-VDC signal, you **must** disable the load govern range checking setpoint using the electronic service tool.

Refer to Troubleshooting Fault Code t05-1323.
