---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "60-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2007-12-14"
engines:
  - "37292556"
  - "37295879"
families:
  - "QST30"
manuals:
  - "4021674"
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QST30"
  - "группа/60"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `60-019-087`
> **Двигатели:** [[37292556 — QST30 CM552 CPL 1244|37292556]], [[37295879 — QST30 CM552 CPL 2139|37295879]]
> **Семейство:** QST30
> **Входит в руководства:** [[4021674 — QST30 CM850 Power Generation Interface Engine Electronic Control System Troubleshooti|4021674]]
> **Секции:** Section 19 — Electronic Engine Controls — Group 19
> **Даты:** изменён 2007-12-14
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/60/60-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/60-019-087.pdf)

### General Information

The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the positive (+) battery post. There is one INLINE™ 15 ampere fuse in the unswitched battery wire to protect the ECM.

![[19802554.png]]

### Initial Check

Inspect the battery cable connections for loose or corroded connections. Repair or replace the battery connections, if necessary. Refer to the OEM manual.

![[19400082.png]]

Inspect the harness fuse connections for loose or corroded fuses. Replace the fuses, if necessary. [[99-019-198 — Fuse, Harness In-Line|Refer to Procedure 019-198 (Fuse, Harness In-Line) in Section 19.]]

![[19400084.png]]

Check the battery voltage. Place the multimeter positive probe on the positive (+) terminal of the battery. Place the multimeter negative probe on the negative (-) terminal of the battery. Measure the battery voltage. The voltage **must** be ± 17.3 to 34.7-VDC for a ± 24-VDC system. If the battery voltage is below ± 17.3-VDC, replace the battery. Refer to the OEM manual for battery replacement.

![[19400083.png]]

### Preparatory Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Disconnect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the Service Manual, QST30, Bulletin [[4021539 — QST30 Service Manual\|4021539]].

![[ck800wa.png]]

### Resistance Check

Disconnect the engine wiring harness and OEM wiring harness from the ECMs. Inspect the connector pins in the ECMs and the harness.

![[19a00834.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or leads other than Part Number 3822917. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Insert the lead into one of the unswitched battery voltage supply (+) pins of the engine harness. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the battery connector on the harness. Measure the resistance. The resistance **must** be 10 ohms or less.

Repeat this test for all the unswitched battery voltage supply (+) pins in the harness. Measure the resistance. The resistance **must** be 10 ohms or less.

If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19 or the OEM service manual.]]

Repeat this test for all the B- pins in the harness. Measure the resistance. The resistance **must** be 10 ohms or less.

If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness. [[60-019-043 — Engine Wiring Harness|Refer to Procedure 019-043 (Engine Wiring Harness) in Section 19 or the OEM service manual.]]

![[19a00835.png]]

### Finishing Steps

> [!danger] WARNING · Опасно
> Batteries can emit explosive gases. To reduce the possibility of personal injury, always ventilate the compartment before servicing the batteries. To reduce the possibility of arcing, remove the negative (-) battery cable first and attach the negative (-) battery cable last.

- Connect the batteries. Refer to Procedure 013-009 (Battery Cables and Connections) in Section 13 in the QST30 Service Manual, Bulletin [[4021539 — QST30 Service Manual\|4021539]].

![[ck800wa.png]]
