---
aliases:
  - "Управляющие электромагниты Centinel™"
type: "Процедура"
doc: "96-019-138"
title_en: "Centinel™ Control Solenoids"
title_ru: "Управляющие электромагниты Centinel™"
modified: "2004-04-22"
engines:
  - "37292556"
  - "37295879"
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
  - "QST30"
manuals:
  - "3666231"
figures: 18
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-138.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-019-138.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "двигатель/QST30"
  - "группа/96"
---

# Centinel™ Control Solenoids
**Управляющие электромагниты Centinel™**

> [!abstract] Процедура · `96-019-138`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]], [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11, QST30
> **Входит в руководства:** [[3666231 — Centinel™ Master Repair Manual|3666231]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-04-22
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/96/96-019-138.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/96-019-138.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Inspect the solenoid circuit. Place the pin of the lead into the supply pin A of the solenoid connector. Place the other lead pin into the return pin B of the solenoid connector. Connect the alligator clips to the multimeter probes.

![[19801510.png]]

Measure the resistance. Subtract the multimeter test lead resistance value from this value to determine the true solenoid circuit resistance value. The resistance **must** be:

12-VDC solenoid: 18 to 24 ohms at 25°C \[77°F\]

24-VDC solenoid: 78 to 94 ohms at 25°C \[77°F\].

If the resistance value is **not** correct, proceed with the following sections. If the resistance is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[nobox.png]]

If the resistance value is below specifications, inspect the solenoid wires for short circuits between the wires. If the wires are damaged, replace the wires. Refer to Procedure [[99-019-201 — Weather Pack Connector Series|019-201]].

![[19801511.png]]

If the resistance value of the solenoid is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness.

![[19400386.png]]

Check the wiring harness. Measure the resistance between pins A and B of the harness side of the connector that was removed from the solenoid. The resistance **must** be an open circuit (more than 1M ohms). If the resistance is less than 1M ohms, replace the wiring harness or Centinel™ control module. Refer to Procedure [[96-019-130-tr — Centinel™ Control Module|019-130]] or [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

Connect the wiring harness connector when the repair is completed.

![[ee2coke.png]]

If the resistance value is above specification, inspect the solenoid wires for broken wires. If the wires are damaged, replace the wires. Refer to Procedure [[99-019-201 — Weather Pack Connector Series|019-201]]. Do **not** repair the wires.

![[19801511.png]]

Check the 2-pin connector of the solenoid wires for proper connection.

If the wire and connector look OK, replace the solenoid. Refer to Procedure [[96-007-076 — Burn Solenoid|007-076]].

![[05100041.png]]

If the resistance value is within specification, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19801512.png]]

### Check for Short Circuit to Ground

Check the solenoid circuit for a short circuit to chassis ground.

The key should be in the OFF position

Use the multimeter to measure the resistance between the solenoid output pin on the harness side of the Centinel™ control module and the engine block ground.

The resistance **must** be more than 1M ohms (open circuit).

![[19801512.png]]

If the resistance value is less than 1M ohms, there is a short circuit to ground in the solenoid, the solenoid wires, or the wiring harness. Proceed as follows to locate the short circuit to ground. If the resistance value is correct, the circuit **must** still be checked for a short circuit from pin to pin.

![[19801513.png]]

Inspect the solenoid wires for a short circuit to ground. If the wires are damaged, replace the wires. Refer to Procedure [[99-019-201 — Weather Pack Connector Series|019-201]]. Do **not** repair the wires.

![[19801511.png]]

Check the solenoid for a short circuit to ground. Disconnect the solenoid supply and return wires from the solenoid.

Touch one multimeter probe to one of the solenoid pins. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1M ohms (open circuit). If the resistance is less than 1M ohms, replace the solenoid. Refer to Procedure [[96-007-076 — Burn Solenoid|007-076]].

![[19801514.png]]

If the resistance value is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness.

![[19400386.png]]

Check the wiring harness for a short circuit to ground. Disconnect both the solenoid and wiring harness connectors. Touch the multimeter probe on the supply pin of the wiring harness connector. Touch the other multimeter probe to the engine block.

Measure the resistance. The resistance value **must** be more than 1M ohms (open circuit).

![[19801518.png]]

Remove the multimeter probe from the supply pin and touch it to the return pin. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1M ohms (open circuit).

If less than 1M ohms are measured in either check, there is a short circuit to ground in the wiring harness. Replace the wiring harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

Connect the wiring harness connector and the solenoid connector when the repair is completed.

![[19801519.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> The batteries must be disconnected before performing this check. The multimeter will be damaged if the batteries are not disconnected.

Disconnect the batteries.

Check for a short circuit between the wires for the problem solenoid and all other wires in the wiring harness.

![[ea8coha.png]]

Turn the vehicle keyswitch to the OFF position.

Make sure that the wiring harness connector and the solenoid connector are disconnected.

Insert the lead into the supply pin. Insert the other lead into all of the pins of the connector except the return pin of the problem solenoid. Measure the resistance. The resistance **must** be more than 1M ohms (open circuit).

![[19801515.png]]

If less than 1M ohms are measured between the supply pin and any pin, there is a short circuit in the wiring harness between the supply or return wire to any pin that measured less than 1M ohms. Repair or replace the wiring harness. Refer to Procedure [[96-019-131-tr — Centinel™ Wiring Harness|019-131]].

![[19801516.png]]
