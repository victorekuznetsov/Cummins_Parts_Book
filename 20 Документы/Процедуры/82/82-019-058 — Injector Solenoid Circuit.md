---
aliases:
  - "Цепь электромагнита форсунки"
type: "Процедура"
doc: "82-019-058"
title_en: "Injector Solenoid Circuit"
title_ru: "Цепь электромагнита форсунки"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 38
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-058.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-058.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Injector Solenoid Circuit
**Цепь электромагнита форсунки**

> [!abstract] Процедура · `82-019-058`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-058.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-058.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.

Inspect the injector solenoid circuit of the cylinder referenced on the recorded fault code. Refer to the accompanying chart for the pins of the injector circuit of the problem cylinder. Cylinder Number 1 will be used in this example.

![[19200339.png]]

The pins of the circuits are as follows:

| Supply Pin | Return Pin |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
| 1 | 10 | 01 | A | 09 | 02 | B |
| 2 | 08 | 03 | A | 07 | 04 | B |
| 3 | 06 | 05 | A | 16 | 06 | B |
| 4 | 26 | 07 | A | 36 | 08 | B |
| 5 | 04 | 09 | A | 03 | 10 | B |
| 6 | 02 | 11 | A | 01 | 12 | B |

![[19200333.png]]

Turn the vehicle keyswitch to the OFF position.

Disconnect the actuator harness connector from the ECM.

Insert a test lead into the supply pin (pin 10 in this example) of the actuator harness connector. Insert the other lead into the return pin (pin 09 in this example) of the actuator harness connector. Connect the alligator clips to the multimeter probes.

![[19200338.png]]

Measure the resistance. Subtract the multimeter test lead resistance value from this value to determine the true injector circuit resistance value. The resistance **must** be 0.5 to 1.5 ohms. If the resistance value is **not** correct, proceed with the following sections. If the resistance is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

> [!note] Note · Примечание
> If the resistance measurement is less than 10 ohms, the circuit is acceptable as long as the resistance of the injector solenoid is within 0.5 to 1.5 ohms (see Resistance Value Above Specification).

![[oi801k07.png]]

Resistance Value Below Specifications

Remove the valve cover.

Inspect the injector solenoid wires for short circuits between the wires. If the wires are damaged, replace the wires. Refer to Procedure [[82-019-057 — Injector Solenoid|019-057]].

![[ee2coka.png]]

Disconnect the injector supply and return wires from the solenoid of the problem cylinder.

Use a small screwdriver to remove the protective cover from the solenoid.

Remove the captive nut assembly from the injector solenoid.

![[ee2cokh.png]]

Measure the resistance between the two posts or the connection of the injector solenoid. Subtract the multimeter resistance. The true injector solenoid resistance **must** be 0.5 to 1.5 ohms. If the resistance value is **not** correct, replace the injector. Refer to Procedure 006-026 in the Troubleshooting and Repair Manual, ISM and QSM11 Engines, Bulletin 3666322.

![[fi2cnka.png]]

If the resistance value of the injector solenoid is correct, the problem is in the internal or external actuator harness. Isolate the problem by checking each harness separately.

![[19200339.png]]

Disconnect the connector inside the head.

Check the internal actuator harness. Measure the resistance between the two captive nut assemblies, or the connection, of the injector solenoid wire that was removed from the injector solenoid. The resistance **must** be an open circuit (more than 100k ohms). If the resistance is less than 100k ohms, replace the internal actuator wiring harness. Refer to Procedure 019-063. Do **not** repair the internal actuator harness.

Connect the 15-pin connector when the repair is completed.

![[ee2coke.png]]

Check the external actuator harness. Make sure that the 15-pin connector is still disconnected. Insert the test lead into the supply pin (pin 10 in this example) of the actuator harness connector. Insert the pin of the other lead into the return pin (pin 09 in this example) of the actuator harness connector. Connect the alligator clips to the multimeter probes.

![[19200338.png]]

Measure the resistance. The resistance **must** be an open circuit (more than 100k ohms). If the resistance is less than 100k ohms, repair or replace the external actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect the 15-pin connector when the repair is completed.

![[19200338.png]]

Resistance Value Above Specification

Remove the valve cover.

