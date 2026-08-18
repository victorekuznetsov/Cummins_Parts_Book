---
aliases:
  - "Выключатель положения педали тормоза"
type: "Процедура"
doc: "99-019-088"
title_en: "Brake Pedal Position Switch"
title_ru: "Выключатель положения педали тормоза"
modified: "2015-06-29"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 9
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-088.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-088.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Brake Pedal Position Switch
**Выключатель положения педали тормоза**

> [!abstract] Процедура · `99-019-088`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-088.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-088.pdf)

### General Information

> [!warning] CAUTION · Осторожно
> When troubleshooting the brake line switch circuit, make sure the brake pressure switch is identified. The vehicle brake light pressure switch, which is not a part of the Signature system, is commonly mistaken for the brake line switch used in the Signature system.

The brake pedal position switch detects the position of the service brake pedal. Certain features such as cruise control and PTO respond to the state of the brake pedal position switch and disengage when the brakes are applied. The circuit has a normally-closed switch, switch return wire, and brake pedal position switch signal wire of the OEM harness. The brake pedal position switch is mounted in the low pressure side of the vehicle pneumatic brake system. When the vehicle brakes are applied, the normally-closed switch opens and disables the cruise control operation.

![[19c01261.png]]

### Remove

> [!danger] WARNING · Опасно
> To avoid personal injury or death, do not apply the vehicle brakes when the switch is removed from the brake line fitting.

Disconnect the OEM harness from the brake pedal position switch.

Remove the brake pedal position switch from the fitting.

![[eb8swha.png]]

### Install

Install the new brake pedal position switch into the fitting according to the vehicle manufacturer's procedures.

![[eb8swhb.png]]

Connect the two wire connectors to the brake pedal position switch.

![[eb8swhc.png]]

### Resistance Check

If an electronic service tool is available, monitor the brake pedal position switch for proper operation. If **not**, follow the troubleshooting procedures in this section.

The brake pedal position switch (1) will be located in the vehicle brake line (2). The location will depend on the OEM installation procedures.

![[eb8swka.png]]

Disconnect the two wire connectors from the brake pedal position switch.

![[eb8swkb.png]]

Connect the probes of the multimeter to the brake pedal position switch terminals.

Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less) when the brakes are **not** applied. If the circuit is **not** closed, replace the brake pedal position switch.

![[eb8swkc.png]]

> [!warning] CAUTION · Осторожно
> The vehicle must have enough air pressure to activate the brakes.

Depress the vehicle brake pedal. The multimeter **must** show an open circuit (100k ohms or more) when the brakes are applied. If the circuit is **not** open, replace the brake pedal position switch.

If the resistance value is correct, the switch **must** still be checked for a short circuit to ground.

![[eb8swkd.png]]

### Check for Short Circuit to Ground

Touch one multimeter probe to one of the brake pedal position switch terminals. Touch the other multimeter probe to chassis ground. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more) when the brake pedal is released. If the circuit is **not** open, replace the brake pedal position switch.

If the brake pedal position switch passed all the previous checks, connect the switch to the wiring harness. The brake pedal position switch circuit **must** still be checked.

![[eb8swke.png]]
