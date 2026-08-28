---
aliases:
  - "Датчик температуры охлаждающей жидкости"
type: "Процедура"
doc: "98-019-019"
title_en: "Engine Coolant Temperature Sensor"
title_ru: "Датчик температуры охлаждающей жидкости"
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
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-019.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-019.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Coolant Temperature Sensor
**Датчик температуры охлаждающей жидкости**

> [!abstract] Процедура · `98-019-019`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-04-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-019.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-019.pdf)

### General Information

The sensor sends engine coolant temperature information to the ECM. The sensor location varies with engine family.

> [!note] Note · Примечание
> **Not** all CENTRY™ applications will use this sensor. Refer to the OEM troubleshooting and repair manual for system features.

![[19801851.png]]

### Remove

> [!danger] WARNING · Опасно
> Wait until the coolant temperature is below 50°C \[120°F\] before removing the coolant system pressure cap. Failure to do so can cause personal injury from heated coolant spray or steam.

Drain the cooling system. Refer to the appropriate base engine troubleshooting and repair manual for the procedure.

![[19801858.png]]

Make sure the sensor connector is disconnected.

Remove the sensor.

![[19801853.png]]

### Install

Verify that the new sensor has an o-ring. Lubricate the o-ring using clean engine oil. Install the new sensor into the engine. Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 35 n•m [26 ft-lb]

![[19801860.png]]

Flush and clean the harness connector pins using contact cleaner, Part No. 3824510.

> [!warning] CAUTION · Осторожно
> Use only Cummins-recommended lubricant DS-ES, Part No. 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause ECM damage, poor engine performance, or premature connector pin wear.

Apply a small amount of lubricant to the connector terminals. Do **not** fill the entire connector cavity with lubricant. Connect the sensor connector. Make sure the connector locks into place. Fill the cooling system and operate the engine to check for leaks.

![[19801861.png]]

### Resistance Check

Disconnect the sensor connector.

Select the resistance function on the multimeter. Touch the two multimeter leads to the two terminals on the sensor.

Measure the resistance. The multimeter **must** show between 175 and 244k ohms.

The resistance value is temperature dependent as shown in the table below.

![[19801852.png]]

| Temperature | Temperature | Resistance Range |
|---|---|---|
| (°C) | \[°F\] | (ohms) |
| 0 | 32 | 30k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1350 to 1500 |
| 100 | 212 | 600 to 675 |

If the resistance is out of range, the sensor has failed.

Replace the sensor.

![[19801853.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter leads to either of the pins on the sensor side of the sensor connector. Touch the other multimeter lead to a good, clean surface on the engine block.

Measure the resistance. The multimeter **must** show greater than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short within the sensor to chassis ground.

Replace the sensor.

![[19801854.png]]
