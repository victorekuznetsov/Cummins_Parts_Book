---
aliases:
  - "Цепь датчика частоты вращения вала"
type: "Процедура"
doc: "82-019-313"
title_en: "Shaft Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения вала"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-313.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-313.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Shaft Speed Sensor Circuit
**Цепь датчика частоты вращения вала**

> [!abstract] Процедура · `82-019-313`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-313.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-313.pdf)

### Resistance Check

Disconnect the actuator harness connector from the ECM. Make sure the shaft speed sensor is connected to the OEM harness.

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The OEM harness will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Insert a test lead into pin 40 of the actuator harness connector. Insert the other lead into pin 30 of the connector.

![[19200265.png]]

Connect the two alligator clips to the two probes of the multimeter. Adjust the multimeter to the resistance setting and measure resistance. The resistance value **must** be 750 to 1500 ohms. If the value is **not** correct, there is a problem with the actuator harness, provided that the shaft speed sensor has been previously checked.

Repair or replace the actuator harness or the OEM harness, depending on the location of the damage. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

If the value is correct, the circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19200265.png]]

### Check for Short Circuit to Ground

Check for a short circuit to ground. Insert the multimeter probe with attached test lead into pin 40 of the actuator harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

If the circuit is **not** open, there is a short circuit to ground in the shaft speed sensor circuit in the actuator harness or OEM harness.

Repair the wires which are shorted in the circuit according to the vehicle manufacturer's procedures.

![[19200254.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit from pin to pin. Insert the multimeter probe with attached test lead into pin 40 of the actuator harness connector. Insert the other test lead into pin 1 of the connector.

Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms).

![[19c00436.png]]

Remove the test lead from pin 1 and test all pins in the connector.

Measure the resistance from pin 40 of the actuator harness connector to all other pins in the connector, one at a time. The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

> [!note] Note · Примечание
> If the values are correct for all of the circuit checks, the shaft speed sensor circuit is good.

Connect all components after completing the repair.

![[19c00437.png]]
