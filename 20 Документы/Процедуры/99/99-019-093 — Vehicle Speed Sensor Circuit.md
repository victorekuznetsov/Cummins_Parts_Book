---
aliases:
  - "Цепь датчика скорости машины"
type: "Процедура"
doc: "99-019-093"
title_en: "Vehicle Speed Sensor Circuit"
title_ru: "Цепь датчика скорости машины"
modified: "2015-06-29"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-093.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-093.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/99"
---

# Vehicle Speed Sensor Circuit
**Цепь датчика скорости машины**

> [!abstract] Процедура · `99-019-093`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2015-06-29
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/99/99-019-093.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/99-019-093.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Proper leads and/or a Cummins® approved circuit testing tool must be used when working with electrical connectors to prevent pin expansion and damage to the connector.

Disconnect the original equipment manufacturer (OEM) harness engine interface connector. To determine the location of the connector, see the corresponding engine wiring diagram. Make sure the vehicle speed sensor is connected to the OEM harness.

Insert a test lead into the magnetic vehicle speed sensor signal positive (+) pin in the OEM harness connector. Insert the other lead into the magnetic vehicle speed sensor signal negative (-) pin of the connector.

Connect the two alligator clips to the two probes of the multimeter. Adjust the multimeter to the resistance setting and measure resistance. When measuring the resistance with the sensor connected, refer to the OEM troubleshooting and repair manual for the correct resistance value. If the value is **not** correct, there is a problem with the OEM harness, provided that the vehicle speed sensor component has been previously checked.

> [!note] Note · Примечание
> Repair or replace the OEM harness. [[99-019-071 — OEM Wiring Harness|Refer to Procedure 019-071]], or to the OEM troubleshooting and repair manual for OEM harness replacement.

If the value is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin-to-pin.

![[19c01215.png]]

### Check for Short Circuit to Ground

Check for a short circuit to ground. Insert the multimeter probe with attached test lead into the magnetic vehicle speed sensor signal positive (+) pin of the OEM harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit to ground in the vehicle speed sensor circuit in the engine harness or OEM harness.

Repair the wires which are shorted in the circuit according to the vehicle manufacturer's procedures.

![[19c01241.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin-to-pin. Insert the multimeter probe with attached test lead into the magnetic vehicle speed sensor signal positive (+) pin of the OEM harness connector. Insert the other test lead into all the other pins, one at a time, to check for a short to another pin.

Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms).

![[19c01215.png]]
