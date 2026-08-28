---
aliases:
  - "Цепь датчика температуры наружного воздуха"
type: "Процедура"
doc: "97-019-135"
title_en: "Ambient Air Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры наружного воздуха"
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
figures: 18
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSM11"
  - "двигатель/QSX15"
  - "группа/97"
---

# Ambient Air Temperature Sensor Circuit
**Цепь датчика температуры наружного воздуха**

> [!abstract] Процедура · `97-019-135`
> **Двигатели:** [[35354607 — QSM11 CM570 CPL 8608|35354607]], [[35373113 — QSM11 CM570 CPL 8471|35373113]], [[71156161 — QSM11 CM570 CPL 8543|71156161]], [[80141463 — QSX15 CM570 CPL 3088|80141463]], [[80248213 — QSX15 CM570 CPL 8760|80248213]]
> **Семейство:** QSM11, QSX15
> **Входит в руководства:** [[3666415 — ICON Idle Control System Master Repair Manual|3666415]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-06-13
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/97/97-019-135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/97-019-135.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Turn the keyswitch to the OFF position. Disconnect the ambient air temperature sensor from the temperature sensor harness.

Set the multimeter to measure resistance.

![[19c00945.png]]

Disconnect the temperature sensor harness from the cab thermostat.

![[19c00949.png]]

Touch one of the multimeter leads to pin 1 of the temperature sensor harness connector on the ambient air temperature sensor side.

Touch the other multimeter lead to pin 1 of the temperature sensor harness connector, cab thermostat side.

Read the value displayed on the multimeter.

![[19c00950.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair the defective temperature sensor harness connector or replace the temperature sensor harness. Refer to Procedure 019-202, 019-203, or [[97-019-296 — Temperature Sensor Harness|019-296]].

Repeat the resistance check for the return wire.

![[19801619.png]]

Touch one of the multimeter leads to pin 2 of the temperature sensor harness connector, sensor side. Touch the other multimeter lead to pin 3 of the temperature sensor harness connector, cab thermostat side. Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms. If the circuit is **not** closed, repair the defective sensor harness connector or replace the temperature sensor harness. Refer to Procedure 019-202, 019-203, or [[97-019-296 — Temperature Sensor Harness|019-296]].

Connect all components after completing the repair.

![[19c00950.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Turn the keyswitch to the OFF position.

Disconnect the ambient air temperature sensor from the temperature sensor harness.

![[19c00945.png]]

Disconnect the temperature sensor harness from the cab thermostat.

Set the multimeter to measure resistance.

![[19c00949.png]]

Touch one of the multimeter leads to pin 1 of the temperature sensor harness connector on the ambient air temperature sensor side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00951.png]]

The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.

Repair or replace the temperature sensor harness. Refer to Procedure 019-202 or [[97-019-296 — Temperature Sensor Harness|019-296]].

![[19801621.png]]

Touch one of the multimeter leads to pin 2 of the temperature sensor harness connector on the ambient air temperature sensor side. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

The multimeter **must** display more than 100k ohms (open circuit). If the circuit is **not** open, there is a short circuit to ground. Repair or replace the temperature sensor harness. Refer to Procedure 019-202 or [[97-019-296 — Temperature Sensor Harness|019-296]].

Connect all components after completing the repair.

![[19c00951.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Turn the keyswitch to the OFF position.

Disconnect the ambient air temperature sensor from the temperature sensor harness.

![[19c00945.png]]

Disconnect the temperature sensor harness from the cab thermostat.

Set the multimeter to measure resistance.

![[19c00949.png]]

Touch one of the multimeter leads to pin 1 of the temperature sensor harness connector, cab thermostat side. Touch the other multimeter lead to each of the other three pins in the connector. Repeat the pin-to-pin check for the other 3 pins in the connector.

Read the value displayed on the multimeter.

![[19c00952.png]]

The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the two pins.

Repair or replace the temperature sensor harness. Refer to Procedure 019-203 or [[97-019-296 — Temperature Sensor Harness|019-296]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Disconnect the temperature sensor harness from the cab thermostat.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19c00949.png]]

Touch one of the multimeter leads to pin 1 of temperature sensor harness connector on the cab thermostat side.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00953.png]]

The multimeter **must** display less than 0.5 VDC. If the circuit is **not** less than 0.5 VDC, there is a short circuit to an external voltage source.

Remove the external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the temperature sensor harness that carries voltage.

![[19c00954.png]]

Repeat the check for the return wire.

Touch one of the multimeter leads to pin 3 of temperature sensor harness connector on the cab thermostat side. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

The multimeter **must** display less than 0.5 VDC. If the circuit is **not** less than 0.5 VDC, there is a short circuit to an external voltage source. Remove the external voltage source.

Connect all components after completing the repair.

![[19c00953.png]]
