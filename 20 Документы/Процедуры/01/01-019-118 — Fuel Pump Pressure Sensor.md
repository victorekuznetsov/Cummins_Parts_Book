---
aliases:
  - "Датчик давления топливного насоса"
type: "Процедура"
doc: "01-019-118"
title_en: "Fuel Pump Pressure Sensor"
title_ru: "Датчик давления топливного насоса"
modified: "2003-07-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-118.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-118.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Pump Pressure Sensor
**Датчик давления топливного насоса**

> [!abstract] Процедура · `01-019-118`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-118.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-118.pdf)

### Remove

Disconnect the engine harness from the pressure sensor.

Remove the fuel pump pressure sensor from the fuel pump.

![[19e00169.png]]

### Test

Connect the electronic service tool to the datalink.

![[19800902.png]]

Connect the engine harness to the fuel pump pressure sensor.

Allow the sensor and harness to hang in air.

![[19e00170.png]]

Monitor the fuel pump pressure with the electronic service tool.

The fuel pump pressure **must** be within ±110.3 kPa \[16 psi\] of the barometric pressure sensor value.

If the fuel pump pressure is **not** within specification, the fuel pump pressure sensor **must** be replaced.

Disconnect the electronic service tool.

Disconnect the fuel pump pressure sensor from the engine harness.

![[19800902.png]]

### Install

If a new fuel pump pressure sensor is used, make sure the o-ring is installed.

![[19e00171.png]]

Install the fuel pump pressure sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

Connect the engine harness to the fuel pump pressure sensor.

![[19e00169.png]]
