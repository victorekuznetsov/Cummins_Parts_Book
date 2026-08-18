---
aliases:
  - "Цепь постоянного питания от АКБ"
type: "Процедура"
doc: "07-019-087"
title_en: "Unswitched Battery Supply Circuit"
title_ru: "Цепь постоянного питания от АКБ"
modified: "2003-12-01"
engines:
  - "93058669"
families:
  - "C8.3 · 6C8.3"
manuals:
  - "4021442"
figures: 7
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-087.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-087.pdf"
tags:
  - "документ/процедура"
  - "двигатель/C8.3"
  - "группа/07"
---

# Unswitched Battery Supply Circuit
**Цепь постоянного питания от АКБ**

> [!abstract] Процедура · `07-019-087`
> **Двигатели:** [[93058669 — 6C8.3 CPL 3105|93058669]]
> **Семейство:** C8.3 · 6C8.3
> **Входит в руководства:** [[4021442 — C8.3 Marine Electronic Control System Troubleshooting and Repair Manual|4021442]]
> **Секции:** Section 19 - Electronic Engine Controls - Group 19
> **Даты:** изменён 2003-12-01
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/07/07-019-087.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/07-019-087.pdf)

### General Information

The Electronic Control Module (ECM) receives constant voltage from the batteries through the unswitched battery wires connected directly to the (+) positive battery post.

There are two in-line 10-ampere fuses in the unswitched battery wires to protect the ECM.

![[19a00746.png]]

### Initial Check

Inspect the battery cable connections for loose or corroded connections.

If corroded, repair or replace the battery connections. Refer to the OEM manual.

![[19400082.png]]

Inspect the OEM interface harness fuse connections for loose or corroded fuses.

If corroded, replace the fuses. Refer to Procedure [[99-019-198 — Fuse, Harness In-Line|019-198]].

Touch one multimeter lead to each fuse terminal and measure the resistance.

The fuse should measure a closed circuit.

Resistance: 10 ohms or less

![[19400084.png]]

Place the multimeter positive probe on the positive (+) terminal of the battery.

Place the multimeter negative probe on the negative (-) terminal of the battery.

Measure the battery voltage.

Voltage for a 12-VDC system: 9.6 to 16.0 VDC

If the battery voltage is below 9.6 VDC, replace the battery.

Voltage for a 24-VDC system: 17.3 to 34.7 VDC

If the battery voltage is below 17.3 VDC, replace the battery.

Refer to the OEM manual for battery replacement.

![[19400083.png]]

### Resistance Check

Disconnect the engine harness connector from the ECM.

Check for damaged pins in the ECM and the harness.

![[19900781.png]]

> [!warning] CAUTION · Осторожно
> Do not use probes or test leads other than Part Number 3822758, otherwise the connector will be damaged. The leads must fit tightly in the connector without expanding the pins in the connector.

Insert the lead into one of the four unswitched battery supply pins of the engine harness connector.

Connect the alligator clip to the multimeter probe.

Touch the other multimeter probe to the battery connection on the engine harness.

Measure the resistance.

Resistance: 10 ohms or less

Repeat the check from each of the remaining three unswitched battery supply pins of the engine harness connector to the battery connection on the engine harness.

![[19901347.png]]

If more then 10 ohms are measured in any check, there is an open circuit. Repair or replace the engine harness.

Refer to Procedures [[07-019-043 — Engine Wiring Harness|019-043]], [[99-019-197 — Ring Terminal|019-197]], [[99-019-199 — Connector, Butt Splice|019-199]], and [[99-019-204 — Deutsch DRC Connector Series|019-204]].

![[19901348.png]]
