---
aliases:
  - "Датчик давления топлива в рампе"
type: "Процедура"
doc: "98-019-115"
title_en: "Rail Fuel Pressure Sensor"
title_ru: "Датчик давления топлива в рампе"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 13
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-115.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-115.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Rail Fuel Pressure Sensor
**Датчик давления топлива в рампе**

> [!abstract] Процедура · `98-019-115`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-115.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-115.pdf)

### General Information

The rail pressure sensor is mounted in the rail line between the fuel pump and the rail inlet to the block. This sensor monitors the fuel pressure in the rail line.

> [!note] Note · Примечание
> Each engine type will have the sensor mounted in a different location. Refer to the appropriate base engine manual.

![[19801765.png]]

### Remove

Disconnect the sensor by lifting the locking tab and pulling apart the connector.

![[19801786.png]]

Remove the sensor.

![[19801787.png]]

### Install

Verify that the new sensor has an o-ring. Lubricate the o-ring with clean engine oil.

Install the new sensor. Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 16 n•m [142 in-lb]

![[19801788.png]]

> [!warning] CAUTION · Осторожно
> Use only Cummins recommended lubricant DS-ES, Part No. 38232934. Other lubricants, such as lubricating oil or grease in the connectors, can cause ECM damage, poor engine performance, or premature connector pin wear.

Apply a small amount of lubricant to the connector terminals. Do **not** fill the entire connector cavity with lubricant.

Connect the sensor connector. Make sure the locking tab clicks into place.

![[19801786.png]]

### Voltage Check

Disconnect the rail pressure sensor from the main engine harness.

![[19801786.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use the following test lead when taking a measurement: Part No. 3824774 - breakout cable.

Connect the breakout cable, Part No. 3824774, to the rail pressure sensor and the main engine harness.

Set multimeter to read VDC.

Turn keyswitch ON.

![[19802632.png]]

Install supply (pin A) and return (pin B) into the multimeter.

The voltage should measure between 4.75 VDC and 5.25 VDC.

If the voltage is **not** between 4.75 VDC and 5.25 VDC, troubleshoot the main engine harness. Refer to Procedures 019-250 and 019-043.

![[19802633.png]]

Connect all components after completing the repair.

![[nobox.png]]

Disconnect the rail pressure sensor from the main engine harness.

![[19801786.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use the following test lead when taking a measurement: Part No. 3824774 - breakout cable.

Connect the breakout cable, Part No. 3824774, to the rail pressure sensor and the main engine harness.

Set multimeter to read VDC.

Turn keyswitch ON.

![[19802632.png]]

Install signal (pin C) and return (pin B) into the multimeter.

The voltage should measure between 0.46 VDC and 4.56 VDC.

If the voltage is **not** between 0.46 VDC and 4.56 VDC, replace the rail pressure sensor. Refer to Procedure 019-115.

![[19802634.png]]

Connect all components after completing the repair.

![[nobox.png]]
