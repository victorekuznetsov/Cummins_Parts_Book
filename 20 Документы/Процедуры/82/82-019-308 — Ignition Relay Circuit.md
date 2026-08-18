---
aliases:
  - "Цепь реле зажигания"
type: "Процедура"
doc: "82-019-308"
title_en: "Ignition Relay Circuit"
title_ru: "Цепь реле зажигания"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-308.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-308.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Ignition Relay Circuit
**Цепь реле зажигания**

> [!abstract] Процедура · `82-019-308`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-308.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-308.pdf)

### Resistance Check

Turn the keyswitch to the OFF position.

Disconnect the OEM harness connector from the ECM.

Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.

Set the multimeter to measure resistance.

![[19c00736.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Touch one of the multimeter leads to pin 35 of the OEM harness connector.

Touch the other multimeter lead to the ignition bus relay harness connector pin.

Read the value displayed on the multimeter.

![[19c00726.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.

Connect all components after completing the repair.

![[19801619.png]]

### Check for Short Circuit to Ground

Turn the keyswitch to the OFF position.

Disconnect the OEM harness connector from the ECM.

Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.

Set the multimeter to measure resistance.

![[19c00736.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Touch one of the multimeter leads to pin 35 of the OEM harness connector.

Touch the other multimeter lead to the engine block ground.

Read the value displayed on the multimeter.

![[19c00741.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, repair or replace the OEM harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit from Pin to Pin

Turn the keyswitch to the OFF position.

Disconnect the OEM harness connector from the ECM.

Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.

Set the multimeter to measure resistance.

![[19c00736.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Touch one of the multimeter leads to pin 35 of the OEM harness connector.

Touch the other multimeter lead to all other pins in the connector.

Read the value displayed on the multimeter.

![[19c00754.png]]

The multimeter **must** display a reading of more than 100k ohms, which is an open circuit.

If the circuit is **not** open, there is a short circuit between pin 35 and any other pin that registered a closed circuit. Repair or replace the OEM harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19801621.png]]

### Check for Short Circuit to External Voltage Source

Disconnect the OEM harness connector from the ECM.

Disconnect the idle shutdown/ignition bus relay harness connector from the OEM harness.

Set the multimeter to measure VDC.

Turn the keyswitch to the ON position.

![[19c00736.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test lead, Part Number 3822758, when taking a measurement.

Touch one of the multimeter leads to pin 35 of the OEM harness connector.

Touch the other multimeter lead to the engine block ground.

Read the value displayed on the multimeter.

![[19c00741.png]]

The multimeter **must** display a reading of less than 1.5 VDC.

If the voltage is **not** less than 1.5 VDC, there is a short circuit to an external voltage source.

> [!note] Note · Примечание
> An external voltage source is any wire in the OEM or engine harness wiring that carries voltage.

Remove the external voltage source.

Connect all components after completing the repair.

![[19c00724.png]]
