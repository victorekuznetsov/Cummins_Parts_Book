---
aliases:
  - "Выключатель круиз-контроля или отбора мощности"
type: "Процедура"
doc: "82-019-021"
title_en: "Cruise Control or PTO ON/OFF Switch"
title_ru: "Выключатель круиз-контроля или отбора мощности"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-021.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-021.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Cruise Control or PTO ON/OFF Switch
**Выключатель круиз-контроля или отбора мощности**

> [!abstract] Процедура · `82-019-021`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-021.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-021.pdf)

### General Information

The on/off toggle switch is used to activate or disable the cruise control operation and PTO operation. The cruise control ON and OFF circuit consists of pin 23 (on/off signal), switch common ground, and the OEM cab-mounted toggle switch.

![[19c00184.png]]

### Resistance Check

If INSITE™ is available, monitor the switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

Locate the desired on/off toggle switch. Remove and tag the two connectors from the terminals on the switch. Touch the multimeter probes to the terminals on the switch.

![[19900590.png]]

Move the switch to the OFF position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures.

![[19900591.png]]

Move the switch to the ON position and measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, the switch has failed. Refer to the OEM troubleshooting and repair manual for the replacement procedures.

If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[wr8swkd.png]]

### Check for Short Circuit to Ground

Touch one of the multimeter probes to one of the switch terminals. Touch the other probe to chassis ground. Move the switch to the ON position and measure the resistance. The multimeter **must** show an open circuit (100k ohms or more). If the circuit is **not** open, the switch has failed. Refer to the OEM troubleshooting and repair manual for replacement procedures. If the switch passes all of the previous checks, the circuit **must** be checked for an open circuit, a short circuit to ground, a short circuit from pin to pin, and a short circuit to an external voltage source.

![[19900592.png]]
