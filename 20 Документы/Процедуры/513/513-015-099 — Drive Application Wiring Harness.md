---
type: "Процедура"
doc: "513-015-099"
title_en: "Drive Application Wiring Harness"
modified: "2019-10-15"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 6
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-099.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-099.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Drive Application Wiring Harness

> [!abstract] Процедура · `513-015-099`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 15 - Instruments and Controls - Group 15
> **Даты:** изменён 2019-10-15
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-015-099.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-015-099.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Electrical test lead, Part Number 3824812
- Electrical test lead, Part Number 3823993
- Electrical test lead, Part Number 3823994.

#### Additional Service Items

- No additional service items required.

### General Information

**PS102**

The drive application wiring harness connects the system enable signal, exhaust temperature sensor, neutral safety switch, and transmission gear oil pressure and temperature sensors to the engine control module (ECM) original equipment manufacturer (OEM) interface round 19 pin connection located at the rear of the engine.

**PS103**

The drive application wiring harness connects the transmission gear oil pressure and temperature sensor to the ECM and does not go through the 19 pin connection. These sensors are monitored through the ECM. Refer to the engine service manual for troubleshooting.

> [!note] Note · Примечание
> The neutral safety connection will be connected to the drive application wiring harness or the OEM interface wiring harness.

The primary purpose of this harness is to provide the length necessary to connect the components and interface with the engine ECM. Use the wiring diagram for details.

> [!note] Note · Примечание
> The harness may be supplied by the OEM, therefore the Cummins® service tools listed in this procedure may **not** fit. Contact the OEM for repair information.

![[00e00105.png]]

### Test

Use the following procedure for detailed component diagrams. [[513-208-002 — Component Diagrams|Refer to Procedure 208-002 in Section E]]

Use the wiring diagram, if necessary.

Check the harness for connectivity and damage. Use the following procedure for general resistance measurement techniques. [[99-019-360 — Resistance Measurement Using a Multimeter|Refer to Procedure 019-360 in Section 19.]]

Use the following procedure for service tools. Refer to Procedure 022-001 in Section 22.

Use the above Select Service Tools section for test lead information.

Use the following procedure for general inspection techniques. [[99-019-361 — Component Connector and Pin Inspection|Refer to Procedure 019-361 in Section 19.]]

![[3164133.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.

### Remove

**PS102**

Disconnect the drive application wiring harness from the engine, system enable connector, neutral safety switch connector, exhaust temperature sensor, and transmission gear oil pressure and temperature sensors.

If necessary for repair, remove the harness.

Note the harness routing and location of harness mounting points for installation.

![[15e00032.png]]

**PS103**

Disconnect the drive application wiring harness from the engine, transmission gear oil pressure and temperature sensors.

If necessary for repair, remove the harness.

Note the harness routing and location of harness mounting points for installation.

![[15e00192.png]]

### Install

**PS102**

Connect the drive application wiring harness to the engine, system enable connector, neutral safety switch connector, exhaust temperature sensor, and transmission gear oil pressure and temperature sensors.

Route and secure the harness to mounting points noted during removal.

![[15e00032.png]]

**PS103**

Connect the drive application wiring harness from the engine, transmission gear oil pressure and temperature sensors.

Route and secure the harness to mounting points noted during removal.

![[15e00192.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- Perform system test to verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
