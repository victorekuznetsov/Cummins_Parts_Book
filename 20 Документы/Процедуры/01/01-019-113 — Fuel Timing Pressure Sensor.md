---
aliases:
  - "Датчик давления опережения впрыска"
type: "Процедура"
doc: "01-019-113"
title_en: "Fuel Timing Pressure Sensor"
title_ru: "Датчик давления опережения впрыска"
modified: "2003-07-08"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-113.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-113.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Fuel Timing Pressure Sensor
**Датчик давления опережения впрыска**

> [!abstract] Процедура · `01-019-113`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-07-08
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-113.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-113.pdf)

### Initial Check

Connect the electronic service tool to the datalink.

![[19800902.png]]

Turn the Run/Stop switch to the Run position.

Monitor the timing pressure with the electronic service tool.

The fuel timing pressure **must** be 101.4 kPa \[14.7 psi\] if at sea level or approximately equal to the barometric pressure.

Start the engine and let it idle. Monitor the timing pressure with the electronic service tool. The fuel timing pressure **must** be 413.7 kPa \[60 psi\].

If the fuel timing pressure sensor is **not** within specifications, the fuel timing pressure sensor **must** be replaced.

![[19600070.png]]

### Remove

Clean the control valve body around the fuel timing pressure sensor.

Disconnect the engine harness from the fuel timing pressure sensor.

![[19400306.png]]

Remove the fuel timing pressure sensor using a deep-well socket, Part Number 3823843.

![[19400307.png]]

### Test

Connect the electronic service tool to the datalink.

![[19800902.png]]

Connect the engine harness to the fuel timing pressure sensor.

Allow the sensor and harness hang in air.

![[19e00166.png]]

Monitor the fuel timing pressure with the electronic service tool.

The fuel timing pressure **must** be within ±58.6 kPa \[8.5 psi\] of the barometric pressure sensor value.

If the fuel timing pressure sensor is **not** within specifications, the fuel timing pressure sensor **must** be replaced.

Disconnect the electronic service tool.

Disconnect the fuel timing pressure sensor from the engine harness.

![[19800902.png]]

### Install

If a new fuel timing pressure sensor is used, make sure the o-ring is installed.

Install the sensor into the electronic control valve assembly. Use a deep-well socket, Part Number 3823843, to tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

Connect the engine harness to the timing rail pressure sensor.

![[19400308.png]]
