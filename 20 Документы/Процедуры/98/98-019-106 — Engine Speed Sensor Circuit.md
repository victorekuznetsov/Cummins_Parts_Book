---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "98-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2004-05-14"
engines:
  - "37269910"
  - "37280605"
families:
  - "K19"
manuals:
  - "3666070"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/K19"
  - "группа/98"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `98-019-106`
> **Двигатели:** [[37269910 — K19 CPL 1253|37269910]], [[37280605 — K19 CPL 447|37280605]]
> **Семейство:** K19
> **Входит в руководства:** [[3666070 — CENTRY™ Electronic Control System Troubleshooting and Repair Manual|3666070]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2004-05-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/98/98-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/98-019-106.pdf)

### Resistance Check

Disconnect the main engine harness connector from the ECM.

Make sure the engine speed sensor is connected to the main engine harness.

![[19801636.png]]

Touch one of the multimeter leads to pin 4 of the main engine harness connector. Touch the other multimeter lead to pin 17 of the main engine harness connector.

![[19801637.png]]

Measure the resistance.

The multimeter **must** measure between 750 and 1500 ohms. If the measured resistance does **not** fall within this range, then there is a problem with the main engine harness, provided that the engine speed sensor has already been checked and is good. Repair or replace the main engine harness. Refer to Procedure 019-228 or [[98-019-043 — Engine Wiring Harness|019-043]].

Flex the harness softly when checking the circuit to check for intermittent open circuits.

![[19801638.png]]

Repeat the above resistance check to measure the resistance between pin 18 and pin 24 of the main engine harness connector.

Touch one of the multimeter leads to pin 18 of the main engine harness connector. Touch the other multimeter lead to pin 24 of the main engine harness connector.

The multimeter **must** measure between 750 and 1500 ohms.

![[19801639.png]]

Separate the two connectors. Lift the tab on the connectors and pull them apart.

When measuring the resistance values of the engine speed sensor coils, connect a mating connector with short lead extensions. This will allow the electrical leads of the sensor to be softly flexed to check for damaged or partially broken wire strands under the insulation.

![[19801627.png]]

### Check for Short Circuit from Pin to Pin

Check for a short circuit between pin 4 of the main engine harness connector and **all** other pins in the connector **except** pin 17.

Touch one of the multimeter leads to pin 4 of the connector. Touch the other multimeter lead to **all** other pins in the connector **except** pin 17, one at a time.

![[19801640.png]]

Measure the resistance.

The multimeter **must** show more than 100k ohms, which is an open circuit. If the circuit is **not** open, then there is a short between the wires connected to pin 4 of the main engine harness connector and any other pin that measured less than 100k ohms.

Repair or replace the main engine harness. Refer to Procedure 019-228 and Procedure [[98-019-043 — Engine Wiring Harness|019-043]].

![[19801621.png]]

Repeat the above procedure to check for a short circuit between pin 24 of the main engine harness connector and **all** other pins in the connector **except** pin 18.

Touch one of the multimeter leads to pin 24 of the connector. Touch the other multimeter lead to **all** other pins in the connector **except** pin 18, one at a time.

Measure the resistance. The multimeter **must** show more than 100k ohms.

![[19801642.png]]
