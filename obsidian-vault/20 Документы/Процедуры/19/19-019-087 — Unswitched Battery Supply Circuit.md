---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "19-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
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
figures: 8
lang: "en"
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/QSK23"
  - "двигатель/QSK60"
  - "группа/19"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `19-019-087`
> **Двигатели:** [[33210083 — QSK60 CM500 CPL 2699|33210083]], [[33219033 — QSK60 CM500 CPL 2848|33219033]], [[33224343 — QSK60 CM500 CPL 2849|33224343]], [[85017333 — QSK23 CM500 CPL 2858|85017333]]
> **Семейство:** QSK23, QSK60
> **Входит в руководства:** [[3666113 — QSK19, QSK23, QSK45, QSK60, and QSK78 Electronic Control System Troubleshooting and R|3666113]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2002-08-20
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/19/19-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/main/bulletins/procedures/19-019-087.pdf)

### General Information

The ECM receives constant voltage from the batteries through the unswitched battery wires that are connected directly to the (+) positive battery post. There are two in-line 10 AMP fuses in the unswitched battery wires to protect the ECM.

![[19400081.png]]

### Initial Check

Inspect the battery cable connections for loose or corroded connections. Repair or replace the battery connections. Refer to the OEM manual.

![[19400082.png]]

Inspect the OEM interface harness fuse connections for loose or corroded fuses. Replace the fuses if necessary. Refer to Procedure 019-198.

![[19400084.png]]

Check the battery voltage. Touch the multimeter positive (+) probe to the positive (+) terminal of the battery. Touch the multimeter negative (-) probe to the negative (-) terminal of the battery. Measure the battery voltage. The VDC should be 17.3 to 34.7 VDC for a 24-VDC system. If the battery voltage is below 17.3 VDC, replace the battery. Refer to the OEM manual for battery replacement.

![[19400083.png]]

### Resistance Check

> [!warning] CAUTION · Осторожно
> To reduce the possibility of connector damage, do not use probes or leads other than Part Number 3822758. The connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Disconnect the OEM interface harness from the ECM. Check for damaged pins in the ECM and the harness connector.

![[19400401.png]]

Insert the lead into pin 3 of the OEM interface harness connector. Connect the alligator clip to the multimeter probe. Touch the other multimeter probe to the battery connection (ring terminal) on the OEM harness. Measure the resistance. The resistance **must** be 10 ohms or less.

![[19800985.png]]

Remove the lead from pin 3 and insert it into pins 4 and 5 of the OEM interface harness connector. Touch the other multimeter probe to the battery connection on the OEM harness. Measure the resistance. The resistance **must** be 10 ohms or less.

![[19800986.png]]

If more than 10 ohms are measured in any check, there is an open circuit. Repair or replace the OEM interface harness or the OEM harness. Refer to Procedures 019-199, [[19-019-072 — OEM Interface Harness|019-072]], or the OEM manual.

![[19800987.png]]
