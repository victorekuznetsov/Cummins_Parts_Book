---
aliases:
  - "Цепь дистанционного выключателя отбора мощности"
type: "Процедура"
doc: "99-019-079"
title_en: "Remote PTO Switch Circuit"
title_ru: "Цепь дистанционного выключателя отбора мощности"
modified: "2015-06-29"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-079.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-079.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Remote PTO Switch Circuit
**Цепь дистанционного выключателя отбора мощности**

> [!abstract] Процедура · `99-019-079`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-079.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-079.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert a test lead into the remote power take-off (PTO) switch return pin of the OEM harness connector and connect it to the multimeter probe. Insert the other test lead into the remote PTO switch signal pin of the connector and connect it to the other probe.

Make sure the switch is connected to the circuit. Move the remote PTO switch to the ON position. Measure the resistance with the multimeter. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, inspect the switch return wire and the remote PTO switch signal wire for an open circuit. Repair or replace the OEM harness, provided the switch has been previously checked. Refer to the OEM troubleshooting and repair manual for the procedures.

![[19c01256.png]]

If the resistance is correct, the remote PTO switch return wire and the remote PTO switch signal wire **must** be checked for a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

Connect all components after the repair is complete.

![[19c01257.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram.

Insert the test lead into the remote PTO switch signal pin in the OEM harness connector and connect it to the multimeter probe. Touch the other probe to engine block ground.

With the remote PTO switch in the OFF position, read the resistance.

The multimeter **must** show an open circuit (100k ohms or more).

If the resistance values are **not** correct, make sure the remote PTO switch signal wire and the ground wire are properly installed on the switch. If both wires are correctly installed, inspect the wires for a short to ground circuit, provided the remote PTO switch has been previously checked.

![[19c01258.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin to pin. Set the remote PTO switch to the OFF position. Insert the test lead into the remote PTO switch return pin of the OEM harness connector and connect it to the multimeter probe. With a test lead connected to the other multimeter probe, check all the other pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

![[19c01168.png]]

Remove the lead from the remote PTO switch return pin and insert it into the remote PTO switch signal pin of the harness connector. With the other test lead, check all other pins in the connector. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit between the switch circuit and any pin that did **not** measure an open circuit, provided the switch has previously been checked. Repair or replace the wires in the OEM harness according to the vehicle manufacturer's procedures.

Connect all components after completing the repair.

![[19c01236.png]]
