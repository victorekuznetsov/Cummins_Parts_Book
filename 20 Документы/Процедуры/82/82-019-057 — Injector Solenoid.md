---
aliases:
  - "Электромагнит форсунки"
type: "Процедура"
doc: "82-019-057"
title_en: "Injector Solenoid"
title_ru: "Электромагнит форсунки"
modified: "2002-06-03"
engines:
  - "41343322"
families:
  - "NT/NTA855 · ISM/QSM11"
manuals:
  - "3666266"
figures: 5
source: "https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-057.html"
pdf: "https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-057.pdf"
tags:
  - "документ/процедура"
  - "двигатель/NT/NTA855"
  - "группа/82"
---

# Injector Solenoid
**Электромагнит форсунки**

> [!abstract] Процедура · `82-019-057`
> **Двигатели:** [[41343322 — NH NT 855 CPL 3362|41343322]]
> **Семейство:** NT/NTA855 · ISM/QSM11
> **Входит в руководства:** [[3666266 — ISM and QSM11 Electronic Control System Troubleshooting and Repair Manual|3666266]]
> **Секции:** Section 19 - Electronic Engine Controls
> **Даты:** изменён 2002-06-03
> **Источник:** [QuickServe](https://quickserve.cummins.com/qs3/pubsys2/xml/en/procedures/82/82-019-057.html) · [PDF-оригинал](https://github.com/victorekuznetsov/Cummins_Parts_Book/raw/claude/cummins-parts-knowledge-base-qa0n50/bulletins/procedures/82-019-057.pdf)

### General Information

The injector solenoid circuits are the supply and return wires in the actuator harness. The wires go from the ECM connector to a 15-pin connector in the rocker lever housing. The 15-pin connector connects the external and internal actuator harness. The internal harness goes to each injector. Three of the wires operate the engine brake actuator circuits.

![[19200332.png]]

The pins of the circuits are as follows:

| Supply Pin | Return Pin |  |  |  |  |  |
|---|---|---|---|---|---|---|
| Cyl. No. | ECM Conn. | 15-Pin Conn. | Inj. Pin | ECM Conn. | 15-Pin Conn. | Inj. Pin |
| 1 | 10 | 01 | A | 09 | 02 | B |
| 2 | 08 | 03 | A | 07 | 04 | B |
| 3 | 06 | 05 | A | 16 | 06 | B |
| 4 | 26 | 07 | A | 36 | 08 | B |
| 5 | 04 | 09 | A | 03 | 10 | B |
| 6 | 02 | 11 | A | 01 | 12 | B |

![[19200333.png]]

Remove the actuator harness connector from the ECM and check for damaged pins.

![[19c00178.png]]

### Resistance Check

The resistance value of the injector solenoid circuit is very low. The solenoid resistance is also temperature sensitive. To read an accurate resistance value, the resistance of the multimeter **must** be subtracted from the total resistance of the injector solenoid circuit.

![[19800481.png]]

> [!warning] CAUTION · Осторожно
> Use a multimeter for this procedure. Use Cummins multimeter, Part No. 3377161, or a meter with the same accuracy of ±1/2 percent.

Turn the multimeter on. Set the meter range to the lowest ohm scale. Measure the resistance across the two test probes. This is the multimeter resistance value which will be subtracted from the injector solenoid resistance value.

![[ee8cok80.png]]
