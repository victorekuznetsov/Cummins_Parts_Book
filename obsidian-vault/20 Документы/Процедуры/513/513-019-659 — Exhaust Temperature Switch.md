---
type: "Процедура"
doc: "513-019-659"
title_en: "Exhaust Temperature Switch"
modified: "2019-09-27"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
families:
  - "QSM11"
manuals:
  - "5411480"
figures: 4
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-019-659.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-019-659.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "группа/513"
---

# Exhaust Temperature Switch

> [!abstract] Процедура · `513-019-659`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]]
> **Семейство:** QSM11
> **Входит в руководства:** [[5411480 — C Command Connect and Connect Premier Marine Panel Systems PS102, PS103 and PS108 Mas|5411480]]
> **Секции:** Section 19 - Electronic Controls - Group 19
> **Даты:** изменён 2019-09-27
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/513/513-019-659.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/513-019-659.pdf)

### Select Service Tools

#### Recommended Cummins® Service Tools

- Electrical test lead, Part Number 3823993
- Electrical test lead, Part Number 3823994.

#### Additional Service Items

- No additional service items required.

### General Information

The exhaust temperature switch is used to indicate an over temperature condition of the exhaust and is located on the exhaust plumbing.

> [!note] Note · Примечание
> The content of this procedure is for the Cummins®-supplied part. Some applications may use an exhaust temperature sensor instead of a switch. Refer to the engine service manual if a sensor is used.

### Initial Check

Use the following procedure for information on using the ED-4 to troubleshoot sensor issues. [[513-015-035 — Display(s) and Instrumentation|Refer to Procedure 015-035 in Section 15]].

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. See equipment manufacturer service information.
- Clean the area around the switch.

### Remove

Disconnect the switch connector from the harness.

Remove the switch from the exhaust plumbing.

![[19e02085.png]]

### Clean and Inspect for Reuse

Inspect the harness connector and switch for the following:

- Cracked or broken connector shell, if equipped
- Missing or damaged connector seals, if equipped
- Dirt, debris, or moisture, in or on the connector pins
- Corroded, bent, broken, pushed back, or expanded pins
- Chipped, cracked, extruded or damaged switch.

Repair or replace parts as necessary.

![[19e02086.png]]

Measure across the switch terminals and compare with the table shown below.

| Temperature +/- 12°C | Temperature +/- 10°F | State | Resistance Ohms |
|---|---|---|---|
| Below 99°C | Below 210°F | Open | 10 or Less |
| Above 121°C | Above 250°F | Closed | 100k or More |

![[19e02105.png]]

### Install

Install the switch into the exhaust plumbing.

Tighten the mounting screws hand-tight.

Connect the harness to the switch.

![[19e02085.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. See equipment manufacturer service information.
- Operate the engine. Check for leaks.
- Perform system test to verify proper function. [[513-015-047 — Final Verification|Refer to Procedure 015-047 in Section 15.]]
