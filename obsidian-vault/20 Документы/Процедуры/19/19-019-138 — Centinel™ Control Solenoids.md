---
aliases:
  - "Управляющие электромагниты Centinel™"
type: "Процедура"
doc: "19-019-138"
title_en: "Centinel™ Control Solenoids"
title_ru: "Управляющие электромагниты Centinel™"
modified: "2002-08-20"
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
figures: 18
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-138.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-138.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Centinel™ Control Solenoids
**Управляющие электромагниты Centinel™**

> [!abstract] Процедура · `19-019-138`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-138.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-138.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins in the connector.

Inspect the solenoid circuit. Insert the pin of the lead into the supply pin A of the solenoid connector. Insert the other lead pin into the return pin B of the solenoid connector. Connect the alligator clips to the multimeter probes.

![[19801513.png]]

Measure the resistance. Subtract the multimeter test lead resistance value from this value to determine the true solenoid circuit resistance value. The resistance **must** be 14 to 120 ohms. If the resistance value is **not** correct, proceed with the following sections. If the resistance is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19801513.png]]

**Resistance Value Below Specifications**

Inspect the solenoid wires for short circuits between the wires. If the wires are damaged, replace the wires. Refer to Procedure 019-202.

![[19801511.png]]

If the resistance value of the solenoid is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness. Inspect the wiring harness for wires that have worn through insulation, cuts, and any other damage that may cause an open or short circuit. If any physical damage is found, repair or replace the damaged harness. Refer to Procedure [[19-019-072 — OEM Interface Harness|019-072]], or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19400386.png]]

Check the wiring harness. Measure the resistance between pin A and B of the harness side of the connector that was removed from the solenoid. The resistance **must** be an open circuit (more than 1k ohms). If the resistance is less than 1k ohms, replace the wiring harness or ECM. Refer to Procedure [[19-019-043 — Engine Wiring Harness|019-043]] or [[19-019-031 — Engine Control Module|019-031]].

Connect the wiring harness connector when the repair is completed.

![[ee2coke.png]]

**Resistance Value Above Specification**

Inspect the solenoid wires for broken wires. If the wires are damaged, replace the wires. Refer to Procedure 019-202. Do **not** repair the wires.

![[19801511.png]]

Check the 2-pin connector of the solenoid wires for proper connection.

If the wire and connector looks OK, replace the solenoid. Refer to Section 2 of the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098, the Troubleshooting and Repair Manual, QSK45 and QSK60 Series Engines, Bulletin 3666261, or the Troubleshooting and Repair Manual, QSK78 Series Engines, Bulletin 3666727.

![[05100041.png]]

**Resistance Value Within Specification**

If the resistance value is within specification, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19801512.png]]

### Check for Short Circuit to Ground

Check the solenoid circuit for a short circuit to chassis ground.

Turn the keyswitch to the OFF position

Use the multimeter to measure the resistance between the solenoid output pin on the harness side of the Centinel™ Control Module and the engine block ground.

The resistance **must** be more than 1k ohms (open circuit).

![[19801512.png]]

If the resistance value is less than 1k ohms, there is a short circuit to ground in the solenoid, the solenoid wires, or the wiring harness. Proceed as follows to locate the short circuit to ground. If the resistance value is correct, the circuit **must** still be checked for a short circuit from pin to pin.

![[19801513.png]]

Inspect the solenoid wires for a short circuit to ground. If the wires are damaged, replace the wires. Refer to Procedure 019-202. Do **not** repair the wires.

![[19801511.png]]

Check the solenoid for a short circuit to ground. Disconnect the solenoid supply and return wires from the solenoid.

Touch one multimeter probe to one of the solenoid pins. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1k ohms (open circuit). If the resistance is less than 1k ohms, replace the solenoid. Refer to Section 2 of the Troubleshooting and Repair Manual, QSK19 Series Engines, Bulletin 3666098, Troubleshooting and Repair Manual, the QSK45 and QSK60 Series Engines, Bulletin 3666261, or the Troubleshooting and Repair Manual, QSK78 Series Engines, Bulletin 3666727.

![[19801514.png]]

If the resistance value is correct, the problem is in the wiring harness. Isolate the problem by checking the wiring harness.

![[19400386.png]]

Check the wiring harness for a short circuit to ground. Disconnect both the solenoid and wiring harness connectors. Touch the multimeter probe on the supply pin of the wiring harness connector. Touch the other multimeter probe to the engine block.

Measure the resistance. The resistance value **must** be more than 1k ohms (open circuit).

![[19801518.png]]

Remove the multimeter probe from the supply pin and touch it to the return pin. Touch the other multimeter probe to the engine block. Measure the resistance. The resistance **must** be more than 1k ohms (open circuit).

If less than 1k ohms are measured in either check, there is a short circuit to ground in the wiring harness. Replace the wiring harness. Refer to Procedure [[19-019-043 — Engine Wiring Harness|019-043]].

Connect the wiring harness connector and the solenoid connector when the repair is completed.

![[19801519.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

> [!warning] CAUTION · Осторожно
> The batteries must be disconnected before performing this check. The multimeter will be damaged if the batteries are not disconnected.

Disconnect the batteries.

![[ea8coha.png]]

Check for a short circuit between the wires for the problem solenoid and all other wires in the wiring harness.

Turn the keyswitch to the OFF position.

Make sure that the wiring harness connector and the solenoid connector are disconnected.

Insert the lead into the supply pin. Insert the other lead into all pins of the connector except the return pin of the problem solenoid. Measure the resistance. The resistance **must** be more than 1k ohms (open circuit).

![[19801515.png]]

If less than 1k ohms is measured between the supply pin and any pin, there is a short circuit in the wiring harness between the supply or return wire to any pin that measured less than 1k ohms. Repair or replace the wiring harness. Refer to Procedure 019-202 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19801516.png]]
