---
aliases:
  - "Дистанционный выключатель отбора мощности"
type: "Процедура"
doc: "82-019-080"
title_en: "Remote PTO Switch"
title_ru: "Дистанционный выключатель отбора мощности"
modified: "2002-06-03"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 6
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-080.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-080.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Remote PTO Switch
**Дистанционный выключатель отбора мощности**

> [!abstract] Процедура · `82-019-080`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-080.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-080.pdf)

### General Information

A remote PTO switch is available for applications where PTO operation control is desired away from the operator controls.

![[gp8swks.png]]

The remote PTO switch circuit consists of wire No. 34 (input signal) and a switch common return.

![[19c00348.png]]

### Resistance Check

Locate the desired on/off toggle switch.

Remove and tag the two connectors from the switch terminals.

Touch the multimeter probes to the terminals on the switch.

![[19900590.png]]

Turn the switch off and measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Replace the switch.

Refer to the OEM troubleshooting and repair manual for the replacement procedures.

![[19900591.png]]

Turn the switch ON and measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, the switch has failed. Replace the switch.

Refer to the OEM troubleshooting and repair manual for the replacement procedures.

If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[wr8swkd.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Turn the switch off and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Replace the switch. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

![[19900592.png]]
