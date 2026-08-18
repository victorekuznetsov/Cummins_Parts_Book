---
aliases:
  - "Датчик давления подачи масла к топливному насосу"
type: "Процедура"
doc: "56-019-679"
title_en: "Fuel Pump Lubricating Oil Supply Pressure Sensor"
title_ru: "Датчик давления подачи масла к топливному насосу"
modified: "2020-05-14"
engines:
  - "33239746"
  - "33239899"
families:
  - "K38/K50 · QSK38, QSK50, QSK60"
manuals:
  - "4022102"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-019-679.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/56-019-679.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K38/K50"
  - "группа/56"
---

# Fuel Pump Lubricating Oil Supply Pressure Sensor
**Датчик давления подачи масла к топливному насосу**

> [!abstract] Процедура · `56-019-679`
> **Двигатели:** [[33239746 — QSK60 CM2150 MCRS CPL 3451|33239746]], [[33239899 — QSK50 CM2150 MCRS CPL 3379|33239899]]
> **Семейство:** K38/K50 · QSK38, QSK50, QSK60
> **Входит в руководства:** [[4022102 — QSK38, QSK50, and QSK60 CM2150 Electronic Control System Troubleshooting and Repair M|4022102]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2020-05-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/56/56-019-679.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/56-019-679.pdf)

### Component Diagram

![[07e00235.png]]

Engine Fuel Pump Lubricating Oil Pressure Sensor

### Select Service Tools

#### Recommended Cummins® Service Tools

- INSITE™ electronic service tool

#### Additional Service Items

- No additional service items required.

### General Information

The Engine fuel pump lubricating oil pressure sensor measures fuel pump lubricating oil pressure at the outlet of the lubricating oil filter head. The engine fuel pump lubricating oil pressure sensor is located in the engine fuel pump lubricating oil filter head mounted to the top of the fuel pump adapter drive. Certain engines may have the filter head mounted remotely.

The mating connector on the engine wiring harness is an ITT Cannon™ connector.

The INSITE™ electronic service tool parameter for this sensor is fuel pump lubricating oil pressure. The sensor value is displayed as gauge pressure.

### Initial Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Disconnect batteries and power supplies. See equipment manufacturer service information.

Disconnect air supply line from air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.

> [!danger] WARNING · Опасно
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.

> [!note] Note · Примечание
> Some oil may drain from port in filter head when plug is removed.

Remove the Fuel Pump Lubricating Oil Filter Head Outlet Pressure Port (2).

Install Compuchek™ fitting into M14 port.

Connect pressure transducer and multimeter to Compuchek™ fitting.

![[07800464.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Connect batteries and power supplies. See equipment manufacturer service information.

Connect air supply line to air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.

Connect INSITE™ electronic service tool to engine data link.

Start engine and run at idle.

Idle engine for at least 5 minutes to allow oil pressure to stabilize.

If fuel pump lubricating oil pressure value in INSITE™ electronic service tool is **not** within 48 kPa \[7 psi\] of pressure transducer measurement, replace Engine fuel pump lubricating oil pressure sensor.

![[19203975.png]]

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

Shut engine OFF.

Disconnect batteries and power supplies. See equipment manufacturer service information

Disconnect air supply line from air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.

> [!danger] WARNING · Опасно
> Some state and federal agencies have determined that used engine oil can be carcinogenic and cause reproductive toxicity. Avoid inhalation of vapors, ingestion, and prolonged contact with used engine oil. If not reused, dispose of in accordance with local environmental regulations.

> [!danger] WARNING · Опасно
> To reduce the possibility of personal injury, avoid direct contact of hot oil with your skin.

Remove Compuchek™ fitting.

Install M14 straight thread o-ring plug. Use new o-ring seal.

> [!tip] Момент затяжки · Torque Value
> 11 n•m [98 in-lb]

![[07800464.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect batteries and power supplies. See equipment manufacturer service information.
- Disconnect air supply line from air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.

### Remove

Disconnect engine wiring harness from Engine fuel pump lubricating oil pressure sensor by turning connector **counterclockwise**.

Remove sensor.

Remove and discard o-ring seal.

![[07e00235.png]]

### Clean and Inspect for Reuse

Clean Engine fuel pump lubricating oil pressure sensor. Use clean, lint-free cloth.

Inspect sensor.

Replace sensor if:

- Connector shell cracked or broken
- Connector seal missing or damaged
- Connector terminals contaminated with dirt, debris, or moisture
- Connector terminals corroded, bent, broken, pushed back, or expanded
- Threads damaged or corroded.

![[19j00113.png]]

Inspect engine wiring harness connector.

Replace connector if:

- Shell cracked or broken
- Seals missing or damaged
- Terminals contaminated with dirt, debris, or moisture
- Terminals corroded, bent, broken, pushed back, or expanded.

[[99-019-209 — ITT Cannon Connector Series|Refer to Procedure 019-209]] in Section 19.

![[19j00114.png]]

### Install

Install Engine fuel pump lubricating oil pressure sensor. Use new o-ring seal.

> [!tip] Момент затяжки · Torque Value
> 11 n•m [98 in-lb]

Connect extension wiring harness to sensor.

![[07e00235.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect air supply line to air starting motor, if equipped. Refer to Procedure 012-022 in Section 12.
- Connect batteries and power supplies. See equipment manufacturer service information.
- Fill lubricating oil pan, if necessary. Refer to Procedure 007-037 in Section 7.
- Operate engine. Check for leaks.
