---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "87-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2003-02-10"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "3666214"
figures: 9
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/87"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `87-019-106`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[3666214 — QST30 Industrial Electronic Control System Troubleshooting and Repair Manual|3666214]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-02-10
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/87/87-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/87-019-106.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness connector from the ECM.

Insert the male pin of one of the leads into pin 17 of the engine harness connector. Insert the male pin of the other lead into pin 18 of the connector.

![[19a00169.png]]

Make sure the engine speed sensor is connected to the engine harness.

Connect the alligator clips to the multimeter probes. Measure the resistance. The resistance value **must** be 1000 to 2000 ohms.

If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was previously checked.

![[19a00170.png]]

### Check for Short Circuit to Ground

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness connector from the ECM. Insert the test lead into pin 17 of the engine harness connector, and connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the engine block. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19900538.png]]

Remove the lead from pin 17 and insert it into pin 8 of the engine harness connector. Touch the other multimeter probe to the engine block. Measure the resistance.

The multimeter **must** show an open circuit (more than 100k ohms).

![[19a00721.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine speed sensor from the sensor harness. Disconnect the engine harness connector and OEM interface harness connector from the ECM. Insert a test lead into pin 8 of the engine harness connector. Insert the other test lead into pin 1 of the connector. Connect the alligator clips to the multimeter probes. Measure the resistance. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00722.png]]

Measure the resistance from pin 8 to all other pins of the engine harness connector. The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

Then, repeat the pin-to-pin check from pin 8 of the engine harness connector to all pins of the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more) at all pins.

![[19a00723.png]]

Measure the resistance from pin 17 of the engine harness connector to all pins of the connector. The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

Then, repeat the pin-to-pin check from pin 17 of the engine harness connector to all pins of the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00724.png]]

Remove the lead from pin 17 of the engine harness connector and insert it into pin 18. Measure the resistance from pin 18 of the engine harness connector to all other pins of the connector.

The multimeter **must** show an open circuit (more than 100k ohms) at all pins.

Then, repeat the pin-to-pin check from pin 18 of the engine harness connector to all pins of the OEM interface harness connector. The multimeter **must** show an open circuit (100k ohms or more).

![[19a00726.png]]

If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from pin 8, 17, or 18 to any pin that measured less than 100k ohms. Repair or replace the engine harness.

Refer to Procedure [[87-019-250 — Connector, 50-Pin|019-250]] or [[87-019-043 — Engine Wiring Harness|019-043]].

![[19a00726.png]]
