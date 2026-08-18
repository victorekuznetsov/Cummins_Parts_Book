---
aliases:
  - "Цепь сигнализации пуска двигателя"
type: "Процедура"
doc: "82-019-310"
title_en: "Engine Start Alarm Circuit"
title_ru: "Цепь сигнализации пуска двигателя"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 21
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-310.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-310.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Start Alarm Circuit
**Цепь сигнализации пуска двигателя**

> [!abstract] Процедура · `82-019-310`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-310.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-310.pdf)

### Resistance Check

Turn the keyswitch to the OFF position.

Disconnect the engine start alarm from the OEM harness.

Disconnect the 31-pin OEM connector.

Set the multimeter to measure resistance.

![[19c00737.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.

Touch one of the multimeter leads to the supply wire, pin B (or 2), of the engine start alarm harness connector. Touch the other multimeter lead to pin 29 of the 31-pin OEM connector, OEM harness side. Read the value displayed on the multimeter.

Repeat the resistance check for the return wire. Measure the resistance from the return wire, pin A (or 1), of the engine start alarm harness connector to pin 28 of the 31-pin OEM connector, OEM harness side. Read the value displayed on the multimeter.

![[19c00738.png]]

For both pin checks, the multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure [[99-019-202 — Metripack Connector Series|019-202]] or 019-071.

![[19801619.png]]

Disconnect the actuator harness connector from the ECM.

Touch one of the multimeter leads to pin 29 of the 31-pin OEM connector, engine harness side.

Touch the other multimeter lead to pin 25 of the actuator harness connector.

Read the value displayed on the multimeter.

![[19c00728.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19801619.png]]

Then check the resistance of the return wire. Touch one of the multimeter leads to pin 28 of the 31-pin OEM connector, engine harness side. Touch the other multimeter lead to pin 32 of the actuator harness connector. Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the engine harness.

Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19c00728.png]]

### Check for Short Circuit to Ground

Turn the keyswitch to the OFF position.

Disconnect the engine start alarm from the OEM harness.

Disconnect the actuator harness connector from the ECM.

Set the multimeter to measure resistance.

![[19c00746.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.

Touch one of the multimeter leads to pin 25 of the actuator harness connector.

Touch the other multimeter lead to engine block ground.

Read the value displayed on the multimeter.

![[19c00741.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit to ground.

Isolate the short circuit to the OEM harness or engine harness.

![[19801621.png]]

Disconnect the 31-pin OEM connector.

Touch one of the multimeter leads to pin 29 of the 31-pin OEM connector, OEM harness side.

Touch the other multimeter lead to engine block ground.

Read the value displayed on the multimeter.

![[19c00742.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the OEM harness. Refer to Procedure 019-071. If the circuit is open, the short is in the engine harness. Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

Turn the keyswitch to the OFF position.

Disconnect the engine start alarm from the OEM harness.

Disconnect the actuator harness connector from the ECM.

Set the multimeter to measure resistance.

![[19c00746.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.

Touch one of the multimeter leads to pin 25 of the actuator harness connector.

Touch the other multimeter lead to all other pins in the connector, one at a time

Read the value displayed on the multimeter.

![[19c00735.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If any pin-to-pin measurement registers a closed circuit, there is a short circuit from pin 25 to that pin.

Isolate the short to the OEM or engine harness.

![[19801621.png]]

Disconnect the 31-pin OEM connector.

Touch one of the multimeter leads to pin 29 of the 31-pin OEM harness connector, OEM harness side.

Touch the other multimeter lead to all other pins in the connector, one at a time

Read the value displayed on the multimeter.

![[19c00744.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If any pin-to-pin measurement registers a closed circuit, there is an electrical connection between pin 29 and that pin.

Repair or replace the OEM harness. Refer to Procedure 019-071.

If the circuit at all pins measures an open circuit, the problem is on the engine harness side. Repair or replace the engine harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the engine start alarm from the OEM harness.

Disconnect the actuator harness connector from the ECM.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19c00746.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822917 and 3822758, when taking a measurement.

Touch one of the multimeter leads to pin 25 of the actuator harness connector.

Touch the other multimeter lead to engine block ground.

Read the value displayed on the multimeter.

![[19c00741.png]]

The multimeter **must** display a reading of less than 1.5 VDC.

If the voltage is more than 1.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM or engine harness that carries voltage.

Isolate the short circuit to the OEM harness or engine harness.

![[19c00724.png]]

Turn the keyswitch off to connect/disconnect the appropriate connectors. Disconnect the 31-pin OEM connector.

Turn the keyswitch to the ON position.

Touch one of the multimeter leads to pin 29 of the 31-pin OEM harness connector, OEM harness side.

Touch the other multimeter lead to engine block ground.

Read the value displayed on the multimeter.

![[19c00742.png]]

The multimeter **must** display a reading of less than 1.5 VDC.

If the voltage is more than 1.5 VDC, there is a short circuit to an external voltage source on the OEM harness side. If the voltage is less than 1.5 VDC, the short circuit to an external voltage source is on the engine harness side.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM or engine harness that carries voltage.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00724.png]]
