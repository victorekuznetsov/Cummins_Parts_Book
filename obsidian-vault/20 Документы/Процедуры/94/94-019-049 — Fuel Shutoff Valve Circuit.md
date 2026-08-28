---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "94-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2003-03-24"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666184"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/94"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `94-019-049`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666184 — QST30 G-Drive Electronic Control System Troubleshooting and Repair Manual|3666184]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-03-24
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/94/94-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/94-019-049.pdf)

### Initial Check

Inspect the fuel shutoff solenoid post for extra wires that may be connected to supply power to another device. Remove the extra wires that are found connected to the solenoid post.

> [!note] Note · Примечание
> Be sure to check both fuel shutoff solenoids.

![[19400454.png]]

### Resistance Check

The fuel shutoff valve circuits are B+ signal wires, pins 39 and 40, of the engine harness to the fuel shutoff valve solenoids. The solenoids are grounded through the harness ground wires, which are attached to a mounting bolt or a post on the solenoid provided on isolated fuel solenoid shutoff valves, which are optional.

![[19400242.png]]

Use a 4 mm \[5/32 in\] hex head wrench to disconnect the engine harness Deutsch connector from the ECM.

![[19400242.png]]

Check the ECM and engine harness connector pins for damage.

![[19400007.png]]

Disconnect the fuel shutoff solenoid wire from the solenoid post. Check the solenoid wire ring terminal for damage.

> [!note] Note · Примечание
> Be sure to check both fuel shutoff solenoids.

![[19400088.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part No. 3822758. The connector will be damaged. The leads must fit tight in the connector without expanding the pins of the connector.

Insert the pin of one lead into pin 39 of the engine harness connector. Connect the alligator clip to the multimeter probe.

![[19a00033.png]]

Touch the other multimeter lead to the corresponding fuel shutoff valve solenoid wire. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the engine harness. Refer to procedures 019-197, 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], or [[94-019-043 — Engine Wiring Harness|019-043]]. If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.

![[19a00033.png]]

Insert the pin of one lead into pin 40 of the engine harness connector. Connect the alligator clip to the multimeter probe.

Touch the other multimeter lead to the corresponding fuel shutoff valve solenoid wire. Measure the resistance. The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the engine harness. Refer to procedures 019-197, 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], or [[94-019-043 — Engine Wiring Harness|019-043]]. If the circuit is closed, it **must** still be checked for a short to ground and a short from pin to pin.

![[19a00033.png]]

### Check for Short Circuit to Ground

Insert the lead into pin 39. Touch the other multimeter probe to engine block. The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short to ground in the wire connected to pin 39. Repair or replace the engine harness. Refer to Procedures 019-197, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00033.png]]

Insert the lead into pin 40. Touch the other multimeter probe to engine block. The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short to ground in the wire connected to pin 40. Repair or replace the engine harness. Refer to Procedures 019-197, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00033.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin 39 to all of the other pins in the engine harness connector. Connect one test lead to pin 39. Use the other probe to test all of the other pins in the connector.

The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded.

![[19a00033.png]]

Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between pin 39 and any pin that measured a closed circuit. Repair or replace the engine harness. Refer to Procedures 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00029.png]]

Check for a short circuit from pin 40 to all of the other pins in the engine harness connector. Connect one test lead to pin 40. Use the other probe to test all of the other pins in the connector.

The ring terminal at the corresponding solenoid **must** be disconnected and can **not** touch anything that is grounded.

![[19a00033.png]]

Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between pin 40 and any pin that measured a closed circuit. Repair or replace the engine harness. Refer to Procedures 019-199, [[94-019-240 — Connector, 40-Pin|019-240]], and [[94-019-043 — Engine Wiring Harness|019-043]].

![[19a00029.png]]
