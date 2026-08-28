---
aliases:
  - "Датчик температуры моторного масла"
type: "Процедура"
doc: "98-019-067"
title_en: "Engine Oil Temperature Sensor"
title_ru: "Датчик температуры моторного масла"
modified: "2003-04-01"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-067.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Oil Temperature Sensor
**Датчик температуры моторного масла**

> [!abstract] Процедура · `98-019-067`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-067.pdf)

### General Information

The oil temperature sensor sends engine oil temperature information to the ECM. The location of the sensor varies with engine family. Refer to the appropriate base engine manual.

> [!note] Note · Примечание
> **Not** all CENTRY™ applications will use this sensor. Refer to the OEM manual for system features.

![[19801851.png]]

### Remove

Make sure the sensor connector is disconnected. Remove the sensor.

![[19801853.png]]

### Install

Verify that the new sensor has an o-ring. Lubricate the o-ring with clean engine oil.

Install the new sensor into the engine. Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 35 n•m [26 ft-lb]

![[19801860.png]]

Connect the sensor connector. Make sure the connector locks into place.

![[19801861.png]]

### Resistance Check

Disconnect the sensor connector. Select the resistance function on the multimeter. Attach the appropriate test leads to the multimeter probes. Touch the two test leads to the two terminals on the sensor. Measure the resistance. The multimeter **must** show between 115 and 244k ohms. The resistance value is temperature-dependent as shown in the table below.

| Temperature | Temperature | Range |
|---|---|---|
| (°C) | \[°F\] | (ohms) |
| 0 | 32 | 33k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

![[19801852.png]]

If the resistance is out of range, then the sensor has failed.

Replace the sensor.

![[19801853.png]]

### Check for Short Circuit to Ground

Touch the multimeter lead with the attached appropriate test lead to either terminal on the sensor. Touch the other multimeter lead to a good, clean surface on the engine block.

![[19801854.png]]

Measure the resistance.

The multimeter **must** show greater than 100k ohms, which is an open circuit. If the circuit is **not** closed, then there is a short within the sensor to chassis ground.

Replace the sensor.

![[19801621.png]]
