---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "19-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2002-08-20"
engines:
  - "33210083"
  - "33219033"
  - "33224343"
  - "85017333"
families:
  - "QSK23"
  - "QSK60"
manuals:
  - "3666113"
figures: 14
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `19-019-106`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-106.pdf)

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness from the ECM. Insert a test lead into pin 27 of the engine harness connector. Insert the other test lead into pin 28 of the connector.

![[19800952.png]]

Make sure the engine speed sensor is connected to the engine harness.

Connect the alligator clips to the multimeter probes. Measure the resistance.

The resistance value **must** be 1000 to 2000 ohms. If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was previously checked.

![[19800953.png]]

Remove the leads from pins 27 and 28 and insert them into pins 37 and 38 of the engine harness connector. Measure the resistance. The multimeter **must** show between 1000 and 2000 ohms. If the resistance is **not** correct, there is a problem with the engine harness, provided the sensor was previously checked. Repair or replace the engine harness. Refer to Procedure 019-240 or [[19-019-043 — Engine Wiring Harness|019-043]]. If both resistance checks are within specifications, the sensor circuit **must** be checked for short circuit to ground and short circuits from pin to pin.

![[19800954.png]]

### Check for Short Circuit to Ground

Insert the test lead into pin 37 of the engine harness connector. Touch the other multimeter probe to the engine block. Measure the resistance.

The multimeter **must** show an open circuit (more than 10m ohms).

![[19800955.png]]

Remove the lead from pin 37 and insert it into pin 38 of the engine harness connector. Touch the other multimeter probe to the engine block. Measure the resistance.

The multimeter **must** show an open circuit (more than 10m ohms).

![[19800956.png]]

Remove the lead from pin 38 and insert it into pin 27 of the engine harness connector. Touch the other multimeter probe to the engine block. Measure the resistance.

The multimeter **must** show an open circuit (more than 10m ohms).

![[19800957.png]]

Remove the lead from pin 27 and insert it into pin 28. Touch the other multimeter probe to the engine block. Measure the resistance. The multimeter **must** show an open circuit (more than 10m ohms). If the resistance values in any of the previous checks are **not** within the specification, there is a short circuit to ground, provided the engine speed sensor has been previously checked.

Repair or replace the engine harness. Refer to Procedure 019-240 or [[19-019-043 — Engine Wiring Harness|019-043]].

![[19800958.png]]

### Check for Short Circuit from Pin to Pin

Disconnect the engine speed sensor from the engine harness. Insert the test lead into pin 27 fo the engine harness connector. Insert the other lead into pin 2 of the connector. Measure the resistance.

The multimeter **must** show an open circuit (more than 10m ohms).

![[19800959.png]]

Measure the resistance from pin 27 to all other remaining pins in the engine harness connector.

The multimeter **must** show an open circuit (more than 10m ohms) at all pins.

![[19800960.png]]

Remove the lead from pin 27 and insert it into pin 28. Measure the resistance from pin 28 of the engine harness connector to all other pins in the connector.

The multimeter **must** show an open circuit (more than 10m ohms) at all pins.

![[19800961.png]]

Remove the lead from pin 28 and insert it into pin 37. Insert he other lead into pin 1. Measure the resistance.

The multimeter **must** show an open circuit (more than 10m ohms).

![[19800962.png]]

Measure the resistance from pin 37 of the engine harness connector to all pins in the connector.

The multimeter **must** show an open circuit (more than 10m ohms) at all pins.

![[19800963.png]]

Remove the lead from pin 37 and insert it into pin 38 of the engine harness connector. Insert the other lead into pin 1. Measure the resistance.

The multimeter **must** show an open circuit (more than 10m ohms).

![[19800964.png]]

Remove the lead from pin 1 and measure the resistance from pin 38 to all other pins in the engine harness connector.

The multimeter **must** show an open circuit (more than 10m ohms) at all pins.

If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from pins 27, 28, 37, or 38 to any pin that measured less than 10m ohms. Repair or replace the engine harness. Refer to Procedure 019-240 or [[19-019-043 — Engine Wiring Harness|019-043]]. Connect all components after completing the repairs.

![[19800965.png]]
