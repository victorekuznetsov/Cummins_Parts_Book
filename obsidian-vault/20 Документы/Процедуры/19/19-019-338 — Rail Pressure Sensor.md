---
aliases:
  - "Датчик давления в топливной рампе"
type: "Процедура"
doc: "19-019-338"
title_en: "Rail Pressure Sensor"
title_ru: "Датчик давления в топливной рампе"
modified: "2002-09-27"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 7
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-338.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-338.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Rail Pressure Sensor
**Датчик давления в топливной рампе**

> [!abstract] Процедура · `19-019-338`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-338.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-338.pdf)

### Initial Check

Connect an electronic service tool to the vehicle datalink.

![[19400357.png]]

Turn the keyswitch to the ON position.

Monitor the rail pressure with the electronic service tool.

Rail pressure should be zero psi.

![[19800978.png]]

Start the engine and let it idle.

Monitor the rail pressure with the electronic service tool.

The rail pressure should be 15 psi.

![[19800979.png]]

### Remove

Remove the ECM. Refer to Procedure 019-031.

Clean the control valve body around the pressure sensor.

Disconnect the sensor connector from the engine harness.

![[19400371.png]]

Remove the pressure sensor with a 1 1/4-inch deep flank drive socket, Part Number 3823843, and a ratchet.

![[19400372.png]]

### Install

Inspect the new sensor for an o-ring.

Install the new pressure sensor and tighten.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

Connect the sensor connection.

![[19400373.png]]

Install the ECM. Refer to Procedure 019-031.

![[19400295.png]]
