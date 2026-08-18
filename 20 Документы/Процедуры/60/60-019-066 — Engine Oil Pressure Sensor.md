---
aliases:
  - "Датчик давления моторного масла"
type: "Процедура"
doc: "60-019-066"
title_en: "Engine Oil Pressure Sensor"
title_ru: "Датчик давления моторного масла"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-066.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-066.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Oil Pressure Sensor
**Датчик давления моторного масла**

> [!abstract] Процедура · `60-019-066`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-066.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-066.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative battery cable last.

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.

> [!danger] WARNING · Опасно
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.

- Disconnect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin 4021539.
- Drain lubricating oil from the engine. Refer to Procedure 007-037 (Lubricating Oil System) in Section 7 in the QST30 Service Manual, Bulletin 4021539.

![[ck800wa.png]]

### Remove

[[60-100-002 — Engine Diagrams|Refer to Procedure 100-002 (Engine Diagrams) in Section E for sensor locations.]]

Disconnect the engine harness connector from the engine oil pressure sensor.

Remove the engine oil pressure sensor from the engine block with a deep-well socket, Part Number 3823843, or equivalent.

![[19801029.png]]

### Install

Make sure the engine oil pressure sensor has an o-ring installed.

Install the engine oil pressure sensor.

Tighten the engine oil pressure sensor with deep well socket, Part Number 3823843, or equivalent.

> [!tip] Момент затяжки · Torque Value
> 14 n•m [124 in-lb]

Connect the engine harness connector to the engine oil pressure sensor.

![[19801029.png]]

### Test

Connect INSITE™ electronic service tool to the J1939 data link connector.

![[19800902.png]]

Remove the engine oil pressure sensor.

Connect the engine harness to the engine oil pressure sensor.

Allow the sensor and harness to hang freely.

Monitor the lubricating oil pressure with the INSITE™ electronic service tool.

If the sensor is **not** within ±17.2 kPa \[2.5 psi\] of the ambient pressure, it **must** be replaced.

![[08600402.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative battery cable last.

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.

> [!danger] WARNING · Опасно
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.

- Fill the engine with lubricating oil. Refer to Procedure 007-037 (Lubricating Oil System) in Section 7 in the QST30 Service Manual, Bulletin 4021539.
- Connect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin 4021539.

![[ck800wa.png]]
