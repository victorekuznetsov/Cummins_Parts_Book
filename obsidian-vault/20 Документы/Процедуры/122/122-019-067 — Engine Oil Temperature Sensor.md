---
aliases:
  - "Датчик температуры моторного масла"
type: "Процедура"
doc: "122-019-067"
title_en: "Engine Oil Temperature Sensor"
title_ru: "Датчик температуры моторного масла"
modified: "2017-04-21"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-067.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-067.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/122"
---

# Engine Oil Temperature Sensor
**Датчик температуры моторного масла**

> [!abstract] Процедура · `122-019-067`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls
> **Даты:** изменён 2017-04-21
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/122/122-019-067.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/122-019-067.pdf)

### General Information

The oil temperature sensor sends engine oil temperature information to the engine control module (ECM). The exact location of the sensor varies with engine family. Refer to the appropriate base engine manual.

![[19801851.png]]

### Remove

> [!danger] WARNING · Опасно
> Some state and federal agencies in the United States of America have determined that used engine oil can be carcinogenic and can cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. Always use the proper environmental procedures to dispose of the oil.

Partially drain the engine lubricating oil system. Refer to Procedure 007-037 in Section 7.

Lift up on the locking tab and pull the electrical connectors apart.

Remove the sensor.

![[19800823.png]]

### Resistance Check

Disconnect the sensor connector.

Select the resistance function on the multimeter.

Attach the appropriate test leads to the multimeter probes.

Touch the two test leads to the two terminals on the sensor. Measure the resistance.

The multimeter **must** show between 115 and 244k ohms. The resistance value is temperature-dependent as shown in the table below.

| Temperature | Range |  |
|---|---|---|
| °C | °F | Ohms |
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

The multimeter **must** show greater than 100k ohms, which is an open circuit. If the circuit is **not** closed, then there is a short within the sensor to chassis ground. Replace the sensor.

![[19801621.png]]

### Install

Verify that the new sensor has an o-ring.

Lubricate the sensor o-ring with clean engine oil.

Install the sensor into the engine.

Tighten the sensor.

> [!tip] Момент затяжки · Torque Value
> 15 n•m [11 ft-lb]

Push the connectors together until they lock.

Fill the engine to the proper level with lubricating oil and operate the engine to check for leaks.

![[19800824.png]]
