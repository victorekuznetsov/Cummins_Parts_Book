---
aliases:
  - "Датчик давления моторного масла"
type: "Процедура"
doc: "98-019-066"
title_en: "Engine Oil Pressure Sensor"
title_ru: "Датчик давления моторного масла"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-066.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-066.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Oil Pressure Sensor
**Датчик давления моторного масла**

> [!abstract] Процедура · `98-019-066`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-066.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-066.pdf)

### General Information

The oil pressure sensor (OPS) sends engine oil pressure information to the ECM.

The location of the sensor varies with engine family. Refer to the appropriate base engine manual.

> [!note] Note · Примечание
> **Not** all CENTRY™ applications will use this sensor. Refer to the OEM manual for system features.

![[nobox.png]]

### Remove

Disconnect the lubricating oil pressure sensor from the main engine harness.

Using a 1-1/4-inch socket, remove the oil pressure sensor.

![[19900794.png]]

### Install

Verify that there is an o-ring on the sensor. Lubricate the o-ring with clean engine oil.

Using a 1-1/4-inch socket, install the oil pressure sensor.

> [!tip] Момент затяжки · Torque Value
> 11 n•m [97 in-lb]

Connect the OPS to the main engine harness. Make sure the connector locks in place.

![[19900794.png]]

### Voltage Check

Disconnect the oil pressure sensor from the OEM harness.

![[19801861.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use the following test lead when taking a measurement:Part No. 3824775 - breakout cable.

Connect the breakout cable, Part No. 3824775, to the oil pressure sensor and the OEM harness.

Set multimeter to read VDC.

Turn keyswitch ON.

![[19802632.png]]

Install supply (pin A) and return (pin B) into the multimeter.

The voltage should measure between 4.75 VDC and 5.25 VDC.

If the voltage is between 4.75 VDC and 5.25 VDC check the supply voltage with the sensor disconnected.

![[19802633.png]]

Disconnect the oil pressure sensor from the OEM harness.

![[19801861.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use the following test lead when taking a measurement:Part No. 3824775 - breakout cable.

Connect the breakout cable, Part No. 3824775, to the OEM harness. Do **not** connect the sensor.

Set multimeter to read VDC.

Turn keyswitch ON.

![[19802632.png]]

Install supply (pin A) and return (pin B) into the multimeter.

The voltage should measure between 4.75 VDC and 5.25 VDC.

If the voltage is between 4.75 VDC and 5.25 VDC replace the oil pressure sensor. Refer to the OEM troubleshooting and repair manual.

If the voltage is **not** between 4.75 VDC and 5.25 VDC troubleshoot the OEM harness or ECM. Refer to the OEM troubleshooting and repair manual.

![[19802633.png]]

Connect all components after completing the repair.

![[nobox.png]]

Disconnect the oil pressure sensor from the OEM harness.

![[19801861.png]]

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use the following test lead when taking a measurement:Part No. 3824775 - breakout cable.

Connect the breakout cable, Part No. 3824775, to the oil pressure sensor and the OEM harness.

Set multimeter to read VDC.

Turn keyswitch ON.

![[19802632.png]]

Install signal (pin C) and return (pin B) into the multimeter.

The voltage should measure between 0.46 VDC and 0.58 VDC.

If the voltage is **not** between 0.46 VDC and 0.58 VDC, replace the oil pressure sensor. Refer to the OEM troubleshooting and repair manual.

![[19802634.png]]

Connect all components after completing the repair.

![[nobox.png]]
