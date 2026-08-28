---
type: "Процедура"
doc: "97-019-134"
title_en: "Ambient Air Temperature Sensor"
modified: "2003-06-13"
engines:
  - "35354607"
  - "35373113"
  - "71156161"
  - "80141463"
  - "80248213"
families:
  - "QSM11"
  - "QSX15"
manuals:
  - "3666415"
figures: 11
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-134.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-134.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Ambient Air Temperature Sensor

> [!abstract] Процедура · `97-019-134`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-134.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-134.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.

Locate the ambient air temperature sensor installed under or near the vehicle's fifth wheel.

Turn the keyswitch to the OFF position.

Disconnect the ambient air temperature sensor from the temperature sensor harness.

![[19c00945.png]]

Set the multimeter to measure resistance.

Touch one of the multimeter leads to pin 1 of the ambient air temperature sensor.

Touch the other multimeter lead to pin 2 of the ambient air temperature sensor.

Read the value displayed on the multimeter.

![[19c00947.png]]

The resistance **must** fall within the resistance range as shown in the table below. If the circuit is **not** closed, replace the ambient air temperature sensor.

| **(°C)** | **\[°F\]** | **(ohms)** |
|---|---|---|
| 0 | 32 | 29k to 36k |
| 25 | 77 | 9k to 11k |
| 50 | 122 | 3k to 4k |
| 75 | 167 | 1300 to 1600 |
| 100 | 212 | 600 to 750 |

Connect all components after completing the repair.

![[19c00947.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822917, when taking a measurement.

Locate the ambient air temperature sensor installed under or near the vehicle's fifth wheel.

Turn the keyswitch to the OFF position.

Disconnect the ambient air temperature sensor from the temperature sensor harness.

![[19c00945.png]]

Set the multimeter to measure resistance.

Touch one multimeter lead to pin 1 of the ambient air temperature sensor.

Touch the other multimeter lead to the sensor casing.

Read the value displayed on the multimeter.

![[19c00948.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground. Replace the ambient air temperature sensor.

Connect all components after completing the repair.

![[19801621.png]]

### Remove

Locate the ambient air temperature sensor installed under or near the vehicle's fifth wheel.

Remove any nylon wire ties securing the ambient air temperature sensor and its wiring to an air line or wire conduit.

![[15800060.png]]

Disconnect the ambient air temperature sensor from the temperature sensor harness.

Remove the ambient air temperature sensor.

![[19c00944.png]]

### Install

Install the ambient air temperature sensor under or near the vehicle's fifth wheel using nylon wire ties to secure it to an air line or wire conduit.

Make sure that the sensor is located in a spot where it is **not** exposed to engine heat, engine exhaust, or direct sun, and not located directly over an axle. It **must** also be located in an area with airflow.

![[15800060.png]]

> [!warning] CAUTION · Осторожно
> Use only Cummins-recommended lubricant DS-ES, Part Number 3822934. Other lubricants, such as lubricating oil or grease, in the connectors can cause idle control module damage, poor engine performance, or premature connector pin wear.

Apply a small amount of lubricant to the connector terminals. Do **not** fill the entire cavity with lubricant.

![[19d00722.png]]

Connect the ambient air temperature sensor to the temperature sensor harness.

![[19c00944.png]]