Inspect the injector solenoid wires for broken wires. If the wires are damaged, replace the wires. Refer to Procedure [[82-019-057 — Injector Solenoid|019-057]]. Do **not** repair the wires.

![[ee2coka.png]]

Check the 2-pin connector of the injector solenoid wires for proper connection.

Use a small screwdriver to remove the protective cover from the solenoid.

Use inch pound torque wrench, Part Number 3823208, and screwdriver socket, Part Number 3823209, to check the captive nut assembly for correct torque.

> [!tip] Момент затяжки · Torque Value
> 1.6 n•m [14 in-lb]

![[ee2cokf.png]]

Check pass-through connector for a tight connection. Check for an open circuit in the injector solenoid. Use a small screwdriver to remove the protective cover from the solenoid.

Remove the captive nut assembly from the injector solenoid.

![[ee2cokh.png]]

Measure the resistance between the posts or the connection of the injector solenoid. Subtract the multimeter resistance. The true injector solenoid resistance **must** be 0.5 to 1.5 ohms. If the resistance is **not** correct, replace the injector. Refer to Procedure 006-026 in the Troubleshooting and Repair Manual, ISM and QSM11 Engines, Bulletin 3666322.

![[fi2cnka.png]]

If the resistance is correct, check the solenoid wires for an open circuit.

Disconnect the 2-pin connector of the injector solenoid wires.

![[fi8coad.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than the mating connector. The connector will be damaged. The leads must fit tightly in the connector without expanding the connector pins.

Connect a mating connector with short lead extensions to the injector side of the 2-pin connector.

![[ee2cokb.png]]

Touch one multimeter probe to the end of the short lead extension. Touch the other multimeter probe to the captive nut assembly of the injector solenoid wire. Measure the resistance. Repeat the procedure for the other injector wire. The resistance for both of these checks **must** be less than 10 ohms. If the resistance is more than 10 ohms, replace the injector solenoid wires. Refer to Procedure [[82-019-057 — Injector Solenoid|019-057]]. Do **not** repair the wires.

![[ee2cokc.png]]

Disconnect the 15-pin connector to separate the internal and external actuator harness.

![[ea200hf.png]]

Refer to the accompanying chart at the beginning of this section for the pins of the injector circuit of the problem cylinder.

Cylinder Number 1 will be used in this example. Check the supply wire. Touch one multimeter probe to the supply pin (pin A) at the injector 2-pin connector, internal actuator harness side.

![[19200340.png]]

Touch the other multimeter probe to the supply pin (pin 01) at the 15-pin connector, internal actuator harness side. Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, replace the internal actuator harness. Refer to Procedure 019-063. Do **not** repair the wire.

Connect the 15-pin connector when the repair is completed.

![[19200340.png]]

Check the return wire for an open circuit. Touch one multimeter probe to the return pin (pin B) at the injector 2-pin connector, internal actuator harness side. Touch the other multimeter probe on the return pin (pin 02) of the 15-pin connector, internal actuator harness side.

![[19200341.png]]

Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, replace the internal actuator harness. Refer to Procedure 019-063. Do **not** repair the wires.

Connect the 15-pin connector when the repair is completed.

![[19200341.png]]

Check the external actuator harness for an open circuit. Refer to the accompanying chart at the beginning of this section for the pins required.

Cylinder Number 1 will be used as an example. Insert the pin of the lead into the supply pin (pin 10 in this example) of the actuator harness. Connect the alligator clip to the multimeter probe.

![[19200342.png]]

Insert the other multimeter probe on the supply pin (pin 01) at the 15-pin connector, external actuator harness side. Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, repair the wire or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect the 15-pin connector when the repair is completed.

![[19200342.png]]

Insert the pin of the lead in the return pin (pin 09 in this example) of the actuator harness connector. Place the other multimeter probe on the return pin (pin 02) at the 15-pin connector, external harness side.

![[19200343.png]]

Measure the resistance. The resistance **must** be less than 10 ohms. If more than 10 ohms are measured, repair the return wire or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect the 15-pin connector when the repair is completed.

![[19200343.png]]

Resistance Value Within Specification

If the resistance value is within specification, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19200344.png]]

### Check for Short Circuit to Ground

> [!danger] WARNING · Опасно
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.

Check for a short circuit to ground in the external actuator harness. Refer to the accompanying chart for the pins to check. Cylinder Number 1 will be used for this example.

