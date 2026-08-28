---
aliases:
  - "Цепь датчика температуры наружного воздуха"
type: "Процедура"
doc: "82-019-135"
title_en: "Ambient Air Temperature Sensor Circuit"
title_ru: "Цепь датчика температуры наружного воздуха"
modified: "2006-05-12"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 15
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-135.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-135.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Ambient Air Temperature Sensor Circuit
**Цепь датчика температуры наружного воздуха**

> [!abstract] Процедура · `82-019-135`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2006-05-12
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-135.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-135.pdf)

### Resistance Check

ICON™ System

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Turn the keyswitch to the OFF position.

Disconnect the ambient air temperature sensor from the temperature sensor harness.

Disconnect the temperature sensor harness from the cab thermostat.

Set the multimeter to measure resistance.

![[19c00719.png]]

Touch one of the multimeter leads to the sensor supply wire, pin 1 (or A), of the temperature sensor harness connector on the ambient air temperature sensor end of the harness.

Touch the other multimeter lead to the sensor supply wire, pin 1 (or A), of the temperature sensor harness connector on the cab thermostat end of the harness.

Read the value displayed on the multimeter.

![[19c00720.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is open, repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.

![[19801619.png]]

Repeat the check for the return wire. Measure the resistance from the return wire, pin 2 (or B), at the sensor end of the temperature sensor harness to the return wire, pin 3 (or C), at the thermostat end of the harness. Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is open, repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.

Connect all components after completing the repair.

![[19c00720.png]]

### Check for Short Circuit to Ground

ICON™ System

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Turn the keyswitch to the OFF position.

Disconnect the ICON™ ambient air temperature sensor from the temperature sensor harness.

Disconnect the temperature sensor harness from the cab thermostat.

Set the multimeter to measure resistance.

![[19c00719.png]]

Touch one of the multimeter leads to the supply wire, pin 1 (or A), of the temperature sensor harness connector on the cab thermostat end of the harness.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00721.png]]

The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit to ground.

Repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.

![[19801621.png]]

Touch one of the multimeter leads to the return wire, pin 2 (or B), of the temperature sensor harness connector on the cab thermostat end of the harness. Touch the other multimeter lead to ground. Read the value displayed on the multimeter.

The multimeter **must** display more than 100k ohms (open circuit). If the circuit is **not** open, there is a short circuit to ground.

Repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.

Connect all components after completing the repair.

![[19c00721.png]]

### Check for Short Circuit from Pin to Pin

ICON™ System

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Turn the keyswitch to the OFF position.

Disconnect the ICON™ ambient air temperature sensor from the temperature sensor harness.

Disconnect the temperature sensor harness from the cab thermostat.

Set the multimeter to measure resistance.

![[19c00719.png]]

Touch one of the multimeter leads to the supply wire, pin 1 (or A), of the temperature sensor harness connector, cab thermostat end of the harness.

Touch the other multimeter lead to the return wire, pin 3 (or C), of the connector.

Read the value displayed on the multimeter.

![[19c00722.png]]

The multimeter **must** display more than 100k ohms, which is an open circuit. If the circuit is **not** open, there is a short circuit between the two pins.

Repair or replace the temperature sensor harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or Procedure 019-071.

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

ICON™ System

> [!warning] CAUTION · Осторожно
> To avoid pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Disconnect the temperature sensor harness from the cab thermostat.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19c00723.png]]

Touch one of the multimeter leads to the supply wire, pin 1 (or A), of the temperature sensor harness connector on the cab thermostat end of the harness.

Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

![[19c00721.png]]

The multimeter **must** display less than 1.5 VDC. If the circuit is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.

Remove the external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the temperature sensor harness that carries voltage.

![[19c00724.png]]

Repeat the check for the return wire.

Touch one of the multimeter leads to the return wire, pin 3 (or C), of temperature sensor harness connector on the cab thermostat end of the harness. Touch the other multimeter lead to ground.

Read the value displayed on the multimeter.

The multimeter **must** display less than 1.5 VDC. If the circuit is **not** less than 1.5 VDC, there is a short circuit to an external voltage source. Remove the external voltage source.

Connect all components after completing the repair.

![[19c00721.png]]
