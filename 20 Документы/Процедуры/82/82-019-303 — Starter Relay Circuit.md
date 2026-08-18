---
aliases:
  - "Цепь реле стартера"
type: "Процедура"
doc: "82-019-303"
title_en: "Starter Relay Circuit"
title_ru: "Цепь реле стартера"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 9
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-303.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-303.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Starter Relay Circuit
**Цепь реле стартера**

> [!abstract] Процедура · `82-019-303`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-303.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-303.pdf)

### Resistance Check

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first, and attach the negative (-) battery cable last.

Turn the keyswitch to the OFF position.

Disconnect the vehicle battery cables from the battery.

> [!note] Note · Примечание
> Disconnecting the vehicle battery connections may require that the engine ECM real-time clock be reset using INSITE™.

![[ea8coha.png]]

> [!warning] CAUTION · Осторожно
> To reduce the possibility of pin and harness damage, use test leads, Part Number 3822758 and 3822917, when taking a measurement.

Verify that the neutral position switch, the hood tilt switch, and the parking brake switch are closed.

Disconnect the ICON™ starter relay from the OEM harness. Disconnect the 31-pin OEM connector. Disconnect the actuator harness connector from the ECM.

Set the multimeter to measure resistance.

![[19c00734.png]]

Check the OEM harness portion of the circuit.

Touch one of the multimeter leads to pin 85 of the ICON™ starter relay harness connector, OEM harness side, or the equivalent pin on the OEM 31-pin connector side of the relay. Refer to the ISM wiring diagram, Bulletin 3666269.

Touch the other multimeter lead to pin 27 of the 31-pin OEM connector, OEM harness side.

Read the value displayed on the multimeter.

![[19c00731.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.

![[19801619.png]]

Check the engine harness portion of the circuit.

Verify that the 6-pin ICON™ shorting plug is installed.

Touch the multimeter lead to pin 27 of the 31-pin OEM connector, engine harness side. Touch the other multimeter lead to pin 14 of the actuator harness connector.

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, check the ICON™ shorting plug for continuity.

![[19c00728.png]]

Disconnect the ICON™ shorting plug from the 6-pin engine harness connector.

Touch the multimeter lead to pin 5 of the ICON™ shorting plug. Touch the other multimeter lead to pin 4 of the ICON™ shorting plug. Read the value displayed on the multimeter.

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit. If the circuit is **not** closed, repair or replace the shorting plug. Refer to Procedure [[99-019-206 — Deutsch DTM and DTP Connector Series|019-206]]. If the circuit is closed, the problem is in the harness. Repair or replace the OEM harness. Refer to Procedure 019-071.

![[19c00730.png]]

Disconnect the OEM harness connector from the ECM.

Touch one of the multimeter lead to pin 33 of the 50-pin OEM harness connector, OEM harness side.

Touch the other multimeter lead to the corresponding pin of the ICON™ starter relay harness connector, OEM harness (nearest to ECM) side. Read the value displayed on the multimeter.

![[19c00726.png]]

The multimeter **must** display a reading of less than 10 ohms, which is a closed circuit.

If the circuit is **not** closed, repair or replace the OEM harness. Refer to Procedure 019-071.

![[19801619.png]]

Touch the multimeter lead to pin 33 of the 50-pin OEM harness connector.

Touch the other multimeter lead to pin 20 of the 31-pin OEM harness connector, OEM side. Read the value displayed on the multimeter.

The multimeter must display a reading of less than 10 ohms, which is a closed circuit. If the circuit is not closed, repair or replace the OEM harness. Refer to Procedure 019-071.

Connect all components after completing the repair.

![[19c00728.png]]
