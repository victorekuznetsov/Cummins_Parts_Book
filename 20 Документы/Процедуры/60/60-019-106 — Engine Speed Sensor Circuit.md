---
aliases:
  - "Цепь датчика частоты вращения двигателя"
type: "Процедура"
doc: "60-019-106"
title_en: "Engine Speed Sensor Circuit"
title_ru: "Цепь датчика частоты вращения двигателя"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 10
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-106.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-106.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Engine Speed Sensor Circuit
**Цепь датчика частоты вращения двигателя**

> [!abstract] Процедура · `60-019-106`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-106.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/60-019-106.pdf)

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin 4021539.

![[ck800wa.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness 50-pin connectors from ECM1, ECM2, and ECM3.

Make sure the engine speed sensor is connected to the harness.

![[19a00825.png]]

Measure the resistance between the engine crankshaft speed signal and engine crankshaft speed return pin at the engine harness ECM1 connector. The resistance value **must** be 750 to 1100 ohms.

Measure the resistance between the engine crankshaft speed sensor signal and engine crankshaft speed return pin at the engine harness ECM2 connector. The resistance value **must** be 1100 to 1500 ohms.

If either of the readings are outside of the specifications, provided the engine speed sensor has been checked, replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

![[19a00826.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758. The leads must fit tightly in the connector without expanding the pins of the connector.

Connect the engine harness 50-pin connection to ECM1, ECM2, and ECM3.

Make sure the engine speed sensor is connected to the harness.

![[19a00825.png]]

Measure the resistance between the engine crankshaft speed signal and the engine crankshaft speed return at ECM1 50-pin connector. Measure the resistance between the engine crankshaft signal and the engine crankshaft speed return at the ECM2 50-pin connector. The resistance values **must** be between 1000 to 2000 ohms.

If either of the readings are outside of the specifications, provided the engine speed sensor has been checked, replace the extension harness.

![[19a00826.png]]

### Check for Short Circuit to Ground

Disconnect the engine harness 50-pin connector from ECM1, ECM2, and ECM3.

![[19a00825.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.

Insert the test lead into the engine crankshaft speed sensor signal pin and the other test lead into the engine crankshaft speed sensor return in the ECM1 50-pin connector. Repeat the resistance test for ECM2 AND ECM3. Measure the resistance. The multimeter **must** show an open circuit (more than 100 k ohms).

If the resistance values in any of the previous checks are **not** within the specification, there is a short circuit to ground, provided the engine crankshaft speed sensor has been previously checked. Replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]]

![[19a00826.png]]

### Check for Short Circuit from Pin to Pin

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822758 or 3822917. The leads must fit tightly in the connector without expanding the pins of the connector.

Disconnect the engine harness 50-pin connector from ECM1, ECM2, and ECM3.

Disconnect the engine speed sensor from the engine harness.

![[19a00825.png]]

Insert the test lead into the engine crankshaft speed sensor 1 signal pin at the ECM1 engine harness. Insert the other test lead into all of the other pins on the ECM1 engine harness, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 100k ohms) for all pins in the connector.

Repeat the test procedure for ECM2 and ECM3.

Insert the test lead into the engine speed sensor 1 return pin at the engine harness inline connector. Insert the other test lead into all of the other pins on the engine harness inline connector, one at a time. Measure the resistance for each pin. The multimeter **must** show an open circuit (more than 100k ohms) for all pins in the connector.

If the resistance values in any of the previous checks are **not** within specification, there is a short circuit from one of the engine speed sensor wires to any pin that measures less than 10M ohms. Repair or replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19.]] [[99-019-208 — Deutsch HDP20 and HD30 Connector Series|Refer to Procedure 019-208 (Deutsch™ HDP20 and HD30 Connector Series) in Section 19.]]

![[19a00826.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin 4021539.

![[ck800wa.png]]
