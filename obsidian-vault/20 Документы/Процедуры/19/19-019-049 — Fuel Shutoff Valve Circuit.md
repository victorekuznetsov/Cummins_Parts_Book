---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "19-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2004-12-07"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 10
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `19-019-049`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-12-07
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-049.pdf)

### Initial Check

Inspect the fuel shutoff solenoid post for extra wires that may be connected to supply power to another device. Remove the extra wires that are found connected to the solenoid post.

![[19400454.png]]

Check that the terminal post is **not** in contact with the fuel pump damper, or any other metallic object other than the harness terminal.

![[19400742.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins in the connector.

The fuel shutoff valve circuit is a signal wire, pin 30, of the engine harness to the fuel shutoff valve solenoid. The solenoid is grounded through the engine.

Disconnect the engine harness from the ECM.

![[19400242.png]]

Check the ECM and engine harness connector pins for damage.

![[19400007.png]]

Disconnect the fuel shutoff solenoid wires from the solenoid posts. Check the solenoid wire ring terminals for damage.

![[19400088.png]]

Insert the pin of one lead into pin 30 of the engine harness connector. Connect the alligator clip to the multimeter probe.

![[19400479.png]]

Touch the other multimeter lead to the fuel shutoff valve solenoid wire. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less).

If the circuit is **not** closed, repair or replace the engine harness. Refer to Procedures [[99-019-197 — Ring Terminal|019-197]], [[99-019-199 — Connector, Butt Splice|019-199]], or [[99-019-204 — Deutsch DRC Connector Series|019-204]].

If the circuit is closed it **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19400480.png]]

### Check for Short Circuit to Ground

Insert the electrical lead into pin 30. Touch the other multimeter probe to engine block. The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short circuit to ground in the wire connected to pin 30. Repair or replace the engine harness. Refer to Procedures [[99-019-197 — Ring Terminal|019-197]] and [[99-019-204 — Deutsch DRC Connector Series|019-204]].

![[19400481.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin 30 to all other pins in the engine harness connector. Connect the alligator clip of a second test lead to the other multimeter probe. Insert the pin of the lead into all other pins in the actuator.

The ring terminals at the solenoid **must** be disconnected and can **not** touch anything that is grounded. The battery voltage supply **must** be disconnected.

![[19400482.png]]

Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short circuit between pin 30 and **any** pin that measured a closed circuit. Repair or replace the engine harness. Refer to Procedure [[99-019-199 — Connector, Butt Splice|019-199]] and [[99-019-204 — Deutsch DRC Connector Series|019-204]].

![[19400483.png]]
