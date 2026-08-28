---
aliases:
  - "Цепь датчика положения коленвала (EPS)"
type: "Процедура"
doc: "82-019-039"
title_en: "Engine Position Sensor (EPS) Circuit"
title_ru: "Цепь датчика положения коленвала (EPS)"
modified: "2005-01-28"
engines:
  - "41343322"
  - "41370103"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 12
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-039.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-039.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Engine Position Sensor (EPS) Circuit
**Цепь датчика положения коленвала (EPS)**

> [!abstract] Процедура · `82-019-039`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]], [[41370103 — NH NT 855 CPL 3362|41370103]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2005-01-28
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-039.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/82-019-039.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly without expanding the pins of the connector.

Disconnect the sensor harness connector from the ECM. Insert a test lead into pin 47 of the sensor harness connector. Insert another test lead into pin 48 of the connector.

![[19200210.png]]

Make sure the EPS is connected to the sensor harness.

Connect the test leads to the multimeter probes. Measure the resistance. The resistance value **must** be 1000 to 2000 ohms. If the resistance value is **not** correct, there is a problem with the sensor harness, provided the sensor has been previously checked.

![[19200210.png]]

Insert the leads into pins 50 and 49 of the sensor harness connector. Measure the resistance. The multimeter **must** show between 1000 and 2000 ohms. If the resistance is **not** correct, there is a problem with the sensor harness, provided that the sensor has been previously checked. Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]]. If both resistance checks are within specification, the sensor circuit **must** still be checked for a short circuit to ground and a short circuit from pin to pin.

![[19200212.png]]

### Check for Short Circuit to Ground

Check for a short circuit to ground. Adjust the multimeter to the resistance setting. Insert a test lead into pin 47 of the sensor harness connector, and connect it to a multimeter probe. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

If the circuit is **not** open, there is a short circuit to ground in the wire connected to pin 47.

Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200406.png]]

Remove the test lead from pin 47 of the sensor harness connector and insert it into pin 50 of the connector. Touch the other multimeter probe to the engine block ground. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

If the circuit is **not** open, there is a short circuit to ground in the wire connected to pin 50.

Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

![[19200407.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the engine position sensor from the sensor harness. Insert test lead into pin 48 of the sensor harness connector. Insert other test lead into pin 45 of the connector. Set the multimeter to the resistance setting and measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200392.png]]

Remove the test lead from pin 45 of the sensor harness connector and check all other pins in the connector. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200213.png]]

Insert the test lead into pin 49 of the sensor harness connector and test all other pins in the connector. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200214.png]]

Remove the test lead from pin 49 of the sensor harness connector and insert it into pin 50 of the connector. Insert the other lead into pin 48. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200393.png]]

Remove the test lead from pin 48 of the sensor harness connector and check all other pins in the connector. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200215.png]]

Remove the test lead from pin 50 of the sensor harness connector and insert it into pin 47 of the connector. Insert the other test lead into pin 48. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19200210.png]]

Remove the test lead from pin 48 of the sensor harness connector and test all other pins. Measure the resistance. The multimeter **must** show an open circuit (more than 100k ohms).

If the resistance values in any of the previous tests are **not** within the specification, there is a short circuit from pins 47, 48, 49, or 50 to any pin that measures less than 100k ohms. Repair or replace the sensor harness. Refer to Procedure [[82-019-043-tr — Engine Wiring Harness|019-043]].

Connect all components after completing the repair.

![[19200216.png]]
