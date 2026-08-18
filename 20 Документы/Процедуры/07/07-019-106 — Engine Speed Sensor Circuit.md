---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "07-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2003-12-01"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 3
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `07-019-106`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-106.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness connector from the electronic control module (ECM).

Insert the male pin of one of the leads into the engine speed signal primary pin of the engine harness connector.

Insert the male pin of the other lead into the engine speed return primary pin of the engine harness connector.

Make sure the engine speed sensor is connected to the engine harness.

Connect the alligator clips to the multimeter probes.

Measure the resistance.

The resistance value **must** be 1000 to 2000 ohms.

If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was checked.

Insert the male pin of one of the leads into the engine speed signal secondary pin of the engine harness connector.

Insert the male pin of the other lead into the engine speed return primary pin of the connector.

Make sure the engine speed sensor is connected to the engine harness.

Connect the alligator clips to the multimeter probes.

Measure the resistance.

The resistance value **must** be 1000 to 2000 ohms.

If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was checked.

![[19901383.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness connector from the ECM.

Insert the test lead into the engine speed signal primary pin of the engine harness connector and connect the alligator clip to the multimeter probe.

Touch the other multimeter probe to the engine block.

Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

Remove the lead from the engine speed signal primary pin and insert it into the engine speed signal secondary pin of the engine harness connector.

Touch the other multimeter probe to the engine block.

Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

Remove the lead from the engine speed signal secondary pin and insert it into the engine speed +5 VDC primary pin of the engine harness connector.

Touch the other multimeter probe to the engine block.

Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19901407.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758 or the connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine speed sensor from the sensor harness.

Disconnect the engine harness connector from the ECM.

Insert a test lead into the engine speed +5 VDC primary pin of the engine harness connector.

Insert the other test lead into all other pins of the connector in succession.

Connect the alligator clips to the multimeter probes.

Measure the resistance.

The multimeter **must** show an open circuit (100k ohms or more) in each case.

Measure the resistance from the engine speed signal primary pin of the engine harness connector to all pins of the connector.

The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

Remove the lead from the engine speed signal primary pin of the engine harness connector and insert it into the engine speed return primary pin.

Measure the resistance from the engine speed return primary pin of the engine harness connector to all other pins of the connector.

The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from the engine speed +5 VDC primary pin, the engine speed signal primary pin, or the engine speed return primary pin to any pin that measured less than 100k ohms.

Repair or replace the engine harness.

Refer to Procedure [[07-019-043 — Engine Wiring Harness|019-043]] or [[99-019-204 — Deutsch DRC Connector Series|019-204]].

![[19901415.png]]