![[19200339.png]]

The pins of the circuits are as follows:

| Supply Pin | Return Pin |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
| 1 | 10 | 01 | A | 09 | 02 | B |
| 2 | 08 | 03 | A | 07 | 04 | B |
| 3 | 06 | 05 | A | 16 | 06 | B |
| 4 | 26 | 07 | A | 36 | 08 | B |
| 5 | 04 | 09 | A | 03 | 10 | B |
| 6 | 02 | 11 | A | 01 | 12 | B |

![[19200333.png]]

Turn the vehicle keyswitch to the OFF position. Disconnect the actuator harness connector from the ECM.

Insert a test lead into pin 10 of the actuator harness connector, and connect it to a multimeter probe. Touch the other multimeter probe to engine block ground. Measure the resistance.

The circuit **must** be open (100k ohms or more). If it is **not** open, isolate the short to the external or internal actuator harness.

![[19200344.png]]

Disconnect the 15-pin pass-through connector from the actuator harness.

Insert the test lead into pin 01 of the 15-pin connector, internal harness side. Touch the other multimeter probe to engine block ground. Measure the resistance.

The circuit **must** be open (100k ohms or more). If it is **not** open, the short circuit is on the internal harness side. Replace the internal actuator harness. Refer to Procedure 019-063. If the circuit is open, repair or replace the external actuator harness.

![[19200409.png]]

### Check for Short Circuit from Pin to Pin

> [!danger] WARNING · Опасно
> The injector solenoids receive high voltage when the engine is operating. To reduce the possibility of personal injury or death from electrical shock, do not wear jewelry or damp clothing, and do not touch the injector solenoids or the solenoid wires when the engine is operating.

Check for a short circuit from pin to pin. Refer to the accompanying chart for the pins required. Cylinder Number 1 will be used as an example.

![[19200339.png]]

The pins of the circuits are as follows:

| Supply Pin | Return Pin |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
| 1 | 10 | 01 | A | 09 | 02 | B |
| 2 | 08 | 03 | A | 07 | 04 | B |
| 3 | 06 | 05 | A | 16 | 06 | B |
| 4 | 26 | 07 | A | 36 | 08 | B |
| 5 | 04 | 09 | A | 03 | 10 | B |
| 6 | 02 | 11 | A | 01 | 12 | B |

![[19200333.png]]

Turn the vehicle keyswitch to the OFF position. Disconnect the actuator and sensor harness connectors from the ECM. Disconnect the actuator harness from the 15-pin pass-through connector.

Insert a test lead into pin 10 of the actuator harness connector. Insert the other test lead into all other pins of the actuator harness connector, one at a time. Measure the resistance.

Repeat same check as previous from pin 9. The circuit **must** be open (100k ohms or more) at all pins. If the circuit is not open, repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

> [!missing]- Иллюстрация `19200410.png` не извлечена — смотрите PDF-оригинал документа

Insert a test lead into pin 10 of the actuator harness connector. Insert the other test lead into all other pins of the sensor harness connector, one at a time. Measure the resistance.

Repeat same check as previous from pin 9. The circuit **must** be open (100k ohms or more) at all pins. If the circuit is **not** open, repair or replace the actuator or sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

> [!missing]- Иллюстрация `19200411.png` не извлечена — смотрите PDF-оригинал документа

Check for a short circuit from pin to pin in the 15-pin pass-through connector. Disconnect the internal harness from the injector solenoid.

Insert a test lead into pin 01 of the 15-pin pass-through connector, internal harness side. Insert the other test lead into all other pins of the pass-through connector, one at a time. Measure the resistance.

The circuit **must** be open (100k ohms or more). If it is **not** open, replace the internal actuator harness. Refer to Procedure 019-063.

> [!missing]- Иллюстрация `19200412.png` не извлечена — смотрите PDF-оригинал документа

Insert a test lead into pin 02 of the 15-pin pass-through connector, internal harness side. Insert the other test lead into all other pins of the pass-through connector, one at a time. Measure the resistance.

The circuit **must** be open (100k ohms or more). If it is **not** open, replace the internal actuator harness. Refer to Procedure 019-063.

Connect all components after completing the repair.

> [!missing]- Иллюстрация `19200413.png` не извлечена — смотрите PDF-оригинал документа
