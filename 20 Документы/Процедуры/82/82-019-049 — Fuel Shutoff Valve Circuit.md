---
aliases:
  - "Цепь клапана отсечки топлива"
type: "Процедура"
doc: "82-019-049"
title_en: "Fuel Shutoff Valve Circuit"
title_ru: "Цепь клапана отсечки топлива"
modified: "2005-01-28"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 8
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-049.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-049.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Fuel Shutoff Valve Circuit
**Цепь клапана отсечки топлива**

> [!abstract] Процедура · `82-019-049`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-049.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-049.pdf)

### General Information

The fuel shutoff solenoid valve located on the fuel system housing. The solenoid is controlled by the ECM.

> [!note] Note · Примечание
> **Only** one wire from the ECM will be attached to the solenoid post. The ECM is **not** capable of supplying power for other auxiliary components. If an external voltage source is attached, a fault code will be induced.

![[19c01393.png]]

Turning the vehicle keyswitch on signals the ECM to open the fuel shutoff solenoid valve. The solenoid closes when the ECM senses the vehicle keyswitch is turned off or when the ECM senses an engine overspeed.

For more information on the fuel shutoff valve, refer to Procedure 005-043 in the Troubleshooting and Repair Manual, ISM and QSM11 Series Engines, Bulletin 3666322.

![[fv2swkb.png]]

### Resistance Check

The fuel shutoff valve circuit is a signal wire, pin 33, of the actuator harness connector to the shutoff valve solenoid. The valve is grounded through the engine.

Disconnect the actuator harness connector from the ECM. Check for damaged pins.

Disconnect the fuel shutoff solenoid wire from the valve terminal post.

![[fv2swkc.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Insert a test lead into pin 33 of the actuator harness connector. Connect the alligator clip to the multimeter probe.

![[19200337.png]]

Touch the other multimeter probe to the fuel shutoff valve solenoid wire. Measure the resistance.

The multimeter **must** show a closed circuit (10 ohms or less). If the circuit is **not** closed, repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

If the circuit is closed, it **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19200337.png]]

### Check for Short Circuit to Ground

Insert a test lead into pin 33 of the actuator harness connector and connect it to the multimeter. Touch the other multimeter probe to engine block ground. The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short circuit to ground in the wire connected to pin 33. Repair or replace the actuator harness.

Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19900627.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin 33 to all other pins of the actuator harness connector. Insert a test lead into pin 33 of the actuator harness connector, and connect the lead to the multimeter probe. Insert the other test lead into all other pins of the actuator harness connector, one at a time.

The ring terminal at the solenoid **must** be disconnected and can **not** touch anything that is grounded. The battery voltage supply **must** be disconnected.

> [!missing]- Иллюстрация `19c00435.png` не извлечена — смотрите PDF-оригинал документа

Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms). If the circuit is **not** open, there is a short between pin 33 and any pin that measured a closed circuit.

Repair or replace the actuator harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

> [!missing]- Иллюстрация `19c00435.png` не извлечена — смотрите PDF-оригинал документа
