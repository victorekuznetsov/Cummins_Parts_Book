---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "01-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2003-12-04"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021419"
figures: 24
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/01"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `01-019-106`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021419 — QSX15, QSK23, QSK45, QSK60, QSK78, and QST30 Power Generation Electronic Control Syst|4021419]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-04
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/01/01-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/01-019-106.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness inline connector.

Make sure the engine speed sensor is connected to the harness.

![[19802556.png]]

Measure the resistance between the engine speed sensor 1 signal and return pin at the engine harness inline connector. The resistance value **must** be 750 to 1100 ohms.

Measure the resistance between the engine speed sensor 2 signal and return pin at the engine harness inline connector. The resistance value **must** be 1100 to 1500 ohms.

If either of the readings are outside the specifications, provided the engine speed sensor has been checked, replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].

![[19802557.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.

Connect the engine harness inline connector.

Disconnect the extension harness from the ECM.

Make sure the engine speed sensor is connected to the harness.

![[19802479.png]]

Measure the resistance between the engine speed sensor 1 signal and return pin at the extension harness connector. Measure the resistance between the engine speed sensor 2 signal and return pin at the extension harness connector. The resistance values **must** be 1000 to 2000 ohms.

If either of the readings are outside the specifications, provided the engine speed sensor has been checked, replace the extension harness. Refer to Procedure [[01-019-175 — Extension Wiring Harness|019-175]].

![[19802558.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness inline connector.

![[19802556.png]]

Insert the test lead into the engine speed sensor 1 signal pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

Insert the test lead into the engine speed sensor 1 return pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

![[19802559.png]]

Insert the test lead into the engine speed sensor 2 signal pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

Insert the test lead into the engine speed sensor 2 return pin at the engine harness inline connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

![[19802559.png]]

If the resistance values in any of the previous checks are **not** within the specification, there is a short circuit to ground, provided the engine speed sensor has been previously checked. Replace the engine harness. Refer to Procedure [[01-019-043 — Engine Wiring Harness|019-043]].

![[19802559.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.

Connect the engine harness inline connector.

Disconnect the extension harness from the ECM.

![[19802479.png]]

Insert the test lead into the engine speed sensor 1 signal pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

Insert the test lead into the engine speed sensor 1 return pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

![[19802560.png]]

Insert the test lead into the engine speed sensor 2 signal pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

Insert the test lead into the engine speed sensor 2 return pin at the extension harness connector. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10M ohms).

![[19802560.png]]

If the resistance values in any of the previous checks at the extension harness connector are **not** within the specification, there is a short circuit to ground, provided the engine speed sensor has been previously checked. Replace the extension harness. Refer to Procedure [[01-019-175 — Extension Wiring Harness|019-175]].

![[19802560.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness inline connector.

Disconnect the engine speed sensor from the engine harness.

![[19802556.png]]

Insert the test lead into the engine speed sensor 1 signal pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802557.png]]

Insert the test lead into the engine speed sensor 1 return pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802557.png]]

Insert the test lead into the engine speed sensor 2 signal pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802557.png]]

Insert the test lead into the engine speed sensor 2 return pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802557.png]]

If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from one of the engine speed sensor wires to any pin that measures less than 10M ohms. Repair or replace the engine harness. Refer to Procedures [[01-019-043 — Engine Wiring Harness|019-043]] and [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|019-208]].

![[19802557.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the extension harness from the ECM.

![[19802555.png]]

Insert the test lead into the engine speed sensor 1 signal pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802558.png]]

Insert the test lead into the engine speed sensor 1 return pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802558.png]]

Insert the test lead into the engine speed sensor 2 signal pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802558.png]]

Insert the test lead into the engine speed sensor 2 return pin at the extension harness connector. Insert the other test lead into all of the other pins on the extension harness connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 10M ohms) for all pins in the connector.

![[19802558.png]]

If the resistance values in any of the previous checks at the extension harness connector are **not** within specification, there is a short circuit from one of the engine speed sensor wires to any pin that measures less than 10M ohms. Repair or replace the extension harness. Refer to Procedures [[01-019-175 — Extension Wiring Harness|019-175]] and [[99-019-213 — D-Sub Miniature Connector Series|019-213]].

![[19802558.png]]
