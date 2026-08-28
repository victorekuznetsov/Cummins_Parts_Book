---
aliases:
  - "Цепь управления вентилятором"
type: "Процедура"
doc: "82-019-045"
title_en: "Fan Control Circuit"
title_ru: "Цепь управления вентилятором"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 16
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-045.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-045.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Fan Control Circuit
**Цепь управления вентилятором**

> [!abstract] Процедура · `82-019-045`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-045.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-045.pdf)

### General Information

The ISM system can control the fan clutch activation. The ECM energizes the fan clutch or air valve solenoid.

See vehicle manufacturer's publications for more information on troubleshooting and repair of the fan clutch wiring.

![[19c00703.png]]

The fan clutch circuit is in the actuator harness. The fan clutch actuator signal wire runs from pin 5 in the actuator harness connector to pin 12 in the 31-pin Deutsch connector at the OEM harness. The fan clutch actuator return wire runs from pin 42 in the actuator harness connector to pin 13 in the 31-pin Deutsch connector at the OEM harness. From the 31-pin Deutsch connector, the circuit passes through the OEM wiring to the fan clutch.

![[19c00705.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the actuator harness connector from the ECM. Disconnect the OEM wiring at the fan clutch solenoid. Set the multimeter to the resistance setting.

Insert a test lead into pin 5 of the actuator harness connector, and connect it to the multimeter probe.

![[19c00704.png]]

Touch the other multimeter probe to the connector terminal of the fan clutch solenoid. Make sure the fan clutch solenoid is disconnected.

Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is closed, it **must** still be checked for a short circuit to ground and a short circuit from pin to pin. If the circuit is **not** closed, there is a connection problem or an open circuit in the wiring harness.

![[19c00704.png]]

Remove the lead from pin 5 and insert it into pin 42 of the actuator harness connector. Touch the other multimeter probe to the connector terminal of the other fan clutch solenoid. Make sure the fan clutch solenoid is disconnected.

Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is closed, it **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

If the circuit is **not** closed, there is a connection problem or an open circuit in the wiring harness.

![[19c00888.png]]

Check the harness connections at the 31-pin Deutsch connector.

If the connections are good, isolate the open circuit to the OEM wiring to the fan clutch solenoid or the actuator harness as described in the following steps.

![[19c00705.png]]

Check the OEM wiring to the fan clutch solenoid for an open circuit. Disconnect the 31-pin Deutsch connector.

Insert the multimeter lead into pin 12 of the 31-pin connector.

Touch the other multimeter probe to the fan clutch solenoid connector terminal. Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, there is an open circuit in the OEM wiring to the fan clutch solenoid. Repair or replace the OEM harness according to the OEM procedures.

![[19c00665.png]]

Remove the lead from pin 12 of the 31-pin connector and insert it into pin 13 of the 31-pin connector.

Touch the other multimeter probe to the fan clutch solenoid connector terminal. Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, there is an open circuit in the OEM wiring to the fan clutch solenoid.

Repair or replace the OEM harness according to the OEM procedures.

![[19c00706.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit between pin 5 and all of the other pins in the actuator harness connector. Make sure the fan clutch solenoid is disconnected. Make sure the battery voltage supply is disconnected.

Insert a test lead into pin 5 of the actuator harness connector. Insert the other test lead into all other pins of the actuator harness connector, one at a time.

Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

![[19200309.png]]

If the circuit is **not** open, there is a short circuit between pin 5 and any pin that measured a closed circuit.

Repair or replace the actuator harness.

Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200309.png]]

Check for a short circuit between pin 42 and all other pins in the actuator harness connector. Make sure the fan clutch solenoid is disconnected. Make sure the battery voltage supply is disconnected.

Insert a test lead into pin 42 of the actuator harness connector. Insert the other lead into all other pins of the actuator harness connector, one at a time.

Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

![[19200310.png]]

If the circuit is **not** open, there is a short circuit between pin 42 and any pin that measured a closed circuit.

Repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200310.png]]

Disconnect the sensor harness connector from the ECM.

Check for a short circuit from pin 5 of the actuator harness connector to all pins in the sensor harness connector.

Insert test lead into pin 5 of the actuator harness connector. Connect the alligator clip of the test lead to the multimeter probe. Insert the other test lead into all pins of the sensor harness connector.

Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200394.png]]

If the circuit is **not** open, there is a short circuit between pin 5 of the actuator harness connector and any pin in the sensor harness connector which measured a closed circuit.

Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200394.png]]

Check for a short circuit from pin 42 of the actuator harness connector to all pins in the sensor harness connector.

Insert the test lead into pin 42 of the actuator harness connector. Connect the alligator clip of the test lead to the multimeter probe. Insert the other test lead into all pins of the sensor harness connector.

Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200395.png]]

If the circuit is **not** open, there is a short circuit between pin 42 of the actuator harness connector and any pin in the sensor harness connector which measured a closed circuit.

Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after the repair is complete.

![[19200395.png]]
